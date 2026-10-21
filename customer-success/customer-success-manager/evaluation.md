# Customer Success Manager: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Formulate 90-day Client Success Plan with measurable business outcomes
**Prompt:** "Create a 90-day Client Success Plan for a multi-specialty dental clinic that just launched an online appointment booking and patient records portal. Define 3 adoption milestones, establish the 100-point health score model, and map technical features to business ROI."
**Inputs provided:** Clinic handles 40 patients/day; goal: reduce booking phone calls by 50% and decrease appointment no-shows.
**Expected qualities:** 3 phased adoption milestones, health score formula across Adoption (40%), Service (30%), Sentiment (30%), business ROI mapping (no-show reduction).

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Adoption milestones definition | Vague goals | 1-2 generic milestones | 3 phased, measurable adoption milestones with target dates |
| Health score modeling | No scoring | Basic score | Objective 100-point model across Adoption, Service, Sentiment |
| Business ROI translation | Technical jargon | Basic metrics | Translates features into clinic metrics (phone call reduction, no-shows) |
| Actionable review cadence | No review schedule | Mentions meetings | Defines monthly touchpoints and QBR agenda |

Threshold: 7 of 8.
Auto-fail: health score lacks measurable criteria; fails to connect portal usage to clinic business outcomes.

## Task 2: Triage declining health score and formulate intervention
**Prompt:** "A school client's health score has dropped from 85 to 55 over the past 30 days. Weekly staff logins dropped by 60%, and 3 bug tickets regarding report card printing have remained unresolved for 2 weeks. Formulate an immediate 4-step intervention plan."
**Inputs provided:** Health score = 55 (Red); login drop 60%; 3 open bug tickets.
**Expected qualities:** Acknowledges critical churn threshold (<60), prioritizes resolving blocking report card bugs with engineering, schedules operational retraining, coordinates with `retention-specialist`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Severity identification | Misses risk level | Notes low score | Explicitly recognizes Red-zone health score requiring immediate intervention |
| Root cause resolution | Ignores bugs | Mentions tickets | Directly ties staff login drop to open report card printing bugs |
| Coordinated action plan | Vague advice | 2 steps | 4 concrete steps: bug escalation, staff retraining, executive check-in, retention play |

Threshold: 5 of 6.
Auto-fail: treats a sub-60 health score as normal; ignores unresolved software bugs driving user disengagement.

## Task 3: Boundary: pushback against scope creep during business review
**Prompt:** "During a quarterly review, the client says: 'We are happy with the website, but you must now integrate an AI chatbot that answers customer questions over phone calls for free as part of our retainer.' How do you respond?"
**Inputs provided:** None beyond prompt.
**Expected qualities:** Acknowledges idea, clarifies retainer scope boundaries (maintenance vs new development), protects studio from unpaid engineering, routes to `account-manager` for formal scoping.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Scope boundary clarity | Agrees to build | Hedges | Firmly clarifies that telephony AI bots are outside maintenance retainers |
| Diplomatic client handling | Rude refusal | Over-apologetic | Warm, professional acknowledgement while protecting commercial boundaries |
| Commercial handoff path | Drops request | Suggests hack | Routes request to `account-manager` for proper scoping and quotation |

Threshold: 5 of 6.
Auto-fail: commits the studio to building custom telephony AI modules for free under a maintenance retainer.
