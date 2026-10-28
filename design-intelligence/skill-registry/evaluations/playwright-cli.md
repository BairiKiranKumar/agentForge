# Evaluation: playwright-cli

Repo: microsoft/playwright-cli. Pinned b1a5903c5b633b8c9f843ad7b629c2a78437040c (commit 2026-10-19). Evaluated 2026-10-22 by clone and read. Nothing was run.

## Summary
The official Playwright CLI for coding agents, with a skill that teaches agents to use it for browser automation, screenshots and test debugging. Status: conditional.

## Capabilities as read
- skills/playwright-cli/SKILL.md: automate browser interactions, test web pages, work with Playwright tests.
- Reference guides in skills/playwright-cli/references.
- A search result from playwright.dev says the skill installs with playwright-cli install --skills and lists Claude Code, GitHub Copilot and Cursor [not opened directly, Unverified].

## Limitations
Not design-aware: no baseline comparison, no rubric. Package is 0.1.22 on an alpha Playwright build, so APIs may change. Reference files not read in full.

## Security review
SKILL.md frontmatter declares allowed-tools: Bash(playwright-cli:*) Bash(npx playwright:*) Bash(npx --no-install playwright:*). That grants shell access to those commands. Install needs the npm package and browser binaries. A browser pointed at arbitrary pages is exposed to hostile content and to prompt injection from page text. Repo includes SECURITY.md and a skillCheck.js script. Risk: medium, contained by the narrow command patterns.

## Licence
Apache-2.0 (LICENSE present; package.json says Apache-2.0; author Microsoft Corporation).

## Overlap
qa/* and design/design-reviewer for responsive screenshots. Competes with anthropic-webapp-testing; taste-skill also has its own browser inspector.

## Evidence of effectiveness
None found.

## Recommendation and conditions
Conditional. Preferred browser tool of the two official options because it has a narrow allowed-tools list and a Microsoft maintainer. Conditions: install in a sandbox, pin the npm version and SHA, restrict to localhost or approved URLs, and treat page content as untrusted data. Human approval needed for any run against a client site.

## What was NOT verified
Runtime behaviour, install side effects, the references folder, the Cursor and Claude Code claims on playwright.dev.
