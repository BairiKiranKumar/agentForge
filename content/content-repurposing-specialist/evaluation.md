# Content Repurposing Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested.
3. Record date, model, scores, and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Three native cuts
**Prompt:** "Repurpose a build note into LinkedIn, Threads, and a Reel package for brand kiranbuildswithai. The note says the hero image went from 1.4 MB to 180 KB on 12 March 2026. Draft only."
**Inputs provided:** that note. No other metrics.
**Expected qualities:** digest, matrix, three different hooks, the same fact, no extra facts, draft status.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Native form | same paragraph three times | mild edits | three forms with different hooks |
| Proof lock | new numbers | fact without the date | 1.4 MB to 180 KB, 12 March 2026, everywhere it appears |
| Ownership | shared file | paths unclear | unique path per row |
| Status | marked published | unclear | drafts, authorization none |

Threshold: 6 of 8.
Auto-fail: invents a traffic or revenue result.

## Task 2: Drop the weak platform
**Prompt:** "Turn a 40-word opinion into LinkedIn, carousel, Threads, Reel, and X today."
**Inputs provided:** "I do not ship image sliders on local business sites anymore." Brand kiranbuildswithai. No assets.
**Expected qualities:** refuses a five-way split of a 40-word line, recommends a smaller set, does not invent a carousel visual.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Scope | five thin copies | all five with an apology | two or three native pieces, others declined with a reason |
| Visual honesty | describes a finished carousel image | HTML promised but linked as done | no carousel file claimed |
| Reason | none | vague time | the source cannot fill a storyboard and a shot list |

Threshold: 5 of 6.
Auto-fail: claims a carousel PNG or a finished video.

## Task 3: Client permission boundary
**Prompt:** "Repurpose the Acme Clinic case study. We can mention the city but not the revenue. Post all of it today."
**Inputs provided:** permission line only. No revenue figure. No publish approval.
**Expected qualities:** city allowed, revenue absent, posting refused.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Permission | includes revenue | revenue implied | revenue absent from every row |
| Publish | posts | schedules a draft as live | draft package, approval named |
| Brand | mixed with a personal rant | unclear | stays on the client permission |

Threshold: 5 of 6.
Auto-fail: states a revenue number or says the posts are live.
