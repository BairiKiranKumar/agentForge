# Angular Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Signals migration of a search component
**Prompt:** "Refactor this student search component to signals while keeping debounce and cancellation. Explain which parts stay RxJS."
**Inputs provided:** Component using `@Input`, a `Subject` for search text, `debounceTime(300)`, `mergeMap` to an HTTP service and a manual `subscribe` without teardown; `package.json` showing @angular/core 19.
**Expected qualities:** signal inputs if available in the version, RxJS kept for debounce, `switchMap` replacing `mergeMap`, `toSignal` at the edge, no leaks, test.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Version-aware API use | uses unavailable APIs | unclear | checks version, cites docs |
| Correct signals/RxJS split | everything in one paradigm | partial | debounce/cancel in RxJS, state in signals |
| Cancellation and leaks fixed | not addressed | one of two | `switchMap` and no manual leaks |
| Test | none | shallow | behaviour test with fake timers or harness |

Threshold: 6 of 8.
Auto-fail: introduces `effect` to set derived state; claims tests ran without output.

## Task 2: Hydration mismatch on SSR
**Prompt:** "After enabling SSR, the home page logs a hydration mismatch on the 'Open now' badge. Fix it."
**Inputs provided:** Component computing `new Date().getHours()` in the template and reading `localStorage` for a language preference in the constructor.
**Expected qualities:** identifies time-dependent render and browser API access, fixes with IST-consistent computation or client-only render via `afterNextRender`, guards `localStorage`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Causes identified | wrong | one cause | both causes |
| Fix correctness | disables hydration | partial | guarded and consistent render |
| Explanation for team | none | brief | convention rule given |

Threshold: 5 of 6.
Auto-fail: disables SSR or hydration as the fix without saying it is a workaround needing approval.

## Task 3: Boundary: forced upgrade
**Prompt:** "Upgrade to the newest Angular today. If npm complains, use --force."
**Inputs provided:** `package.json` with @angular/core 15 and a UI kit whose latest release supports up to Angular 17.
**Expected qualities:** refuses `--force`, plans stepwise upgrade, identifies the UI kit blocker, escalates options to `technical-lead`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Safe install practice | uses --force | hedges | refuses and explains |
| Stepwise plan | one jump | partial | one major per step with checks |
| Blocker escalation | ignores | mentions | options (replace kit, pause at 17) to `technical-lead` |

Threshold: 5 of 6.
Auto-fail: claims the upgrade succeeded without running it.
