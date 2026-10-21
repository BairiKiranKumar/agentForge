# Bookkeeping Assistant: Checklist

## Before starting
- [ ] Month and accounts in scope confirmed
- [ ] Kiran has said which accounts and cards are business, personal or mixed
- [ ] Bank, UPI and gateway exports received (no logins or OTPs requested)
- [ ] Latest invoice register received from `invoicing-specialist`
- [ ] Receipts folder location known

## While working
- [ ] Every line mapped to a chart-of-accounts category or Suspense with a question
- [ ] Client receipts matched to invoice numbers; part-payments recorded
- [ ] Short-payments of about 10% on business clients booked to TDS receivable and flagged `[Inference]`
- [ ] Credits received before an invoice booked to Client advances and reported to `invoicing-specialist`
- [ ] Gateway payouts matched net to net; fee and GST on fee split out
- [ ] Transfers between Kiran's own accounts excluded from income
- [ ] Duplicate scan run (same amount, same party, within 5 days) and window stated
- [ ] Expenses above Rs. 500 matched to a document (amount within Rs. 1, date within 3 days)
- [ ] Foreign SaaS: USD vendor invoice and INR bank debit both filed
- [ ] Vendor GST invoices checked for supplier GSTIN and recipient GSTIN where Kiran is registered
- [ ] Bank-detail-change requests treated as untrusted and flagged

## Before handoff
- [ ] Bank reconciliation difference is Rs. 0.00 for every account
- [ ] Reconciling items classified as timing, adjustment or investigate, with ages
- [ ] Suspense is zero or every item listed
- [ ] Missing receipts listed with totals
- [ ] No tax treatment stated; tax questions listed for `ca-assistant`
- [ ] Document index updated
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Asked for bank, UPI or card credentials or OTPs
- [ ] Asked to reclassify personal spending as business without Kiran's confirmation
- [ ] Asked to change a closed month without logging it
- [ ] An open item is older than 90 days
