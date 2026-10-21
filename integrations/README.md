# Tool adapters

agentForge stays in this GitHub repository. A project should fetch the files it needs instead of copying all 180-plus roles.

| Tool | How it learns the rules | Adapter |
|---|---|---|
| Cursor | Root `AGENTS.md` plus `.cursor/rules/agentforge.mdc` when this repo is the workspace | [cursor/BOOTSTRAP.md](cursor/BOOTSTRAP.md) |
| Claude Code | Generated subagents and `install.sh` | [claude-code/install.sh](claude-code/install.sh) |
| OpenAI Codex | Root `AGENTS.md` (Codex reads it automatically) | [codex/BOOTSTRAP.md](codex/BOOTSTRAP.md) |
| Google Antigravity | Root `AGENTS.md` and `.agents/rules/` | [antigravity/BOOTSTRAP.md](antigravity/BOOTSTRAP.md) |
| Anything else that can read a file | `python -m runtime.discover` | [../docs/INSTALL.md](../docs/INSTALL.md) |

Pin the ref in `agentforge.lock` or pass `--ref` with a full commit SHA. If the network fails, discovery uses the cache, then a local checkout, then stops. It does not invent a missing rule, and it does not execute fetched files.
