# Risk Manager Examples

## Example 1: Risk Register for an Enterprise Telehealth Platform
**Context:** A digital healthcare platform in India was building a real-time video consultation feature. The Risk Manager built the delivery risk register.

**Output Register Extract:**
```markdown
# Project Risk Profile: Telehealth Web Platform

## 1. High-Priority Risk Entry: R-003
- Risk ID: R-003
- Category: Technical & Third-Party Integration
- Risk Statement: "If the WebRTC media server fails to traverse symmetric NAT firewalls on low-end Indian mobile networks, then video consultation calls will fail to connect for tier-2/3 patients, resulting in severe client product rejection."
- Accountable Owner: `technical-lead`

## 2. Assessment & Scoring
- Pre-Mitigation Probability: 4 (Likely: 60-80%)
- Pre-Mitigation Impact: 5 (Catastrophic: Core value proposition fails)
- Exposure Score: 20 / 25 (High / Red Tier)

## 3. Early Warning Indicators & Triggers
- Indicator: WebRTC connection failure rate exceeding 5% in staging automated tests.
- Trigger Threshold: >3% call failure rate on 4G simulated network throttling.

## 4. Treatment Strategy & Action Plan
- Strategy: Treat (Mitigate)
- Mitigation Plan (Preventive):
  1. Provision dedicated TURN servers across dual Indian regions (Mumbai & Hyderabad) using coturn on AWS EC2.
  2. Implement automated fallback from video to VoIP audio-only if bandwidth drops below 150 kbps.
  3. Schedule a 2-day network stress test across real 3G/4G connections by Sprint 3.
- Contingency Plan (Fallback):
  - License commercial Agora / Twilio video SDK fallback if open-source WebRTC connection rates stay below 95% by Week 6.
- Target Post-Mitigation Score: Probability 2 * Impact 3 = Score 6 (Low / Green Tier).
```

## Example 2: Boundary Pushback on Treating Active Bugs as Risks
**Context:** A project manager faced 15 open critical defect tickets on the staging environment 3 days before client UAT. To avoid reporting an "Amber" project status, the PM attempted to log the active defects as "Technical Risks" in the Risk Register.

**Pushback Response:**
```markdown
To: Project Manager
Cc: `delivery-manager`, `qa-lead`
From: Risk Manager
Subject: Governance Boundary: Classification of Active Defects vs Risks

I have reviewed the 15 items you submitted for logging in the Project Risk Register. I must decline to log these items as delivery risks.

Reasons:
1. Probabilistic Risks vs Deterministic Issues: By definition (ISO 31000 and PMBOK), a Risk is an uncertain future event that has not yet occurred (Probability < 100%). A software defect that is currently active and reproducible on staging is a known, deterministic Issue (Probability = 100%).
2. Transparency & Governance: Logging active blockers as future risks obscures the true health of the software. Active defects belong in the Defect / Issue Log and directly impact our Quality Gates.
3. Correct Operational Action:
   - These 15 items must remain in the Defect Tracking System under `qa-lead` triage.
   - You must report the schedule status as AMBER or RED in Friday's status report because these active defects currently block the UAT entry gate.
   - I will maintain a legitimate Risk entry: "R-008: If defect remediation takes longer than 3 days, then UAT kickoff will slip to next Wednesday."

Let's maintain clear, honest separation between current reality and future uncertainty.
```
