# WF-21: Design-First

A reusable path for any digital experience: websites, applications, dashboards, e-commerce, mobile interfaces and marketing experiences. It does not assume a technology stack or a brand. Scale it to the work.

**Requirements, Research, Creative Exploration, Design Direction, Prototype, Review, Implementation, Visual QA, Refinement, Delivery.**

## Inputs
- Brief: goal, audience, main user action, constraints, deadline.
- Stack constraints, or permission for `technical-lead` to choose. Nothing in this workflow names a framework.
- Brand inputs if they exist. If none, `brand-strategist` or `brand-designer` joins; otherwise the direction defines the visual brand.
- Authorization. Default: local or preview build only, no publish, no deploy.

## Choose the tier first (`design-lead`)
| Tier | When | Stages used |
|---|---|---|
| S | Small change to an approved system (label, spacing, a component state) | Requirements, Implementation, light Visual QA. No exploration, no committee |
| M | New page or feature in an existing system | Requirements, short Research, one Design Direction, Review, Implementation, Visual QA |
| L | New product, brand-defining or high-visibility work | All stages, `high_visibility` rubric profile, human approval |

Record the tier and the reason in the brief. When unsure, choose the smaller tier and say what would move it up.

## Specialists
Research wave: `design-researcher`, `motion-researcher`, `design-skill-researcher` (only if the team lacks a capability), `ux-researcher` or `market-researcher` for domain and audience questions.
Creative wave: `creative-director` (owner), `ui-designer`, `interaction-designer`, `brand-designer`, `motion-designer`, `accessibility-designer` as the work needs.
Implementation wave: engineering specialists chosen by `technical-lead` for the project's stack (`frontend-architect`, `frontend-developer`, and any framework or CSS specialist the stack calls for).
Review wave: `design-reviewer` (independent), `accessibility-tester`, `performance-engineer`, `qa-lead` or a QA specialist.
`orchestrator` integrates. Add only the roles the tier needs.

## Parallel and sequential stages
Independent stages with finished inputs and separate output files run in parallel (`orchestration/parallel-execution.md`). If the runtime cannot spawn workers, run the same plan in dependency order and say so in the execution report.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| 1 Requirements | `requirements-specialist` or `product-manager` | none | none | `requirements.md` with acceptance criteria | Goal, audience, main action stated | requester |
| 2 Research | `design-researcher` | 1 | `motion-researcher`, `design-skill-researcher`, `market-researcher` | `design-research-brief.md`, KB entries | Sources dated; inspection level stated | `research-lead` for scope changes |
| 2b Motion research | `motion-researcher` | 1 | 2 | `motion-recommendation.md` | Each pick tied to a user need, with fallback | none |
| 2c Skill check | `design-skill-researcher` | 1 | 2, 2b | `skill-recommendation.md` | Only registry skills with status approved or conditional | Kiran for any installation |
| 3 Creative exploration | `creative-director` | 2, 2b | `brand-designer` | `concept-routes.md` | Routes differ in idea; difference test | none |
| 4 Design direction | `creative-director` | 3 | none | `art-direction.md`, `direction-approval.md` | Anti-slop defaults named and replaced or justified | Kiran or client (Tier L) |
| 5 Prototype | `ui-designer` | 4 | `interaction-designer`, `motion-designer` | prototype of the signature moment and one representative screen | Rendered at 375 and 1440 px | none |
| 6 Design review | `design-reviewer` | 5 | `accessibility-designer` | rubric score and verdict | Rendered evidence; independent | `design-lead` |
| 7 Implementation | engineering owner for the stack | 6 Ship | `motion-designer` support | working build | Builds locally | `code-reviewer` |
| 8 Visual QA | `design-reviewer` | 7 | `accessibility-tester`, `performance-engineer`, `qa-lead` | visual QA report with captures | Per `design-intelligence/guides/browser-research-and-qa.md`; tool tier stated | `design-lead` |
| 9 Refinement | stage owner for each finding | 8 | none | closed findings list | Re-review of listed findings only | `design-reviewer` |
| 10 Delivery | `orchestrator` | 9 | none | execution report, artifacts, QA report, open issues, approval record | Evidence per criterion | Kiran before any publish or deploy |

Tier S and M skip the stages their tier does not use. A skipped stage is listed in the report with the reason.

## Deliverables
Requirements, research brief, motion and skill recommendations (when used), concept routes, art direction and approval record, prototype, review reports with rubric scores, the build, a visual QA report with captures, the closed findings list, and one execution report that separates what was run from what was not.

## Validations
Rubric scored with `python tools/design_kb.py score`. Visual QA performed with the strongest tool tier available, stated in the report. If no browser tool exists, the QA report lists the missing evidence and the exact checks to run later. Never claim a render that did not happen.

## Approval gates
Direction approval (Tier L): Kiran or the client, recorded in the handoff `authorization` field. High-visibility Ship verdict: human approval required by the rubric profile. Publishing, deployment, spend, third-party skill installation and sending anything outside: explicit authorization per `AGENTS.md` section 3.

## Refinement rules
Iterate against documented findings only. Each change cites the finding id. No "while I am here" restyling. Maximum two revision rounds between the same producer and reviewer, then escalate to `design-lead`.

## Exit criteria
The profile's weighted minimum and floors are met with no open Blocker, required approvals are recorded, and every unverified item is listed as unverified.

## Example invocation
"Run WF-21 at Tier L for a new analytics product site. Draft through Visual QA on a local build. Do not publish."
