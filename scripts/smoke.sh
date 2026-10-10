#!/usr/bin/env bash
set -euo pipefail
printf 'Codeedge FCC Cloud Lab: isolated cloud shell smoke test\n'
printf 'UTC time: '; date -u +'%Y-%m-%dT%H:%M:%SZ'
printf 'Operating system: '; uname -s
for tool in git bash python3 node npm; do
  command -v "$tool" >/dev/null 2>&1 || { printf 'Missing required tool: %s\n' "$tool" >&2; exit 1; }
done
printf 'Git: '; git --version
printf 'Python: '; python3 --version
printf 'Node: '; node --version
printf 'npm: '; npm --version
printf 'Shell execution passed. No AI model calls, external writes, or secrets used.\n'
