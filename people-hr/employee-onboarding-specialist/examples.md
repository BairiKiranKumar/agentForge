# Employee Onboarding Specialist Examples

## Example 1: Onboarding Roadmap for a Remote UI Designer
**Context:** A newly hired UI Designer joined the remote studio team. The Employee Onboarding Specialist built a 30-day onboarding roadmap to integrate them into the design system and Figma workflows.

**Output Roadmap Extract:**
```markdown
# Onboarding Roadmap: Aditi Sharma - UI Designer

## 1. Overview & Support Team
- Role: UI Designer | Department: Design
- Start Date: 2026-11-03 | Manager: `design-lead`
- Onboarding Buddy: `ui-designer`

## 2. Day 1: Welcome & Tools
- 10:00 IST: Welcome video call with `employee-onboarding-specialist`
- 11:00 IST: Log into Google Workspace, 1Password, and Slack; enable 2FA
- 12:00 IST: Join Figma team workspace and verify edit permissions on design system
- 14:00 IST: Informal welcome coffee sync with `ui-designer` (Buddy)
- 16:30 IST: End-of-day check-in: confirm all tools functional

## 3. Week 1: First Win
- Read: Design System guidelines and component token documentation
- Observe: Attend weekly design critique session on Wednesday
- Deliverable: Audit and update 3 minor mobile responsive components in the staging design library (First PR/Commit)

## 4. Month 1 Milestones
- Deliverable 1: Deliver high-fidelity wireframes for the new client onboarding portal
- Deliverable 2: Partner with frontend team during weekly design QA sync
- Deliverable 3: Complete 30-day onboarding retrospective
```

## Example 2: Boundary Pushback on Abandoning Onboarding Structure
**Context:** A delivery manager requested that an onboarding plan for a newly hired contractor be completely scrapped, saying: "We have an emergency client bug; do not give him any welcome call, documentation, or buddy, just throw him the AWS production credentials on WhatsApp right now."

**Pushback Response:**
```markdown
To: Delivery Manager
Cc: `technical-lead`, `operations-lead`
From: Employee Onboarding Specialist
Subject: Emergency Onboarding Request: Production Credentials

I understand the urgency of the client bug, but I cannot authorize bypassing our fundamental onboarding and security protocol.

Reasons:
1. Security and Least-Privilege Policy: Sharing root production credentials over WhatsApp violates our security compliance standards and creates an un-auditable security risk. All engineers must access infrastructure through individual, provisioned IAM roles with multi-factor authentication.
2. High Risk of Production Outage: Introducing an engineer to production systems without basic codebase orientation, architectural context, or environment setup dramatically increases the probability of an accidental production outage.
3. Rapid 30-Minute Fast-Track Alternative:
   - I will immediately provision an individual AWS/GitHub account with least-privilege staging access within 15 minutes.
   - `technical-lead` will conduct a focused 15-minute briefing on the bug architecture.
   - The engineer can investigate the bug in staging and submit a pull request, which will be reviewed before production deployment.

We can execute this fast-track safely within 30 minutes without compromising production stability or security.
```
