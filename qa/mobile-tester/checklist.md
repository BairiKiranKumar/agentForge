# Mobile Tester: Checklist

## Before starting
- [ ] Mobile build artifact, staging URL, or preview deployment accessible
- [ ] Target mobile device matrix verified (mid-range Android, budget Android, iOS)
- [ ] USB debugging or real-device testing environment initialized
- [ ] Pre-seeded mobile test user accounts available
- [ ] Third-party app dependencies identified (WhatsApp, UPI, Phone, Camera)

## While working
- [ ] Page tested at 360px viewport width (standard Indian entry Android width)
- [ ] All clickable buttons and icons meet the 44 x 44 px touch target standard
- [ ] Form inputs tested with virtual keyboard active; input remains visible
- [ ] Dropdowns, date pickers and select menus open native mobile pickers cleanly
- [ ] Pinch-to-zoom and double-tap behaviors verified
- [ ] Android hardware/gesture back button closes drawers and modals first
- [ ] WhatsApp intent links open native WhatsApp app with pre-filled message
- [ ] Tel links trigger phone dialer with sanitized phone number
- [ ] Network throttled to congested 4G (200ms latency, 1.5 Mbps); skeleton states verified
- [ ] Offline mode tested; app shows user-friendly offline message without crash
- [ ] Orientation switched to landscape; layout adapts without text clipping
- [ ] Bottom navigation bars do not obscure bottom content or sticky buttons
- [ ] Touch gestures (horizontal carousel swipes, pull-to-refresh) operate smoothly

## Before handoff
- [ ] Mobile test report filled with actual device models and OS versions
- [ ] Defects logged with screen recording videos and clear reproduction steps
- [ ] Verified on at least one physical Android hardware handset
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Core checkout or enquiry flow is impossible to complete on a 360px screen
- [ ] Virtual keyboard completely blocks the submit action with no scroll ability
- [ ] Site causes catastrophic browser freezing or crashes on mid-range Android phone
- [ ] Payment flow fails or breaks deep links on mobile devices
