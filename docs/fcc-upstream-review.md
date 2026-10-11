# FCC upstream source review — partial, pinned

The reference source is [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code), at commit `42bf8439cba25eae02a4dcb909a72227a46510a6` (observed 2026-10-10).

## Verified source and runtime identity
- Package `free-claude-code`, license `AGPL-3.0-only`, required Python `==3.14.7`.
- Entry points declared: `fcc-server`, `fcc-doctor`, `fcc-codex`, and other agent launchers.
- Large transitive dependency set; install was performed **only** in an ephemeral GitHub runner with no service secrets.
- Installation uses pinned upstream Git checkout and `uv sync --locked`, not the moving `main` installer.
- The documented NVIDIA config name is `NVIDIA_NIM_API_KEY`. The lab's one-shot test uses this name consistently.
- [Installation smoke passed](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38116120418); [loopback server HTTP health passed](https://github.com/sohail654312-gif/codeedge-fcc-cloud-lab/actions/runs/38116193151).

## Security cautions
- Upstream `scripts/install.sh` and `install.ps1` contain optional installation paths for other tools and external download locations; the lab **does not execute them**.
- The executable source and dependency graph have **not** undergone a full code-level security or telemetry audit. A successful boot is not a security certification.
- AGPL-3.0 licensing should be reviewed before distribution or hosted service use.
- A local FCC proxy is not an unattended coding agent by itself: running Codex still requires an agent installation and approved provider credentials.
- README/provider claims do not guarantee free quotas, unlimited credits, or support for every model.

## Before expanding scope
Verify provider credentials and billing guardrails; inspect outbound destinations and model prompt data; test an isolated coding task with no cross-repo access; then request owner review for deployment or credential expansion.
