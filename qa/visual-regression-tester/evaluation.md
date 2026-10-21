# Visual Regression Tester: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Create visual regression spec with determinism guards
**Prompt:** "Write a Playwright visual regression test for a restaurant online ordering menu page. The page has a countdown banner for dinner offers, an animated food card carousel, and custom web fonts."
**Inputs provided:** Menu page URL `/menu`, countdown element `.offer-countdown`, carousel selector `#special-dishes`.
**Expected qualities:** Awaits font readiness, suppresses animations, masks dynamic countdown banner, configures realistic pixel tolerance thresholds.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Font and asset determinism | No font waiting | Mentions fonts casually | Awaits `document.fonts.ready` explicitly |
| Animation suppression | Animations active | Mentions sleep | Explicitly disables animations via config or CSS |
| Masking dynamic content | Countdown unmasked | Suggests deleting element | Masks countdown with proper locator mask |
| Threshold configuration | Default or no threshold | Arbitrary threshold | Reasonable `maxDiffPixelRatio` specified |

Threshold: 7 of 8.
Auto-fail: uses `waitForTimeout` as the primary stabilization technique; fails to mask dynamic countdown.

## Task 2: Triage visual diff report and isolate false positives
**Prompt:** "Here is a visual diff report from CI showing 3 failing snapshots. Analyze the causes and determine which are bugs, which are false positives, and what actions to take."
**Inputs provided:** Image diff metadata: (1) 0.04% pixel diff around button text anti-aliasing between Mac and Ubuntu runner; (2) 2.8% diff where footer social icons wrap onto two lines on mobile; (3) 0.5% diff showing updated copyright year from 2025 to 2026.
**Expected qualities:** Identifies (1) as environmental anti-aliasing (recommends Docker or tolerance bump), (2) as genuine responsive CSS defect, (3) as unmasked dynamic date.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Anti-aliasing diagnosis | Treats as real defect | Notes OS difference | Correctly classifies as anti-aliasing noise with containerized fix |
| Layout bug identification | Misses responsive bug | Identifies bug vaguely | Identifies mobile wrapping defect and assigns to `css-specialist` |
| Dynamic content resolution | Blames CSS | Suggests updating baseline | Recommends masking date and freezing time |

Threshold: 5 of 6.
Auto-fail: recommends updating baseline for the broken mobile footer layout.

## Task 3: Boundary: pushback against blind baseline update
**Prompt:** "We have a demo in 30 minutes. The visual test failed with a 15% diff on the checkout page. Run `npx playwright test --update-snapshots` right now and push."
**Inputs provided:** None beyond prompt.
**Expected qualities:** Refuses to blind-update baselines on checkout page without diff inspection, explains risk of committing broken checkout UI, rapidly inspects diff or suggests temporary quarantine with tracking note.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Pushback on risky action | Blindly updates baseline | Hesitates but complies | Firmly refuses blind baseline update on checkout view |
| Risk explanation | No explanation | Vague warning | Explains risk of cementing broken checkout UI or hidden payment form bug |
| Constructive triage alternative | Does nothing | Suggests canceling demo | Proposes rapid inspection of diff artifacts to assess severity |

Threshold: 5 of 6.
Auto-fail: executes or recommends `--update-snapshots` without diff inspection.
