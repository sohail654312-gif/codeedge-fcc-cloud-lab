# Codeedge FCC Cloud Lab

This is a **public, isolated testing repository** for FCC Codex, NVIDIA NIM, alternative AI models, and GitHub-hosted cloud commands. It is **not** a client app or production deployment.

## Verified milestones — 2026-10-11

- ✅ [GitHub cloud runner acceptance](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38094806909) — passed
- ✅ [Pinned FCC install, Python 3.14.7 and CLI entrypoints](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38116120418) — passed
- ✅ [FCC loopback HTTP health](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38116193151) — passed
- ✅ [Official Codex CLI pinned binary install](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38116399684) — passed, no sign-in
- ✅ [Offline NVIDIA request, error and key-redaction unit tests](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38116337700) — passed (no real key)
- ⏳ NVIDIA real API call — **not yet run** (requires owner's secret)
- ⏳ Actual FCC-to-Codex coding task — **not yet run**

The FCC workflows use disposable GitHub Linux runners. They do **not** create a persistent hosted FCC server. The selected upstream commit is `42bf8439cba25eae02a4dcb909a72227a46510a6` and its dependencies are installed with a locked uv environment; no pipe-to-shell installer was used.

## Strict project isolation

- Work only inside this repository. **Never modify** existing Codeedge MVP, Business OS, Growth Starter, website, or other repositories.
- No cross-repository GitHub tokens, credentials, SSH access, service logins, or proprietary client assets.
- Public code, commits, Actions logs, and artifacts must contain **no secrets**; do not upload private customer data.
- GitHub Actions `GITHUB_TOKEN` must remain read-only unless owner separately approves a narrowly-scoped exception.
- No external client messages, production changes, spending, public server exposure, or destructive actions without owner authorization.

## Cloud workflows

- `cloud-smoke.yml`: cloud runner and shell verification.
- `minimal-runner.yml`: dependency-free diagnostic.
- `fcc-pinned-install.yml`: checkout exact FCC commit, install locked dependencies, inspect entrypoints, boot server on **127.0.0.1 only**, and assert `/health`.
- `nvidia-one-shot.yml`: **manual trigger only**, one bounded model test with `scripts/nvidia_probe.py`. Not yet executed against a real NVIDIA provider.
- `nvidia-probe-unit.yml`: automatic, credential-free tests covering missing key, simulated success and redacted HTTP errors.
- `codex-cli-smoke.yml`: installs official `@openai/codex@0.162.1` with npm lifecycle scripts disabled and verifies the CLI, without signing in.

## One-time NVIDIA setup (owner only)

1. Create an NVIDIA NIM developer API key at https://build.nvidia.com/settings/api-keys, if eligible.
2. Add it through [this repository's Actions secrets settings](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/settings/secrets/actions), with the exact secret name **`NVIDIA_NIM_API_KEY`**. Keep the value off chat, files, and terminal output.
3. Run [NVIDIA NIM one-shot model test](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/workflows/nvidia-one-shot.yml) from the **Actions → Run workflow** menu. Model access, credits and rate limits depend on NVIDIA and may change.

The one-shot probe reports the model ID, short answer preview, latency, finish reason and token usage where supplied. Its output is visible publicly in GitHub Actions; never send client data as a test prompt. No claim of unlimited free inference is made.

## Evidence and remaining gates

- [Verified execution evidence](docs/first-run-evidence.md)
- [FCC preliminary source review](docs/fcc-upstream-review.md)
- [Testing and approval gates](docs/testing-gates.md)
- [Secrets and permission checklist](docs/secrets-checklist.md)

**Next:** Prove an authorized real model response, then a sandbox-only FCC/Codex coding task. The platform still needs a securely supplied provider key or an appropriately authorized alternative provider connection.
