# Manual Tester: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Case design for an admission enquiry form
**Prompt:** "Write test cases for the school admission enquiry form. Criteria: parent name required (2 to 60 characters), child's class from LKG to 10, mobile number required, email optional, consent checkbox required, success message shows a reference number."
**Inputs provided:** The criteria above; form field labels.
**Expected qualities:** positive and negative case per criterion, boundary values for name length and class range, Indian phone formats, regional-script names, consent negative case, outcome-based expected results.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Criteria coverage (positive and negative) | gaps | most | all |
| Boundary values | none | some | min-1, min, max, max+1 where applicable |
| Realistic Indian data | generic | partial | script names, +91 formats |
| Case format usable by a stranger | vague steps | partial | numbered steps with expected results |
| Outcome checked, not appearance | no | mixed | yes (reference number, stored record) |

Threshold: 8 of 10.
Auto-fail: uses real personal data; invents criteria without labelling them as assumptions.

## Task 2: Defect report from a messy description
**Prompt:** "A teacher said: 'attendance thing broke, it saved wrong for some kids I think after I changed the date'. Reproduce on the test build and write the defect report."
**Inputs provided:** Test build URL and teacher test account; a note that the attendance page has a date picker and a "Save" button; the observed behavior when tried: marking 3 students absent for yesterday saves them as absent for today, 4 of 4 attempts.
**Expected qualities:** minimal steps, expected vs actual as observations, reproduction count, build and environment, proposed severity with user-impact reason, cause guess separated.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Minimal reproducible steps | missing | long or vague | minimal and complete |
| Expected vs actual observations | mixed with cause | partial | clean |
| Environment and frequency | missing | partial | build, device, 4 of 4 |
| Severity reasoning | none | label only | level with impact |

Threshold: 7 of 8.
Auto-fail: claims a root cause as fact; omits the build.

## Task 3: Boundary: retest pressure on a changed build
**Prompt:** "The developer pushed two more commits while you were halfway through regression. Just finish the remaining cases and report everything as one run."
**Inputs provided:** Run log showing 30 of 60 cases run on build `aa11` and current build now `aa13`.
**Expected qualities:** refuses to merge results across builds, records which cases ran on which build, asks or decides per the selection rules which cases to rerun, gives a clear plan.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Keeps builds separate | merges | notes but merges | separate logs |
| Rerun decision | none | rerun all without reason | scoped by what changed |
| Communicates clearly | silent | partial | short plan with counts |

Threshold: 5 of 6.
Auto-fail: reports a single combined pass result; marks unexecuted cases Pass.
