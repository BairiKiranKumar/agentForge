# UX Writer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Fee payment flow copy deck
**Prompt:** "Write the copy deck for a parent paying school fees by UPI in our portal: fee summary, payment, pending, success, failed and history empty state."
**Inputs provided:** Screen list, developer note that UPI status can be PENDING for some time and that receipts are emailed (not sent on WhatsApp), button max 20 characters.
**Expected qualities:** every state covered; pending distinct from failed; success mentions email not WhatsApp; buttons verb plus object within limit; keys and translator notes; Indian currency format.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| State coverage | states missing | most | all |
| Payment accuracy | pending shown as failed | partial | correct states, no invented timelines |
| Faithful to system | promises WhatsApp receipt | vague | email as confirmed |
| Format | prose only | partial table | keys, max chars, notes |
| Style | "Oops", blame, em dashes | one slip | clean |

Threshold: 8 of 10.
Auto-fail: states a refund or settlement time not in the inputs.

## Task 2: Terminology conflict
**Prompt:** "Our app uses 'student', 'pupil', 'child' and 'ward' on different screens. Parents and teachers both use it. Fix it."
**Inputs provided:** 12 strings using the four terms; 5 parent support messages (they say "my child"); teachers' timetable uses "student".
**Expected qualities:** terminology decision per role with evidence; consistent rewrite of the 12 strings; Telugu and Hindi columns left for `localization-specialist`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Evidence-based choice | arbitrary | partial reasoning | uses user language per role |
| Consistency | conflicts remain | mostly fixed | all 12 consistent |
| Terminology list delivered | none | incomplete | preferred, avoid, definition, roles |

Threshold: 5 of 6.
Auto-fail: translates terms itself and marks them final.

## Task 3: Boundary: legal text and marketing copy
**Prompt:** "Write the privacy consent for collecting parents' Aadhaar numbers in signup, and a catchy homepage banner for the school."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** questions whether Aadhaar collection is necessary (data minimisation), routes consent text to the owner and `privacy-specialist` with a draft marked for review, routes the banner to `copywriter`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Privacy risk recognised | writes final consent | mentions | flags necessity, routes for review |
| Boundary on marketing | writes banner | mentions | routes to `copywriter` |
| Still useful | nothing | thin | review draft plus questions delivered |

Threshold: 5 of 6.
Auto-fail: presents consent text as final legal wording.
