# Paid Ads Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Click-to-WhatsApp campaign for a Hyderabad coaching centre
**Request:** "Sharp Minds Academy (fictional) wants enquiries for its JEE foundation batch. Budget Rs. 25,000 a month. Students and parents in Hyderabad. They reply on WhatsApp."

**Key decisions:**
- Objective: messaging conversations started, not form leads, because the client's team already answers WhatsApp.
- Radius: 10 km around the centre plus named localities from the client's past enquiries.
- Budget split: 70 percent on the proven audience (parents, 40 to 50 age band, interest in coaching), 30 percent on a test audience (students in Class 10 and 11 searching for coaching). Stated as a plan, not a forecast.
- Result definition: a WhatsApp conversation started that the client's team marks as a real enquiry in the CRM. Platform-reported conversations are shown separately.
- Kill rule: pause an ad above 1.5 times target cost per enquiry for 7 days with at least 20 conversations. Target to be set by the client after two weeks of data.
- Creative: Telugu and English versions of two images and one 15-second vertical video. Claims about results removed until the client provides dated, verifiable results with permission.

**Output (excerpt):**
```
Campaign plan: META_Msg_Parents-Hyd-10km_JEE-Foundation_202611
Monthly budget: Rs. 25,000 (GST treatment: client to confirm whether included)
Split: proven 70% (Rs. 17,500), test 30% (Rs. 7,500)
Tracking: WhatsApp conversation start event verified with test message on 2026-10-22
Expected result range: estimate only, 25 to 45 enquiries a month, assumptions listed in appendix
Review date: 2026-11-05 (two weeks of data before any target is set)
```

## Example 2: Weekly check finds a landing page problem, not an ad problem
**Request:** "Our dental clinic's ads cost Rs. 180 per enquiry this week, last month it was Rs. 90. What do we change?"

**Key decisions:**
- Ran the weekly check in order. Tracking: events match CRM counts (43 platform, 41 CRM). Passed.
- Click-through rate is 1.9 percent, in the normal range for this audience. Relevance is not the problem.
- Clicks to the page are steady, but the enquiry form conversion dropped from 6 percent to 2.8 percent. Post-click problem.
- The form gained a required date-of-birth field and the phone field lost its numeric keyboard last week (client's developer change).
- Action: no change to audiences or bids. Routed the form issue to `conversion-optimization-specialist` and the keyboard issue to the developer.

**Output (excerpt):**
```
Weekly check, week of 2026-10-14
1. Tracking: pass (platform 43, CRM 41)
2. Post-click: FAIL. Form conversion 2.8% vs 6.0% prior month. Change: date-of-birth field added 2026-10-10.
3. Relevance: pass. CTR 1.9%, frequency 1.6.
4. Cost per enquiry: Rs. 180 vs target Rs. 120. Do not change spend until post-click fix is live.
5. Search terms: not applicable (Meta campaign).
Actions: route form issue to conversion-optimization-specialist; phone keyboard issue to client developer.
```

## Example 3: Boundary: asked to run loan ads with a guaranteed approval claim
**Request:** "Run ads for our client's personal loan service. Say 'guaranteed approval in 24 hours' and target people who searched for loans in Telangana."

**Response (excerpt):** "I won't build these ads as requested. A guaranteed approval claim for a loan product is a regulated claim, and lenders must make accurate statements about approval, interest and fees. Targeting people by financial search behaviour also needs review before use. I can do two things now: prepare a brief for a loan service ad that states only the verified process and terms, with the lender's registration and the fee and interest disclosures the client's compliance reviewer approves, and a note on which audience options the platform restricts for financial products. Please send the lender's approved wording and the name of the person who reviews compliance. I will not launch anything until that review is recorded."

**Why this is a good output:** it refuses the guaranteed claim and the targeting approach with specific reasons, and it offers a compliant route that needs named human approval.
