# Codeedge FCC Cloud Lab

**Purpose:** Private and standalone experiments for FCC Codex, NVIDIA NIM, alternative AI coding models, and GitHub-hosted command execution.

**Status:** Bootstrap phase. AI model provider accounts, FCC installation and real model inference are not yet verified.

## Scope and isolation
- Only this repository may be used for experiments.
- Do not modify or deploy `codeedge`, `codeedge-business-os`, `codeedge-growth-starter`, or other existing Codeedge repositories.
- Do not grant AI workflows write tokens, credentials or SSH access to other repositories.
- Do not place credentials or tokens in source, logs, prompts, issues, artifacts or chat.
- No external client messages, production deployments, purchases, destructive operations or financial actions without explicit owner approval.

## Cloud-shell test
Open **Actions → Cloud shell smoke test**. A normal push to `main` also triggers this workflow. It runs on an ephemeral GitHub-hosted Linux runner and verifies Bash, Git, Python, Node, npm and OS information.

The workflow grants `contents: read` only, disables persisted checkout credentials, has a 10-minute timeout and makes **no AI API requests or changes to other repositories**.

## Roadmap
1. **Gate 0 — Isolation:** Private repository, least-privilege workflows.
2. **Gate 1 — Cloud execution:** Verify GitHub Actions run and logs.
3. **Gate 2 — FCC source audit:** Identify and pin a reviewed upstream commit; avoid pipe-to-shell installers.
4. **Gate 3 — Provider key:** Add `NVIDIA_API_KEY` through GitHub encrypted Actions secrets (never in chat).
5. **Gate 4 — Real response:** Record model, provider, latency, available token usage and test outcome.
6. **Gate 5 — Coding agent test:** Run a harmless coding task here, review diffs, and only then consider scope expansion.

See [testing gates](docs/testing-gates.md) and [secrets checklist](docs/secrets-checklist.md).

**Important:** GitHub Actions runners are temporary. This repo is not a continuously running FCC server. Free usage is bounded by GitHub and provider quotas.
