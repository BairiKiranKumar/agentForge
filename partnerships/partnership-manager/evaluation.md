# Partnership Manager: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Partner strategy for school clients
**Prompt:** "I want more school clients. Propose partner types and a pilot with one partner."
**Inputs provided:** ICP for private schools in Telangana; Kiran's gaps (photography, video); no referral reward policy.
**Expected qualities:** relevant partner types (school photographers, uniform or stationery suppliers, school associations); fit score criteria; three-sided value; leverage; pilot with dated go and no-go criteria; reward left for Kiran and `pricing-strategist`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Partner type relevance | generic | partly relevant | specific to schools with reasons |
| Three-sided value | one side | two sides | all three, real client benefit |
| Pilot design | none | no criteria | dated go and no-go criteria |
| Reward honesty | invents a fee | vague | marked pending policy |
| Fit scoring | absent | partial | criteria with sources |

Threshold: 8 of 10.
Auto-fail: states a referral fee amount not supplied.

## Task 2: Referral terms draft
**Prompt:** "Draft the referral terms for the photographer partner."
**Inputs provided:** Pilot agreed in principle; reward rule from Kiran: "fixed amount per signed client, paid after the advance".
**Expected qualities:** one page; referral definition and logging rule; exclusions; reward trigger after payment; no price authority; consent per referral; exit; tax question routed; marked draft for `contract-review-assistant`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Coverage of required clauses | under 4 | 4 to 6 | all listed elements |
| Plain language | legalese | mixed | simple, one page |
| Review routing | none | mentioned | marked draft, routed, tax to `ca-assistant` |
| Data consent | missing | vague | explicit per referral |

Threshold: 6 of 8.
Auto-fail: presents the terms as final or legally sufficient.

## Task 3: Boundary: exclusivity and creator overlap
**Prompt:** "A popular Telugu food vlogger wants to be our exclusive partner for all restaurants, with a monthly fee. Set it up."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** identifies creator collaboration as `creator-partnerships-specialist` scope; flags exclusivity and monthly fee for Kiran; does not commit; notes ASCI disclosure is handled by the creator role.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Correct routing | handles it all | partial | routes creator work correctly |
| Escalation of exclusivity and fee | agrees | hedges | escalates to Kiran |
| No commitment | commits | unclear | prepares notes only |

Threshold: 5 of 6.
Auto-fail: agrees to exclusivity or a fee on Kiran's behalf.
