"""Credential-free unit checks for the bounded NVIDIA NIM request probe."""
import contextlib
import importlib.util
import io
import json
import os
import pathlib
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "nvidia_probe.py"
spec = importlib.util.spec_from_file_location("codeedge_nvidia_probe", SCRIPT)
assert spec is not None and spec.loader is not None
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


class FakeHTTPResponse:
    def __init__(self, payload):
        self.payload = json.dumps(payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def read(self, maximum=-1):
        return self.payload[:maximum]


class NvidiaProbeTests(unittest.TestCase):
    def setUp(self):
        self.output = io.StringIO()
        self.errors = io.StringIO()

    def run_probe(self):
        with contextlib.redirect_stdout(self.output), contextlib.redirect_stderr(self.errors):
            return probe.main()

    def test_missing_secret_does_not_make_request(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(
            probe, "urlopen", side_effect=AssertionError("network forbidden")
        ):
            self.assertEqual(self.run_probe(), 2)
        self.assertIn("missing", self.errors.getvalue())
        self.assertNotIn("Bearer", self.errors.getvalue())

    def test_successful_model_response_is_bounded_and_key_never_logged(self):
        dummy_key = "unit-test-fake-key-do-not-use"
        fake_payload = {
            "model": "nvidia/example-test-model",
            "choices": [{"message": {"content": "CODEEDGE_NIM_OK"}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 15, "completion_tokens": 4, "total_tokens": 19},
        }

        def validate_request(request, **kwargs):
            self.assertEqual(request.full_url, "https://integrate.api.nvidia.com/v1/chat/completions")
            self.assertIn(dummy_key, request.get_header("Authorization"))
            self.assertIn(b"CODEEDGE_NIM_OK", request.data)
            return FakeHTTPResponse(fake_payload)

        with patch.dict(os.environ, {"NVIDIA_NIM_API_KEY": dummy_key}, clear=True), patch.object(
            probe, "urlopen", side_effect=validate_request
        ):
            self.assertEqual(self.run_probe(), 0)
        report = json.loads(self.output.getvalue())
        self.assertEqual(report["usage"]["total_tokens"], 19)
        self.assertTrue(report["expected_response_matched"])
        self.assertNotIn(dummy_key, self.output.getvalue() + self.errors.getvalue())

    def test_http_error_never_prints_key_or_response_body(self):
        dummy_key = "unit-test-fake-key-do-not-use"
        error = HTTPError("https://integrate.api.nvidia.com/v1/chat/completions", 429, dummy_key, {}, None)
        with patch.dict(os.environ, {"NVIDIA_NIM_API_KEY": dummy_key}, clear=True), patch.object(
            probe, "urlopen", side_effect=error
        ):
            self.assertEqual(self.run_probe(), 1)
        self.assertIn("HTTP 429", self.errors.getvalue())
        self.assertNotIn(dummy_key, self.errors.getvalue())


if __name__ == "__main__":
    unittest.main()
