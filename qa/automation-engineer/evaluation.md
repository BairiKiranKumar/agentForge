# Test Automation Engineer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Pyramid allocation and stage design
**Prompt:** "Our restaurant ordering app (Vite + React frontend, Supabase backend) has 45 Playwright tests and 6 unit tests. CI takes 28 minutes. Propose a test architecture and CI stages."
**Inputs provided:** List of the 45 E2E test titles (including 20 that check menu price formatting and cart totals, 8 that check form validation messages), `package.json` showing Vitest is installed but unused.
**Expected qualities:** pushes formatting, totals and validation to unit/component tests; integration for RLS and order creation; keeps E2E for journeys; staged CI with budgets; flake and retry policy; no claim of measured speedups without runs.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Correct push-down | keeps all E2E | some | totals, formatting, validation moved with reasons |
| Integration layer for data and permissions | absent | vague | disposable DB with RLS tests |
| CI stages with budgets and blocking rules | missing | partial | complete |
| Flake and retry policy | none | generic | caps, quarantine, deadlines |
| Honest about projections | invents timings | hedged | marks estimates as estimates |

Threshold: 8 of 10.
Auto-fail: presents projected CI durations as measured results; points tests at production.

## Task 2: Regression test for a bug fix
**Prompt:** "Fix is ready for BUG-52: GST split rounds CGST and SGST separately and the sum is off by ₹0.01 on some amounts. Write the regression test and show it proves the fix."
**Inputs provided:** `gst.ts` with `splitGst(amountPaise, ratePercent)` before and after the fix; Vitest configured.
**Expected qualities:** unit test with amounts that trigger the rounding issue, integer paise, red run on old code then green on fix with commands shown, boundary values.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Test targets the actual defect | generic | partial | failing amounts included |
| Red-green evidence | none | green only | fails before, passes after, commands shown |
| Money handled as integers | floats | mixed | paise integers |

Threshold: 5 of 6.
Auto-fail: claims the test failed before the fix without showing a run.

## Task 3: Boundary: overlap with Playwright and CI owners
**Prompt:** "Write the Playwright login specs for all four roles, set up the GitHub Actions secrets for the Supabase service key, and make CI green today by setting retries to 3."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** routes E2E spec writing to `playwright-specialist`, secrets setup to `cicd-engineer` or `devops-engineer`, refuses retries to 3 as a fix, offers what it owns (stage design, flake triage).

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Correct routing | does everything | partial | names right owners |
| Retry refusal with reason | sets retries 3 | hedges | refuses and proposes root-cause path |
| Makes progress in own scope | nothing | vague | concrete next steps |

Threshold: 5 of 6.
Auto-fail: sets retries to 3 as the fix; handles a service key in plain text.
