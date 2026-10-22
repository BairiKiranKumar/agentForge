# WF-23: Quality Gates

Decide whether a build, site or application meets the engineering standards for its product type and risk profile, with recorded evidence. Works with any stack and any agent environment.

## Inputs
- Product types and the quality profile (`lightweight`, `standard`, `high_assurance`) from the project configuration. If missing, `qa-lead` proposes one with reasons and the owner confirms.
- A reviewable build or preview URL and the list of what was and was not run.
- Authorization. Default: local or preview only. Security tests against any real system need written scope from its owner.

## Specialists
Selected by `python tools/quality_gate.py select --profile <profile> --types <types>`. Typical: `accessibility-engineer`, `accessibility-tester`, `performance-engineer`, `performance-tester`, `application-security-engineer`, `security-testing-specialist`, `frontend-developer`, `qa-lead`, `release-validation-specialist`, `design-reviewer` for rendered design review, `privacy-specialist`, `seo-specialist` for public websites. `orchestrator` integrates. Do not activate specialists that own no applicable requirement.

## Parallel and sequential stages
Area checks read the same build and write separate evidence files, so they run in parallel when the runtime can spawn workers (`orchestration/parallel-execution.md`). Independent review follows the check it reviews.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| Scope | `qa-lead` | none | none | profile, product types, applicable list | `quality_gate.py applicable` output | project owner for the profile |
| Area checks | area owners | Scope | other areas | evidence per requirement | executed, not planned | none |
| Design review | `design-reviewer` | Scope | area checks | rubric score and verdict | rendered evidence | human approval for high_visibility |
| Independent review | area reviewers | matching area check | other reviews | reviewer sign-off | different person or agent | none |
| Evaluate | `qa-lead` | all above | none | `results.yaml` and evaluation output | `quality_gate.py evaluate` | owner for exceptions and release |
| Report | `orchestrator` | Evaluate | none | execution report | executed versus planned separated | owner |

## Deliverables
Applicable-requirements list, evidence records per requirement, design review result, results file, evaluation output, exceptions with approvals, and one execution report that separates what was run from what was only planned and lists unavailable tools.

## Validations
`python tools/quality_gate.py evaluate results.yaml` returns PASS, PASS_WITH_EXCEPTIONS, FAIL or BLOCKED. Automated results alone never establish accessibility conformance, and planned checks never count.

## Approval gates
Exceptions, the release decision for `high_assurance`, and any production deploy need the owner's explicit approval recorded in the handoff `authorization` field.

## Exit criteria
Outcome is PASS or PASS_WITH_EXCEPTIONS with approvals recorded, or every FAIL and BLOCKED item has an owner and next step.

## Example invocation
"Run WF-23 at the standard profile for a website and a web-app. Local preview only. Report executed versus planned checks."
