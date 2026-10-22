# Privacy audit (summary)

Date: 2026-10-22. Scope: the working tree, all tracked files, Git history, remote metadata and author metadata of the repository before the `public-ready/architecture-and-standards` branch. Values are not reproduced here. File-level detail: [privacy-audit-files.md](privacy-audit-files.md).

## Method
- Enumerated tracked files (1,191) and read configuration, role definitions, workflows, brand profiles, knowledge bases, the skill registry, examples, evaluation runs, scripts and CI configuration.
- Ran `tools/privacy_scan.py` with generic detectors (email, phone, local path, cloud identifier, private address) plus a private, ignored list of identity terms supplied by the maintainer for this audit. Ran it on tracked files and on lines added in all history.
- Searched all history for common credential formats (cloud keys, tokens, private keys, JWTs, assigned secrets). Result: no matches.
- Checked the remote and release state: the remote repository responds publicly (unauthenticated HTTP 200 on 2026-10-22). Its `develop` branch is at the v1.1 commit. No release artifacts were enumerated (no API token used).
- Reviewed assets: 15 PNG captures from a design evaluation, all of synthetic pages.

## Findings by category
| Category | Files (before) | Classification | Disposition |
|---|---|---|---|
| Owner's first name hard-coded as the human approver | about 611 | ANONYMIZE | Replaced by the neutral term "the owner" / "Owner" and the configurable owner in the organization profile |
| Owner's public brand handle and display name | 127 | ANONYMIZE; brand profile MOVE_TO_PRIVATE_WORKSPACE | Replaced by a fictional brand (`example-brand`); the real profile is in the ignored workspace |
| Personal studio concept name | 8 | MOVE_TO_PRIVATE_WORKSPACE | Company profile moved to the ignored workspace; neutral template added |
| Local-market city used in examples | 85 | ANONYMIZE | Replaced by generic small-town wording |
| Showcase project with a personal-brand voice | 16 | ANONYMIZE | Fictional clinic renamed and rewritten as a synthetic example; originals kept privately |
| Client-style project and domain names (a school ERP, salon, store) | 66 | ANONYMIZE | Replaced by fictional names and reserved example domains |
| Maintainer full name and local machine paths | 5 | MOVE_TO_PRIVATE_WORKSPACE | Personal scratch scripts moved to the workspace and removed from the tree |
| Example email addresses and phone numbers | 11 | ANONYMIZE or PUBLIC_SAFE | Real-looking addresses replaced by `example.com`; obviously synthetic numbers allowlisted |
| Third-party author email in source metadata | 1 | ANONYMIZE | Removed |
| Repository owner username in canonical repository URLs | 4 | PUBLIC_SAFE (NEEDS_HUMAN_REVIEW) | Kept as upstream coordinates; the owner decides whether to keep it |
| Region defaults (India, INR, GST, DPDP) hard-coded in core rules | AGENTS.md and generated agent footers | ANONYMIZE (generalize) | Moved to configuration and an optional regional pack |
| Credentials, tokens, keys | 0 | PUBLIC_SAFE | None found in the tree or history |
| Cloud identifiers | 1 | PUBLIC_SAFE | AWS documentation example account id in an example |
| Third-party attribution (maintainer names, licenses, upstream URLs) | many | PUBLIC_SAFE | Required attribution is retained (`NOTICE`, `SOURCE-MANIFEST.md`, `sources/licenses/`) |

Not every personal name or domain was treated as sensitive. Public attribution, the repository URL, license texts and external research references were kept.

## Git history and remote (important)
- The remote repository is publicly reachable and its history already contains the material above. Changes on this branch clean the working tree going forward. They do not remove the material from published history, forks or caches.
- Local history has 5 commits, all authored under one name and one personal email address. Author metadata is public in a public repository. Whether to keep it is a maintainer decision.
- Of the 5 commits, 4 are on the remote and 1 (the design intelligence commit) is local only. The commit on this branch's parent is local only.
- History scan (added lines): findings in 3 commits across personal-identity terms, email addresses and one local path. No credential patterns.
- Remediation options, backup, impact analysis and approval gates: [../security/history-remediation.md](../security/history-remediation.md). Nothing was rewritten, pushed or deleted.

## Residual items
See [human-review.md](human-review.md).

## Limits
Pattern scanning finds known shapes, not every private fact. The identity term list covers terms known to the maintainer; unknown identities in free text may remain. Screenshots and other binary assets were reviewed by file name and origin, not pixel by pixel. A human should read the public-facing documents once before release.
