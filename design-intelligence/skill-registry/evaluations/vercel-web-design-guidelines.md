# Evaluation: vercel-web-design-guidelines

Repo: vercel-labs/agent-skills, folder skills/web-design-guidelines. Pinned 063bee94c3f4df8453406c830b0a7df0f2860278 (clone HEAD dated 2026-08-28; API pushed_at 2026-10-14). Evaluated 2026-10-22.

## Summary
A reviewer skill that checks UI files against Vercel's Web Interface Guidelines and prints file:line findings. Status: candidate.

## Capabilities as read
- Frontmatter triggers: "review my UI", "check accessibility", "audit design", "review UX".
- Workflow: fetch the guidelines from https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, read the target files, output terse findings.

## Limitations
The rules are not stored in the skill. Every run fetches them live. No network, no review. Some rules are React and Next.js specific.

## Security review
No scripts in this skill folder. The risk is the live remote fetch: the instructions come from an unpinned main branch, so the behaviour can change with no change in this repo, and the fetched text is an injection surface. The wider repo contains other skills, zip files and a build script (scripts/build-discovery-index.mjs) that were not reviewed. Risk: medium for the remote instructions.

## Licence
Unclear. No LICENSE file in the repo root or skill folder, and the GitHub API reports none. README ends with "## License MIT", which is a statement but not a licence file. Under the registry rules this blocks approval.

## Overlap
design/design-reviewer, qa/*. Overlaps vercel-web-interface-guidelines (same rules source) and jakubkrehel-skills.

## Evidence of effectiveness
None found in the repo. A Tessl registry listing was reported by search with a 61 percent quality score; I did not open it, so this is [Unverified].

## Recommendation and conditions
Candidate only. Better route: vendor the rule text from vercel-web-interface-guidelines (MIT) at its pinned SHA and drop the live fetch. Revisit if Vercel adds a licence file.

## What was NOT verified
Whether the live command.md has changed since the pinned SHA, other skills in the repo, agent compatibility beyond the skills CLI model.
