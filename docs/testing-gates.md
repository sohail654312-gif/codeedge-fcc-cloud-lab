# Test gates

- **Gate 0: Secure scope** — private repository, no access to existing Codeedge repos, owner-controlled settings.
- **Gate 1: Cloud shell** — GitHub Actions smoke workflow completes successfully.
- **Gate 2: FCC audit** — validate FCC repo identity, licensing, dependencies, install instructions and external telemetry before installing.
- **Gate 3: Provider test** — securely inject provider key; capture model, response, latency and usage fields if returned; never log the key.
- **Gate 4: Coding test** — create a harmless test file in this repository on a feature branch; run tests and inspect changes.
- **Gate 5: Owner review** — explicitly approve any access expansion, additional expenses or integrations.

No gate above Gate 1 has been performed yet.
