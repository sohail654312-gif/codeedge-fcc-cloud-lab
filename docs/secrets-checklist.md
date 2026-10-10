# Credentials & secrets checklist

Never commit API keys, OAuth client secrets, SSH private keys, or authentication tokens. Never paste them into chat.

Future NVIDIA usage, when approved, should load `NVIDIA_API_KEY` from a GitHub Actions repository secret and avoid echoing it to logs.

Useful controls for agent workflows:
- Default `GITHUB_TOKEN` to `contents: read`; grant scoped write access only to a deliberately reviewed job.
- Prefer trusted, pinned upstream dependencies rather than `curl | bash` or arbitrary installation scripts.
- Prevent credentials from being sent to an agent's model prompt or stored in model transcripts.
- Scope workloads, billing, and write capabilities to this isolated repository.

This document does not authorize credentials access or installation.
