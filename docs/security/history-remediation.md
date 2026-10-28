# History remediation proposal

Status: proposal only. Nothing in this document has been done. Do not push, force-push, rewrite history, delete branches or change repository visibility without explicit approval from the repository owner.

## Why this matters
Cleaning the working tree does not remove sensitive material from commits that are already published. Anyone with a clone, fork, cache, archive or search index can still read it. If any credential was ever committed, assume it is compromised: revoke or rotate it. Deleting it from history is not sufficient.

## What the audit found about history
See [../release-readiness/privacy-audit.md](../release-readiness/privacy-audit.md). In short: no credential patterns; personal-identity terms, a project and client-style names, and one local machine path appear in published commits; all commits carry one author identity and a personal email address.

## Decision first: is a rewrite needed?
| Option | When it fits | Effect | Risk |
|---|---|---|---|
| A. Leave history, clean going forward | Terms are low sensitivity and already public by the owner's choice | No disruption; old commits remain readable | Residual exposure remains |
| B. Fresh public repository with a squashed initial commit from the sanitized tree | The old history is not needed publicly, no collaborators depend on it | Clean public history; old repository kept private or deleted later | Loses commit history and links; old forks and caches persist |
| C. Rewrite history in place (`git filter-repo`) | History must be preserved but specific content removed | Rewrites every commit hash | Breaks clones and forks, needs coordination, forks keep old data |
Recommendation: decide A, B or C after reading the owner-only list in `human-review.md`. If the owner wants the public repository free of the old material, B is the least error-prone.

## Procedure if B or C is chosen
1. **Freeze.** Tell collaborators to stop pushing. List forks, open pull requests, tags, releases and protected branches.
2. **Back up.** Create a full backup before any change: `git bundle create agentforge-backup.bundle --all` stored offline. A bundle of the pre-sanitization state exists in the ignored workspace on the maintainer's machine. Verify it with `git bundle verify`.
3. **Impact analysis.** Count affected commits, tags and links; note any external references to commit hashes (lock files, documentation, other projects that pin a SHA, such as `agentforge.lock`). Pinned consumers will break.
4. **Rotate.** Revoke or rotate any credential that may have been exposed. None was found, but confirm with the owner.
5. **Prepare in a clone.** For option C, run `git filter-repo` in a fresh clone using a replacement file (text to replace) and path filters (files to drop). Review with `python tools/privacy_scan.py --history` and `python tools/scan_secrets.py`. Do not run it in the working repository.
6. **Review.** The owner reviews the rewritten history, including author and committer metadata (`git filter-repo --mailmap` can change identity metadata).
7. **Approval gate.** Written approval from the repository owner for the exact operation, target repository and date.
8. **Publish.** Force-push (C) or push to the new repository (B) only after approval. Re-protect branches. Ask collaborators to re-clone rather than merge.
9. **Cleanup.** Ask the hosting provider to run garbage collection and purge cached views if needed; contact support for sensitive data removal. Delete or archive the old repository only after confirming the new one. Remove deprecated forks where you control them.
10. **Update pins.** Refresh `agentforge.lock` and any documentation that cites old commit hashes.
11. **Record.** Add a dated note to `docs/release-readiness/` with what was done and what remains exposed (forks and caches cannot be recalled).

## Collaborator coordination
Identify collaborators and forks before acting. Share the plan, the freeze window and the re-clone instructions. A rewrite that surprises collaborators causes lost work and diverging histories.

## Approval gates
| Step | Needs |
|---|---|
| Choosing option A, B or C | Repository owner |
| Any history rewrite or force-push | Explicit written approval for the exact command and target |
| Deleting or archiving the old repository | Explicit written approval |
| Changing repository visibility | Explicit written approval |

## What stays out of scope
Recalling copies already cloned, forked or indexed elsewhere. Nobody can guarantee this. Plan on the assumption that anything once published remains available.
