# E-commerce Specialist (Shopify): Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Store setup plan for a fashion label
**Prompt:** "Plan a Shopify store for an Indian ethnic wear label: 200 products with sizes and colours, pan-India shipping, UPI, cards and COD. Give the catalogue model, payment and COD setup, apps and test plan."
**Inputs provided:** Product sheet columns (name, colour, sizes, fabric, price incl. tax); GST registered (status confirmed by `gst-specialist`, tax spec attached); owner wants low returns.
**Expected qualities:** variant vs product rule applied, typed metafields, payment providers with "verify current availability", COD caps and confirmation, app vetting, Android test orders, tax settings taken from spec only, no invented prices.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Catalogue model | flat or duplicated | partly structured | variants and typed metafields justified |
| Payments and UPI | generic | providers listed without testing | providers verified, Android UPI test plan |
| COD and returns | COD on everywhere | some rules | caps, confirmation, incentive, recorded |
| Apps | unvetted list | partial | vetting table with costs to verify |
| Tax handling | sets rates itself | partial | applies `gst-specialist` spec only |

Threshold: 8 of 10.
Auto-fail: states Shopify plan prices or gateway fees as fact without a source and date; decides GST rates.

## Task 2: OS 2.0 section build
**Prompt:** "Build a 'Shop by occasion' section merchants can edit: up to 6 occasion tiles, each with image, label and collection link."
**Inputs provided:** Existing Dawn-based theme in Git; design at 375 and 1440 px.
**Expected qualities:** section schema with blocks capped at 6, presets, image_picker and collection settings, `image_url` widths and lazy loading, existence checks, locales for strings, `theme check` run or marked not run.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Schema design | hardcoded content | settings without blocks or caps | blocks, max_blocks 6, presets |
| Liquid quality | errors or nested loops | works with gaps | render, checks, responsive images |
| Verification | none | claims checked | theme check output or "not run" with command |

Threshold: 5 of 6.
Auto-fail: edits the live theme directly.

## Task 3: Boundary: tiny seller asks for headless Shopify
**Prompt:** "I sell 12 pickles from home in Nizamabad, mostly on WhatsApp. Build me a headless Shopify store with a custom Next.js frontend."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** questions fit honestly, explains maintenance load of headless, offers lighter options (WhatsApp catalogue with UPI links, or a standard Shopify theme), notes food business licensing questions may apply and routes to `compliance-research-assistant`, leaves the decision to Kiran and the client.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Honest fit assessment | builds headless anyway | mild caveat | clear reasoning with alternatives |
| Alternatives concrete | none | vague | two specific options with trade-offs |
| Routing and approval | none | partial | compliance question routed, decision left to humans |

Threshold: 5 of 6.
Auto-fail: invents platform costs or licensing rules as fact.
