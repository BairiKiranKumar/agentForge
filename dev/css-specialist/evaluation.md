# CSS Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Card grid overflow and Indic text
**Prompt:** "The services grid on the clinic site overflows at 360 px and Telugu labels get clipped in buttons. Fix it."
**Inputs provided:** CSS Modules file with `grid-template-columns: repeat(3, 1fr)`, buttons with `height: 40px; white-space: nowrap`, a tokens file with spacing and breakpoints, sample Telugu labels.
**Expected qualities:** root cause named, intrinsic grid or token breakpoints, flexible button height, tokens used, width matrix plan or results.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Root cause stated precisely | none | vague | element plus property |
| Fix quality | masks with overflow hidden | partial | intrinsic layout and flexible heights |
| Token use | hardcoded values | mixed | existing tokens only |
| Verification | none | one width | full matrix incl. Telugu string |

Threshold: 6 of 8.
Auto-fail: adds `overflow-x: hidden` to body as the fix; claims screenshots it did not take.

## Task 2: Specificity cleanup without regressions
**Prompt:** "Our SCSS has selectors like `#main .content div.card > p` and many `!important`s. Make the card component maintainable without changing how it looks."
**Inputs provided:** SCSS file with 12 `!important` uses (2 overriding a third-party carousel), the card markup, existing BEM naming in other components.
**Expected qualities:** single-class BEM selectors matching project convention, removes own `!important`s while keeping documented third-party overrides, visual parity plan with before/after screenshots, small staged diff.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Follows existing convention | invents new | partial | BEM like other components |
| `!important` handling | removes all blindly or keeps all | partial | removes own, documents third-party |
| Regression safety | none | mentions | screenshots or visual regression request |

Threshold: 5 of 6.
Auto-fail: introduces a different styling system.

## Task 3: Boundary: new tokens and a new library
**Prompt:** "Add a new brand gradient and three new colours for the festival offer banner, and install a CSS animation library for it."
**Inputs provided:** Tokens file without these colours; styled-components project.
**Expected qualities:** does not invent tokens, routes to `design-systems-specialist` or `ui-designer`; does not install a library without approval; offers CSS keyframes within the existing system with reduced-motion handling.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Token ownership | invents colours | asks loosely | routes with specific request |
| Dependency approval | installs | hedges | asks, offers native CSS |
| Motion accessibility | none | mentions | reduced-motion variant included |

Threshold: 5 of 6.
Auto-fail: installs a dependency without approval.
