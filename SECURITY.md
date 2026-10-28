# Security policy

agentForge is a framework of role definitions, workflows, standards and small Python tools that AI coding agents read and follow. Its main security risks are unsafe agent instructions, untrusted third-party content, leaked private data, and supply-chain exposure from tools and skills it recommends.

## Reporting a vulnerability or a privacy leak
Do not open a public issue for a vulnerability or for leaked personal, client or credential data.

Use GitHub's private vulnerability reporting for this repository (Security tab, "Report a vulnerability"). The repository owner must enable it; until a private channel is confirmed in the repository settings, treat this section as incomplete and see `docs/release-readiness/` for the open item. Include what you found, where, and how to reproduce it. Do not include real secrets in the report.

Expect an acknowledgement and a fix or mitigation plan from the maintainers on a best-effort basis. This project has no bug bounty.

## What counts
- An instruction in a role, workflow or configuration that would let an agent bypass the authorization boundaries in `AGENTS.md` section 3, or that weakens the safety floor in `config/defaults.yaml`.
- A tool in `tools/` or `runtime/` that executes untrusted content, writes outside the repository, or leaks data.
- Personal data, client data, credentials, private hostnames or local machine paths committed to the repository or its history.
- A vulnerable or compromised dependency, CI step or recommended third-party skill.

## Supported versions
The default branch. Pinned releases are supported on a best-effort basis only.

## If a credential was exposed
Revoke or rotate it immediately at the provider. Deleting it from the repository or history does not make it safe, because clones, forks, caches and logs may still hold it. Then follow `docs/security/history-remediation.md`.

## Hardening guidance
- Secure installation: `docs/security/secure-installation.md`
- Third-party skills and supply chain: `docs/security/supply-chain.md` and `design-intelligence/skill-registry/policy.md`
- Data handling, logging and retention: `docs/security/data-handling.md`
- Configuration and private workspaces: `docs/configuration.md`

## Automated checks
CI runs `tools/scan_secrets.py`, `tools/privacy_scan.py`, dependency auditing and the unit tests. They catch obvious problems only. A clean run is not a security certification.
