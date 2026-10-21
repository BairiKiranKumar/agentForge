# Technical Support Specialist: Checklist

## Before starting
- [ ] Triaged support ticket and customer symptom description reviewed
- [ ] Staging environment access and appropriate test user credentials verified
- [ ] Customer browser, operating system, and screen resolution identified
- [ ] Error monitoring tools (Sentry, server logs) accessible
- [ ] Recent deployment commits checked for related modifications

## While working
- [ ] Reproduction attempted in staging matching customer's exact role and device profile
- [ ] Browser developer tools inspected: Console errors and Network payloads captured
- [ ] Failure layer isolated (Frontend UI vs API/Backend vs Database vs Third-Party)
- [ ] Minimum reproduction steps isolated (unnecessary steps eliminated)
- [ ] Safe, non-technical customer workaround formulated and shared
- [ ] Structured Bug Report authored with Repro Steps, Expected vs Actual, and Logs
- [ ] Specific code location or architectural cause identified where possible
- [ ] Bug ticket assigned to owning developer (`frontend-developer` or `backend-developer`)

## Before handoff
- [ ] Fix deployed to staging independently re-tested using original reproduction steps
- [ ] Customer resolution message drafted in clear, plain business English
- [ ] Ticket updated with resolution evidence and closed
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Bug causes catastrophic live production data loss or corruption
- [ ] Bug reveals an unauthenticated security vulnerability exposing customer data
- [ ] Bug is confirmed to impact 100% of users attempting checkout or login
- [ ] Developer and support specialist reach complete impasse on reproduction validity
