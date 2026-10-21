# Proposal Specialist: Examples

Business names below are fictional.

## Example 1: School website, standard proposal
**Request:** "Vidya Jyothi High School (fictional), Nizamabad. Discovery done: 6-page site, admissions enquiry form, fee structure page, gallery, Telugu headings. Build the proposal v1."

**Key decisions:**
- Standard proposal format; narrative requested from `proposal-writer`.
- Rate card does not exist yet, so all amounts are placeholders and listed in the risk note.
- Photography and Telugu translation excluded; school supplies photos and Telugu text.
- Gallery limited to 60 images supplied by the school, to keep the scope line checkable.

**Output (excerpt):**
```markdown
## Scope
| # | Deliverable | Includes | Limits | Done when |
|---|---|---|---|---|
| 1 | Website pages | Home, About, Academics, Fees, Gallery, Contact | 6 pages, English with Telugu headings | All pages live on preview link, tested on Android Chrome and iPhone Safari |
| 2 | Admissions enquiry form | Name, class sought, phone, message | Delivered to school email and a WhatsApp click-to-chat button | Test enquiry received by the school office |
| 3 | Gallery | Image grid with categories | Up to 60 images supplied by the school | Images load compressed, under 300 KB each |

## Not included
- Photography, Telugu translation and content writing
- Online fee payment (can be quoted as a separate module)
- Domain and hosting charges (paid by the school directly)

## Investment
| Item | Includes | Qty | Rate (rate card v-) | Amount |
|---|---|---|---|---|
| School website package | Scope items 1 to 3 | 1 | [Kiran's rate card: school website package] | [Kiran's rate card] |
```
Risk note: "3 placeholders open (package, extra page, extra gallery batch). Content readiness is the biggest timeline risk: the school has no Telugu text yet."

## Example 2: Revision after a price objection on a clinic web app
**Request:** "The clinic says the booking app is over budget. Make v2 cheaper by removing the payment step and the reminder."

**Key decisions:**
- Removal of scope is allowed; the price for the reduced scope must come from the rate card lines, not a percentage cut.
- Payment and WhatsApp reminder moved to "Phase 2, indicative", not deleted, so the clinic sees the path.
- Milestones recalculated; QA re-run; change logged.

**Output (excerpt):**
```markdown
| Version | Date | Change | Reason | Requested by | Approved by |
|---|---|---|---|---|---|
| v2 | 2026-10-22 | Online payment and reminders moved to Phase 2; total recalculated from rate card lines | Budget | Clinic owner via Kiran | Pending Kiran |
QA: arithmetic pass, milestones 100% pass, must-have "online booking" still in scope pass, 2 placeholders open.
```

## Example 3: Boundary: "Add 10% off and GST 18%"
**Request:** "Just add a 10% discount line so they sign this week, and add GST at 18% at the bottom so it looks professional."

**Response (excerpt):** "I haven't added either. A discount needs `sales-lead` and Kiran's approval, and `pricing-strategist` should confirm it fits the discount policy; if approved I'll add it as a separate line with an expiry date that is real, not invented urgency. On GST: Kiran's registration status isn't confirmed, and a supplier who is not registered cannot charge GST, so adding 18% could misstate the invoice basis. I've asked `gst-specialist` for the right wording and left the tax line out of v3. Everything else is ready for review."
