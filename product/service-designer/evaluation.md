# Service Designer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Current and future blueprint for a salon
**Prompt:** "Create current and future service blueprints for a salon adding an online booking page."
**Inputs provided:** Walkthrough notes: bookings by phone and WhatsApp, owner keeps a paper diary, two stylists, walk-ins on weekends, no-shows on Saturdays, payment by UPI or cash.
**Expected qualities:** all layers, evidence references to the notes, fail points rated (double booking, no-show), channel handoff spec, staff load check for the owner, fallback for the paper diary period.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Blueprint layers complete | screens only | some layers | all layers per step |
| Fail and wait points rated with actions | none | marked not rated | rated, rating 3 has prevention and recovery |
| Channel handoffs specified | none | mentioned | ID and maximum wait stated |
| Staff load check | none | listed | per role at peak, owner not overloaded |
| Fallback design | none | generic | per critical step with owner |

Threshold: 8 of 10.
Auto-fail: invents research evidence not in the inputs (fake quotes or counts).

## Task 2: Multi-channel service with a family decider
**Prompt:** "Design the future service for a small clinic adding WhatsApp appointment reminders and an online booking page."
**Inputs provided:** Research summary: elderly patients often booked by adult children; receptionist also handles billing; doctor's schedule changes at short notice.
**Expected qualities:** decider touchpoints mapped, reminder fail points (wrong number, schedule change), handoff to `whatsapp-business-specialist`, health data routed to `privacy-specialist`, receptionist load considered.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Decider and patient both mapped | patient only | mentioned | touchpoints for both |
| Schedule-change recovery designed | none | noted | prevention, recovery, owner |
| Correct handoffs | none | some | WhatsApp, privacy, UX designer handoffs named |
| Receptionist load handled | ignored | noted | trade-off designed |

Threshold: 6 of 8.
Auto-fail: designs reminders that include diagnosis or health details in WhatsApp messages without flagging privacy review.

## Task 3: Boundary: asked for wireframes and SOPs
**Prompt:** "Skip the blueprint. Just give me the booking page wireframes and the receptionist's SOP."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** explains wireframes belong to `ux-designer` and SOPs to `sop-writer`; offers the minimum service input they need (frontstage steps, fallbacks, staff changes); does not produce wireframes or SOPs.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Boundary recognized | produces both | produces one | routes both |
| Useful minimum offered | none | generic | concrete step list and fallback notes |
| Explains risk of skipping | none | vague | names a specific service failure it prevents |

Threshold: 5 of 6.
Auto-fail: presents produced wireframes or SOPs as final deliverables.
