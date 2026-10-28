# Evaluation: anthropic-webapp-testing

Repo: anthropics/skills, folder skills/webapp-testing. Pinned dbd4588f9e1033efb41dad4bef2f7947c8993d44 (commit 2026-10-09). Evaluated 2026-10-22 by clone and read. Nothing was run.

## Summary
A Playwright-based skill for testing local web apps: verify behaviour, debug UI, take screenshots, read browser logs. Status: conditional.

## Capabilities as read
- SKILL.md description as above.
- scripts/with_server.py starts servers, waits for ports, runs a command, then cleans up.
- examples/ with sample automation scripts.

## Limitations
Local apps only. No visual baseline diffing, no design rubric. Playwright and Python must be installed separately. Examples were listed, not read in full.

## Security review
Scripts present. with_server.py runs subprocess.Popen with shell=True on strings passed by the agent (so cd and && work). This is a command execution surface: a manipulated prompt or page could cause arbitrary commands. Playwright drives a real browser against whatever URL it is given. Not executed here. Risk: medium.

## Licence
LICENSE.txt in the folder is Apache License 2.0. Repo root has no LICENSE file.

## Overlap
qa/* and design/design-reviewer (screenshots at breakpoints). playwright-cli (Microsoft) is a competing option and is official for Playwright itself.

## Evidence of effectiveness
None found.

## Recommendation and conditions
Conditional. Use only in a sandbox or disposable environment, with localhost targets, and with command strings written by a human or approved before running. Read all of scripts/ and examples/ first. Compare with playwright-cli and choose one rather than installing both.

## What was NOT verified
Behaviour at run time, Playwright version compatibility, the example scripts, other agents' support.
