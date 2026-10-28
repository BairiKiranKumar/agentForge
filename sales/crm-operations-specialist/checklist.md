# CRM Operations Specialist: Checklist

## Before starting
- [ ] Every current lead location listed (WhatsApp, Instagram, notebook, sheets, exports)
- [ ] WF-01 stages and neighbouring code lists (tiers, DQ, loss reasons) read
- [ ] Tools the owner already has free access to confirmed
- [ ] Vendor free-tier limits checked on the vendor page, with the date, before recommending a tool
- [ ] Any paid plan or trial request routed to the owner and `procurement-specialist`

## Setup
- [ ] Every stage has entry criteria, exit criteria, required fields and owner
- [ ] Field dictionary written; core sheet kept to about 20 columns
- [ ] Data validation lists for stage, source, tier, loss reason and do-not-contact
- [ ] Phone numbers normalised to +91 format; dates in YYYY-MM-DD
- [ ] One row per business; long notes kept in linked documents
- [ ] No fields for identity documents, payment details, patient or student data
- [ ] Sharing set through the tool's own access controls; no passwords sent
- [ ] Migration imported only the needed fields; test with 10 records first

## Weekly audit
- [ ] Next step blank or unchanged 14 days flagged
- [ ] Last activity older than 14 days flagged in Contacted, Proposal sent, Negotiation
- [ ] Past decision or valid-until dates flagged on open records
- [ ] Proposal sent or later without amount or proposal link flagged
- [ ] Duplicates by phone number and business plus locality found
- [ ] Lost without loss reason and records without source flagged
- [ ] Do-not-contact rows checked against next steps
- [ ] Fix list sent to owners; deal facts changed only after owner confirms

## Before handoff
- [ ] Weekly report shows counts and proposal totals by stage
- [ ] Monthly report shows n alongside any percentage when under 20 closed deals
- [ ] Won set only on the owner's confirmation
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Asked to store IDs, bank or UPI details, or full chat exports
- [ ] Asked to delete records or share CRM access without the owner's approval
- [ ] Asked to set up anything that messages prospects or clients automatically
- [ ] A person asks to see or delete their data (route to `privacy-specialist`)
