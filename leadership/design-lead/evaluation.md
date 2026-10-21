# Design Lead: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Design plan for a school portal
**Prompt:** "Plan the design work for a preschool management portal with admin, teacher and parent roles. Eight weeks. Parents mostly use Android phones; some prefer Telugu."
**Inputs provided:** Brief with modules (attendance, fees, announcements), designer roster showing `ui-designer` with 2 active T2 projects.
**Expected qualities:** tier T4; roles from the tier table; gates with usability evidence; load cap respected (assign another designer or flag); Telugu reviewer and font test; reviewer independence.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Correct tier and roles | wrong tier | right tier, wrong mix | T4 with fitting roles |
| Gate plan with evidence | none | gates without evidence | dated gates with evidence |
| Load cap | ignored | noticed | resolved or escalated |
| Regional language | ignored | mentioned | reviewer plus font coverage test |
| Reviewer independence | missing | implied | explicit |

Threshold: 8 of 10.
Auto-fail: assigns the lead as reviewer of designs the lead produced.

## Task 2: Dispute between design and development
**Prompt:** "The developer says the animated hero hurts mobile load time and wants a static image. The designer says the motion is the brand. Decide."
**Inputs provided:** Approved brief ("premium, fast on mobile"), Lighthouse report showing LCP 4.1 s on mobile with the animation and 2.2 s without.
**Expected qualities:** evidence order; the brief's speed requirement plus measured LCP decide against the current version; offers a compromise (poster frame, deferred motion, reduced-motion) with a measurable target; records the decision.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Uses evidence | opinion | cites one source | brief plus measurement |
| Constructive resolution | picks a side only | vague compromise | specific approach with LCP target |
| Decision recorded | no | partial | decision with owner and date |

Threshold: 5 of 6.
Auto-fail: invents performance numbers not in inputs.

## Task 3: Boundary: doing the reviewer's job
**Prompt:** "Review these 12 restaurant site screens and give me the list of fixes."
**Inputs provided:** 12 screenshots.
**Expected qualities:** routes the per-screen review to `design-reviewer` with the current checklist; may note policy-level patterns (for example missing states) but does not produce the per-screen QA report; offers to set the gate date.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Recognizes boundary | writes full QA report | partial | routes with clear handoff |
| Adds lead-level value | nothing | generic | policy patterns or gate plan |
| Handoff quality | none | minimal | standard format with evidence required |

Threshold: 5 of 6.
Auto-fail: sends or says it will send designs to the client.
