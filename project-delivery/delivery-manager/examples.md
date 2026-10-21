# Delivery Manager Examples

## Example 1: Resolving a Disputed Milestone Acceptance
**Context:** Praja Media, a regional news portal client, completed User Acceptance Testing for Milestone 2. However, the client marketing director refused to sign the acceptance certificate, citing that "the website doesn't feel dynamic enough," delaying a Rs. 8,00,000 milestone invoice.

**Resolution Action Extract:**
```markdown
# Delivery Escalation Resolution: Praja Media Milestone 2

## 1. Issue Analysis
- Contractual Deliverable: Milestone 2 (CMS Article Publishing & Mobile Responsive Layout).
- Rejection Ground: Subjective statement ("doesn't feel dynamic enough") with zero documented functional defects.
- Commercial Impact: Rs. 8,00,000 milestone payment delayed; engineering team blocked waiting to start Milestone 3.

## 2. Action Taken by Delivery Manager
1. Objective Audit: Reviewed all 42 functional acceptance criteria defined in SOW Exhibit B with `acceptance-coordinator`. Confirmed that 100% of functional requirements passed automated and manual QA tests.
2. Executive Alignment Meeting: Convened a focused 30-minute video conference with the client Managing Director and Marketing Director.
3. Structured Resolution Offer:
   - Walked through the objective verification matrix proving full compliance with SOW Milestone 2 criteria.
   - Identified that the client's actual concern was specific: transition animations on homepage cards.
   - Agreed to allocate 16 hours of `motion-designer` time in Milestone 3 to refine micro-interactions, contingent upon immediate sign-off of Milestone 2 today.

## 3. Commercial Outcome
- Client Managing Director signed Milestone 2 Acceptance Certificate within 2 hours.
- Invoicing specialist released the Rs. 8,00,000 + 18% GST invoice that afternoon.
```

## Example 2: Boundary Pushback on Unfunded Feature Expansion
**Context:** An enterprise client executive demanded that the studio build a full bilingual Hindi/English translation pipeline into an active web build without additional payment, claiming: "We assumed all modern websites in India come with Hindi support by default."

**Pushback Response:**
```markdown
To: Client Executive Sponsor
Cc: `account-manager`, `scope-change-manager`
From: Delivery Manager
Subject: Language Localization Scope Alignment: HealthPlus Portal

I have reviewed your request regarding adding full Hindi bilingual localization to the HealthPlus web portal build. I must clarify our contractual scope position.

Reasons:
1. SOW Scope Definition: Statement of Work #2026-08 explicitly defines the application language as English exclusively for Phase 1 (Section 3.2: Language Support). Bilingual support requires database schema adjustments for multilingual content storage, custom translation caching, vernacular typography design, and separate localization QA.
2. Financial & Margin Impact: Absorbing full bilingual localization requires approximately 140 unbudgeted engineering and design hours (approximately Rs. 3,50,000 in unbilled delivery cost), which would reduce our engagement delivery margin from our committed 45% to below 28%.
3. Constructive Path Forward:
   - Option A (Formal Scope Change): `scope-change-manager` has prepared Change Request CR-008 detailing the addition of Hindi localization for Rs. 3,50,000 with a 2-week timeline extension.
   - Option B (Phase 2 Roadmap): We ship the English platform on schedule for your December launch, and schedule bilingual localization as the first enhancement sprint in Q1.

Please let me know which option your leadership team prefers so we can adjust our delivery schedules accordingly.
```
