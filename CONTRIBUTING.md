# Contributing

agentForge is a set of role definitions, workflows, engineering standards, quality gates and a small runtime. Changes should keep them in agreement. Read `AGENTS.md` first and follow `CODE_OF_CONDUCT.md`.

## Ground rules
1. **No private data.** Do not commit personal names or handles that are not public attribution, client or project information, real domains tied to private work, credentials, local machine paths, logs from real work, or screenshots of real client work. Use fictional organizations and synthetic data. Keep real profiles in your private workspace (`docs/configuration.md`).
2. **Be project-, brand-, framework- and vendor-neutral.** Do not hard-code a person, organization, region, client, framework or provider as a default. Region-specific knowledge goes in `regional-packs/`.
3. **Do not weaken the safety floor** in `AGENTS.md` sections 1, 3, 4, 5 or in `config/defaults.yaml`.
4. **Verify licenses.** Only adapt from sources whose licenses permit it, record them in the role's frontmatter, and keep attribution (`SOURCE-MANIFEST.md`, `sources/licenses/`, `NOTICE`). Never copy proprietary design assets or code. Third-party skills are reviewed per `design-intelligence/skill-registry/policy.md` and are never approved without that review.
5. **Honest evidence.** Do not claim a test, scan, conformance or evaluation that was not run. Label anything unverified.

## Setup and checks
```text
python -m pip install -r requirements.txt
python tools/validate.py
python tools/build_indexes.py          # regenerates indexes and agent files; commit the output
python tools/design_kb.py validate
python tools/quality_gate.py validate
python -m unittest discover -s tests
python tools/scan_secrets.py
python tools/privacy_scan.py
```
CI runs the same checks (`.github/workflows/ci.yml`). Optional local tools (browsers, accessibility and performance tools) are described in `engineering-standards/` and are never required for the basic checks.

To catch your own identity terms before pushing, list them one regular expression per line in `.agentforge/private/identity-patterns.txt` (ignored by Git). `tools/privacy_scan.py` loads it.

## Roles
1. Add the role to `orchestration/roster.yaml` with slug, department, mission, owns and excludes. Aliases must be unique. Prefer extending an existing role over creating a duplicate; say so in `excludes`.
2. Create `<department>/<slug>/AGENT.md`, `checklist.md`, `examples.md` and `evaluation.md`, from `templates/`. See `templates/AUTHORING-GUIDE.md`.
3. Status starts at `untested`. Do not mark a role passed without recorded results in `evaluations/STATUS.md`.

## Standards and quality gates
Standards live in `engineering-standards/<area>/requirements.yaml` (schema in `engineering-standards/SCHEMA.md`). Gates are in `quality-gates/`. A new requirement needs a read source with a retrieval date, an owner and a different reviewer, a severity, and evidence. `python tools/quality_gate.py validate` checks references.

## Knowledge base and skill registry
Add entries following `design-intelligence/knowledge-base/SCHEMA.md` and `design-intelligence/skill-registry/SCHEMA.md`. Run `python tools/design_kb.py validate`.

## Pull requests
Work on a branch and open a pull request using the template. Do not force-push shared branches. Maintainers decide merges and releases.

## Licensing of contributions
agentForge is licensed under the Apache License 2.0 (`LICENSE`). By contributing you confirm you have the right to submit the work and that it is provided under the same license.
