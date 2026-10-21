# CSS Specialist: Checklist

## Before starting
- [ ] Styling system and version identified from `package.json` and files
- [ ] Tokens file and breakpoint config located
- [ ] Browser targets known (`browserslist` or stated audience)
- [ ] Repro details: width, device, browser, font scale, language
- [ ] Before screenshots captured at the failing width

## While working
- [ ] Overflowing or misbehaving element identified with DevTools
- [ ] Root cause written as element plus property
- [ ] Fix made in the component's existing style location
- [ ] No `overflow-x: hidden` on html or body used to hide the bug
- [ ] Flex items that must shrink have `min-width: 0`; grid uses `minmax(0, 1fr)` where needed
- [ ] Viewport units use `dvh`/`svh` with fallback where mobile bars matter
- [ ] Only existing tokens used; missing tokens listed, not invented
- [ ] Selectors kept to single class or `:where()`; no new IDs or `!important`
- [ ] `:focus-visible` styled with at least 3:1 contrast
- [ ] Text contrast meets WCAG 2.2 AA in every theme
- [ ] Tap targets about 44 px
- [ ] Motion limited to transform and opacity, with reduced-motion handling
- [ ] Images and embeds reserve space with `aspect-ratio` or dimensions
- [ ] Newer features checked against targets with `@supports` fallbacks

## Before handoff
- [ ] Width matrix checked: 320, 360, 390, 768, 1024, 1280, 1440
- [ ] Large font setting (about 1.3x) checked
- [ ] Long Telugu or Hindi string checked where UI is regional
- [ ] Dark theme checked if present
- [ ] Lint, tests and build run with results recorded
- [ ] After screenshots attached
- [ ] Visual regression run requested if shared styles changed
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] The fix requires a new styling system or CSS dependency
- [ ] Global resets or tokens affecting every page must change
- [ ] Design gives no guidance for a breaking in-between width
- [ ] A required token does not exist (`design-systems-specialist`)
