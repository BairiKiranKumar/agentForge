# Acceptance Coordinator Checklist

## Before starting
- [ ] Review approved Statement of Work (SOW) milestone deliverables and functional requirements
- [ ] Ingest internal QA certification report from `qa-lead` verifying 0 open Sev 1/2 defects
- [ ] Verify that UAT staging environment is deployed, stable, and seeded with realistic test data
- [ ] Confirm client tester roster and identify authorized contractual acceptance sign-off authority
- [ ] Author comprehensive UAT Plan detailing entry/exit gates, schedule, and defect severity rules

## While working
- [ ] Translate functional specs into plain-language business test scripts with expected outcomes
- [ ] Host UAT Kickoff orientation with client testers to explain test tool and scoring rules
- [ ] Verify client tester credentials and ensure all testers can access staging without impediment
- [ ] Triage incoming client feedback twice daily, separating legitimate defects from scope changes
- [ ] Route all out-of-scope feedback items immediately to `scope-change-manager`
- [ ] Facilitate daily 15-minute UAT defect review sync with engineering and client test leads
- [ ] Track daily test execution burn-down and chase lagging client test cases
- [ ] Coordinate with `devops-engineer` and developers to deploy verified bug fixes to staging

## Before handoff
- [ ] Conduct final UAT Exit Gate audit: verify 100% core test cases passed and 0 open Sev 1/2 defects
- [ ] Formulate Milestone Acceptance Certificate detailing test metrics and formal declaration
- [ ] Secure dual execution signatures from authorized client sponsor and `delivery-manager`
- [ ] Transmit signed Acceptance Certificate to `invoicing-specialist` to release milestone invoice
- [ ] Hand over accepted milestone build records to `handover-specialist`
- [ ] Confirm zero em dashes are present in any acceptance documentation
- [ ] Format handoff according to `orchestration/handoff-format.md` standards

## Stop and escalate if
- [ ] Client encounters a critical Sev 1 defect on Day 1 that halts all further testing
- [ ] Client leadership refuses to execute acceptance certificate despite 100% passed test criteria
- [ ] Client testing stalls completely due to internal client unavailability past contractual review window
