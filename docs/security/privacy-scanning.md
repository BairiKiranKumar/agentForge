# Privacy scanning: what it catches and what it does not

`python tools/privacy_scan.py` checks files (and optionally history) for personal or private data before they become public. It works in two layers.

## Layer 1: generic detectors (run in public CI)
Built in, no configuration, run on every clean checkout:
- email addresses (reserved example domains and the project's noreply address are allowed)
- phone-like numbers (obviously synthetic patterns are allowlisted)
- local machine paths (Windows user folders, macOS and Linux home folders)
- cloud account identifiers and private network addresses

The scan covers tracked files and untracked files that are not ignored, so new files are checked before they are added. `--history` also scans lines added in every commit. Evidence is masked in all output.

## Layer 2: your private identity-term list (local only)
Generic detectors cannot know who you are. Names, handles, studio and client names, product code names and places tied to your business are not recognizable by shape. List them one regular expression per line in `.agentforge/private/identity-patterns.txt` (ignored by Git) or in the file named by `AGENTFORGE_IDENTITY_PATTERNS`. The scanner loads the list when present and flags matches, masked.

Why the list is private: putting your identity terms in a public file would publish them. Because it is private, public CI cannot see it. Public CI therefore enforces layer 1 only. Run the full scan locally before every release:

```text
python tools/privacy_scan.py --history --verbose
```

## Demonstration (clean clone, 2026-10-22)
In a fresh clone with no private files, a test line containing a studio name, a fake email address and a fake phone number produced two findings from the generic layer (email, phone) and none for the studio name. With the studio name added to the private list, the scan reported the name as well. A social handle (`@name`) was caught by neither layer, because handle shapes are too common to flag generically.

## Limits
- It finds known shapes and listed terms, not every private fact. Unlisted names, handles, pseudonyms and free-text stories can pass.
- It does not read images, PDFs or archives. Review screenshots by eye.
- File allowlists hide every finding in that file. Keep `config/privacy-allowlist.yaml` short and justified.
- It cannot remove anything from published history. See `docs/security/history-remediation.md`.
- It does not replace a human read of the public documents.

## Related guards
- `tools/scan_secrets.py`: obvious credential formats.
- `tools/precommit_check.py` and `tools/hooks/pre-commit`: block private paths, bundles, backups, env and key files from being committed (`git config core.hooksPath tools/hooks`). CI runs `precommit_check.py --tracked`. A deliberate `git add -f` with `--no-verify` can bypass the hook but not CI.
- Host features such as push protection and secret scanning can add a further layer; enable them in repository settings (not verified for this repository).
