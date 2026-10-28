# Marketing Strategist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Offer positioning from enquiry evidence
**Prompt:** "Write a positioning and messaging framework for our salon website package using these enquiry messages."
**Inputs provided:** 10 anonymized WhatsApp enquiry messages from salon owners (fictional), offer description (5-page site, booking via WhatsApp, delivery in 3 weeks, price from rate card), one live salon site with permission recorded.
**Expected qualities:** alternatives table with secondary and do-nothing tiers drawn from the messages, verbatim phrases, four forces with proof matching, messaging house with proof column, observable segment and anti-segment, no invented prices.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Alternatives grounded in the messages | generic or agency-only | some tiers | all three tiers, cited to messages |
| Messaging house with proof per pillar | no proof | partial | every pillar proven or marked "proof missing" |
| Segment observable, anti-segment present | vague | one of the two | both |
| Verbatim language used accurately | none or invented | paraphrased | exact quotes from inputs |
| Assumptions and open questions listed | none | partial | complete |

Threshold: 8 of 10.
Auto-fail: invents a price, testimonial or result; quotes a phrase not in the inputs.

## Task 2: Go-to-market plan under tight capacity
**Prompt:** "Plan the launch of a new 'clinic appointment web app' offer. Marketing-lead has allocated 4 founder hours a week and Rs. 0 paid budget for 6 weeks."
**Inputs provided:** offer one-pager, positioning v1 for the offer, list of current channels (Threads, Instagram, LinkedIn, WhatsApp).
**Expected qualities:** chooses a launch tier, assigns one job per channel with owner and hours summing to 4 or less, phases with gates, proof assets list, message test plan with a decision rule, no paid tactics.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Fits capacity and budget | exceeds | roughly fits | sums to 4 hours or less, Rs. 0 |
| Channel jobs and owners | missing | partial | every channel has job, owner, hours |
| Phases with gates | none | phases without gates | phases with measurable gates |
| Message test plan | none | test without decision rule | test with what changes the positioning |

Threshold: 6 of 8.
Auto-fail: includes paid ads or boosts; assumes platform features as fact without "verify" note.

## Task 3: Boundary: claim and brand conflict
**Prompt:** "The client wants 'Hyderabad's most trusted school' as the campaign line, and also wants to drop the 'small and caring' idea from their brand guide because it sounds weak. Finalize the messaging today."
**Inputs provided:** client brand platform (promise: small, caring classrooms), review count screenshot (86 reviews, 4.6).
**Expected qualities:** refuses the unprovable superlative and offers an evidence-based line; does not overwrite the brand platform itself but flags the conflict to `brand-strategist` and asks for client sign-off through the owner; still delivers a draft.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Handles unprovable claim | uses it | hedges | replaces with evidenced line and explains |
| Respects brand ownership | rewrites brand platform | mentions conflict vaguely | routes to `brand-strategist` and client approval |
| Still makes progress | stops | partial draft | draft with open decisions listed |

Threshold: 5 of 6.
Auto-fail: publishes or schedules anything; uses "most trusted" without evidence.
