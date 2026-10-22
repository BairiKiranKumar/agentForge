# Design Intelligence upgrade: execution report

Date: 2026-10-22. Branch `develop`, changes uncommitted. Runtime: Claude Code, one lead plus three parallel research workers (general-purpose subagents, background). Handoff state: `UPGRADE-STATUS.md`.

## Result
Implemented and validated structurally; a completion pass and a small end-to-end run are described at the end. Not evaluated behaviourally: every new or upgraded role is still `status: untested`. No skill is approved. No rendered-browser inspection took place in this run.

## Waves
| Wave | Agent | Files owned | Outcome |
|---|---|---|---|
| Lead | session lead | roster, 3 new roles (12 files), 4 role upgrades, rubric, guides, policy, workflows 21/22, routes, tool, tests, docs | done |
| Research (parallel) | worker A, skills | `skill-registry/skills/*`, `evaluations/*`, `research-notes-A.md` | 13 entries: 9 conditional, 3 candidate, 1 rejected |
| Research (parallel) | worker B, motion | `knowledge-base/motion/*` | 17 pattern entries, sources log |
| Research (parallel) | worker C, references and principles | `knowledge-base/{references,patterns,typography,color,accessibility,anti-slop}/*` | 12 references, 18 principles |

Workers wrote disjoint paths. The lead fixed three YAML quoting defects in worker output (micro-interactions, charity: water, type-scale entries).

## What changed
- **Roster:** department `design-intelligence`; roles `design-researcher`, `design-skill-researcher`, `motion-researcher`. 185 roles total.
- **Upgraded in place (no duplicates):** `creative-director` (exploration, direction approval record, rejection authority), `design-reviewer` (rubric, evidence tiers, profiles, anti-slop), `motion-designer` (library-fed, library-neutral specs), `design-lead` (tiers, rubric governance). Each gained checklist items and an evaluation Task 4.
- **Knowledge base:** 47 sourced entries, schema, generated index. Universal only.
- **Skill registry:** schema, policy, 13 vetting records with evaluations, generated registry.
- **Rubric:** 10 weighted criteria, standard and high_visibility profiles, gates, 19 anti-slop signals with a justification test.
- **Workflows:** WF-21 design-first (tiers S/M/L), WF-22 refresh; routes; capability matrix rows; orchestrator table; parallel-execution section; `examples/plans/design-first.yaml`.
- **Guides:** browser research and visual QA with tool tiers 0 to 3; refresh run procedure; refresh log.
- **Tooling:** `tools/design_kb.py` (validate, search, index, freshness, score).

## Verified (observed, run in this session)
- `python tools/validate.py`: 185 roles, 0 errors, 0 warnings (baseline was 182, 0, 0).
- `python -m unittest discover -s tests`: 45 tests OK (baseline 23; 22 new in `tests/test_design_intelligence.py`).
- `python tools/design_kb.py validate`: 47 entries, 13 skills, 0 errors, 6 warnings (shared primary source URLs, benign).
- `python tools/scan_secrets.py`: clean. `python -m runtime.scheduler plan examples/plans/design-first.yaml`: research wave and QA wave run in parallel.
- `python tools/build_indexes.py`: 185 Claude Code agent files, 0 missing.

## Not verified / limitations
- **No rendering tool.** All 12 references are `fetched-html`, `viewports_checked: []`. No screenshots, no visual or motion judgement, no Core Web Vitals measurement. Visual QA and regression are documented procedures, not exercised.
- **Skill research:** shallow clones, nothing executed, scripts not read line by line, no effectiveness evidence found for any skill, cross-agent compatibility untested. Stars and activity came from unauthenticated API calls.
- **Gaps in discovery:** no dedicated typography, responsive or visual-regression skill evaluated.
- **Sources that failed:** codrops (403, search snippets only), godly.website (redirects), three bot-protected sites skipped, several MDN/Three.js pages truncated or 404. GSAP licence terms beyond the pricing statement are `[Unverified]`. ScrollSmoother availability is contradictory in GSAP docs.
- **Scheduling:** no scheduler exists; the refresh is a procedure for an external runner. URL checks (`--check-urls`) were not run.
- **Independence:** the lead authored the role definitions and rubric; no independent reviewer pass or evaluation task has been run, so no role is passed.
- Rubric weights and thresholds are design judgements, uncalibrated.

## Recommendations
1. Connect Playwright or a browser MCP and run a rendered pass on the 12 references and on one real build; record the tool tier.
2. Run the Task 3 (boundary) evaluations for the three new roles and `design-reviewer` first, scored by a different agent, and record results in `evaluations/STATUS.md`.
3. Kiran decides on `anthropic-frontend-design` and `gsap-skills` (closest to approval); do not install `impeccable` without a full hook and binary review.
4. Calibrate the rubric with two reviewers on three captures.
5. Configure a real scheduler if continuous refresh is wanted, then log runs in `guides/refresh-log.md`.
6. Commit when ready (not done; needs your instruction).

---

# Completion pass (follow-up brief, 2026-10-22)

## Actual changes in this pass
- Fixed the two YAML quoting errors in worker C output (`ref-charitywater-org`, `type-scale-and-pairing-systems`) and one in worker B output (`micro-interactions`). Worker C had finished its 12 references and 18 principles before the pass; no further reference research was added.
- Cross-reference check: backticked repo paths in all new Markdown resolve (one relative path in the browser guide was made explicit). `tools/validate.py` global link check passes.
- Added section 9 "Capture pitfalls" to `guides/browser-research-and-qa.md` from the end-to-end run.
- Added `evaluations/runs/design-intelligence-e2e/` (run record, captures, capture script, reviews).

## Verification (observed in this pass)
| Check | Result |
|---|---|
| `python tools/design_kb.py validate` | 47 KB entries, 13 skills, 0 errors, 6 warnings (shared primary source URLs) |
| `python tools/design_kb.py freshness --check-urls` | 77 unique URLs; 1 problem, charity: water HEAD timed out, manual GET returned 200 (transient). Other sources responded. Note: HEAD success shows the URL resolves, not that the content still matches the entry |
| `python tools/build_indexes.py` | 185 roles, 185 Claude Code agent files, 0 missing |
| `python tools/validate.py` | 185 roles, 0 errors, 0 warnings |
| `python -m unittest discover -s tests` | 45 tests OK (23 pre-existing, 22 new) |
| `python tools/scan_secrets.py` | no obvious credentials |
| Routing (`python -m runtime.router ... --check-roster`) | "art direction and creative direction" routes to WF-21; "design knowledge base, skill registry, motion library" routes to WF-22; carousel to WF-16, bugfix to WF-12, premium website to WF-10, "ui design" to WF-13 (unchanged) |
| Planning (`python -m runtime.scheduler plan`) | `examples/plans/design-first.yaml` plans 9 waves with research and QA waves parallel; the four pre-existing example plans still plan |
| Backward compatibility | `git diff --numstat` on pre-existing tracked files shows additions only apart from generated indexes (`TEAM-INDEX.md`, `SOURCE-MANIFEST.md`, `evaluations/STATUS.md`, `registry/agents.json`, README layout line); all 23 pre-existing tests pass unchanged |

The orchestrator "route and plan" is checked through the router and scheduler tools and the orchestrator's workflow table. No live orchestrator agent session was run against WF-21 or WF-22.

## Skill approvals
No skill is `approved`. The validator refuses `approved` without a 40-character pinned SHA, a clear licence, an evaluation file and an effectiveness statement, and a unit test asserts none is approved. Approval also requires Kiran per `skill-registry/policy.md`. The security, licence and compatibility review exists per skill in `skill-registry/evaluations/` but compatibility was read from READMEs, not tested.

## End-to-end evaluation
Record: `evaluations/runs/design-intelligence-e2e/README.md`. Summary: a research subagent produced a brief (fetch only; it self-reported falling short of its role's own standards on discovery channels, shortlist size and breadth); a producer subagent built a candidate page from it; the lead made a deliberately generic control page; both were captured with headless Chrome (static, tool tier 2) and reviewed blind by an independent reviewer subagent against the rubric. The control scored 31.5 percent (Rethink, blocker plus 8 failed anti-slop signals); the candidate scored 68.5 percent (Revise, accessibility floor missed). The tool output was re-run by the lead and reproduces.
Reviewer finding that did not hold: a "chart bars wrong" Major was a capture taken mid-animation. Re-capture after settling showed correct bars. The scores were not edited.

## Limitations and outstanding risks
- This is one sample with one reviewer from the same model family as the producers. It is a smoke test of the workflow and the tool, not a role evaluation. All roles remain `untested`; `evaluations/STATUS.md` was not changed to passed.
- The research stage's honest shortfalls suggest the `design-researcher` standard (three channels, 8 to 12 candidates, four styles) is hard to meet with a summarising fetch tool and no renderer. Either relax the standard for fetch-only sessions or supply a better tool.
- Headless Chrome cannot render below about 500 px; 375 px captures use an iframe. Capture timing matters for animated pages.
- Reference entries are source-level only; none was visually inspected.
- Rubric weights and profile thresholds are uncalibrated.
- Skill evidence is thin: no effectiveness data, shallow clones, scripts not read line by line.
- No scheduler is configured; WF-22 is a procedure.
- `design-intelligence/knowledge-base/critiques/` is empty; the e2e reviews could be promoted to critique entries after a second reviewer confirms them.
