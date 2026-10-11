# Codeedge FCC Cloud Lab — acceptance gates

| Gate | Requirement | Current result |
| --- | --- | --- |
| 0 | One-purpose repo, no secrets or cross-repo writes | PASS for repository isolation (repo is intentionally public) |
| 1 | GitHub Linux shell commands actually execute | PASS |
| 2A | Exact upstream source and package identity checks | PASS |
| 2B | Locked FCC install and CLI entrypoints on ephemeral runner | PASS |
| 2C | Start FCC on localhost and validate HTTP health | PASS |
| 2D | Full code/dependency security, telemetry and licensing review | NOT COMPLETE |
| 2E | Official pinned Codex CLI binary smoke test | PASS |
| 3A | Offline NVIDIA probe and secret-redaction tests | PASS |
| 3B | Authorized low-token NVIDIA NIM inference through secret | NOT RUN |
| 4 | Real FCC/Codex harmless coding task scoped to this repository | NOT RUN |
| 5 | Owner approves any production integration or spending | NOT REQUESTED |

Every claim requires evidence linked in [first-run-evidence.md](first-run-evidence.md).

In a **public** repository, source, Actions logs and artifacts can be read by anyone. Never use genuine client data or log bearer tokens. Maintain default read-only workflow permissions; do not grant agents write access to other repositories.
