# Contributing

agentForge is a set of role definitions, workflows, and a small runtime. Changes should keep those three in agreement.

## Roles
1. Add the role under `orchestration/roster.yaml` with a slug, department, mission, owns, and excludes. Aliases must be unique.
2. Create `<department>/<slug>/AGENT.md`, `checklist.md`, `examples.md`, and `evaluation.md`.
3. Match the twelve section headings already used by `tools/validate.py`.
4. Status starts at `untested`. Do not mark a role passed without a row in `evaluations/STATUS.md`.
5. If you extend an existing role instead of adding one, say so in the roster excludes so two roles do not own the same artifact.

## Checks
```text
python -m pip install -r requirements.txt
python tools/validate.py
python tools/build_indexes.py
python -m unittest discover -s tests
python tools/scan_secrets.py
```

`build_indexes.py` rewrites `TEAM-INDEX.md`, `SOURCE-MANIFEST.md`, `evaluations/STATUS.md` (keeping recorded results), `registry/agents.json`, and `integrations/claude-code/agents/`. Commit those generated files with the role change.

## Brands and safety
New client work gets a new folder in `brands/`. Do not put secrets, tokens, or client credentials in the repo. Do not add instructions that tell agents to ignore higher-priority safety rules.

## Pull requests
Use a branch. Do not force-push. The default branch on GitHub is `develop`.
