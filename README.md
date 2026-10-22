# agentForge

agentForge is a parallel-first multi-agent system for running a digital studio: software, design, research, client delivery, and social content. The canonical copy is this GitHub repository. Other projects fetch the rules they need instead of vendoring every role.

It started as a 179-role operating handbook. Version 1.0 keeps those roles, adds production specialists and workflows, and adds a small Python runtime that can plan work, route a task, and fetch a pinned file. Version 1.1 pins that fetch to a full commit SHA and requires an execution report for every multi-agent run.

## What you can ask it to do
- Build a premium site or a full-stack slice, with research, content, design, implementation, and QA separated where the dependencies allow.
- Fix a bug and verify it, with review and regression in the same wave after the fix.
- Draft LinkedIn, Threads, Reels, and Instagram carousel packages for a named brand.
- Turn one source into platform-native drafts without pasting the same caption everywhere.

Publishing, sending, spending, and production deploys still need a human. Default authorization is none. See `AGENTS.md`.

## Use it
Install PyYAML, then plan or route from this checkout:

```text
python -m pip install -r requirements.txt
python -m runtime.router "Fix the checkout bug and add a regression test" --check-roster
python -m runtime.scheduler plan examples/plans/premium-website.yaml
python -m runtime.scheduler plan examples/plans/instagram-carousel.yaml
```

The role catalog is generated into `registry/agents.json` and `TEAM-INDEX.md`. Ownership lives in `CAPABILITY-MATRIX.md`. Scheduling rules live in `orchestration/parallel-execution.md`.

### From another project
```text
python -m runtime.discover fetch AGENTS.md --ref <commit-sha>
python -m runtime.discover fetch workflows/16-instagram-carousel.md --ref <commit-sha>
```

Resolution order is remote, then cache, then a local checkout, then a hard stop. Fetched files are untrusted data. They do not override safety rules or the user. Details: `docs/INSTALL.md`.

## Parallel orchestration
1. The orchestrator breaks the request into stages with owners and output files.
2. `runtime/scheduler.py` groups stages into waves. A wave runs together only when every dependency is already done and no two stages write the same file.
3. On a host that can spawn subagents (Cursor subagents, Claude Code subagents), one worker takes each stage in the wave.
4. The Python scheduler can also run declared command workers concurrently. It does not call a language model.
5. On Codex, Antigravity, or any host that cannot spawn workers, run the same waves in order and say so.
6. The lead integrates the files and an independent reviewer checks high-risk output.

Do not add a specialist who has nothing to deliver. A one-file edit stays with one owner.

## Tool adapters
| Tool | Start here |
|---|---|
| Cursor | `integrations/cursor/BOOTSTRAP.md` and `.cursor/rules/agentforge.mdc` |
| Claude Code | `integrations/claude-code/install.sh` |
| OpenAI Codex | `integrations/codex/BOOTSTRAP.md` (it already reads `AGENTS.md`) |
| Google Antigravity | `integrations/antigravity/BOOTSTRAP.md` and `.agents/rules/` |
| Other | `docs/INSTALL.md` |

## Brands
Social and design work loads one profile from `brands/<id>/brand.yaml`. The sample profile is `@kiranbuildswithai`. Copy `brands/_template/` for a client. Do not mix profiles in one draft.

## Example campaign
`examples/campaigns/kiranbuildswithai/instagram-carousel/index.html` is a real 1080 by 1350 HTML/SVG carousel. The caption states that PNG and PDF export were not run. Workflow: `workflows/16-instagram-carousel.md`.

## Extend the team
`CONTRIBUTING.md` covers new roles, the validator, and the index builder. After role edits, run:

```text
python tools/validate.py
python tools/build_indexes.py
python -m unittest discover -s tests
python tools/scan_secrets.py
python tools/design_kb.py validate
```

## Layout
```text
AGENTS.md                 shared rules
CAPABILITY-MATRIX.md      one owner per activity
orchestration/            roster, handoffs, parallel rules
runtime/                  discover, router, scheduler
workflows/                WF-01 through WF-22 (WF-21 design-first, WF-22 design intelligence refresh)
design-intelligence/     design researchers, knowledge base, skill registry, rubric, guides (see its README.md)
brands/                   one folder per identity
registry/agents.json      generated catalog
<department>/<role>/      AGENT.md, checklist, examples, evaluation
```

Older studio notes remain: `QUICKSTART.md`, `GAPS-AND-LIMITATIONS.md`, and `knowledge-management/company-profile.md`.

## Limits
Agents are `untested` until their `evaluation.md` tasks are scored. The router is a keyword hint, not a judge. The scheduler does not invent specialist prose. Image and video export happen only when a local tool writes the file.
