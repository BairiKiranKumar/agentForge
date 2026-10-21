# Accessibility Engineer: Checklist

## Before starting
- [ ] Defect has WCAG criterion, location and steps, or the spec has accessibility annotations
- [ ] Defect reproduced with keyboard and a screen reader before coding
- [ ] Component library and its existing a11y primitives identified
- [ ] Target standard and assistive tech recorded (default WCAG 2.2 AA, TalkBack, NVDA)
- [ ] Source located: shared component, page markup, library config or third party

## While working
- [ ] Native element used wherever one exists
- [ ] Custom widgets follow the APG pattern's roles, states and keyboard table
- [ ] Every interactive element has an accessible name containing its visible label
- [ ] No positive `tabindex`; no `aria-hidden` on focusable content
- [ ] Dialogs: focus in on open, Tab contained, Escape closes, focus restored, background inert
- [ ] Route changes move focus or announce the new page; `document.title` updated
- [ ] Focus indicator visible with sufficient contrast; not hidden by sticky headers
- [ ] Targets at least 24 by 24 CSS px or spaced
- [ ] Inputs have visible labels, `autocomplete` tokens and text-based required state
- [ ] Errors linked via `aria-describedby` with `aria-invalid`; summary or first-error focus on submit
- [ ] Live regions exist before content changes; `status` vs `alert` chosen correctly
- [ ] `lang` set on Telugu or Hindi blocks
- [ ] `prefers-reduced-motion` respected for large motion
- [ ] Fix applied in the shared component; other usages searched

## Before handoff
- [ ] axe shows zero serious or critical violations on fixed components and pages
- [ ] Keyboard test and focus-return assertion added where relevant
- [ ] Keyboard-only task completion recorded
- [ ] TalkBack and NVDA announcements recorded (or untested readers listed)
- [ ] 200% zoom and 320 px reflow checked
- [ ] Tests, type check and lint run; results recorded
- [ ] Retest requested from `accessibility-tester`
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] The fix needs a visible design change without designer sign-off
- [ ] Someone proposes an accessibility overlay script as the fix
- [ ] You are asked to state the product is WCAG or legally compliant
- [ ] A third-party widget blocks a core task and cannot be fixed in our code
