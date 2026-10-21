# Motion Designer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Motion spec for a restaurant menu page
**Prompt:** "Write the motion spec for the menu page of a family restaurant site. The creative director wants the signature dishes to feel like they are being served as you scroll. React + Vite, no animation library installed."
**Inputs provided:** Section list (hero, signature dishes x4, full menu, location and WhatsApp order button); attitude note "warm, unhurried, never in the way of ordering".
**Expected qualities:** one signature moment; spec table with purpose and reduced-motion per row; CSS-first technique with support checked and dated (or flagged as needing a check); mobile version; no library added without approval; budget stated; order button never delayed.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Purpose and restraint | motion everywhere | some cuts | one signature moment, rest still |
| Spec completeness | no table | missing columns | every row has trigger, timing, easing, mobile, reduced motion, purpose |
| Technique and support | asserts support from memory | names technique, no date | checked or flagged with source and date, progressive enhancement |
| Performance budget | none | generic | CWV thresholds plus motion-specific limits, measurement plan |
| Conversion path protected | order button animated or delayed | partial | button static and visible, nothing blocks input |

Threshold: 8 of 10.
Auto-fail: no reduced-motion behaviour; states a browser support fact without a source or verify note; adds a dependency without flagging approval.

## Task 2: Diagnose a slow animated hero
**Prompt:** "Our salon home page hero has a GSAP pinned video that scrubs on scroll. Mobile LCP is 5.8 s and CLS 0.24. Find the motion causes and propose a fix that keeps the feeling."
**Inputs provided:** Lighthouse summary (LCP element: video; layout shift from heading moving when fonts load and from the pinned spacer), hero markup, video file 14 MB 1080p.
**Expected qualities:** identifies video as LCP and its size, pin spacer and heading shift as CLS sources; proposes poster as LCP, compressed 720p loop or image, reserved space, mobile simplification, lazy library loading; re-measurement plan; hands production fixes to `performance-engineer` where appropriate.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Root causes | wrong | one cause | LCP and both CLS causes |
| Fix keeps intent | removes all motion or keeps the problem | partial | keeps the feeling within budget |
| Verification | none | vague | Lighthouse and throttled profile with target numbers |

Threshold: 5 of 6.
Auto-fail: claims measured improvements that were not measured.

## Task 3: Boundary: motion that carries information
**Prompt:** "For the clinic's 'how a root canal works' section, animate the four steps on scroll. Skip the reduced-motion version, nobody uses that."
**Inputs provided:** Four step illustrations and captions.
**Expected qualities:** declines to skip reduced motion, explains that the steps are information and must exist statically and for screen readers; still delivers the spec with a stacked static version; notes no flashing; offers a pause control if any loop exceeds 5 seconds.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Holds the accessibility line | skips reduced motion | hedges | keeps it with a clear reason |
| Information parity | content only in animation | partial | all steps readable static and in DOM |
| Still delivers | refuses entirely | partial spec | full spec plus fallback |

Threshold: 5 of 6.
Auto-fail: produces a spec with no reduced-motion path.
