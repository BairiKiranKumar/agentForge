# Support Triage Specialist: Checklist

## Before starting
- [ ] Inbound support channels checked (Email, WhatsApp, Web Portal, Support Desk)
- [ ] Account tier and SLA commitments reviewed for submitting client
- [ ] Technical ownership directory and on-call schedule confirmed
- [ ] Known system incidents or ongoing deployments checked

## While working
- [ ] Duplicate submissions identified and merged into single ticket
- [ ] Inbound inquiry categorized (Bug, Usability, How-To, Billing, Feature Req)
- [ ] Objective severity level assigned (P1 Critical through P4 Low)
- [ ] Mandatory details verified: user ID, URL, device/browser, error message
- [ ] Targeted clarification drafted if critical repro context is missing
- [ ] First-response acknowledgment drafted with empathetic, professional tone
- [ ] Next check-in time and ticket ID explicitly stated in acknowledgment
- [ ] Ticket assigned to appropriate technical or commercial owner
- [ ] P1 outages escalated immediately to `incident-coordinator`

## Before handoff
- [ ] Ticket status, severity, and assigned owner updated in support tracker
- [ ] First response draft dispatched (or approved by the owner for client communication)
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Ticket reports an active data breach, unauthenticated data exposure, or security vulnerability
- [ ] Widespread outage affects all clients or core payment processing
- [ ] Client decision-maker issues an ultimatum threatening contract termination
- [ ] Ticket volume surges >300% above normal, indicating major platform incident
