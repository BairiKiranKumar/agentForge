# WF-24: Public Release Audit

A repeatable review before a repository, framework or content set is made public or distributed. It finds privacy, license, security and honesty problems, and ends in a human decision sheet. It never pushes, merges, rewrites history, changes visibility, publishes or approves third-party material. It works for any project and stack.

## Inputs
- The repository or content set, the intended audience and the target hosting.
- The private identity-term list for this project (kept outside version control, for example `.agentforge/private/identity-patterns.txt`).
- The current license position and the list of third-party sources.
- Authorization. Default: read-only review plus reports. Any change to history, visibility or releases is a human decision.

## Specialists
`privacy-specialist`, `licensing-ip-assistant`, `application-security-engineer`, `release-engineer`, `documentation-curator`, `security-testing-specialist` (independent verification), `qa-lead` (checks and evidence), `compliance-research-assistant` (regulatory questions to hand to a human lawyer), `technical-lead` (decisions), `orchestrator` (integration). Add `design-reviewer` only if public-facing visual assets are included. Do not add roles with no deliverable.

## Parallel and sequential stages
The first four stages read the same tree and write separate files, so they run in parallel when the runtime can spawn workers (`orchestration/parallel-execution.md`). A reviewer never reviews their own stage.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| 1 Privacy and identity sweep | `privacy-specialist` | none | stages 2 to 4 | file-level findings with classification (PUBLIC_SAFE, ANONYMIZE, MOVE_TO_PRIVATE_WORKSPACE, REMOVE_FROM_PUBLIC_HISTORY, NEEDS_HUMAN_REVIEW), masked evidence | `python tools/privacy_scan.py --history`, plus manual sampling | none |
| 2 License and attribution | `licensing-ip-assistant` | none | 1, 3, 4 | license review: own license text, notices, third-party licenses, attribution gaps | license text compared with the canonical text; every adapted source has its license file | the owner for the license choice |
| 3 Security and supply chain | `application-security-engineer` | none | 1, 2, 4 | findings on secrets, CI permissions, dependency and skill risks, safe installation | `python tools/scan_secrets.py`, dependency audit, CI review | none |
| 4 History and remote state | `release-engineer` | none | 1, 2, 3 | what history contains, what is already public, options and consequences | history scan, remote visibility check, author metadata review | the owner for any option |
| 5 Clean-room CI check | `qa-lead` | 1 to 4 | none | results of the CI steps in a fresh clone without private files | commands, exit codes, dates | none |
| 6 Independent verification | `security-testing-specialist` | 5 | none | independent sampling of the tree and adversarial checks of release tooling | different person or agent from stages 1 to 5 | none |
| 7 Documentation honesty | `documentation-curator` | 1 to 4 | 5 | check claims, links, counts and limitations in public docs | no unearned conformance or readiness claims | none |
| 8 Integrate | `orchestrator` | 5, 6, 7 | none | final review report: confirmed findings, recommendations, unverified assumptions | evidence per finding | none |
| 9 Decision sheet | `technical-lead` | 8 | none | human decision sheet with options and consequences | every open decision has an owner | the owner |

## Deliverables
File-level privacy audit, license review, security and supply-chain findings, history options and consequences, clean-clone CI results, independent verification report, documentation honesty check, final review report and the human decision sheet.

## Validations
Checks run in a fresh clone with no private files, matching public CI. Confirmed findings, recommendations and unverified assumptions are reported separately. A test run is never presented as certification or legal compliance.

## Approval gates
Choosing a license, choosing a history option, any history rewrite or force-push, changing visibility, publishing a release, enabling reporting channels, and approving third-party skills all need explicit written approval from the repository owner. The audit prepares evidence only.

## Exit criteria
The decision sheet is complete, every Blocker is fixed or explicitly accepted by the owner, and unresolved items are listed with an owner.

## Example invocation
"Run WF-24 on this repository before we make it public. Read-only. Do not push or change visibility."
