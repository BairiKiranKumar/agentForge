# Research notes A (design-skill-researcher)

Date: 2026-10-22. Runtime: Claude Code, no GitHub CLI (gh not installed). Nothing from any repo was installed or run. Shallow clones (depth 1) were made into the session scratchpad under skills/<owner_repo>/ and only read with grep, head and listing commands. Because clones are shallow, commit counts and 90-day activity could not be measured; activity uses the API pushed_at date instead.

## Sources opened

| Source | Date | Method |
| --- | --- | --- |
| https://github.com/Leonxlnx/taste-skill | 2026-10-22 | git clone depth 1, read README, CHANGELOG, install.sh, SKILL.md head, scripts grep, LICENSE, evals.json head |
| https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | 2026-10-22 | git clone depth 1, read README, skill.json, SECURITY.md, SKILL.md head, grep of scripts, cli/package.json |
| https://github.com/miqdadbadjuber/anti-slop | 2026-10-22 | git clone depth 1, read README, package.json, plugin.json, SECURITY.md, launcher grep, skill head |
| https://github.com/anthropics/skills | 2026-10-22 | git clone depth 1, frontend-design and webapp-testing folders, LICENSE.txt heads, with_server.py head |
| https://github.com/vercel-labs/agent-skills | 2026-10-22 | git clone depth 1, web-design-guidelines SKILL.md, README licence line |
| https://github.com/vercel-labs/web-interface-guidelines | 2026-10-22 | git clone depth 1, README head, install.sh head, LICENSE |
| https://github.com/greensock/gsap-skills | 2026-10-22 | git clone depth 1, README, gsap-core head, llms.txt head, LICENSE |
| https://github.com/jakubkrehel/skills | 2026-10-22 | git clone depth 1, README, file listing, LICENSE |
| https://github.com/pbakaus/impeccable | 2026-10-22 | git clone depth 1, README, hooks.json, .claude/settings.json, fetch-engine.mjs head, package.json |
| https://github.com/microsoft/playwright-cli | 2026-10-22 | git clone depth 1, SKILL.md head, package.json |
| https://github.com/Leonxlnx/imagegen-skills | 2026-10-22 | git clone depth 1, README, listing, grep of SKILL.md |
| https://github.com/mgifford/accessibility-skills | 2026-10-22 | git clone depth 1, README, listing, one SKILL.md head, LICENSE head |
| https://github.com/agentskills/agentskills | 2026-10-22 | git clone depth 1 only (HEAD 69ef37e9424c0a7ea9dd2293b559e43ec8176379, Apache-2.0). Not read further; it is the format spec, not a design skill, so no registry entry |
| https://api.github.com/repos/<owner>/<repo> for all repos above | 2026-10-22 | curl, unauthenticated, metadata only (stars, pushed_at, licence). Stars are as of this date |
| Web search result pages (listed below) | 2026-10-22 | WebSearch summaries only; the pages themselves were not opened |

All three requested URLs exist and were reachable. No entry was rejected as unreachable.

## Web search summaries used (not opened, treated as [Unverified])
- tessl.io listing for web-design-guidelines (61 percent quality score)
- skills.sh and vibeindex listings for web-design-guidelines, accessibility skills
- playwright.dev/agent-cli/skills (agent list for the Playwright skill)
- agentskills.io (format basics: SKILL.md, name and description, optional scripts, references, assets)
- impeccable write-ups on abduzeedo.com, emelia.io, mintlify.com (not used for any registry value)

## Discovery queries
1. github agent skill SKILL.md frontend design accessibility web interface guidelines
2. github agent skill Playwright visual regression screenshot design review SKILL.md
3. github GSAP skills agent skill animation SKILL.md greensock
4. impeccable design skill pbakaus github frontend-design critique anti-patterns
5. Playwright CLI skill microsoft github playwright-cli SKILL.md coding agents
6. Agent Skills specification agentskills.io SKILL.md format github agentskills/agentskills

## Entries written
taste-skill, ui-ux-pro-max, anti-slop, anthropic-frontend-design, anthropic-webapp-testing, vercel-web-design-guidelines, vercel-web-interface-guidelines, gsap-skills, jakubkrehel-skills, impeccable, playwright-cli, imagegen-skills, mgifford-accessibility-skills.

## Gaps and candidates not evaluated
- Typography, responsive and design-system specific skills beyond those in the entries above were not found as separate repos in the limited searches.
- Visual regression skills named in search (Skrillz visual-testing, PramodDutta qaskills, agentx visual-regression, testland playwright-snapshots) were seen only as search summaries and not cloned.
- Other skills inside anthropics/skills (canvas-design, theme-factory, web-artifacts-builder, algorithmic-art) were listed but not evaluated.
- taste-skill-classics (Leonxlnx) was named in taste-skill's CHANGELOG and not cloned.
- No effectiveness evidence from independent users was found for any entry.
