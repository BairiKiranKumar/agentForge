# Upgrade status: Design Intelligence System

Handoff file. Any agent can resume from here. Update the stage table and the log as you work. Brief source: the "Universal Design Intelligence System" upgrade request (project-agnostic, brand-agnostic, framework-agnostic).

Last updated: 2026-10-22 (complete, committed locally, not pushed)

## How to resume
1. Read `AGENTS.md`, then this file.
2. Run baseline checks: `python tools/validate.py`, `python -m unittest discover -s tests` (PowerShell; `python` is not on the bash PATH).
3. Pick the first stage that is not `done`. Respect "Owns files" so parallel workers do not collide.
4. After any change to roster or role files: `python tools/build_indexes.py`, then validate and test again.
5. Do not commit, push, or publish without Kiran's approval. Work stays uncommitted on branch `develop`.

## Baseline (before the upgrade, observed 2026-10-22)
- `python tools/validate.py`: 182 roles, 0 errors, 0 warnings.
- `python -m unittest discover -s tests`: 23 tests OK.

## Audit findings (observed by reading the repo)
- Existing design roles, all `status: untested`: `creative-director`, `design-reviewer`, `motion-designer`, `design-lead`, `ui-designer`, `interaction-designer`, `design-systems-specialist`, `accessibility-designer`, `brand-designer`, `illustrator`, `conversion-designer`.
- Existing research roles: `competitor-researcher` (business competitors, not visual), `ux-researcher`, `usability-researcher`.
- Engineering and QA roles exist for framework choice: `frontend-architect`, `frontend-developer`, `react-specialist`, `nextjs-specialist`, `angular-specialist`, `css-specialist`, `accessibility-engineer`, `performance-engineer`, `accessibility-tester`.
- Gaps (no existing owner): visual design reference research, design-skill discovery and vetting, motion reference research and a pattern library, a design knowledge base, a skill registry, a weighted design rubric, browser-evidence rules.
- Decision: upgrade `creative-director`, `design-reviewer`, `motion-designer`, `design-lead`, `orchestrator` (routing) in place. Add three roles in a new department `design-intelligence`: `design-researcher`, `design-skill-researcher`, `motion-researcher`. No duplicate of `ui-designer`, `interaction-designer`, `brand-designer`, `accessibility-specialist` (use `accessibility-designer` / `accessibility-tester`), `performance-specialist` (use `performance-engineer`), `qa-specialist` (use `qa-lead`), `domain researcher` (use `market-researcher`).
- Conventions: roster in `orchestration/roster.yaml`; four files per role (`AGENT.md` with 12 sections, `checklist.md` 15+ checks, `examples.md` 2+, `evaluation.md` 3+ tasks, "Status: untested"); validator `tools/validate.py` rejects em dashes and placeholders; routing in `runtime/routes.yaml`; workflows `workflows/NN-*.md`.
- Tooling limit observed: no rendered-browser tool is connected in this session. Research uses fetched page text only. Any entry made this way is labelled `method: fetched-html` and must not be described as visually inspected.

## Target layout
```
design-intelligence/
  <role>/ (design-researcher, design-skill-researcher, motion-researcher: 4 files each)
  README.md                      capability structure and ownership
  knowledge-base/                universal knowledge only. SCHEMA.md, INDEX.md (generated)
    references/ patterns/ motion/ typography/ color/ accessibility/ anti-slop/ critiques/
  skill-registry/                SCHEMA.md, skills/<id>.yaml, evaluations/<id>.md, REGISTRY.md (generated), policy.md
  rubric/                        design-review-rubric.md, anti-slop.md, rubric.yaml
  guides/                        browser-research-and-qa.md, research-run.md (scheduled-run workflow)
tools/design_kb.py               validate / search / index / freshness for KB and skill registry
workflows/21-design-first.md     universal design-first workflow
workflows/22-design-intelligence-refresh.md  external-runner research cycle
```

## Stages
| # | Stage | Owner | Owns files | Status |
|---|---|---|---|---|
| 0 | Audit repo, baseline checks | lead | this file | done |
| 1 | KB + skill-registry schemas | lead | `design-intelligence/knowledge-base/SCHEMA.md`, `design-intelligence/skill-registry/SCHEMA.md`, `policy.md` | done |
| 2 | Research wave (A skills, B motion, C references) | workers | see Target layout | done (all three reported; YAML quoting fixed by lead) |
| 3 | Roster + 3 new roles (4 files each) | lead | `orchestration/roster.yaml`, `design-intelligence/<role>/*` | done (validated 0 errors; run build_indexes later) |
| 4 | Upgrade creative-director, design-reviewer, motion-designer, design-lead | lead | those AGENT.md/checklist.md/evaluation.md | done (orchestrator routing handled via routes.yaml, stage 7) |
| 5 | Rubric + anti-slop | lead | `design-intelligence/rubric/*` | done (rubric.yaml, design-review-rubric.md, anti-slop.md) |
| 6 | Guides: browser research and QA, scheduled research run | lead | `design-intelligence/guides/*` | done except refresh-log.md stub (todo) |
| 7 | Workflows 21, 22; routes.yaml; CAPABILITY-MATRIX; parallel-execution; orchestrator table; design-first plan | lead | those files + `examples/plans/design-first.yaml` | done (README.md root and TEAM docs update pending in stage 10) |
| 8 | `tools/design_kb.py` + tests | lead | `tools/design_kb.py`, `tests/test_design_intelligence.py` | done; suite 45 tests, only failure = worker C YAML quoting in 2 KB files (re-check after C finishes) |
| 9 | Specialist evaluations (spec only, not run) | lead | `evaluation.md` files | done for 3 new + 4 upgraded roles (specs only; none run) |
| 10 | Rebuild indexes, validate, test, final report | lead | `BUILD-STATUS.md`, `design-intelligence/REPORT.md`, root README | done |

Status values: todo, in-progress, done, blocked.

## Rules for this upgrade
- No client, brand, industry or framework named as a default. Named external sites appear only as sourced references.
- Third-party skills are read, never installed or executed. Registry status starts at `candidate`.
- Evaluations stay `untested` until run and recorded in `evaluations/STATUS.md`.
- Never claim a site was "inspected" or screenshotted unless a rendering tool did it. Say `fetched-html`.
- No em dashes anywhere in new files.

## Log
- 2026-10-22: Audit done; baseline recorded; this file created.
- 2026-10-22: SCHEMA.md for KB and skill registry written. Research workers A (skills), B (motion), C (references/principles) launched in background.
- 2026-10-22: Stage 3 done: roster has department design-intelligence + 3 roles; all 12 files written; validate --roles OK.
- 2026-10-22: Stages 1, 5, 6 written (policy.md, rubric, anti-slop, browser guide, research-run guide). Next: stage 4 role upgrades, stage 8 tool tools/design_kb.py, stage 7 workflows/routes.
- 2026-10-22: Worker B (motion) done: 17 entries in knowledge-base/motion. Stage 4 done. tools/design_kb.py written. Workers A and C still running when last checked.
- 2026-10-22: Worker A (skills) done: 13 entries (0 approved; 9 conditional, 3 candidate, 1 rejected AGPL). Stage 7 done. design-intelligence/README.md + guides/refresh-log.md written. Worker C (references/principles) still running; one ref file had YAML title colon error (fix: quote the title).

## Open items / limitations (keep current)
- See design-intelligence/REPORT.md "Not verified / limitations" and "Recommendations". Main gap: no rendering tool, so all references are source-level.
- 2026-10-22: Worker C done; all checks green (185 roles 0 errors; 45 tests OK; design_kb validate 0 errors). REPORT.md written.
- 2026-10-22 (session 1, follow-up brief): URL check run (77 URLs, 1 transient timeout, retry 200); router verified WF-21/WF-22 and existing WF-10/12/13/16; 5 example plans schedule; diff of existing files is additive only. E2E evaluation in `evaluations/runs/design-intelligence-e2e/` (research worker, producer worker, independent reviewer blind A/B with a deliberately generic control). Remaining: collect reviewer output, update REPORT.md with E2E results, rebuild + full checks, commit locally (no push).
- 2026-10-22: Follow-up complete: E2E run recorded, REPORT.md updated, all checks green (185 roles/0 errors; 45 tests OK; KB 47/13 0 errors; secrets clean). Committed locally on develop; NOT pushed.
