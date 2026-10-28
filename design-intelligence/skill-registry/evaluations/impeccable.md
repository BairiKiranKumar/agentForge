# Evaluation: impeccable

Repo: pbakaus/impeccable. Pinned 8644175285360c166e57b1e35ecadfbc85ff5209 (commit 2026-10-22). Evaluated 2026-10-22 by clone and read. Nothing was run.

## Summary
A design skill with 24 commands (README) and a deterministic detector for AI-looking frontend. The most capable critique and anti-pattern tool found, and also the heaviest. Status: candidate.

## Capabilities as read
- /impeccable init writes PRODUCT.md; commands include craft, shape, critique, audit, polish, animate, bolder, quieter, document, extract.
- 61 deterministic detector rules via CLI and browser extension, stated in the README.
- Live browser iteration; Cursor plugin and VS Code package directories.
- README says it builds on Anthropic's frontend-design.

## Limitations
Large Rust and JS repo, about 750 MB by API size. Fast release pace means a pin goes stale. Rule quality was not tested because running is forbidden.

## Security review
This is the main concern. plugin/hooks/hooks.json and .claude/settings.json define SessionStart, PostToolUse (matcher Edit|Write) and Stop hooks that execute skills/impeccable/scripts/impeccable. That launcher runs a native engine binary; scripts/fetch-engine.mjs downloads it from GitHub Releases (default base https://github.com/pbakaus/impeccable/releases/download) and verifies a .sha256 only when one is present. bin entry exists in package.json. So installing it means auto-running a downloaded binary after every edit. I did not inspect the binary or Rust sources.

## Licence
Apache-2.0 (LICENSE and NOTICE.md present; GitHub API reports Apache-2.0).

## Overlap
design/design-reviewer, design/creative-director, design/ui-designer, design/motion-designer, qa/*. Competes with taste-skill and anti-slop.

## Evidence of effectiveness
None found in the repo beyond README claims and demos. Third-party articles came up in search but were not opened.

## Recommendation and conditions
Candidate. Do not install. To move to conditional: review the Rust engine source and release signing (bundle-signing-keys.json, sign-bundle.mjs), build it from source, remove the auto-run hooks, and test the detector on a sample site in a sandbox. Consider borrowing its rule list as reading material instead.

## What was NOT verified
Binary contents, detector accuracy, telemetry, Codex or Antigravity support, contents of skill/reference files.
