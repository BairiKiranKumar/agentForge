# Remaining-risk report

State as of 2026-10-22 on branch `public-ready/architecture-and-standards`. Nothing has been pushed, merged, published or approved.

## Risks that need an owner decision
| Risk | Severity | Detail | Next step |
|---|---|---|---|
| Published history still contains removed material | High | The remote repository is public and its history includes the personal identity terms, a personal brand, a market location, client-style example names and a local path that this branch removes from the tree. Forks, clones and caches persist whatever is done. | Choose option A, B or C in `docs/security/history-remediation.md`. |
| License not confirmed | High | The repository had no license. Apache-2.0 and a project-level `NOTICE` are proposed. Without an owner decision, rights are unclear for adopters. | Owner confirms license and copyright holder. |
| Reporting channel not confirmed | Medium | `SECURITY.md` and the code of conduct depend on private vulnerability reporting, which only the repository owner can enable. | Enable it and add a conduct contact. |
| Author metadata | Medium | All commits use one personal name and email address. | Decide with the history option. |
| Owner username in canonical URLs | Low | Appears in the lock file, install guide, fetch tool default and one test. Overridable. | Keep or change on move. |

## Technical and content risks
| Risk | Severity | Detail |
|---|---|---|
| No role is behaviourally tested | High for claims, low for use | Every role is `untested`. Structural validation and unit tests do not show that agents behave well. |
| Standards are unreviewed drafts | High for claims | 298 requirements drafted from public sources on recorded dates. Not reviewed by certified accessibility, security or legal professionals. Several references are marked `[Unverified]` (for example some WCAG success criterion levels, ASVS requirement ids, agentic AI risk names, primary legal texts). |
| Quality gate declares its own scope | Medium | A submitter controls the profile, product types and results. `--expect-*` flags and human review mitigate; they do not eliminate. The tool cannot verify that evidence is true. |
| Evidence is trusted as written | Medium | The evaluator checks that evidence is present, typed, dated and not future-dated, not that the referenced file or tool output exists. |
| Residual single-person and regional wording | Medium | Role bodies and examples still tell one regional small-business story in places (final review F1, F5). Contradicts the neutrality claim until rewritten. |
| Identity detection is limited | Medium | Built-in detectors find known shapes. Private identity terms live in an ignored local file, so CI cannot check them on a clean checkout. Other people's names in free text may remain. |
| Automated anonymization | Medium | About 680 files were rewritten by scripted replacement of names and project terms, then regenerated and scanned. Wording may be awkward and some context may still read as one person's business. A human should skim `examples/` and a sample of roles. |
| Regional content inline | Low to Medium | India-specific roles and some inline regional examples remain. They are legitimate as a regional pack but add regional bias to the default experience. |
| Third-party material | Medium | Roles adapted from MIT and Apache-2.0 sources keep attribution. No legal review was done. 13 external skills are described, not redistributed, and none is approved. |
| Prior evaluation evidence is thin | Medium | Design Intelligence end-to-end run was one sample with one reviewer from the same model family. |
| No browser or scanners bundled | Low | Visual, accessibility and performance checks need tools the user connects. Reports must say when they were not run. |
| CI is untested on the hosting platform | Medium | The workflow was written and its steps run locally. It has not run on GitHub. Action versions are pinned by SHA, fetched on 2026-10-22. |
| Markdown lint noise | Low | Editor diagnostics report style warnings in many documents. They do not affect behaviour. |

## What a passing test run does not establish
It does not establish WCAG conformance, security certification, legal compliance, privacy compliance, or production readiness of any project that uses agentForge.

## Backups
A full Git bundle of the pre-change repository and a snapshot of every file that was rewritten are kept locally in the ignored `workspace/` directory. They contain the original private material. Store or delete them deliberately; they are not part of the repository.
