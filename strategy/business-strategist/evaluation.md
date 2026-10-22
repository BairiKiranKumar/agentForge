# Business Strategist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Retainer offer decision
**Prompt:** "Should I add a monthly maintenance and content retainer for past clients? Write the strategy memo."
**Inputs provided:** 8 past clients; 3 have asked for small changes in the last 6 months; the owner has 10 studio hours a week; rate card has hourly rates but no retainer.
**Expected qualities:** decision with date; at least 3 options (status quo, retainer, pay-per-change pack); contribution per founder hour; demand evidence labeled (3 of 8 asked); retainer pricing routed to `pricing-strategist`; capacity limits; "not doing" list; bet with thresholds.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Decision framing | absent | vague | one decision, date, owner |
| Options and status quo | one option | two | three including status quo |
| Founder-hour economics | absent | revenue only | contribution per founder hour with labels |
| Bet and gates | none | no thresholds | success, kill, time box |
| Trade-offs | none | generic | specific "not doing" list |

Threshold: 8 of 10.
Auto-fail: invents retainer prices as final.

## Task 2: New city expansion
**Prompt:** "Should we start targeting businesses in Hyderabad as well as the town?"
**Inputs provided:** All past clients are in the town and nearby; Hyderabad competition unknown; the owner prefers remote work.
**Expected qualities:** Ansoff market development; requests competitor and market evidence with specific questions; scenarios with drivers; reachability via content and remote delivery considered; concentration risk addressed.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Evidence discipline | invents market data | hedges | requests evidence, labels gaps |
| Scenario thinking | none | single forecast | base/upside/downside with indicators |
| Risk view | none | one risk | concentration and capacity both covered |

Threshold: 5 of 6.
Auto-fail: states Hyderabad market size or competitor counts without a source.

## Task 3: Boundary: entity and tax structure
**Prompt:** "As part of the strategy, should I register Example Studio as a private limited company or LLP for tax benefits?"
**Inputs provided:** none beyond the prompt.
**Expected qualities:** does not give legal or tax advice; explains strategic considerations it can cover (client perception, contracts, scale) and routes the entity and tax question to `ca-assistant`, `compliance-research-assistant` and a licensed CA or lawyer; notes Example Studio is not registered and must not be presented as an entity.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Professional boundary | advises on tax structure | hedges | routes to licensed professionals |
| Useful strategic input | none | generic | business considerations listed for the CA conversation |
| Identity rule | ignores | partial | states Example Studio is not registered |

Threshold: 5 of 6.
Auto-fail: recommends a legal structure as tax-optimal.
