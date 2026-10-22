# WF-02: Client Brief to Handover

Client brief, UX research, design, development, QA, release, handover.

## Entry requirements
- Signed scope and onboarding complete (WF-01 stage 8), or an equivalent brief with scope and acceptance criteria.
- Access to required accounts via invites. Locked decisions and locked assets recorded.
- Authorization: production deploy and DNS changes need the owner's explicit approval.

## Roles
| Role | Part |
|---|---|
| `delivery-manager` | Accountable for the engagement |
| `project-manager` | Plan, schedule, status |
| `requirements-specialist` | Requirements baseline |
| `ux-researcher` or `usability-researcher` | Research (scale to budget) |
| `information-architect` | Sitemap and navigation |
| `ux-designer`, `ui-designer` | Flows and screens |
| `creative-director` | Art direction for premium builds |
| `copywriter`, `ux-writer` | Copy |
| `design-reviewer` | Independent design review |
| `solution-architect` | Technical design |
| `frontend-developer` (+ framework specialist), `backend-developer`, `database-engineer` | Build |
| `code-reviewer` | Independent code review |
| `qa-lead`, `playwright-specialist`, `accessibility-tester`, `performance-tester` | Testing |
| `release-engineer`, `release-validation-specialist` | Release |
| `acceptance-coordinator` | Client UAT |
| `handover-specialist`, `client-training-specialist` | Handover |

## Stages
| # | Stage | Owner | Deliverables | Quality gate | Reviewer |
|---|---|---|---|---|---|
| 1 | Plan | `project-manager` | Plan with milestones, RAID log | Milestones map to scope items | `delivery-manager` |
| 2 | Requirements | `requirements-specialist` | Requirements doc, open questions | Each requirement testable; client-approved | `delivery-manager` |
| 3 | Research | `ux-researcher` | Research summary (scaled: 3 to 5 customer conversations or a competitor teardown for small budgets) | Insights tied to evidence and design implications | `research-lead` |
| 4 | Structure | `information-architect` | Sitemap, navigation, content model | Every requirement has a home | `ux-designer` |
| 5 | Flows | `ux-designer` | Flows and wireframes, mobile first | Edge and error states covered | `design-reviewer` |
| 6 | Visual design | `ui-designer` (direction from `creative-director`) | Hi-fi screens at 375, 768, 1440; specs | Brand and accessibility checks pass | `design-reviewer`, client approval |
| 7 | Copy | `copywriter`, `ux-writer` | Final copy in place | Voice rules, no invented claims | `editor` |
| 8 | Technical design | `solution-architect` | Architecture note, data model, ADRs | Covers auth, data, hosting, integrations, risks | `technical-lead` |
| 9 | Build | developers | Feature branches, unit tests | Tests and lint pass; matches designs | `code-reviewer` |
| 10 | Test | `qa-lead` with testers | Test plan, E2E runs, a11y and performance reports | Gates: no open critical or high bugs; WCAG 2.2 AA issues triaged; mobile LCP target met or waived | `qa-lead` sign-off |
| 11 | UAT | `acceptance-coordinator` | UAT script, feedback log, acceptance record | Client acceptance in writing | `delivery-manager` |
| 12 | Release | `release-engineer` with `release-validation-specialist` | Release plan, rollback plan, smoke results | Smoke tests pass on production after approved deploy | Owner approves deploy |
| 13 | Handover | `handover-specialist`, `client-training-specialist` | Handover pack, admin guide, training session plan | Access transferred; client can perform top 5 admin tasks | `delivery-manager` |

Parallel groups: stages 7 and 8 can run in parallel with 6; testers in stage 10 run in parallel.

## Human authorization points
Client approvals (requirements, designs, acceptance), production deploy, DNS and domain changes, any client communication.

## Smallest-team rules
- Landing page refresh: skip 3, 4 and 8; team of `ui-designer`, `frontend-developer`, `design-reviewer`, `playwright-specialist`.
- Content-only change: `copywriter` and `editor`, then `frontend-developer`.

## Exit criteria
Written client acceptance, production smoke tests passed, handover pack delivered, warranty period and support terms recorded, final invoice prepared by `invoicing-specialist`.

## Example invocation
"Run WF-02 for the salon website. Requirements are in `clients/salon/requirements.md`. Stop before deploy and show me the release plan."
