# WF-11: Full-stack Application Development

Ship an application slice with a shared contract before frontend and backend proceed in parallel.

## Inputs
- The user job, the smallest slice that proves it, and the data it touches.
- Auth, privacy, and hosting constraints.
- Existing repository. Inspect it before choosing a stack.
- Authorization for migrations and deploys. Default is a branch and local checks only.

## Specialists
`solution-architect`, `frontend-developer`, `backend-developer`, `database-engineer` when the schema changes, `api-specialist`, `api-tester`, `code-reviewer`, `application-security-engineer` when auth or personal data is involved. Lead: `solution-architect` until the contract is accepted, then the two implementers.

## Parallel and sequential stages
The contract is sequential and blocking. After it is written, frontend and backend are parallel and must own different directories. QA waits for both. Security review can start from the contract before the code lands, then update from the diff.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| Contract | `solution-architect` | none | none | API and data notes | one slice, open questions listed | `technical-lead` |
| Frontend | `frontend-developer` | Contract | Backend | UI on the contract | local run | `code-reviewer` |
| Backend | `backend-developer` | Contract | Frontend | handlers and persistence | tests that exist in the repo | `code-reviewer` |
| API QA | `api-tester` | Backend | security pass | test notes | requests that were sent | `qa-lead` |
| Integrate | `orchestrator` | Frontend, API QA | none | one branch report | conflicts resolved | Owner for production migration or deploy |

## Deliverables
Contract, frontend slice, backend slice, test notes, and a list of files each role owned.

## Validations
Run the repository's tests. Do not claim they passed without a command log. Schema changes stay off production databases.

## Approval gates
Personal data handling needs `privacy-specialist` consulted before build, and the owner for any production migration. Deploys stay gated.

## Exit criteria
The slice works against the contract on a safe environment, reviews are attached, and production is untouched unless authorized.

## Example invocation
"Run WF-11 for a role-based enquiry inbox. Branch only. No production migration."
