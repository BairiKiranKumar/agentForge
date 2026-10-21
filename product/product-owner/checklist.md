# Product Owner: Checklist

## Before starting
- [ ] PRD or decision is approved and priorities are banded (Now, Next, Later)
- [ ] Designs exist for next-cycle stories, or "no design needed" is stated per story
- [ ] Rule IDs and data definitions available for rule-heavy areas
- [ ] Throughput for the last three cycles known, or marked as first cycle
- [ ] Third-party dependencies (payment gateway, WhatsApp, SMS) checked for setup status

## While working
- [ ] Story map drawn with the first release line
- [ ] Each story names a specific role and a real benefit in "so that"
- [ ] Job story format used where the trigger situation matters
- [ ] Criteria cover happy path, validation, error and empty states, permissions
- [ ] Device and network criteria added for uploads, payments and long lists
- [ ] India formats specified where relevant (+91 phone, ₹ with lakh grouping, dates)
- [ ] Criterion count matches story size; oversized stories split
- [ ] Each split piece is valuable alone; parent and children linked
- [ ] Spikes are time-boxed with a written output
- [ ] Rules referenced by ID, not rewritten in each story
- [ ] Every story passes the INVEST gate and Definition of Ready
- [ ] Ordering reason recorded for any move above a higher priority band

## Before handoff
- [ ] Committed load at or under about 85% of average throughput
- [ ] Cycle goal is one sentence tied to the PRD outcome
- [ ] No criterion uses an adjective without a number or observable state
- [ ] Acceptance verdicts cite evidence per criterion (spec, screenshot, preview URL)
- [ ] Rejected stories returned with failed criteria listed
- [ ] "Not now" list updated
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Asked to accept work that has not been built or shown on a preview
- [ ] A criterion was changed mid-cycle without `product-manager` agreement
- [ ] A story would change what a client or pilot customer was promised
- [ ] A failing security, privacy or payment criterion is proposed for acceptance "for now"
