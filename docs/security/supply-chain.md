# Supply-chain safety

agentForge recommends tools and reviews third-party skills. These rules keep that from becoming a path for untrusted code.

## Third-party skills and plugins
- A skill is instructions plus sometimes scripts. Treat it as untrusted until reviewed.
- Review rules and the registry policy: `design-intelligence/skill-registry/policy.md`. Read the files. Do not run install commands, hooks or helper scripts from a candidate.
- A skill is `approved` only with a clear license, a pinned commit SHA, a written evaluation, no unreviewed scripts and a human decision. The validator and a unit test enforce the mechanical parts.
- Prefer instruction-only skills. Be most careful with skills that add hooks, run binaries, fetch remote content at run time, or write to agent instruction files.
- Never copy third-party code, skill text or proprietary design assets into this repository without verifying the license allows redistribution, and recording attribution (`NOTICE`, `SOURCE-MANIFEST.md`).

## Dependencies
- Keep dependencies few. The runtime needs only PyYAML. Pin versions you deploy and audit them (`pip-audit`, OSV-Scanner).
- CI pins GitHub Actions by commit SHA and runs a dependency audit. Dependabot proposes updates for review; do not auto-merge.
- Verify package names carefully to avoid typosquats.

## Build and CI
- Run CI with read-only permissions by default (`permissions: contents: read`). Grant more only per job and with a reason.
- Do not expose secrets to pull requests from forks.
- Review workflow changes as carefully as code changes.

## Fetching remote rules
`runtime/discover.py` fetches pinned files and saves them as data. It does not execute them and never lets them override safety rules. Keep `ref` pinned to a full SHA.

## Reporting
Suspected malicious skill, dependency or workflow change: see `SECURITY.md`.
