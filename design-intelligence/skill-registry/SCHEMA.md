# Skill registry schema

A versioned registry of third-party design skills for AI coding agents. Entries are data. Nothing here is installed or executed by agentForge. Never run scripts from a candidate skill. Read its files only.

## Layout
- `skills/<id>.yaml`: one machine-readable entry per skill.
- `evaluations/<id>.md`: the written evaluation for that skill.
- `REGISTRY.md`: generated index (`python tools/design_kb.py index`).
- `policy.md`: adoption, pinning, conflict, effectiveness and disable rules.

## Entry fields (`skills/<id>.yaml`)
```yaml
id: kebab-case
name: Human name
source_url: https://github.com/owner/repo
repo: owner/repo
maintainer: owner or org as observed
license: SPDX id or "none found" or "unclear"
registry_version: 1                 # bump when this entry changes
status: candidate | conditional | approved | rejected | disabled
status_reason: one or two sentences
categories: [visual-design-intelligence, ui-ux, creative-frontend, typography-layout, design-systems, motion, accessibility, design-critique, browser-visual-testing, image-video-direction, responsive, component-design, anti-pattern-detection]
capabilities: [list of what it actually does, as read]
limitations: [list]
compatible_agents: [claude-code, cursor, codex, antigravity, ...]   # only those the repo states or that you verified
install_method: what the repo documents, e.g. "copy SKILL.md folder", "npx ...", "plugin"
dependencies: [runtime deps, CLIs, network services]
scripts_present: true | false      # any executable script in the repo
permissions_requested: [file write, shell, network, ...]
risks: [prompt injection surface, remote fetch, postinstall, telemetry, ...]
pinned_ref: full commit SHA observed, or null if not obtained
last_commit_observed: YYYY-MM-DD or null
activity: one line, e.g. "N commits in last 90 days" or "not verified"
stars_observed: number or null (with date in notes)
overlaps: [existing agentForge roles or other registry ids]
evidence_of_effectiveness: "none found" | description with source
owner_roles: [agentForge roles that may use it]
verified_on: YYYY-MM-DD
verification_method: cloned-and-read | fetched-readme | search-only
effectiveness_log: []              # filled by real use: {date, task, outcome, notes}
```

## Rules
1. Fill only what you observed. Use `null` or "not verified" otherwise.
2. `status: approved` requires: licence permits reuse, no unreviewed scripts, a pinned commit SHA, a written evaluation, and no unresolved risk. Anything less is `candidate` or `conditional`.
3. A skill with a missing licence cannot be approved. Mark `rejected` or `candidate` with the reason.
4. No em dashes. Plain language.
