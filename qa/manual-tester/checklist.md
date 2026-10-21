# Manual Tester: Checklist

## Before starting
- [ ] Acceptance criteria read; ambiguous ones sent to `product-owner`
- [ ] Build id and environment recorded (not production)
- [ ] Test accounts per role available
- [ ] Known issues list read to avoid duplicate defects
- [ ] Real messages, emails and payments are stubbed or in test mode

## Case design
- [ ] Each criterion has at least one positive and one negative case
- [ ] Boundary values at min-1, min, max and max+1 for every limit
- [ ] Decision table for rules with three or more conditions
- [ ] State transitions, including invalid jumps, for records with statuses
- [ ] Role x action matrix covered for role-based screens
- [ ] Test data includes Telugu or Hindi script names, long names, +91 formats, PIN codes, INR with lakh grouping
- [ ] No real person's data in test data

## Execution
- [ ] Smoke run first; untestable build reported before full run
- [ ] Result recorded per case with build and device
- [ ] Pass confirmed by outcome (confirmation, stored record, response), not by appearance
- [ ] Every Blocked names its blocker; every Not run has a reason
- [ ] Defects reduced to minimal steps and reproduced at least twice
- [ ] Intermittent defects report frequency
- [ ] Observations outside the script logged for `exploratory-tester`

## Before handoff
- [ ] Every Fail links a defect with proposed severity and user-impact reason
- [ ] Fixed defects retested on the new build plus related cases
- [ ] Regression scope matches the selection table for the change
- [ ] Case added for each escaped defect
- [ ] Evidence screenshots masked of personal data
- [ ] Run summary with totals, defects by severity, blocked and not-run lists
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Only production is available for testing
- [ ] The build changes mid-run
- [ ] A case would trigger a real payment or message to a real person
- [ ] You are asked to mark cases Pass without running them
