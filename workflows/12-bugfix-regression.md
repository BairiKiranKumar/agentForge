# WF-12: Bug Fixing and Regression Verification

Reproduce a defect, fix the smallest cause, and verify the fix without breaking the neighbouring behaviour.

## Inputs
- What the user did, what they expected, and what happened.
- Environment, version, and a way to reproduce.
- The repository. Read it before editing.
- Authorization. Default is a local fix and tests, not a production deploy.

## Specialists
`manual-tester` or `technical-support-specialist` to reproduce, `maintenance-engineer` or the framework owner to fix, `playwright-specialist` or `api-tester` for the regression check, `code-reviewer`. Lead: the engineer who edits.

## Parallel and sequential stages
Reproduction comes first. The fix depends on it. After the fix, the regression check and the code review run together. They write different reports. Integration waits for both. Do not start the review from an unfixed guess and call that parallel quality.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| Reproduce | `manual-tester` | none | none | steps and result | the bug is seen, or the report says it was not | `qa-lead` if it cannot be reproduced |
| Fix | `maintenance-engineer` | Reproduce | none | the smallest code change | local check | `code-reviewer` |
| Regression | `playwright-specialist` | Fix | Code review | test or a manual script that was run | pass, fail, or not run, with the command | `qa-lead` |
| Code review | `code-reviewer` | Fix | Regression | review notes | findings tied to lines | `technical-lead` if the fix widens scope |
| Integrate | `orchestrator` | Regression, Code review | none | one fix report | both reports present | Kiran for production release |

## Deliverables
Reproduction note, patch, regression evidence, review note.

## Validations
The original steps no longer fail, and a neighbouring path was checked. If a browser test could not be run, say that. Do not invent a green suite.

## Approval gates
Production release, data repair, and hotfix deploys need Kiran. A local branch does not.

## Exit criteria
The defect is fixed or still blocked with the missing input named, and the regression status is evidenced.

## Example invocation
"Run WF-12. The enquiry form submits twice on a slow phone. Reproduce, fix, and add a regression check. Do not deploy."

Plan file: `examples/plans/bugfix-regression.yaml`.
