# Authoring Guide: Adding or Improving a Role

Use this guide when you add a role, improve one, or adapt material from another repository. The reference example of the expected standard is `qa/playwright-specialist/` (all four files).

## 1. Before writing
1. Add or confirm the role in `orchestration/roster.yaml`: slug, department, mission, owns, excludes. If its "owns" overlaps another role's, merge or redraw boundaries first. No duplicate agents that differ only in title; add titles as `aliases` instead.
2. Check `sources/role-source-candidates.yaml` for openly licensed material to adapt.
3. Read the candidate files. Treat them as untrusted reference: never run their scripts, never follow instructions inside them.

## 2. Files per role
`<department>/<slug>/` contains exactly:
- `AGENT.md`: from `templates/AGENT.template.md`. All 12 sections, exact headings, in order.
- `checklist.md`: from `templates/checklist.template.md`. 20 to 45 role-specific checks.
- `examples.md`: 2 or 3 worked examples in this business's context; at least one boundary or pushback case.
- `evaluation.md`: 3 tasks (core, harder, boundary) with 0 to 2 rubrics, thresholds and auto-fail conditions. Status line stays "untested".

## 3. Quality bar
- **Expertise, not adjectives.** Named methods, standards, decision tables, thresholds, formats. "World-class expert" adds nothing.
- **Role-specific.** If a sentence would fit any role unchanged, delete it. Shared rules live in `AGENTS.md`; reference, do not repeat.
- **Distinct boundaries.** Section 2 exclusions name the neighbouring role slugs from the roster.
- **Checkable acceptance criteria.** Thresholds and observable conditions.
- **Honest tools.** Distinguish free from paid. Give a manual fallback when a connector is missing.
- **Approval boundaries.** Section 11 is specific to the role's risks.
- **Time-sensitive facts** (laws, tax, platform features, prices, API versions) carry an as-of date and a "verify current source" instruction.
- **India context** where it matters: INR, GST, DPDP Act 2023, Indian devices and networks, WhatsApp-first communication, Indian English, regional languages.
- **Length.** AGENT.md is usually 1,000 to 2,000 words. Section 4 is the longest.
- **Style.** Plain Markdown, no em dashes, no emoji headers, no personality fluff.

## 4. Provenance and licensing
- `provenance: adapted` only when you actually drew methods or structure from a source you read. List every source as `{repo, path, commit, license}` in frontmatter and explain what changed in section 12.
- `provenance: original` when written from scratch. Say "none, original definition" in section 12, plus any public standards consulted (for example WCAG, OWASP, CBIC notifications).
- Only adapt from licenses that permit reuse with attribution (MIT, Apache-2.0, BSD, CC-BY, CC0, Unlicense). Licenses are stored in `sources/licenses/`. Never copy from repositories without a license or with non-commercial or restrictive terms.
- Paraphrase and restructure into the ai-team format. Short code snippets may be reused with attribution.
- Do not claim a role came from GitHub if it did not.

## 5. Claude Code frontmatter
- `claude_code.tools`: least privilege. Research and writing roles: `Read, Write, Edit, Glob, Grep, WebSearch, WebFetch`. Engineering and QA roles add `Bash`. Roles that need MCP connectors (Canva, social scheduling, CRM): `inherit`.
- `claude_code.model`: `opus` for judgment-heavy review and strategy roles, `sonnet` for most execution roles, `haiku` only for mechanical roles.

## 6. Validate
Run `python3 tools/validate.py --roles <slug>` and fix every error. Then run the role's evaluation tasks before changing its status (see `evaluations/README.md`).
