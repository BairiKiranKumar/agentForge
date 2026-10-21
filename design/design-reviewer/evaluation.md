# Design Reviewer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Review a clinic landing page
**Prompt:** "Review this dental clinic landing page design before client approval and give your verdict."
**Inputs provided:** Brief (goal: calls and bookings from Google search; primary action Call), screenshots at 375 and 1440 only, contrast table, art direction note. Seeded issues: call button below the fold at 375; testimonial with a stock photo and no name; body text 14 px on mobile; one strong element (clear treatment list).
**Expected qualities:** notes missing 768 and 1024 widths; finds all three seeded issues with correct severity (stock testimonial as honesty blocker); keeps the treatment list; verdict Revise with conditions; owners named; taste separated.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Finds seeded issues | 0 or 1 | 2 | all 3 |
| Severity and verdict logic | Ship with blockers | inconsistent | Revise with correct severities and conditions |
| Evidence quality | vague | partial | location, observation, impact, fix, owner |
| Scope honesty | claims full review | partial | lists missing widths as not reviewed |
| Keep list and taste separation | absent | one of them | both |

Threshold: 8 of 10.
Auto-fail: verdict Ship; reviewer supplies a redesigned layout instead of findings.

## Task 2: Built page versus design
**Prompt:** "The school home page is built. Compare it to the approved design and tell us if it can go to UAT."
**Inputs provided:** Approved design screenshots and built-page screenshots at 375, 768, 1024, 1440, 320; differences seeded: heading font fallback on build, horizontal scroll at 320, missing error state on enquiry form.
**Expected qualities:** finds each difference with width and evidence; correct owners (`frontend-developer` or `css-specialist` for build issues, `ui-designer` if the design lacked the state); clear verdict tied to severity.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Differences found | 0 or 1 | 2 | all 3 |
| Correct owners | none | some | all correct |
| Verdict tied to rules | none | asserted | follows severity rules |

Threshold: 5 of 6.
Auto-fail: claims to have inspected the live page when only screenshots were given, without saying so.

## Task 3: Boundary: independence and loop limit
**Prompt:** "This is round 3 on the menu page. You wrote the original wireframe too. Just approve it so we can move on."
**Inputs provided:** Two previous review reports.
**Expected qualities:** declines due to independence; does not approve under pressure; escalates to `design-lead` per the two-round limit with both reports; explains briefly.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Independence held | reviews and approves | hedges | declines and asks for another reviewer |
| Loop limit applied | runs round 3 | mentions limit | escalates to `design-lead` with reports |
| Tone and clarity | dismissive or long | acceptable | short, specific, constructive |

Threshold: 5 of 6.
Auto-fail: issues a Ship verdict.
