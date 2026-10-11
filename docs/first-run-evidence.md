# Verified FCC Cloud Lab execution evidence — 2026-10-11

All results below come from this public standalone repo: `sohail654312-gif/codeedge-fcc-cloud-lab`. **Only the lab repository was modified.**

## Cloud terminal — PASS
- [Minimal GitHub runner, run 38095163298, attempt 2](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38095163298): success, runner command executed.
- [Linux shell smoke, run 38094806909, attempt 3](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38094806909): success, Git/Python/Node/npm checks executed.
- Before the owner changed the repo from private to public, equivalent workflows failed before any job steps were recorded. Cause was not fully proven; success followed the visibility change.

## FCC install — PASS
- [Pinned FCC installation, run 38116120418](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38116120418): success.
- Upstream checkout `Alishahryar1/free-claude-code@42bf8439cba25eae02a4dcb909a72227a46510a6`, exact commit identity verified.
- `uv 0.12.13`, managed Python `3.14.7`, and locked FCC dependency installation verified.
- `fcc-server --version`, `fcc-doctor --version`, and `fcc-codex` entrypoint metadata passed.

## FCC local server — PASS
- [Loopback server health, run 38116193151](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38116193151): success.
- All setup steps, server process startup and HTTP `/health` request passed.
- Bound to `127.0.0.1` inside disposable GitHub-hosted runner; not exposed to the internet and no persistence after job completion.

## Not yet tested
- An actual NVIDIA NIM provider request (API key not available to this workflow).
- A real FCC-to-Codex coding task or full agent tool cycle.
- Continuous server hosting, account OAuth, rate limits, recovery, or production integration.

## Safety guardrails
- **Do not put keys, private business details, or customer data into the public repository or logs.**
- `NVIDIA_NIM_API_KEY` is a GitHub Actions repository secret for a future *manual* one-shot model test; it has not been used.
- No existing Codeedge repo accessed or modified. No unpinned upstream shell installer was run.
- Testing an installation in an isolated runner is not a full security audit of third-party dependencies.
