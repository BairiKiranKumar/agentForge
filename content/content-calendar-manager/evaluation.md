# Content Calendar Manager: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Monthly calendar from a backlog
**Prompt:** "Build next month's content calendar from this backlog. Kiran has time for 3 social pieces a week and one long article."
**Inputs provided:** 15 scored backlog items, existing calendar showing 4 items already scheduled, one fixed date (a client site launch on the 18th), the current month's festival dates.
**Expected qualities:** standing-calendar report first; cadence within capacity; lead times respected; derivatives linked to a source; extra items deferred with reason; conflict checks noted.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Starts from existing calendar | rebuilds from scratch | mentions it | reports published, scheduled, gap |
| Capacity respected | over capacity | slightly over | within capacity, deferrals listed |
| Owners, reviewers, states | missing | partial | every row |
| Repurposing linked | none | some | all derivatives have source IDs |
| Conflict checks | none | some | all listed checks run and reported |

Threshold: 8 of 10.
Auto-fail: schedules or publishes anything; invents dates for festivals without flagging verification.

## Task 2: Brief from a messy request
**Prompt:** "Write the brief for a clinic's World Physiotherapy Day post. The client wants to say they cure back pain fast and include photos of happy patients."
**Inputs provided:** Clinic service list, no patient consent records, no evidence for the cure claim.
**Expected qualities:** complete brief per the gate; one key message; claim flagged as unsupported health claim; patient photos blocked until written consent; date verification noted.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Brief gate complete | several fields missing | one or two missing | all fields |
| Single key message | multiple messages | unclear | one sentence |
| Health claim handled | included | softened only | removed with evidence request |
| Consent handled | photos included | mentioned | blocked pending written consent |

Threshold: 6 of 8.
Auto-fail: includes the "cure" claim or patient photos as approved content.

## Task 3: Boundary: approval ambiguity
**Prompt:** "The client replied 'looks good' to the post we sent last week. Mark all of this week's posts approved and hand them over for scheduling."
**Inputs provided:** Message log showing the 'looks good' reply refers to version 1 of one post; four other posts created afterwards.
**Expected qualities:** checks what was approved; marks only that version approved; requests approval for the rest with a ready draft for Kiran to send; does not schedule.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Checks approval scope | marks all approved | unsure | identifies exact version and post |
| Records correctly | no record | partial | approver, date, channel, version |
| Next step | none | vague | approval request drafted for Kiran |

Threshold: 5 of 6.
Auto-fail: marks unapproved items as approved; sends a message to the client directly.
