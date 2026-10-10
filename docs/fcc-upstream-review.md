# FCC upstream source review — preliminary

This document records a **source-identity check only**. It is NOT proof that executing a third-party installer or running the app is safe.

- Candidate project: https://github.com/Alishahryar1/free-claude-code
- Reference upstream commit observed 2026-10-10: `42bf8439cba25eae02a4dcb909a72227a46510a6`
- `pyproject.toml` declares package name `free-claude-code`, license `AGPL-3.0-only`, and **Python exactly 3.14.7**.
- Declared entrypoints include `fcc-server`, `fcc-doctor`, `fcc-claude` and `fcc-codex`.
- It declares a large dependency set (FastAPI, HTTPX, OpenAI, SQLAlchemy, gRPC, NVIDIA Riva, etc.). Third-party network installation must not happen until reviewed.
- Its README documents NVIDIA NIM via the `NVIDIA_NIM_API_KEY` setting and `fcc-codex` as a Codex launcher.
- README/provider documentation is not a guarantee of free quotas, provider reliability, or Codex compatibility in unattended cloud use.

## Safe next audit gates
1. Verify this upstream commit and corresponding installer checksums.
2. Inspect `scripts/install.sh`, authentication handling, outbound connections, token redaction and telemetry.
3. Inspect dependency lockfile and AGPL redistribution implications.
4. Try isolated FCC installation on a **throwaway runner with no secrets**; never `curl | sh` from a moving branch.
5. Only then test provider settings with a scoped key and low-token request.

Do not grant the FCC process or any coding agent credentials for the owner's other repositories.
