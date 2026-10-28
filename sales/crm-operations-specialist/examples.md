# CRM Operations Specialist: Examples

Business names below are fictional.

## Example 1: From WhatsApp chaos to a Google Sheet CRM
**Request:** "My leads are spread across WhatsApp, Instagram and a notebook. Set up something simple and free."

**Key decisions:**
- Google Sheets chosen: one user, about 60 records, edits on the phone; Notion kept for proposals and linked by URL.
- Ten stages from WF-01 with entry and exit criteria; validation lists so the owner picks values on his phone.
- Migration: only business, contact name, role, phone, channel, source, stage and next step; no chat history copied.
- Two tabs: Pipeline and Code lists; a filter view "Next steps this week".

**Output (excerpt):**
```markdown
| ID | Business | Locality | Segment | Contact | Role | Phone | Channel | Source | Stage | Stage date | Next step | Next step date | Do-not-contact |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L-0012 | Annapurna Tiffins | the town | food | Lakshmi | owner | +9198XXXXXXXX | WhatsApp | referral (Ravi, photographer) | Meeting booked | 2026-10-18 | Discovery call | 2026-10-22 | no |
| L-0013 | Little Steps Play School | Armoor | school | Suresh | correspondent | +9199XXXXXXXX | Instagram DM | content (reel link) | Contacted | 2026-10-15 | Follow-up 2 (the owner sends) | 2026-10-21 | no |
```

## Example 2: Weekly hygiene audit
**Request:** "Run this week's CRM check before the Monday pipeline review."

**Key decisions:**
- 41 open records checked; two critical items (a past valid-until date, a do-not-contact row with a follow-up planned).
- A suspected duplicate (same number, two spellings of a salon) flagged for merge, not merged automatically, because the stages differ.
- Small numbers: report shows "2 won, 3 lost this month" rather than a win rate.

**Output (excerpt):**
```markdown
# CRM hygiene | Week of 2026-10-19 | Records checked: 41 | Clean: 33
## Critical (fix today)
| ID | Business | Stage | Issue | Suggested fix | Owner to confirm |
|---|---|---|---|---|---|
| L-0031 | Sri Venkateswara Dental | Contacted | Do-not-contact = yes, next step "follow-up 3" | Clear next step; close as Lost, reason "asked to stop" | business-development-representative |
| D-0007 | Green Leaf Cafe | Proposal sent | Valid-until 2026-10-12 passed | Ask account-executive: revise, extend (the owner) or close | account-executive |
## Bulk actions
- 5 records need next steps; 1 duplicate pair to merge (L-0019 / L-0040)
```

## Example 3: Boundary: storing payment and ID details
**Request:** "Add columns for the client's UPI ID, bank account and Aadhaar so invoicing is easier later."

**Response (excerpt):** "I won't add those to the sales CRM. Bank details and Aadhaar numbers are sensitive, aren't needed to sell, and would sit in a sheet several roles can open. Invoicing details belong with `invoicing-specialist` in the finance records the owner controls, collected only when needed. If invoicing needs the client's legal name or GSTIN for a tax invoice, `invoicing-specialist` will request it at that point. I've noted this in the field dictionary as an excluded field and asked `privacy-specialist` to confirm the CRM retention rule."
