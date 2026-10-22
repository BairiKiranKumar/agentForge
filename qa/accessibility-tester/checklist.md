# Accessibility Tester: Checklist

## Before starting
- [ ] Build id and test URL recorded
- [ ] Key tasks and roles listed; complete processes identified
- [ ] Sample chosen per WCAG-EM (templates, processes, states, random pages)
- [ ] Screen reader and browser pairs chosen by audience (TalkBack included for Indian public sites)
- [ ] Annotations from `accessibility-designer` read, if any
- [ ] Third-party widgets in key flows listed and scope agreed

## Automated
- [ ] axe run with WCAG 2.0, 2.1 and 2.2 A/AA tags per page and per key state
- [ ] Every automated result triaged (issue, false positive, needs review)
- [ ] Lighthouse treated as indicative only

## Manual
- [ ] Keyboard-only pass of every in-scope flow: order, visible focus, no traps, Escape, focus return
- [ ] Custom widgets checked against their APG keyboard pattern
- [ ] Screen reader pass of each key flow per pair, announcements recorded in quotes
- [ ] Errors and status messages announced (3.3.1, 4.1.3)
- [ ] 200% zoom, 320 px reflow and text spacing checked
- [ ] Contrast measured on rendered colours, including text over images
- [ ] WCAG 2.2 additions checked: focus not obscured, dragging, target size, consistent help, redundant entry, accessible authentication
- [ ] `lang` on page and on Telugu or Hindi passages; OTP fields accept paste
- [ ] PDFs in key flows checked or flagged

## Before handoff
- [ ] Criteria table complete for all A and AA criteria
- [ ] Each issue has criterion, severity, qa-scale mapping, evidence and fix direction
- [ ] Conformance statement follows the logic and names scope, date, technologies
- [ ] Not-tested list explicit, including missing AT pairs
- [ ] AT and browser versions recorded
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Asked to certify or declare legal compliance
- [ ] Asked to mark untested criteria as Pass
- [ ] The only test target is a third party's live site
- [ ] A key flow is fully blocked for keyboard users at release time

## Engineering standards upgrade
- [ ] Applicable standards identified with `python tools/quality_gate.py applicable` for the project's profile and product types
- [ ] Requirements I own are met with evidence of the right type; planned checks are labelled planned
- [ ] A different reviewer verifies my requirements where the profile requires independent review
- [ ] Critical defects reported immediately and not averaged away
