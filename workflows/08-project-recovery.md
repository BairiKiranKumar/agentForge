# WF-08: Existing Project Audit, Recovery Plan, Delivery

For inherited, stalled or troubled projects.

## Entry requirements
- Repository and environment access (read), current scope documents, client expectations and deadlines as known.
- Authorization: no production changes during the audit.

## Roles
`delivery-manager` (lead), `technical-lead`, `solution-architect`, `code-reviewer`, `qa-lead`, `accessibility-tester`, `performance-tester`, `application-security-engineer`, `design-reviewer`, `scope-change-manager`, `risk-manager`, `estimation-specialist`, `project-manager`, `client-communication-specialist`.

## Stages
| # | Stage | Owner | Deliverables | Quality gate | Reviewer |
|---|---|---|---|---|---|
| 1 | Fact-finding | `delivery-manager` | What was promised vs what exists; stakeholder list; deadlines | Sourced from documents and messages, not memory | `delivery-lead` |
| 2 | Audit (parallel) | `code-reviewer`, `qa-lead`, `accessibility-tester`, `performance-tester`, `application-security-engineer`, `design-reviewer` | Audit reports with severity and evidence; feature status table (implemented, partial, UI-only, broken, missing) | Every status verified in code or by running the app | `technical-lead` consolidates |
| 3 | Root causes | `technical-lead` with `risk-manager` | Root cause list (scope, quality, process, communication), risk register | Causes linked to evidence | `delivery-lead` |
| 4 | Recovery plan | `delivery-manager` with `estimation-specialist`, `scope-change-manager` | Options (fix forward, partial rebuild, de-scope), estimates with ranges, recommended plan | Each option has cost, time, risk; scope changes explicit | Kiran |
| 5 | Client alignment | `client-communication-specialist` | Recovery message and meeting agenda draft | Honest status; no blame; clear decisions requested | Kiran approves and sends |
| 6 | Delivery | `project-manager` | Hands into WF-02 stages 9 to 13 with the recovery plan as scope | Weekly status against recovery milestones | `delivery-manager` |

## Example invocation
"Audit an Angular application for accessibility, performance and test gaps." (Run stages 2 and 3 with `angular-specialist`, `accessibility-tester`, `performance-tester`, `automation-engineer`; output a prioritized gap report.)

## Exit criteria
Recovery plan approved by Kiran and client, or project formally closed with lessons recorded.
