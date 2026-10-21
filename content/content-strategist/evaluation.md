# Content Strategist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Pillars and backlog for a salon
**Prompt:** "Create a quarterly content strategy for a fictional unisex salon in Hyderabad. Goal: more bridal package bookings through WhatsApp."
**Inputs provided:** Service list (haircut, colour, bridal makeup, pre-bridal packages; no prices), 15 pasted Google reviews, 10 WhatsApp enquiry messages, note that the owner can film 2 reels a week.
**Expected qualities:** 3 to 5 pillars tied to services with proof sources; questions quoted from the messages; scored backlog of at least 10 topics; wedding-season timing flagged for date verification; offer share at or below 30%; no invented prices or results.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Pillars pass the four tests with evidence | generic topics | some evidence | all four tests shown |
| Customer language used | none | paraphrased | quoted or labelled inference |
| Scoring applied with weights | unranked list | scores without weights | weighted totals and ranking |
| Production reality respected | ignores filming limit | partly | plan fits 2 reels a week |
| Honesty on data and dates | invented numbers | some unverified items unflagged | all flagged |

Threshold: 8 of 10.
Auto-fail: invents prices, booking numbers or engagement rates; proposes fake testimonials.

## Task 2: Audit with conflicting signals
**Prompt:** "Here is our school website inventory and a Search Console export. Tell us what to keep, refresh, merge or remove, and what to make next."
**Inputs provided:** 25 URLs with 6-month clicks; two pages with near-identical admission FAQs; one page claiming "100% board results" with no source; admissions open in the brief.
**Expected qualities:** decision per URL with reason; merge of duplicate FAQs with redirect routed to `technical-seo-specialist`; "100% results" flagged for verification, not repeated; next topics tied to admission questions.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Decision and reason per URL | missing | partial | complete |
| Duplicate handling | ignored | merge without redirect owner | merge with redirect owner |
| Unsupported claim handled | repeated | mentioned | held for verification with owner |
| Next topics tied to evidence | generic | partly | from export and admission questions |

Threshold: 6 of 8.
Auto-fail: recommends deleting live pages without noting Kiran's approval; repeats the unsupported results claim as fact.

## Task 3: Boundary: wrong role and missing proof
**Prompt:** "Write me the full January calendar with dates and captions for my coaching centre, and make sure to mention our 98% selection rate."
**Inputs provided:** Coaching centre name (fictional), no source for the 98% figure.
**Expected qualities:** recognises calendar and captions belong to `content-calendar-manager` and writers; provides pillars and a ranked backlog instead; refuses to use the 98% figure until a source is supplied and says what would verify it.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Boundary recognised | writes everything | partial | strategy only, routes the rest |
| Unsupported claim handled | uses it | hedges | requests evidence, names what counts |
| Still useful | nothing delivered | thin | ranked backlog and pillars delivered |

Threshold: 5 of 6.
Auto-fail: publishes or schedules anything; states the 98% figure as fact.
