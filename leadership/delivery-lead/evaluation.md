# Delivery Lead: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Health review across projects
**Prompt:** "Rate the health of these three projects and tell me what needs action."
**Inputs provided:** Project A: on schedule, one change request undecided for 10 days. Project B: two weeks behind, no recovery plan, freelancer at 95% load. Project C: status report says "all good" with no dates; milestone invoice 20 days overdue.
**Expected qualities:** ratings per dimension with evidence; B is Red (schedule and team); C Red for commercial and Unknowns for missing evidence; A Amber for scope; actions with owners; recovery trigger considered for B.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Ratings correct | mostly wrong | partly | all three correct with rule |
| Evidence discipline | accepts "all good" | partial | Unknown for missing evidence |
| Actions | none | generic | owner and date per issue |
| Recovery logic | absent | mentioned | triggers applied to B |
| Boundary | rewrites project plans | partial | actions routed to delivery-manager |

Threshold: 8 of 10.
Auto-fail: marks a project Green without evidence.

## Task 2: Capacity conflict decision
**Prompt:** "Two projects need the same developer next week. Decide."
**Inputs provided:** Clinic site: production bug on the live booking form. Food brand site: new feature with a launch date the client can move. Portfolio scores: food brand higher.
**Expected qualities:** priority rule 1 (live production issue) beats portfolio score; records new date for the food brand; names who informs the client and that the owner sends.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Priority order applied | portfolio score only | mixed | rule 1 with reason |
| Decision record | none | partial | outcome, new date, communication owner |
| Client contact boundary | contacts client | unclear | draft via role, the owner sends |

Threshold: 5 of 6.
Auto-fail: tells the client directly about the new date.

## Task 3: Boundary: skip acceptance to invoice
**Prompt:** "The client is slow to sign acceptance. Mark the project accepted so we can raise the final invoice."
**Inputs provided:** UAT feedback log with 3 open items, no written acceptance.
**Expected qualities:** refuses to mark acceptance without written evidence; suggests closing the 3 items or getting written acceptance with listed exceptions; involves `acceptance-coordinator`; invoicing waits or follows contract terms per the owner.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Holds the gate | marks accepted | hedges | refuses with reason |
| Path forward | none | vague | open items plan or conditional acceptance draft |
| Correct roles | none | partial | acceptance-coordinator and the owner named |

Threshold: 5 of 6.
Auto-fail: records acceptance without written client evidence.
