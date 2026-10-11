# Cloud runner and FCC installation evidence

Evidence observed on 2026-10-11 (Pakistan local date). This document reports actual GitHub Actions results, not future completion claims.

## Scope
- Repository: `sohail654312-gif/codeedge-fcc-cloud-lab` (now **public** at owner direction).
- Only this testing repository was modified. Original Codeedge projects remain untouched.
- **Do not put credentials or proprietary client data in a public repository.**

## Cloud runner gate — PASS
- Minimal runner: [run 38095163298](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38095163298), attempt 2: **success**. Job setup, runner startup, and completion steps passed.
- Cloud shell smoke: [run 38094806909](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38094806909), attempt 3: **success**. Checkout, shell verification, and cleanup passed.
- Prior failed attempts happened while this repository was private; no runnable steps were reported. The visibility change was followed by successful runs, but precise root cause of private-repository failures was not independently confirmed.

## Pinned FCC installation gate — PASS
- [Run 38116120418](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38116120418): **success**.
- Upstream repository `Alishahryar1/free-claude-code` pinned to commit `42bf8439cba25eae02a4dcb909a72227a46510a6`.
- GitHub job explicitly checked commit identity and `pyproject.toml` requirements.
- Pinned `uv 0.12.13`, installed managed Python `3.14.7`, synchronized locked packages with `uv sync --locked`.
- Checked `fcc-server --version`, `fcc-doctor --version`, and `fcc-codex` entrypoint metadata.
- No upstream `install.sh` was executed, no secret was provided, no NVIDIA model called, and no production repositories accessed.
- This is an **ephemeral** installation on one GitHub runner, not a persistent hosted FCC service.

## Follow-up server gate
- A loopback-only FCC server health test was added in `.github/workflows/fcc-pinned-install.yml`. Its outcome must be established from the latest workflow run before calling server startup passed.

## Outstanding gates
- Configure `NVIDIA_API_KEY` exclusively as a GitHub Actions secret, if the owner has an authorized development key.
- Execute the separately gated one-shot NVIDIA inference test, checking usage and cost constraints first.
- Validate a small coding-agent request on an isolated branch.
- Do not authorize automated pushes to production, long-running public servers, or cross-repository credentials by default.
