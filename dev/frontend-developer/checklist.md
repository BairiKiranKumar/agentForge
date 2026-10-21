# Frontend Developer: Checklist

## Before starting
- [ ] Story has acceptance criteria
- [ ] Designs cover every breakpoint and state the criteria need
- [ ] Copy is final or placeholders are approved and marked `[copy pending]`
- [ ] App and tests run locally, or mocks are available
- [ ] Nearest similar feature found and its patterns noted
- [ ] Existing components, hooks, tokens and constants to reuse listed

## While working
- [ ] For bugs: reproduced and a failing test written before the fix
- [ ] Mobile-first styles using design-system breakpoints
- [ ] Loading state matches final layout (no layout shift)
- [ ] Empty, error (with retry) and disabled states built
- [ ] Long names and Telugu or Hindi strings do not break layout
- [ ] Submit disabled while pending; no double submission
- [ ] Every form field has a label; errors shown next to fields; input kept on error
- [ ] Phone fields `type="tel"`, `inputmode="numeric"`, 10-digit validation after stripping +91
- [ ] Amounts formatted with `Intl.NumberFormat('en-IN')`
- [ ] No new hardcoded colors, spacing or strings where tokens or constants exist
- [ ] Tests use role and label queries and mock at the network boundary
- [ ] Diff limited to files the story needs

## Before handoff
- [ ] Type check run and result recorded
- [ ] Lint run and result recorded
- [ ] Unit tests run with counts recorded
- [ ] Build run when routing or config changed
- [ ] Pre-existing failures reported separately
- [ ] Checked at 360, 390, 768, 1024, 1440 px; no horizontal scroll at 360
- [ ] Screenshots attached for key states
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A new dependency, API field or schema change is needed
- [ ] The change touches a shared component used across many screens
- [ ] Criteria conflict with the design
- [ ] Getting green would require disabling tests or lint rules
- [ ] The issue is framework-deep (hydration, change detection, caching): call the specialist
