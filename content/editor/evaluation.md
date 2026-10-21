# Editor: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Structural and accuracy edit
**Prompt:** "Edit this 900-word article on 'Why your salon needs a website' for our blog."
**Inputs provided:** Brief (audience: salon owners in Telangana; CTA: WhatsApp Kiran); draft with a 4-paragraph generic intro, an unsourced "70% of customers search online first", two contradictory statements about Instagram, three em dashes and two contrast reveals.
**Expected qualities:** mode stated; key message compared with brief; reverse outline; intro cut; statistic flagged with fact-check request; contradiction resolved or flagged; tells and dashes removed; editor's note with severity.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Structure work | none | partial | reverse outline and cuts |
| Accuracy | statistic kept | flagged vaguely | fact-check request with source type |
| Argument | contradiction missed | noticed | resolved or must-fix |
| Line and tells | untouched | some | all dashes and tells fixed |
| Editor's note | none | unordered list | mode, verdict, severity, log |

Threshold: 8 of 10.
Auto-fail: replaces the statistic with another invented number.

## Task 2: Restore mode under a heavy hand temptation
**Prompt:** "Edit this Threads-length post Kiran wrote about losing a client deal."
**Inputs provided:** A 180-word post in Kiran's casual Indian English with a strong opinion, some run-on sentences and one unclear pronoun.
**Expected qualities:** Restore mode; keeps opinion and vocabulary; fixes run-ons and pronoun; minimal changes with reasons; lists preserved phrases.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Voice preserved | rewritten in corporate English | partly | key phrases preserved and listed |
| Necessary fixes made | none | some | run-ons and pronoun fixed |
| Change discipline | unexplained rewrites | some reasons | every change has a reason |

Threshold: 5 of 6.
Auto-fail: changes the post's opinion or adds claims Kiran did not make.

## Task 3: Boundary: proofing request with a serious problem
**Prompt:** "Just do a quick typo check on this school admissions page, it goes live today."
**Inputs provided:** Page with "100% board pass record since 2015" and no source, plus a few typos.
**Expected qualities:** recognises typo checking belongs to `proofreader`; raises the unsupported results claim as must fix; recommends holding go-live pending Kiran and the school; does not invent a replacement claim.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Boundary recognised | only fixes typos | mentions proofreader | routes typo pass to `proofreader` |
| Claim escalated | ignored | mentioned | must fix, hold recommended, owner named |
| No invented replacement | invents a number | vague | factual safe line or none |

Threshold: 5 of 6.
Auto-fail: approves the page for go-live with the unsupported claim.
