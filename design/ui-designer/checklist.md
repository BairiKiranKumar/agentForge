# UI Designer: Checklist

## Before starting
- [ ] Wireframes and screen inventory received from `ux-designer` (or a content outline for a small landing page)
- [ ] Art direction and brand guidelines read
- [ ] Existing tokens read from the repo theme, Tailwind config or design system
- [ ] Real copy, photos and prices collected in every site language
- [ ] Tech stack and component library confirmed
- [ ] Figma or Figma MCP availability checked; fallback chosen if missing

## While working
- [ ] Type scale ratio chosen for content density, 6 to 8 steps, whole px
- [ ] Body measure 45 to 75 characters; Indic body line height 1.6 to 1.8
- [ ] Spacing values come from the 4/8 px scale; off-scale values justified
- [ ] Grid set per width: 4 cols at 375, 8 at 768, 12 at 1024 and 1440
- [ ] 375 px designed first; structural changes (not scaling) at larger widths
- [ ] 320 px reflow checked: no horizontal scroll for text
- [ ] Blur test passed: where am I, what is this, what do I do
- [ ] One primary button style per screen
- [ ] Every text pair at or above 4.5:1 (3:1 large) with ratio recorded
- [ ] UI boundaries, meaningful icons and focus indicators at or above 3:1
- [ ] Primary mobile targets 44 px or more; none under 24 px without spacing
- [ ] Focus not hidden by sticky header or bottom bar
- [ ] States drawn: hover, focus, active, disabled, loading, empty, error, success
- [ ] Long content tested: long names, 2-line Telugu buttons, 40-item lists, missing images
- [ ] Image aspect ratios, focal points and the LCP image specified
- [ ] Anti-template check done; remaining patterns justified

## Before handoff
- [ ] Every screen exists at 375, 768, 1024, 1440
- [ ] Handoff spec uses tokens, not raw values, and covers responsive changes and content rules
- [ ] Assets exported with the naming scheme, in WebP/AVIF/SVG plus 2x raster
- [ ] States needing behaviour listed for `interaction-designer`
- [ ] Screens queued for `accessibility-designer` annotation where needed
- [ ] Sent to `design-reviewer`; not self-approved
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Brand colour fails contrast and the brand guide forbids a variant
- [ ] Mockups would need fake reviews, ratings or people shown as real
- [ ] Repo tokens conflict with the art direction and no owner has decided
- [ ] A visual treatment would hide a decline, cancel or fee
