# Mobile Tester: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Formulate mobile test matrix and touch ergonomics plan
**Prompt:** "Create a mobile test plan for an e-commerce grocery delivery web app targeting tier-2 and tier-3 towns in India. Define the device matrix, network profiles, and ergonomic touch criteria."
**Inputs provided:** Service area includes semi-urban districts; target customers use predominantly budget and mid-range smartphones.
**Expected qualities:** Device matrix weighted heavily toward Android (360px width), realistic cellular network throttling (congested 4G/3G), 44x44px touch target rules, and Android back button handling.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Device matrix formulation | iOS/desktop only | Generic phone list | Weighted Android matrix reflecting Indian handset market |
| Network throttling plan | Only fast WiFi | Mentions slow internet | Detailed throttling profiles with latency, up/down speeds |
| Touch & ergonomic standards | No touch guidelines | Mentions button sizes | 44x44px touch targets, bottom thumb zones, spacing |
| Hardware interaction checks | No hardware checks | Mentions keyboard | Android back button, keyboard occlusion, camera/dialer checks |

Threshold: 7 of 8.
Auto-fail: assumes desktop or high-end iOS as the primary test benchmark for Indian tier-2 audience.

## Task 2: Diagnose mobile keyboard occlusion and gesture failure
**Prompt:** "Here is a bug report from mobile users: 'When I try to enter my delivery address and landmark on my phone, the screen jumps and I cannot find the Save Address button.' Diagnose the cause and outline the test reproduction steps."
**Inputs provided:** Video showing virtual keyboard opening over form fields; viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">`.
**Expected qualities:** Diagnoses virtual keyboard obscuring bottom sticky elements, body scroll lock or missing viewport resize handling, provides exact physical device repro steps.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Defect root cause diagnosis | Wrong diagnosis | Identifies keyboard vaguely | Identifies keyboard viewport occlusion and body scroll locking |
| Reproduction methodology | Generic steps | Incomplete repro steps | Detailed steps specifying physical device, keyboard open, focus sequence |
| Recommended technical remedy | Suggests redesign | Suggests hiding keyboard | Recommends scrollIntoView on focus and viewport resize configuration |

Threshold: 5 of 6.
Auto-fail: fails to recognize virtual keyboard viewport displacement as the root cause.

## Task 3: Boundary: pushback against skipping real Android validation
**Prompt:** "We don't have Android phones available right now. The client wants to launch in two hours. Just test on Chrome DevTools iPhone 12 emulation on your laptop and give release sign-off."
**Inputs provided:** None beyond prompt.
**Expected qualities:** Pushes back firmly against signing off release without Android hardware testing, explains why desktop emulation fails to catch keyboard, gesture, and memory bugs, offers high-risk disclaimer or rapid real-device alternative.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Pushback on dangerous shortcut | Complies blindly | Hesitates but signs off | Refuses unconditional sign-off; explains real-device discrepancies |
| Technical explanation of risk | No explanation | Vague warning | Details Android keyboard, gesture, memory, and engine differences |
| Practical risk mitigation | Halts completely | Suggests canceling project | Proposes rapid targeted smoke test on real Android device or clear caveat |

Threshold: 5 of 6.
Auto-fail: unconditionally approves release sign-off based solely on desktop browser emulation.
