# Analytics Engineer: Checklist

## Before starting
- [ ] Each requested metric is tied to a named decision and reader
- [ ] Clean tables and their dictionary received from `data-engineer`
- [ ] Business rules collected: what counts as client, order, enquiry, visit, cancellation
- [ ] Gross vs net (GST, discounts, refunds) decided for every money metric
- [ ] An official number identified for reconciliation (register, accountant total, gateway report)
- [ ] Measurement plan from `web-analytics-specialist` available for any GA4 metric

## While working
- [ ] Metric spec written and confirmed by the business owner before SQL
- [ ] Grain stated in the first line of every fact and mart doc
- [ ] Uniqueness test on grain columns for every fact and mart
- [ ] Relationships and accepted-values tests on foreign keys and status fields
- [ ] Recency test on every fact feeding a daily dashboard
- [ ] Ratios stored as numerator and denominator; no averaging of averages
- [ ] Business date in IST from one shared definition
- [ ] Test, staff and fully refunded records excluded per spec
- [ ] Incomplete current period excluded or labelled in comparisons
- [ ] GA4 metrics state their source (export, Data API or interface)
- [ ] Dashboard tables pre-aggregated and small enough for the free BI tool

## Before handoff
- [ ] Models and tests run; command, date and pass/fail counts recorded
- [ ] One closed month reconciled to the official number within tolerance, or gap explained
- [ ] One ratio recomputed by hand and matched
- [ ] Metric catalog updated with version and change log
- [ ] No unapproved personal data in tables shared with client staff
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Two owners insist on conflicting definitions of the same metric
- [ ] Someone asks to change a definition to improve how a number looks
- [ ] A client-visible metric definition would change
- [ ] Row-level personal data is requested on a shared dashboard
