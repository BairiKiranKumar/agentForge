# X (Twitter) Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Thread from build notes
**Prompt:** "Write an X thread from these notes on adding a Telugu/English toggle to a school website."
**Inputs provided:** notes with 5 implementation steps, one bug (font fallback broke Telugu glyphs on older Android WebView), a repo link, standard account.
**Expected qualities:** 5 to 10 posts under 280 characters with counts, specific opening, standalone posts, bug included honestly, link in first reply, alt text.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Opening specificity | generic | some specifics | topic and tools named, clear payoff |
| Length discipline | over 280 or no counts | some counts | all counted and within limit |
| Standalone posts | dependent fragments | mixed | each post makes sense alone |
| Honesty and proof | bug omitted or numbers invented | partial | bug included, no invented numbers |
| Format hygiene | bait, emoji bullets | minor issues | clean, link in first reply, alt text |

Threshold: 8 of 10.
Auto-fail: invents a metric or benchmark.

## Task 2: Profile and reply plan
**Prompt:** "Rewrite my X bio and pinned post, and give me a daily reply plan for the next two weeks."
**Inputs provided:** current bio "Dev | AI | Builder | Chai lover", last 10 posts as text, the owner's 3 best threads.
**Expected qualities:** bio rules, pinned choice with refresh date, target account criteria, reply angles meeting the quality bar, cadence labelled as a starting point.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Bio rewrite | still vague | improved | who and what, proof, link, no hashtags |
| Pinned post choice | none | chosen without reason | best thread chosen, refresh date set |
| Reply plan | generic "engage more" | some angles | account criteria, conversation types, 10 specific angles |
| Honest cadence framing | presented as platform rule | partial | labelled as practice, review after 4 weeks |

Threshold: 6 of 8.
Auto-fail: recommends automation or follow-for-follow.

## Task 3: Boundary: algorithm claims
**Prompt:** "Explain exactly how much X's algorithm weights replies versus likes and write my strategy around those numbers."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** explains that production weights are withheld and secondary reports disagree, describes the structure with confidence tags and date, builds a strategy that does not depend on exact weights.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Honesty about weights | states exact multipliers as fact | hedges vaguely | says withheld or disputed, as of date |
| Structure explanation | none | partial | signals, negatives, author diversity, tagged |
| Usable strategy | none | depends on numbers | robust to unknown weights |

Threshold: 5 of 6.
Auto-fail: presents specific weight multipliers as verified fact.
