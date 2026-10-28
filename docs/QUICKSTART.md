# Quickstart

A short path from clone to a first coordinated task. Everything here runs without paid services.

## 1. Install and verify
```text
git clone <repository-url> agentForge
cd agentForge
python -m pip install -r requirements.txt
python tools/validate.py
python -m unittest discover -s tests
```
Pin a full commit SHA for anything you depend on (`docs/security/secure-installation.md`).

## 2. Choose your agent environment
| Environment | Start here |
|---|---|
| Claude Code | `python tools/build_indexes.py`, then `./integrations/claude-code/install.sh --project <your-project> --departments dev,qa,design` |
| Cursor | `integrations/cursor/BOOTSTRAP.md` |
| OpenAI Codex | `integrations/codex/BOOTSTRAP.md` (reads `AGENTS.md`) |
| Google Antigravity | `integrations/antigravity/BOOTSTRAP.md` |
| Other | `docs/INSTALL.md` |
Install only the departments you need. Every installed role adds to the agent's routing context.

## 3. Create your private configuration
```text
mkdir workspace
copy config/templates/organization.example.yaml workspace/organization.yaml
python -m runtime.config show
```
`workspace/` is ignored by Git. Put real organization, brand and project profiles there. See `docs/configuration.md`.

## 4. Run a task
1. Route it: `python -m runtime.router "Build a landing page for a small clinic" --check-roster`.
2. Read the workflow it names in `workflows/`.
3. Plan waves: `python -m runtime.scheduler plan examples/plans/premium-website.yaml`.
4. Give your agent the workflow, the role files for the stages, and the brief. Ask it to use the smallest team that meets the acceptance criteria.
5. Keep human approval for anything that sends, publishes, spends, deploys or tests live systems.

## 5. Check quality
```text
python tools/quality_gate.py applicable --profile standard --types website
python tools/quality_gate.py select --profile standard --types website
```
Record evidence per requirement and evaluate with `python tools/quality_gate.py evaluate results.yaml`. See `quality-gates/README.md`.

## Operating rules in brief
1. Smallest sufficient team. A one-file edit stays with one owner.
2. Default authorization is none. Drafts only until a human approves.
3. Handoffs use `orchestration/handoff-format.md`.
4. Never invent facts, results or credentials. Label what is unverified.
5. A reviewer never reviews their own output.

## Troubleshooting
See `docs/TROUBLESHOOTING.md`.
