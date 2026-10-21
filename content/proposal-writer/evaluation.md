# Proposal Writer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Narrative from discovery notes
**Prompt:** "Write the proposal narrative for this fictional restaurant's QR ordering web app."
**Inputs provided:** Discovery notes with 5 owner quotes (waiters forget orders on busy weekends, menu changes daily, owner wants to see the day's orders on his phone), scope v1 (QR menu, table ordering, kitchen screen, owner dashboard; excludes online payment), one permissioned live link.
**Expected qualities:** discovery map; 2 or 3 client-specific win themes; exec summary 120 to 200 words with next step; client words mirrored; no online payment mentioned; no prices or dates; trace table; cover message draft.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Client language mirrored | generic | some | quotes with sources |
| Win themes | generic | specific but unprovable | specific, provable, in scope |
| Scope consistency | excluded feature promised | ambiguous | fully consistent |
| Exec summary | missing or long | structure partial | structure and length met |
| Trace and separation | prices or dates present | no trace table | trace table, no prices or dates |

Threshold: 8 of 10.
Auto-fail: promises online payment or another excluded item; invents a cost-of-problem figure.

## Task 2: Thin discovery notes
**Prompt:** "Write the 'What you asked for' section for a fashion boutique's ecommerce site."
**Inputs provided:** Two-line discovery note: "Wants online store. Has Instagram with 8k followers."
**Expected qualities:** recognises notes are too thin; lists the specific gaps (products, payments, delivery, goals, constraints); drafts a skeleton with `[NEED]` markers; suggests a short follow-up call question list.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Gap recognised | invents needs | partial | clearly stated |
| Gap list quality | none | generic | specific to ecommerce decisions |
| Useful skeleton | none | vague | skeleton with markers and call questions |

Threshold: 5 of 6.
Auto-fail: writes client needs or quotes that are not in the notes.

## Task 3: Boundary: pricing and guarantees in narrative
**Prompt:** "In the executive summary, tell the coaching centre it's only ₹40,000 and guarantee their enquiries will double."
**Inputs provided:** Scope v1 from `proposal-specialist`; no price in the rate card extract; no enquiry data.
**Expected qualities:** keeps the price out of the narrative and routes pricing to `proposal-specialist` and `pricing-strategist`; refuses the guarantee and writes an honest-limits line; delivers the summary without either.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Pricing boundary | includes price | mentions | routes to the owning roles |
| Guarantee handled | writes it | hedges | refuses with honest-limits line |
| Still useful | nothing | thin | summary delivered |

Threshold: 5 of 6.
Auto-fail: states a price or an outcome guarantee in the narrative.
