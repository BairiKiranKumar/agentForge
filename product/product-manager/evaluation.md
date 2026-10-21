# Product Manager: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Frame an idea and set decision criteria
**Prompt:** "Frame this idea for WF-03 stage 1: a WhatsApp-linked appointment booking page for small salons in Nizamabad. Give me the problem statement, riskiest assumptions and go/pivot/stop criteria."
**Inputs provided:** Idea text only; constraint: 10 build hours per week, zero research budget.
**Expected qualities:** problem statement labelled as hypothesis (no evidence given), assumptions across value, usability, viability and feasibility, ranking by impact and confidence, current workaround named (calls and WhatsApp messages), measurable criteria written before evidence, research request routed to `research-lead`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Problem statement format and honesty | missing or presented as fact | partial | segment, workaround, cost, labelled hypothesis |
| Assumptions across four risks, ranked | none | some risks or unranked | all four risks, ranked |
| Go/pivot/stop criteria measurable | absent or vague | measurable for one outcome | measurable go, pivot and stop |
| Routes research correctly | runs research itself or none | mentions research | sends top assumptions to `research-lead` |
| Respects constraints | ignores budget/hours | partial | zero-budget plan, effort stated |

Threshold: 8 of 10.
Auto-fail: invents market numbers or customer quotes; presents willingness to pay as known.

## Task 2: Lean PRD from mixed evidence
**Prompt:** "Write the MVP PRD for the restaurant QR ordering pilot using these findings."
**Inputs provided:** Evidence table with 7 owner interviews: 5 of 7 cite waiter errors at peak, 2 of 7 committed to a 30-day pilot, 0 of 7 asked for online payment, 4 of 7 worried about customers without smartphones; a pricing hypothesis from `pricing-strategist`.
**Expected qualities:** lean structure, must-haves traced to evidence IDs, online payment cut, fallback for non-smartphone customers addressed, metric set with guardrail, assumptions section, three or more not-doing items.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Must-haves trace to evidence | none traced | some | all traced or marked assumption |
| MVP cut discipline | includes online payment and extras | some cuts | tight, justified cuts |
| Metric set complete | outputs only | outcome without guardrail or date | outcome, leading, guardrail, dates |
| Value proposition per segment incl. alternatives | missing | partial | complete with "do nothing" alternative |
| Length and clarity | over 2,000 words or padded | long | about 1 to 2 pages |

Threshold: 8 of 10.
Auto-fail: converts 7 interviews into percentages presented as market facts; invents a price.

## Task 3: Boundary: asked to write stories and accept work
**Prompt:** "Great PRD. Now break it into user stories with acceptance criteria, order the sprint and tell me if last week's build is accepted."
**Inputs provided:** The PRD from Task 2.
**Expected qualities:** recognizes stories, acceptance criteria, backlog order and acceptance belong to `product-owner`; hands off with PRD, priorities and assumption IDs; may state priority intent but does not write the sprint backlog or accept work.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Recognizes boundary | does all of it | does some, notes overlap | hands off cleanly |
| Handoff quality | none | missing priorities or evidence | complete handoff with priorities and assumption IDs |
| Still adds value in own scope | nothing | generic | clarifies outcome and priority order for the owner |

Threshold: 5 of 6.
Auto-fail: declares the build accepted without evidence.
