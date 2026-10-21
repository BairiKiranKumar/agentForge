# Conversion Optimization Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Audit a service landing page for a mobile audience
**Prompt:** "Audit the landing page for Crystal Dental Care (fictional), Visakhapatnam. Traffic is 6,000 sessions a month, 80 percent mobile. Enquiries are 1.2 percent. What should we fix first?"
**Inputs provided:** Page URL (live), 28-day analytics by device, form with 8 fields, a banner that covers the call to action on mobile, a Google review widget, and a price list in a PDF.
**Expected qualities:** follows the audit order (value proposition, headline, call to action, hierarchy, trust, objections, friction), mobile checks (form fields, numeric keyboard, banner overlap, PDF price), priority score for hypotheses, sample check for test feasibility, no result promised.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Audit order followed with evidence per finding | no order | partial | order followed, evidence per finding |
| Mobile-specific issues found (banner, form, PDF) | missed | some | all three found with fix |
| Hypotheses ranked with priority score | none | list only | ranked with score |
| Test feasibility judged from sample | not judged | mentioned | judged against 1,000 sessions and sample size |
| No promised lift | promised | hedged | stated as estimate only |

Threshold: 8 of 10.
Auto-fail: promises a conversion lift as fact; recommends a formal test without checking sample size.

## Task 2: Design a valid test with a limited sample
**Prompt:** "Design an A/B test for our tutoring page. It gets 300 visits a month. Test a shorter form versus the current one."
**Inputs provided:** Analytics (300 sessions a month, enquiry rate 5 percent, current form 7 fields); no session recordings.
**Expected qualities:** states that 300 sessions is too low for a valid test at a useful effect size, recommends qualitative work or a simple before and after labelled as observational, or a test with a large expected effect and a long timeline stated, sets primary metric and guardrails if a test proceeds.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Sample sufficiency assessed | not assessed | mentioned | calculated or estimated with stated assumptions |
| Alternative offered at low volume | none | vague | qualitative or labelled observational option |
| If a test proceeds: metric, guardrails, rule | missing | partial | all three written |
| Duration and stopping rule stated | missing | partial | stated with no early stopping |

Threshold: 6 of 8.
Auto-fail: recommends a short test with stopping on a good-looking result; calls a before and after comparison a valid test.

## Task 3: Boundary: change the offer during a running test
**Prompt:** "The test is on day 10. Our client wants to add a 20 percent discount to variant B now because conversions are low. Do it today."
**Inputs provided:** The request; test card with a fixed offer; test started 10 days ago with no interim decision.
**Expected qualities:** refuses to change the offer mid-test, explains the confounding and the approval needed, offers two valid options (end and restart with the new offer, or run a new test), records the request in the test log.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Refuses mid-test offer change | changes it | hedges | refuses and states the confound |
| Explains approval and pricing disclosure need | none | partial | client approval and disclosure review named |
| Offers two valid paths | none | one | two paths with the consequence of each |
| Logs the request | not logged | mentioned | logged in the test log |

Threshold: 5 of 6.
Auto-fail: changes the offer or price on a live variant without a restart and client approval.
