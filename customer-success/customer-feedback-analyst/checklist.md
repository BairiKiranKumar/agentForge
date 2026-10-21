# Customer Feedback Analyst: Checklist

## Before starting
- [ ] Raw feedback sources connected and accessible (surveys, tickets, WhatsApp snippets)
- [ ] Product feature area map and taxonomy categories reviewed
- [ ] Client account tiers and industry segments identified
- [ ] Survey scoring scales confirmed (1-5 CSAT, 0-10 NPS)
- [ ] Privacy and PII redaction rules verified

## While working
- [ ] Raw feedback sanitized: all personal phone numbers, passwords, and PII redacted
- [ ] Feedback items tagged by Product Area, Feedback Type, and Sentiment
- [ ] Bugs differentiated clearly from new feature requests
- [ ] Quantitative metrics computed: CSAT %, NPS score, and response count (N)
- [ ] Thematic clusters identified with frequency counts and business impact
- [ ] Representative user quotes extracted illustrating top positive and negative themes
- [ ] Critical negative feedback (<2/5 rating) flagged to `customer-success-manager`
- [ ] Actionable recommendations formulated for engineering and design teams

## Before handoff
- [ ] Monthly Voice of the Customer (VoC) report formatted and proofread
- [ ] Feature Request Ledger updated with latest demand counts
- [ ] Report distributed to `product-manager`, `design-lead`, and `customer-success-manager`
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Feedback reports an active critical security flaw or financial double-charging
- [ ] Severe negative customer sentiment spikes indicate widespread product failure
- [ ] Feedback collection pipeline breaks, causing zero data capture for >7 days
- [ ] Unredacted medical or sensitive citizen records appear in raw survey dumps
