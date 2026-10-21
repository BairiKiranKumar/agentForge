# <Role Title>: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score the output against the rubric, ideally by a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: <core competence, realistic>
**Prompt:** <exact task given to the agent>
**Inputs provided:** <files or facts>
**Expected qualities:** <what a strong answer contains>

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| <criterion> | <missing or wrong> | <partial> | <complete and correct> |

Threshold: <x> of <max>.
Auto-fail: <e.g. invents a number, claims a credential, takes a consequential action without authorization>.

## Task 2: <harder realistic case>
...

## Task 3: <edge case, ambiguity or boundary test>
...
