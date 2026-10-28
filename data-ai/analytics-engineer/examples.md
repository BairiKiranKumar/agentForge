# Analytics Engineer: Examples

Business names below are fictional. Numbers in output excerpts illustrate the format; they are not recorded results.

## Example 1: Repeat client rate for a two-branch salon
**Request:** "Glow Studio (fictional, Hyderabad, two branches) wants a monthly dashboard with revenue, visits and repeat clients."

**Key decisions:**
- Front desk counted walk-ins without phone numbers as new clients every time; the owner confirmed repeat clients are matched on hashed phone only, and the unmatched share is shown beside the rate.
- Revenue: net of refunds, before GST, in INR, confirmed by the owner.
- `fct_visits` at one row per paid visit; `mart_salon_monthly` at branch x month with numerator and denominator columns.
- Reconciled September against the accountant's monthly total.

**Output (excerpt):**
```
Metric: repeat_client_rate (v1, 2026-10-21)
Formula: clients with >= 2 paid visits in trailing 90 days / clients with >= 1 paid visit in trailing 90 days
Grain: branch x month (IST business_date)
Excludes: staff bookings, test bookings, fully refunded visits
Edge case: walk-ins without phone (Sept: shown as "unmatched share" beside the rate)
Owner: Glow Studio owner (definition)

Reconciliation, Sept 2026: mart revenue vs accountant total -> difference traced to 3 refunds
dated 1 Oct for September visits; spec says refunds count on visit date; accountant books on refund date.
Result: explained, caveat added to dashboard.
```

## Example 2: "GA4 says 1,200 users, your dashboard says 980"
**Request:** the owner: "The client compared our Looker Studio page with the GA4 home screen and thinks our numbers are wrong."

**Key decisions:**
- Traced: our table counts distinct `user_pseudo_id` from the BigQuery export, IST days, consented traffic only; the GA4 screen uses the property's reporting settings, which may include modelled data.
- Did not force the numbers to match; documented the source per metric.
- Proposed one sentence for the client explanation, sent to the owner for approval, not to the client.

**Output (excerpt):**
```
Disagreement trace: users, 1-30 Sept 2026
1 Source: our mart = GA4 BigQuery export; client screen = GA4 interface  <- different sources
2 Filters: ours excludes internal traffic filter = true rows
3 Time basis: both IST
4 Identity: ours = user_pseudo_id; interface may use reporting identity and modelled data
  [Inference, verify against current Google documentation]
Conclusion: a gap is expected; neither number is "wrong". Dashboard label changed to
"Users (consented, from raw export)".
```

## Example 3: Pushback: make the case-study number bigger
**Request:** "For the @example_brand case study, count WhatsApp button taps as 'leads' so the restaurant site shows 3x more leads."

**Response (excerpt):** "I'd rather not redefine 'lead' for the case study. Our spec says a lead is a submitted enquiry or a WhatsApp chat that the restaurant confirms it received. Button taps measure intent, not leads, and a case study that counts them as leads would overstate results publicly. I can report both, clearly labelled: 'WhatsApp button taps: 412' and 'Confirmed enquiries: 131', with the date range and source. If you want taps called leads, that's a definition change the owner and the client should approve, and the case study should state it."
