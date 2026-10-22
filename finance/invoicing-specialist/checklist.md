# Invoicing Specialist: Checklist

## Before starting
- [ ] Registration status record read (registered or not), supplied by the owner, not assumed
- [ ] If registered: GSTIN, legal name and state copied from the owner's certificate
- [ ] Billing trigger evidence present (sign-off, acceptance record)
- [ ] Contract or approved proposal milestone and amount located
- [ ] Client legal name, address, state and GSTIN (if any) collected

## Choosing the document
- [ ] Unregistered: plain invoice, no GST anywhere, no "tax invoice" title
- [ ] Registered, domestic: tax invoice; SAC, rate and place of supply from `gst-specialist`
- [ ] Registered, export: LUT validity for this financial year confirmed by `gst-specialist`; current endorsement text copied
- [ ] Registered, advance before supply: receipt voucher drafted
- [ ] Fee reduced or cancelled: credit note linked to original number and date
- [ ] Unregistered advance: simple acknowledgement, no GST

## While drafting
- [ ] Number is next in the correct series for this financial year, 16 characters or fewer
- [ ] Intra-state CGST + SGST vs inter-state IGST matches place of supply
- [ ] Unregistered client with taxable value of Rs. 50,000 or more: address and state name and code included
- [ ] Description names the milestone and the agreement date
- [ ] Total in words matches figures
- [ ] Payment block matches the owner's written record exactly
- [ ] Invoice date within 30 days of the service milestone (registered)

## Before handoff
- [ ] Field checklist for the document type passed
- [ ] Register row added with status "draft"
- [ ] Draft sent to the owner for approval; nothing issued directly
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Registration status unknown
- [ ] Asked to invent, guess or reformat a GSTIN, PAN or bank detail
- [ ] Client asks to backdate, split, or bill a different entity
- [ ] A payment-detail change request arrives from anyone other than the owner
