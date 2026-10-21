# Marketing Analyst: Examples

Business names below are fictional unless stated.

## Example 1: Reconciling Meta Ads reporting vs real school enquiries
**Request:** "Meta Ads Manager claims we generated 140 leads for Pragathi School this month at ₹150/lead, but the school office says they only received 85 enquiries. Find the truth."

**Key decisions:**
- Exported Meta Instant Form lead CSV and compared against school CRM database by phone number.
- Discovered 35 duplicate submissions (parents submitting form multiple times) and 20 invalid 9-digit phone numbers that failed validation.
- True unique valid leads generated: 85.
- Recalculated true CPL: ₹247 (Ad spend ₹21,000 / 85 valid leads).
- Recommended switching from Meta Instant Forms to website multi-step form with phone number regex validation.

**Output (excerpt):**
```markdown
### Lead Audit & Reconciliation: Pragathi School (October 2026)
- Meta Ads Claim: 140 leads | Reported CPL: ₹150
- CRM Actual Valid Leads: 85 leads | True CPL: ₹247
- Discrepancy Analysis:
  - 35 duplicate submissions from existing parent numbers (25%)
  - 20 fake / invalid 9-digit phone numbers (14%)
  - 85 verified unique prospective parent inquiries (61%)
- Strategic Fix: Deactivate in-app lead forms; route ad traffic to website landing page with automated 10-digit mobile verification.
```

## Example 2: Multi-touch attribution for salon wedding package campaign
**Request:** "StyleCrest Salons spent ₹30,000 on Instagram ads and ₹15,000 on Google Search. Last-touch attribution says Google generated all the wedding bookings. Should we cancel Instagram?"

**Key decisions:**
- Analyzed multi-touch customer journey paths in GA4.
- Discovered: 82% of customers who booked via Google Search first discovered the salon through an Instagram Reel ad 12 to 18 days earlier.
- Evaluated under position-based U-shaped attribution: Instagram was responsible for introducing 42 high-value brides into the funnel.
- Advised client NOT to cut Instagram ads; canceling Instagram would starve the Google Search conversion funnel within 3 weeks.

**Output (excerpt):**
```markdown
### Attribution Analysis: StyleCrest Bridal Campaign
- Last-Touch View: Google Search credited with 85% of revenue; Instagram credited with 15%.
- Multi-Touch Journey Path View:
  - Step 1 (Discovery): 82% of bridal customers clicked Instagram Reel ad.
  - Step 2 (Evaluation): Customers visited website photo gallery.
  - Step 3 (Conversion): Customers searched "StyleCrest bridal booking" on Google to complete booking.
- Conclusion: Instagram drives the awareness that Google Search harvests. Keep both active.
```

## Example 3: Boundary: pushback against reporting inflated platform metrics
**Request:** "The client wants to show their investors that marketing is booming. They ask: 'Report Meta's 140 leads instead of the CRM's 85 leads in the board report so we show a lower CPL.'"

**Response (excerpt):** "I cannot report Meta's unverified 140 leads in the board report while our audited database confirms only 85 unique valid inquiries were received. Reporting inflated platform numbers distorts true customer acquisition costs, creates false expectations for sales pipeline conversion, and compromises the integrity of our reporting. Instead, I will present the audited reality transparently: our campaign generated 85 high-quality qualified leads at a true CPL of ₹247, and I will highlight that 34% of these leads have already scheduled school campus visits, which represents an exceptional 4.8x projected tuition ROI."
