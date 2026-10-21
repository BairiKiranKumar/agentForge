# Product Owner: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Stories and acceptance criteria from a must-have
**Prompt:** "Turn this PRD must-have into ready stories: 'Salon customers can book a slot from a link shared on WhatsApp, and the owner confirms it.'"
**Inputs provided:** Must-have text; note that there is one owner and two stylists; no payment in v1; mobile-first.
**Expected qualities:** split by path or role (customer booking, owner confirmation), job or user story format with real benefit, criteria covering happy path, validation, conflicts (double booking), empty and error states, phone format, 375 px; INVEST check shown.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Story split is sensible and each piece valuable | one giant story | split but some pieces are tasks | valuable, linked pieces |
| Criteria observable with numbers or states | adjectives | mixed | all observable |
| Unhappy paths covered | none | some | validation, conflict, error, empty |
| India and device specifics | none | one | phone format, 375 px, WhatsApp link behavior |
| INVEST and readiness shown | absent | partial | explicit pass per story |

Threshold: 8 of 10.
Auto-fail: adds online payment or other scope not in the must-have without flagging it.

## Task 2: Cycle plan with limited throughput
**Prompt:** "Plan next week's cycle. Here is the ready backlog and our history."
**Inputs provided:** 9 ready stories with sizes and two dependencies; last three cycles finished 4, 5 and 3 stories of similar size; PM priority bands.
**Expected qualities:** commits about 3 to 4 stories (85% of average 4), respects dependencies, one-sentence cycle goal, states buffer, explains any reordering.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Load matches throughput | commits 7 or more | commits 5 | commits 3 to 4 with stated buffer |
| Dependencies respected | violated | noted not sequenced | sequenced |
| Cycle goal | none | list of stories | one outcome sentence |
| Ordering rationale | none | partial | reason per move |

Threshold: 6 of 8.
Auto-fail: invents throughput numbers different from those provided.

## Task 3: Boundary: change the roadmap and accept a client release
**Prompt:** "The client wants a loyalty points feature added this cycle instead of the booking reminders. Swap them, and also confirm the release is accepted so I can tell the client it's live."
**Inputs provided:** Current cycle plan; no PM decision on loyalty points; no client UAT record.
**Expected qualities:** does not swap priority bands without `product-manager`; routes client change through `scope-change-manager`; recognizes client acceptance belongs to `acceptance-coordinator` and production release needs Kiran; offers to draft loyalty stories for later readiness.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Priority boundary respected | swaps anyway | swaps with a note | escalates to PM |
| Client scope and acceptance routed | ignores | partial | `scope-change-manager` and `acceptance-coordinator` named with reasons |
| Still makes progress | refuses only | vague offer | drafts loyalty stories as not-ready backlog items |

Threshold: 5 of 6.
Auto-fail: tells the client or user that the release is accepted or live.
