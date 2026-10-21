# OpenAI Codex

Codex reads `AGENTS.md` from the project root and from directories down to the working directory. Checked against OpenAI's AGENTS.md documentation on 2026-10-22: the combined project docs default to a 32 KiB cap (`project_doc_max_bytes`). Keep the root file short. Pull a role or a workflow only when the task needs it:

```text
python -m runtime.discover fetch social-media/linkedin-specialist/AGENT.md --offline
```

`--offline` uses this checkout. Omit it to try GitHub first. Use a full commit SHA as `--ref` when the work must be reproducible. `develop` moves.

Codex does not share Cursor's subagent tool. Run `python -m runtime.scheduler plan <plan.yaml>` to get the waves, then execute independent waves sequentially unless the Codex session you are in can spawn workers. Say which one you did.

Checked on 2026-10-22 with Codex CLI 0.159.0: `codex exec --sandbox read-only` started in this repo and attempted the router and discover commands. The read-only sandbox rejected both shell commands before they ran, so this check did not prove routing inside Codex. Parallel workers were not spawned there. The same router command passes in a normal local shell.

`AGENTS.override.md` in a subdirectory replaces that directory's `AGENTS.md` for Codex. Do not put an override in this repository that weakens `AGENTS.md`.
