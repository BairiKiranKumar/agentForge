# UX Designer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: School fee payment flow
**Prompt:** "Design the parent fee payment flow for our school app. Parents get a WhatsApp reminder link. Payment is by UPI through a gateway."
**Inputs provided:** Roles (parent, accountant), rule: fees are per term, instalments allowed for some students (flag on student record), receipts must be downloadable.
**Expected qualities:** job story, flow with all branches, success/failure/pending payment paths, instalment branch, friction counts, edge cases (expired link, wrong child, network loss, app switch), mobile wireframes with one primary action, open rules listed.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Flow completeness | happy path only | some branches | all branches and exits |
| Payment outcomes | success only | success and failure | success, failure and pending with no "pay again" on pending |
| Edge cases | none | a few | checklist applied with paths |
| Friction discipline | not counted | counted | counted and within targets or justified |
| Wireframes | none or desktop | partial | 375 px, realistic content, one primary action |

Threshold: 8 of 10.
Auto-fail: designs a pending payment state that tells the parent to pay again.

## Task 2: Multi-role attendance with offline risk
**Prompt:** "Teachers mark attendance on their phones at 8:30 am. School Wi-Fi is unreliable. Admin wants to see absentees by 9 am and message parents."
**Inputs provided:** Roles (teacher, admin), class sizes up to 45, rule: only the class teacher can edit attendance for their class until 10 am.
**Expected qualities:** offline-tolerant flow (local save, sync status), bulk "all present then mark absent" pattern, conflict rule, admin flow with WhatsApp handoff that respects approval, edit window enforcement, states listed for `interaction-designer`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Offline handling | ignored | mentioned | flow with save, sync and conflict paths |
| Efficiency for 45 students | one-by-one | some shortcut | default-present pattern with counts |
| Role rules | ignored | partial | edit window and role access enforced in flow |
| Handoffs | none | generic | states for interaction design, text slots for UX writing |

Threshold: 6 of 8.
Auto-fail: designs automatic messages to parents without any human approval step or opt-in consideration.

## Task 3: Boundary: visual polish and navigation requested together
**Prompt:** "Also pick the colours, final fonts and the top menu for the whole site while you're at it."
**Inputs provided:** the Task 1 output.
**Expected qualities:** keeps flows and wireframes in scope; routes visual design to `ui-designer` and site navigation to `information-architect`; lists what each needs from the flows.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Recognises boundaries | does all | partial | routes both correctly |
| Handoff usefulness | none | vague | specific inputs for each receiver |
| Stays productive | stops | partial | completes own scope |

Threshold: 5 of 6.
Auto-fail: invents business rules or client approvals to close open questions.
