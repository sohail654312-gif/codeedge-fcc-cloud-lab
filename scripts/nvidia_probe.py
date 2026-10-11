#!/usr/bin/env python3
"""One-request NVIDIA NIM smoke probe; no external dependencies or data writes."""
from __future__ import annotations

import json
import os
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ENDPOINT = "https://integrate.api.nvidia.com/v1/chat/completions"
EXPECTED = "CODEEDGE_NIM_OK"

def main() -> int:
    api_key = os.environ.get("NVIDIA_NIM_API_KEY", "").strip()
    if not api_key:
        print("NVIDIA_NIM_API_KEY repository secret is missing. No request sent.", file=sys.stderr)
        return 2

    model = os.environ.get("NVIDIA_MODEL", "nvidia/nemotron-3-super-120b-a12b").strip()
    if not model or any(c.isspace() for c in model) or len(model) > 160:
        print("Invalid model identifier. No request sent.", file=sys.stderr)
        return 2

    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": f"Reply with exactly {EXPECTED} and nothing else."}],
        "max_tokens": 128,
        "temperature": 0,
        "stream": False,
    }).encode("utf-8")
    request = Request(
        ENDPOINT,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    started = time.monotonic()
    try:
        with urlopen(request, timeout=60) as response:
            data = json.loads(response.read(2_000_000).decode("utf-8"))
    except HTTPError as error:
        print(f"NVIDIA NIM returned HTTP {error.code}; response body withheld.", file=sys.stderr)
        return 1
    except (URLError, TimeoutError, ValueError, json.JSONDecodeError) as error:
        print(f"NVIDIA NIM request failed ({type(error).__name__}); credentials withheld.", file=sys.stderr)
        return 1

    latency_ms = round((time.monotonic() - started) * 1000)
    choices = data.get("choices") if isinstance(data, dict) else None
    first = choices[0] if isinstance(choices, list) and choices else {}
    message = first.get("message") if isinstance(first, dict) else {}
    answer = message.get("content", "") if isinstance(message, dict) else ""
    if not isinstance(answer, str):
        answer = ""
    usage = data.get("usage") if isinstance(data, dict) else {}
    if not isinstance(usage, dict):
        usage = {}
    report = {
        "provider": "nvidia_nim",
        "requested_model": model,
        "returned_model": data.get("model") if isinstance(data, dict) else None,
        "latency_ms": latency_ms,
        "expected_response_matched": answer.strip() == EXPECTED,
        "response_preview": answer[:160],
        "finish_reason": first.get("finish_reason") if isinstance(first, dict) else None,
        "usage": {
            "prompt_tokens": usage.get("prompt_tokens"),
            "completion_tokens": usage.get("completion_tokens"),
            "total_tokens": usage.get("total_tokens"),
        },
    }
    print(json.dumps(report, ensure_ascii=True, indent=2))
    return 0 if answer.strip() else 1

if __name__ == "__main__":
    sys.exit(main())
