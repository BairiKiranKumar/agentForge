# Interaction Designer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Booking form behaviour spec
**Prompt:** "Specify the interaction behaviour for this salon booking form: slot picker, name, phone with OTP, and Confirm."
**Inputs provided:** Wireframes, API notes (slot hold lasts 5 minutes, OTP valid 2 minutes, confirm returns in 1 to 3 s, slot can be taken by someone else meanwhile).
**Expected qualities:** state machines for slot picker, OTP and confirm; validation timing; loading per wait band; slot-taken conflict path; hold expiry warning before it ends; focus rules; reduced-motion variants; text slots for `ux-writer`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| State machines without dead ends | missing | partial | complete for all three |
| Validation timing | absent | partial | blur, re-validate, focus first error |
| Time-bound states (hold, OTP) | ignored | one handled | both with warning and recovery |
| Conflict path | none | mentioned | slot-taken flow with alternatives kept |
| Transitions with reduced motion | none | timings only | timings, easing and reduced-motion variants |

Threshold: 8 of 10.
Auto-fail: clears entered data on error; no pending or conflict handling for the confirm action.

## Task 2: Offline attendance sync
**Prompt:** "Teachers mark attendance offline; sync later. Admin sees absentees live. Specify the behaviour."
**Inputs provided:** Supabase realtime available, edit window until 10 am, one class teacher per class, network drops common.
**Expected qualities:** local queue with pending indicator, idempotent sync, conflict rule after 10 am, admin view shows "not yet synced" distinct from "absent", announcements, no optimistic message to parents.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Offline queue and status | absent | partial | queue, banner, per-class status |
| Data integrity | duplicates possible | partial | idempotent sync and conflict rule |
| Admin view truthfulness | treats unsynced as absent | vague | distinct states with timestamps |
| Downstream messages | auto-sent | unclear | only after confirmed sync and human approval |

Threshold: 6 of 8.
Auto-fail: specifies automatic parent messages from unsynced or optimistic data.

## Task 3: Boundary: scroll storytelling and copy
**Prompt:** "Also design the homepage scroll animation sequence and write all the error messages."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** routes scroll storytelling to `motion-designer` and wording to `ux-writer`; delivers text slots with length and job; offers UI transition specs that stay in scope.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Motion boundary | designs full sequence | partial | routes to `motion-designer` |
| Copy boundary | writes final copy as owner | partial | slots with limits to `ux-writer` |
| Progress in scope | none | partial | UI transition specs delivered |

Threshold: 5 of 6.
Auto-fail: invents API timings or backend capabilities not provided.
