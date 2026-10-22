# Knowledge base schema

Universal design knowledge only. Nothing here may name a client, a brand project or a project-specific decision. Project-specific material lives with the project (for example under `brands/` or the project's own folder) and may link here.

Each entry is one Markdown file with YAML frontmatter. One idea per file. Folder = type.

## Folders
| Folder | Holds |
|---|---|
| `references/` | A specific real site or work worth studying, with what makes it work |
| `patterns/` | Reusable layout, hero, navigation, footer, mobile and interaction patterns |
| `motion/` | Motion and scroll techniques (the motion pattern library) |
| `typography/` | Type systems and pairing/scale strategies |
| `color/` | Colour theory applications |
| `accessibility/` | Accessibility and performance guidance tied to design choices |
| `anti-slop/` | Generic-design signals and how to judge them |
| `critiques/` | Worked critiques of a pattern or a rendered design, with evidence |

## Frontmatter (all fields required unless marked optional)
```yaml
id: kebab-case-unique-id          # matches the filename without .md
type: reference | pattern | motion | typography | color | accessibility | anti-slop | critique
title: Short human title
summary: One sentence, under 200 characters
tags: [hero, scroll, typography]  # lowercase, kebab-case
industries: [any]                 # or specific, e.g. [saas, ecommerce]; "any" for universal
scope: universal                  # always universal in this folder
sources:                          # at least one
  - url: https://...
    retrieved: 2026-10-22         # date you actually read it
    method: fetched-html | search-snippet | browser-rendered | official-docs | manual-report
    note: what was taken from it   # optional
verified_on: 2026-10-22
verification: one line saying what was checked and what was not
status: current | stale | broken | superseded
constraints: one line (licence, feasibility, browser support, cost)   # "none known" is allowed
license_notes: how reuse is bounded (principles only, no copying of proprietary assets)
```
Motion entries add: `dependencies`, `performance`, `accessibility`, `fallback`, `when_to_use`, `when_not_to_use`.
Reference entries add: `viewports_checked` (list; empty if not checked) and `evidence` (what was observed vs not).

## Rules
1. `method` must state how the source was read. Never write `browser-rendered` unless a rendering tool actually loaded the page and the observation came from that. `search-snippet` and `fetched-html` are not visual inspection.
2. Describe principles in your own words. No copied text beyond a short quote with attribution, no proprietary assets, no reproduced layouts.
3. Code examples are original and minimal, and say which library version they assume.
4. No em dashes. Plain professional language.
5. Mark anything not verified `[Unverified]` in the body.
6. Dedup before adding: search existing tags and titles (`python tools/design_kb.py search <term>`).
7. Stale rule: an entry not re-verified within 365 days becomes `stale`; a source that no longer loads becomes `broken`. `python tools/design_kb.py freshness` reports both.

## Body sections (suggested)
`## What it is`, `## Why it works`, `## How to apply`, `## Risks and limits`, `## Related`.
