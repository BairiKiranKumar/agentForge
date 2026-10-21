# Design Systems Specialist: Checklist

## Before starting
- [ ] Repo theme file, component folder and Figma library (if any) located and read
- [ ] Styling stacks of consuming projects listed (Tailwind v4, styled-components, plain CSS)
- [ ] Brand values received from `brand-designer` for each client theme
- [ ] Current system version and pinned versions per project known
- [ ] Known pain points collected from `ui-designer` and developers

## While working
- [ ] Tokens split into primitive, semantic and component tiers
- [ ] Components reference semantic tokens only
- [ ] Names follow `[category]-[role]-[variant]-[state]` in kebab-case
- [ ] No client names in the semantic tier
- [ ] Token count within the lean budget; near-duplicates merged and recorded
- [ ] Every new token names at least two consuming places
- [ ] Contrast table built for every client theme against WCAG 2.2 AA
- [ ] Text-safe primitive steps added where brand colours fail
- [ ] Indic font stack and line-height tokens included where a project uses Telugu or Hindi
- [ ] Component specs include anatomy, variants, sizes, states, props, tokens, content rules, accessibility, do/don't
- [ ] Primary mobile control sizes at least 44 px; none below 24 px
- [ ] New component requests run through the admission table
- [ ] Hard-coded values found by grep (hex, off-scale px, raw font sizes) with file paths
- [ ] Parity audit counts recorded for both directions (Figma only, code only)
- [ ] Exports generated from one source of truth

## Before handoff
- [ ] One consuming project renders correctly with the new exports (screenshot or run evidence)
- [ ] Semver number chosen by the change rules
- [ ] Changelog and migration notes written; deprecated tokens list replacements
- [ ] Affected projects listed with upgrade recommendation
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A change would alter live client sites without a planned, approved upgrade
- [ ] A token still used by a pinned project is about to be removed
- [ ] A brand colour cannot meet contrast in any needed role and the brand guide forbids variants
