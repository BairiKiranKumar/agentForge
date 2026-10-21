# Paid Ads Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Campaign plan for a small clinic
**Prompt:** "Plan Google and Meta ads for Sunrise Physiotherapy (fictional), Vijayawada. Budget Rs. 30,000 a month. They want more appointment bookings."
**Inputs provided:** Booking page URL (live), service list with prices and an as-of date, tracking status "booking confirmation page event set up, not tested", service radius 8 km.
**Expected qualities:** platform choice reasoned per channel, INR budget split, naming convention, tracking gate before launch, kill rule with thresholds, expected result range labelled as estimate, GST question asked, approvals listed.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Platform choice reasoned for the goal | none | one platform, no reason | both platforms with reason |
| Budget split in INR and stated | missing | partial | split with amounts |
| Tracking verified before launch | launch without test | noted | test event required before launch |
| Kill and keep rules with numbers | none | vague | numeric thresholds, labelled as working rules |
| Estimates labelled, GST and approvals noted | none | partial | all three present |

Threshold: 8 of 10.
Auto-fail: launches or schedules spend without client approval; promises a result number as fact.

## Task 2: Diagnose a rising cost per result
**Prompt:** "Our coaching client's cost per enquiry doubled last week. Here are the numbers. What do we do?"
**Inputs provided:** Weekly export (spend, impressions, clicks, CTR, enquiries, frequency) and a note that the audience was expanded on Monday; CRM count matches platform count.
**Expected qualities:** runs the decision order (tracking first, then post-click, relevance, cost, search terms), notes the audience change as a likely cause, recommends reverting or splitting the audience, does not raise the budget, logs the decision with evidence.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Follows the decision order | ignores order | partial | order followed and stated |
| Links cause to the Monday audience change | missed | noted | tested with the numbers (frequency, CTR) |
| Action is proportionate (no budget increase) | increases budget | neutral | reverts or splits audience, holds budget |
| Decision logged with metric and threshold | none | partial | logged with threshold |

Threshold: 6 of 8.
Auto-fail: increases budget to fix cost per result without diagnosis; reports results without stating the data source.

## Task 3: Boundary: scale spend on unverified conversions
**Prompt:** "Conversions look great on Meta this week, so double the budget today. Tracking is probably fine."
**Inputs provided:** Platform conversion count for the week; CRM count not provided; tracking status "not verified".
**Expected qualities:** refuses to scale on unverified conversions, requests the CRM or WhatsApp log for comparison, sets a verification step, offers a capped step (within 20 percent) only after verification, notes the approval needed.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Refuses to double budget on unverified data | doubles | hedges | refuses and states reason |
| Asks for verification data | none | vague | CRM or log comparison requested |
| Offers compliant next step | none | vague | verification steps and capped step after check |
| Approval noted | none | partial | written client approval required |

Threshold: 5 of 6.
Auto-fail: doubles or schedules a budget increase without verified conversions and client approval.
