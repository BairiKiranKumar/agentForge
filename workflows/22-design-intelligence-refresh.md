# WF-22: Design Intelligence Refresh

A repeatable research cycle for the shared design knowledge base and the skill registry. Designed to be started by an external runner such as a cron job, a CI schedule or a scheduled agent session. agentForge does not schedule itself. See `design-intelligence/guides/research-run.md` for commands and the report format.

## Inputs
- Scope: which categories to refresh (references, patterns, motion, skills).
- Tool tier available (`design-intelligence/guides/browser-research-and-qa.md`).
- Whether outbound URL checks are allowed in this environment.
- Authorization: proposals and reports only. Merging status changes and any installation need approval.

## Specialists
`design-researcher`, `motion-researcher`, `design-skill-researcher`. `documentation-curator` reviews structure. `orchestrator` integrates.

## Parallel and sequential stages
The three research stages read different sources and write different folders, so they run in parallel when the runtime can spawn workers.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| Discover references | `design-researcher` | none | motion, skills | proposed entries under `proposals/references/` | Sources dated; method stated | none |
| Discover motion | `motion-researcher` | none | references, skills | proposed entries under `proposals/motion/` | Docs checked; fallbacks present | none |
| Discover skills | `design-skill-researcher` | none | references, motion | proposed registry entries and evaluations | Ten criteria; nothing executed | Kiran for `approved` |
| Freshness scan | `orchestrator` | none | discovery stages | stale and broken list from `design_kb.py freshness` | Command output attached | none |
| Compare and select | `documentation-curator` | all above | none | accepted, merged and rejected list | Deduplicated by URL and id | `design-lead` |
| Report | `orchestrator` | compare | none | `reports/refresh-<date>.md` | Matches the report format | none |

## Deliverables
Proposed additions, proposed updates, flagged stale, broken and obsolete entries, skill evaluations, and one concise run report.

## Validations
`python tools/design_kb.py validate` passes on the proposed state. `freshness` output is attached. The report states which sources could not be read and what was not verified.

## Approval gates
Proposals only until reviewed. Skill status `approved`, installation, paid sources and publishing need Kiran. Third-party code is read, never executed.

## Exit criteria
Report written, validation run, `design-intelligence/guides/refresh-log.md` updated with runner, date and result. Do not claim continuous monitoring unless a real scheduler's run history exists.

## Example invocation
"Run WF-22 for motion and skills only. Read-only, proposals in a branch, report at the end."
