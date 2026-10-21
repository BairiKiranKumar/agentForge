# Interaction Designer: Checklist

## Before starting
- [ ] Flows with required states received from `ux-designer`
- [ ] Screens or components received from `ui-designer` (or wireframes)
- [ ] API timing, idempotency and realtime behaviour confirmed with developers
- [ ] Existing motion tokens read, if any
- [ ] Every stateful component and every network action listed

## While working
- [ ] State machine written per component; no dead-end states
- [ ] Each state defines visible change, accepted input, focus and exit
- [ ] Feedback pattern chosen per event from the pattern table
- [ ] Loading strategy matches expected wait band
- [ ] Loader delay (about 300 ms) and minimum display (about 500 ms) specified
- [ ] Every transition has trigger, properties, duration and easing
- [ ] Only transform and opacity animated where possible; no input blocked
- [ ] Reduced-motion variant written per transition
- [ ] Validation on blur, re-validate on input after error, focus first error on submit
- [ ] Indian formats handled: 10-digit mobile, +91, 6-digit PIN
- [ ] Optimistic vs pessimistic decided per action; none optimistic on money
- [ ] Offline, retry, idempotency and conflict rule defined per network action
- [ ] UPI and app-switch return states specified, including pending
- [ ] Every gesture has a visible single-pointer alternative
- [ ] No gestures conflict with Android edge back gestures
- [ ] Focus destination defined for open, close, submit and error
- [ ] Live region announcements defined for async results

## Before handoff
- [ ] Text slots listed for `ux-writer` with max characters
- [ ] Focus and announcement plan reviewed with `accessibility-designer`
- [ ] Riskiest behaviours prototyped or demonstrated
- [ ] States worth E2E coverage listed for `playwright-specialist`
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] An order, payment or attendance action cannot be made idempotent
- [ ] Undo is required for something already sent outside the app
- [ ] A behaviour would send customer messages automatically without approval
