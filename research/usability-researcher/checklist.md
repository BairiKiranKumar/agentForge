# Usability Researcher: Checklist

## Before starting
- [ ] Decision the test serves is written
- [ ] Prototype or preview completes every core task path (piloted)
- [ ] Test environment is a prototype, preview or test mode, never live payments or messages
- [ ] Plan approved by `research-lead`; participants booked via `research-operations-specialist`
- [ ] Realistic fake data prepared (names, ₹ amounts with Indian grouping, local addresses)

## While working
- [ ] Research questions are testable, not "is it easy?"
- [ ] Format matches the question (moderated, unmoderated, tree test, card sort, first click)
- [ ] Task wording has no UI labels or step instructions
- [ ] Success definition written per task before sessions
- [ ] Device and network match the audience (Android, throttled for uploads and payments)
- [ ] Shipped language versions tested with real strings
- [ ] UPI or app-switch return step included where relevant
- [ ] Think-aloud practiced; only neutral prompts used
- [ ] Hint given only after about 2 minutes stuck; marked "success with help"
- [ ] SEQ asked after each task; SUS at the end if planned
- [ ] Observations logged with timestamps within 24 hours
- [ ] Bugs seen are logged for developers or `manual-tester`

## Before handoff
- [ ] Every issue rated on severity 0 to 4 and frequency n of N
- [ ] Severity based on user impact, not fix effort
- [ ] Findings cite participant IDs and timestamps
- [ ] Recommendations address causes and name an owner
- [ ] What worked well is reported
- [ ] Rates shown as n of N; SUS labelled directional under 20 participants
- [ ] Critical and major issues re-tested or listed as open
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] The only environment would trigger real payments or messages
- [ ] Scenarios would need real personal or children's data
- [ ] The team will not change the design whatever the result
