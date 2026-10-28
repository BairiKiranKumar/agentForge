# Data handling, logging and retention

Guidance for people and agents who use agentForge on real work. It is practical advice, not legal advice. Legal obligations depend on where people and projects are located; see `engineering-standards/privacy/` and any selected regional pack.

## Keep private data out of the repository
- Real organization, brand, client and project profiles live in your private workspace, not in Git.
- Examples and tests use fictional organizations and synthetic data. Use reserved example domains (`example.com`) and obviously fake values.
- Do not commit execution logs, transcripts, screenshots of real work, or exported reports that contain real names, handles, domains or paths. Sanitize or keep them private.
- Run `python tools/privacy_scan.py` and `python tools/scan_secrets.py` before pushing. Add your own identity terms to `.agentforge/private/identity-patterns.txt` (ignored by Git).

## Data minimization for agents
- Give an agent only the data the task needs. Prefer synthetic or masked data for development and evaluation.
- Never paste passwords, API keys or tokens into chat, docs or code (`AGENTS.md` section 5).
- Do not research or profile private individuals beyond what the task requires.

## Logging
- Log decisions, commands run, results and evidence. Do not log secrets, full personal records or raw prompts that contain them.
- Redact before storing: mask emails, phone numbers, tokens and identifiers.
- Execution reports (`templates/execution-report.md`) should name roles, files, checks and gaps. They should not embed sensitive values.
- Keep logs where access is controlled. Treat transcripts as sensitive by default.

## Retention
- Decide a retention period per data class and write it down. Delete what you no longer need.
- Local caches (`.agentforge/cache/`) and task logs (`work/`) are ignored by Git. Clear them when a project ends.
- Backups must follow the same retention and access rules, and restores should be tested.

## If something leaks
Stop sharing it, revoke or rotate any credential, record what was exposed and to whom, and follow `SECURITY.md` and `docs/security/history-remediation.md`. If personal data of other people was exposed, involve your privacy or legal contact. Do not assume deletion is enough.
