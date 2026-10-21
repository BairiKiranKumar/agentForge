# Claude Code from the canonical repo

Local install remains:

```bash
python3 tools/build_indexes.py
./integrations/claude-code/install.sh --project /path/to/project --departments dev,qa,design
```

Prefer a department list. Installing every role adds every description to routing context.

To stay on a pinned revision without a full copy, fetch the orchestrator and the roles you need:

```text
python -m runtime.discover fetch integrations/claude-code/agents/orchestration/orchestrator.md --ref <sha>
```

Generated agent files are created by `tools/build_indexes.py`. Do not edit them by hand. Edit the role's `AGENT.md`, then rebuild.

Claude Code subagents are the parallel workers when this host is Claude Code. The orchestrator assigns exclusive files per wave. Publishing and deploys still follow `AGENTS.md`.
