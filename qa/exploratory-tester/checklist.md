# Exploratory Tester: Checklist

## Before starting
- [ ] What changed and why is known (story, PR summary or release notes)
- [ ] Risk areas from `qa-lead` or your own list drafted
- [ ] Known issues read
- [ ] Build, environment and role accounts recorded (not production)
- [ ] Test data file ready: Telugu and Hindi strings, long names, lakh amounts, month-end and midnight dates

## Charters
- [ ] Each charter states target, resources and information sought
- [ ] Each charter fits one time box (45, 60 or 90 minutes)
- [ ] Charters ranked by risk
- [ ] At least one role-swap charter for multi-role apps
- [ ] At least one interruption charter for mobile flows (network loss, app switch, refresh)

## During a session
- [ ] Timer running; notes time-stamped
- [ ] SFDIPOT rows checked for blind spots, especially Data and Time
- [ ] Tour switched when it stops producing information, and the switch logged
- [ ] "Follow the data" done: value checked in list, detail, PDF, message and export
- [ ] Links opened from WhatsApp (in-app browser) where the product is shared there
- [ ] Bugs given minimal repro steps and platform; issues logged separately
- [ ] Critical bug reported immediately

## Before handoff
- [ ] Session sheet closed with coverage, task breakdown, bugs, issues
- [ ] "Not covered" filled in honestly
- [ ] PROOF debrief written the same day
- [ ] Follow-up charters, cases or automation candidates proposed
- [ ] Coverage summary uses depth and confidence levels
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Exploration needs request tampering, scanning or brute force (route to `security-testing-specialist`)
- [ ] Data from another user or role is visible
- [ ] Only production is available
- [ ] The build is too broken to explore
