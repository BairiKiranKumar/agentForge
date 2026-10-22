# Items needing human review before public release

These decisions or checks are not safe for an agent to make. Nothing here is done unless stated.

## Decisions for the repository owner
| # | Item | Why it needs a human | Suggested default |
|---|---|---|---|
| 1 | **License.** The branch adds `LICENSE` (Apache-2.0) and `NOTICE` ("agentForge contributors") as a proposal. The repository previously had no license file, which means all rights reserved. | Choosing a license and the copyright holder is the owner's legal decision. Adapted third-party material is MIT and Apache-2.0, which is compatible with Apache-2.0 or MIT. | Confirm Apache-2.0, or replace with MIT. Decide whether `NOTICE` names an individual or the project. |
| 2 | **Git history and author metadata.** Published history contains the removed personal and project-style terms; every commit has one personal author identity. | Rewriting or replacing history is destructive and affects collaborators. | Read `docs/security/history-remediation.md` and choose option A, B or C. |
| 3 | **Repository owner username in canonical URLs** (`agentforge.lock`, `docs/INSTALL.md`, `runtime/discover.py`, one test). | Moving the repository changes these. A public repository exposes its owner name in any case. | Keep as the upstream default; it is overridable. |
| 4 | **Private vulnerability reporting and a conduct contact.** `SECURITY.md` and `CODE_OF_CONDUCT.md` rely on GitHub private reporting being enabled. | Needs repository settings only the owner can change. | Enable private vulnerability reporting; add a conduct contact. |
| 5 | **Repository visibility, releases and branch protection.** | Explicitly out of scope for agents. | Review required checks and enable branch protection on the default branch. |
| 6 | **Skill approvals.** 13 third-party skills are reviewed; none is `approved`. | Approval is a human decision under `design-intelligence/skill-registry/policy.md`. | Decide per skill after the documented reviews. |
| 7 | **Regional pack scope.** The India pack and India-specific roles (tax, GST, local languages) remain as optional packs. | Whether to ship, rename or split them out. | Keep as an optional pack with its as-of dates and disclaimers. |

## Checks a human should do
- Read `README.md`, `docs/QUICKSTART.md`, `SECURITY.md` and `CONTRIBUTING.md` once as a new adopter.
- Skim the `examples/` content for anything that still reads like a real client or person. The examples were renamed to fictional entities by automated replacement and a reviewer; wording may still be awkward in places.
- Review `workspace/` locally (ignored by Git) to confirm the private originals are stored where you want them, and decide what to do with `workspace/backup/` (a full Git bundle of the pre-change repository).
- Confirm the CI workflow runs on your host and that pinned action versions are still current (Dependabot is configured to propose updates).
- Run the privacy scan with your own identity terms: add them to `.agentforge/private/identity-patterns.txt`, then `python tools/privacy_scan.py --history`.

## Known content caveats
- Many role files contain India-specific context (tax, GST, languages, payment systems). It is legitimate regional knowledge, now selected through `regional_packs`, but several roles still describe it inline. Review whether this is acceptable for a general audience.
- Role definitions adapted from third-party sources keep their attribution in frontmatter. Their text was written by earlier agent runs and has not had a legal review.
- Engineering standards and the design rubric are drafts based on sources read on recorded dates; items marked `[Unverified]` were not confirmed.
