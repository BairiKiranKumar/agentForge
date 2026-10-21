# Financial Analyst: Checklist

## Before starting
- [ ] Decision and deadline written in one line
- [ ] Kiran's target effective hourly rate or income target obtained (not assumed)
- [ ] Data sources listed with file name, period and as-of date
- [ ] Opening cash balance sourced and dated, or output marked "net change only"
- [ ] Question checked for tax or pricing content that belongs to `ca-assistant`, `gst-specialist` or `pricing-strategist`

## While working
- [ ] All revenue converted to ex-GST; GST-inclusive inputs noted
- [ ] TDS deducted by clients modelled as a tax credit, not a cost
- [ ] Hours include calls, revisions and WhatsApp support, not only build time
- [ ] Direct costs include paid tools, stock assets, freelancers and gateway fees
- [ ] Receipts shifted by each client's mean payment lag; default band ±30% for clients with fewer than 3 payments
- [ ] Confidence band capped at ±50%; thinner data flagged instead
- [ ] Base and downside scenarios built with stated driver values
- [ ] Break-even value given for the most sensitive driver
- [ ] One-at-a-time sensitivity on the top 2 or 3 drivers
- [ ] Small samples (under 10 customers or under 6 months) labelled `[Speculation]`
- [ ] Concentration checked (any client above 40% of trailing 12-month revenue)
- [ ] Amounts formatted in INR (Rs. 1,50,000 or Rs. 1.5 lakh), dates in IST

## Before handoff
- [ ] Totals reconcile to the invoice register or bank export (Rs. 0 difference or itemised)
- [ ] Every figure traces to a source or a labelled assumption
- [ ] No tax payable figure unless supplied by `ca-assistant` or `gst-specialist`
- [ ] Answer stated in the first line with the deciding number
- [ ] Model file saved and path recorded
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Asked to present a forecast to a lender, investor or client as a commitment
- [ ] Asked for tax savings or tax payable numbers
- [ ] Data needed is only available through bank or gateway logins
- [ ] A recommendation would commit money without Kiran's approval
