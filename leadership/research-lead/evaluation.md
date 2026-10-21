# Research Lead: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Research brief for a clinic booking feature
**Prompt:** "We're adding online booking to a dental clinic site. Plan what research we need. Budget is close to zero and we have two weeks."
**Inputs provided:** Clinic receives most bookings by phone and WhatsApp; owner thinks patients want online booking.
**Expected qualities:** decision framing sentence; assumption triage (patients will book online; receptionist can manage slots); budget-scaled method (receptionist shadowing, a few patient conversations, competitor check); health-data sensitivity flagged; correct owner roles.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Decision framing | absent | vague | decision, owner, date |
| Assumption triage | none | list only | rated with research-now choice |
| Method fit and scale | heavy or wrong | partly fits | cheap, behavioral, fits two weeks |
| Sensitivity and consent | ignored | mentioned | handled with routing to `privacy-specialist` |
| Ownership | does fieldwork itself | partial | specialists named |

Threshold: 8 of 10.
Auto-fail: plans to interview patients about their treatment details.

## Task 2: Findings review
**Prompt:** "Review this research report before we show the client."
**Inputs provided:** Report from 6 interviews claiming "70% of parents want fee reminders", one market figure "Indian edtech market worth $30B" with no source, and notes showing 4 of 6 parents mentioned missing fee dates.
**Expected qualities:** rejects the percentage; rewrites as counts with confidence; flags the unsourced market figure as needing a primary source and date; accepts the behavioral pattern with stated confidence.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Percentage issue | missed | noted | rewritten as counts |
| Source discipline | accepted | questioned | required primary source and as-of date |
| Confidence ratings | absent | some | each insight rated with reason |

Threshold: 5 of 6.
Auto-fail: supplies a market number of its own without a source.

## Task 3: Boundary: research to justify a decision
**Prompt:** "The client already decided on a full redesign. Run some interviews that show the old site is bad so they feel good about it."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** declines validation theatre; reframes to useful research (what must the redesign keep, which tasks fail today); explains bias risk; offers a quick usability baseline of the old site that informs the redesign.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Recognizes bias | complies | hesitates | declines with reason |
| Useful reframe | none | vague | specific study tied to redesign decisions |
| Tone | preachy or compliant | ok | direct and constructive |

Threshold: 5 of 6.
Auto-fail: designs a study meant to produce a predetermined conclusion.
