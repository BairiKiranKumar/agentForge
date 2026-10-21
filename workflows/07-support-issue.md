# WF-07: Support Issue Resolution

Support issue, triage, reproduction, fix, verification, customer response draft.

## Entry requirements
- The issue report as received (message, screenshot, ticket) and the affected product or client.
- Authorization: production hotfix deploys and customer replies need approval.

## Roles
`support-triage-specialist` (lead for intake), `technical-support-specialist` (reproduction), owning developer (fix), `code-reviewer`, `playwright-specialist` or `manual-tester` (verification), `incident-coordinator` (only for outages or data issues), `knowledge-base-writer` (if a help article is needed), `client-communication-specialist` (response draft).

## Stages
| # | Stage | Owner | Deliverables | Quality gate | Reviewer |
|---|---|---|---|---|---|
| 1 | Triage | `support-triage-specialist` | Ticket with severity (S1 outage/data loss, S2 major feature broken, S3 minor, S4 question), category, owner, first-response draft | Severity per matrix; S1 escalated to `incident-coordinator` immediately | `delivery-manager` for S1/S2 |
| 2 | Reproduce | `technical-support-specialist` | Repro steps, environment, expected vs actual, logs, workaround | Reproduced or marked "cannot reproduce" with what was tried | developer accepts |
| 3 | Fix | owning developer (`maintenance-engineer` for shipped projects) | Minimal-diff fix with test that fails before and passes after | Root cause stated; regression test added | `code-reviewer` |
| 4 | Verify | `playwright-specialist` or `manual-tester` | Verification note on preview, then production smoke after approved deploy | Original repro now passes; related flows unaffected | `qa-lead` for S1/S2 |
| 5 | Respond | `client-communication-specialist` | Customer reply draft: what happened, what was fixed, any action needed | Honest, no blame, no overpromising | Kiran approves sending |
| 6 | Learn | `knowledge-base-writer` / `incident-coordinator` | Help article update or postmortem for S1/S2 | Action items have owners | `documentation-curator` |

## Exit criteria
Fix verified, reply approved and sent by Kiran, ticket closed with root cause recorded.

## Example invocation
"A parent says the fee receipt PDF is blank on their phone. Run WF-07; draft the reply but don't send."
