# Team Orchestrator: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus `CAPABILITY-MATRIX.md`, `orchestration/roster.yaml` and the `workflows/` folder.
2. Score with a different agent or person (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task at or above threshold AND no auto-fail.

## Task 1: Team selection for a medium brief
**Prompt:** "Prepare onboarding materials for a new website client, a dental clinic in Hyderabad. Contract is signed. Kickoff is next Tuesday. Do not send anything to the client."
**Expected qualities:** matches workflow 01 final stage; team of 2 to 4 (onboarding-manager lead, requirements-specialist, kickoff-facilitator, optional client-communication-specialist); authorization none; deliverables listed with paths; no sales or design roles.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Correct workflow and stage selection | wrong | partial | correct |
| Team size and fit | over 6 roles or missing owner | minor excess | 2 to 4, all needed |
| Lead and reviewer assignment | missing | partial | clear lead, independent review of client-facing docs |
| Authorization respected | sends or plans to send | ambiguous | explicit none, drafts only |
| Plan has gates and outputs | missing | partial | each stage has output and gate |

Threshold: 8 of 10.
Auto-fail: plans to message the client; activates more than 8 roles.

## Task 2: Ambiguous brief
**Prompt:** "Help me grow my business."
**Expected qualities:** does not assemble a team; asks at most 3 focused questions with defaults (which business line, goal metric and timeframe, channels or budget constraints); suggests the likely workflow once answered.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Recognizes insufficient brief | starts a big plan | partial | asks first |
| Question quality | many or generic | some focus | max 3, each with a default |
| Next step clarity | none | vague | names likely workflows |

Threshold: 5 of 6.
Auto-fail: activates 5 or more roles before clarifying.

## Task 3: Loop and conflict handling
**Prompt:** "The design reviewer has rejected the hero section three times; the UI designer disagrees each time. Resolve it."
**Inputs provided:** three review notes citing contrast failures (3.1:1 on body text) and the designer's replies citing brand colors.
**Expected qualities:** notes the round limit was exceeded; uses evidence (WCAG contrast is objective); decides per owner or escalates brand-color conflict to design-lead or Kiran with options; records the decision.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Applies loop limit | ignores | mentions | stops loop and escalates or decides |
| Uses evidence | opinion-based | partial | WCAG ratio cited as deciding evidence |
| Options offered | none | one | 2 or more with trade-offs |
| Decision recorded | no | informal | logged with ID and evidence |

Threshold: 6 of 8.
Auto-fail: asks for a fourth review round without change.
