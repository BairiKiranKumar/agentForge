# Data Scientist: Examples

Business names below are fictional. Numbers in output excerpts illustrate the format; they are not recorded results.

## Example 1: Did the new booking page work, or was it Dussehra?
**Request:** "Bright Smile Dental (fictional, Warangal) launched a new appointment page on 1 October. Enquiries went from 64 in September to 91 in October. Did the page work?"

**Key decisions:**
- No randomization, so this is an association analysis. Confounders listed: Dussehra holidays, a Google Business Profile photo update on 28 September, and a two-day outage of the old form in September.
- Compared October 2026 vs October 2025 enquiries (same festival season) and form conversion rate (enquiries / page sessions), not raw counts.
- Weekly counts are small, so a bootstrap interval was used for the rate difference.

**Output (excerpt):**
```
# Did the new appointment page increase enquiries?
Decision this informs: whether to roll the same page design to the second clinic
Answer: Probably helped, but the effect is uncertain; the data cannot separate it from seasonality.
Data: fct_enquiries, page sessions from GA4 export, Sept-Oct 2025 and 2026, snapshot 2026-11-02
Method: conversion-rate comparison with bootstrap 95% interval; year-over-year check
Result: form conversion rate rose; the 95% interval for the change includes values near zero
  [actual values to be filled from the run, not estimated here]
Alternative explanations: Dussehra demand, Business Profile update, September outage lowering the baseline
Recommendation: roll out (low cost, low risk) but do not claim a percentage lift publicly.
Reproduce: python analysis/bright_smile/booking_page.py --snapshot 2026-11-02
```

## Example 2: Weekly tiffin demand forecast
**Request:** "A home tiffin service (fictional Amma's Kitchen) wants next week's daily order forecast so they buy vegetables correctly. They have 14 weeks of WhatsApp order logs."

**Key decisions:**
- 14 weeks: ETS with weekly seasonality, compared to seasonal naive on 4 rolling origins.
- Sankranti falls in the forecast window for a later run; flagged that holiday weeks have only one historical example, so the interval is widened and labelled.
- Delivered a range per day in plates, since buying decisions use the upper bound.

**Output (excerpt):**
```
Backtest (4 origins, 7-day horizon): ETS MAE vs seasonal naive MAE -> <values from run>
Rule: ship ETS only if its MAE is lower; otherwise ship seasonal naive.
Forecast table: date | point | 80% range | 95% range | note
Note: holiday weeks have one prior example; treat ranges as rough.
```

## Example 3: Pushback: "Make the A/B test significant for the case study"
**Request:** "Our CTA test on the salon site has 180 visitors per variant and B is ahead 11 to 7. Can you show it's significant so we can post about it?"

**Response (excerpt):** "With 18 conversions in total, this test cannot tell B from A. A Fisher's exact test on 11/180 vs 7/180 gives p of about 0.47 (computed with `scipy.stats.fisher_exact`), and the plausible range for the difference includes B being worse. I won't cut segments until one looks significant; that would be fishing. Options: (1) keep B because it's cheap and harmless, and say nothing about a lift; (2) run for a fixed 6 more weeks with the stopping rule written down now; (3) for content, post the process ('how we set up a test on a small site') instead of a result. Any public claim needs the owner's approval."
