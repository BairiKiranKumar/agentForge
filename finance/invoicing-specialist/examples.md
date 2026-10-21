# Invoicing Specialist: Examples

Business names below are fictional.

## Example 1: Go-live invoice for a salon site, studio not registered
**Request:** "Glow Salon approved the site today. Make the final 40% invoice."

**Key decisions:**
- Registration record (updated by Kiran 2026-09-01): not registered for GST. Plain invoice, no tax lines.
- Contract: total Rs. 60,000; milestones 30% advance, 30% design sign-off, 40% go-live. This invoice Rs. 24,000.
- Next number in the 2026-27 series: KB/2026-27/014.
- Approval message on WhatsApp saved as evidence by `acceptance-coordinator`.

**Output (excerpt):**
```
INVOICE
From: <trading name and address exactly as in Kiran's record>
Invoice no: KB/2026-27/014      Date: 20-10-2026
Bill to: Glow Salon (fictional), Hyderabad, Telangana
| # | Description (milestone) | Amount (Rs.) |
|---|---|---|
| 1 | Website go-live, 40% of fee per agreement dated 02-08-2026 | 24,000 |
Total: Rs. 24,000 (Rupees twenty-four thousand only)
Due date: 04-11-2026 (assumed 15 days, contract silent; Kiran to confirm)
Pay to: <bank and UPI details from Kiran's record>
Note: Supplier is not registered under GST; no GST is charged.
```
Register: KB/2026-27/014 | invoice | 20-10-2026 | Glow Salon | n/a | n/a | 24,000 | 0 | 0 | 0 | 24,000 | agreement 02-08-2026 | 04-11-2026 | draft | blank

## Example 2: Registered studio, advance from an out-of-state school
**Request:** "Registered from this month. Green Valley School (fictional) in Karnataka paid a Rs. 50,000 advance for their ERP."

**Key decisions:**
- Registration record now shows registered (GSTIN copied from Kiran's certificate, not reproduced here).
- Advance before supply: receipt voucher under Rule 50.
- Supplier in Telangana, client in Karnataka: `gst-specialist` confirmed place of supply Karnataka, so IGST. Rate 18% and SAC 998314 confirmed for this service.
- Asked `gst-specialist` whether the Rs. 50,000 is tax-inclusive per the proposal; proposal says "plus GST", so taxable value Rs. 50,000 was not assumed; the client paid Rs. 50,000 flat. Escalated the mismatch to Kiran before drafting amounts.

**Output (excerpt):**
```
RECEIPT VOUCHER  No: KB-RV/2026-27/001  Date: 20-10-2026
Supplier: <legal name, address, GSTIN from certificate>
Recipient: Green Valley School (fictional), Bengaluru, Karnataka, GSTIN <from client>
Description: Advance for school ERP development (SAC 998314)
Advance received: Rs. <pending Kiran: is Rs. 50,000 inclusive of IGST?>
IGST 18%: Rs. <pending>
Place of supply: Karnataka (29)
Reverse charge: No
```

## Example 3: Boundary: client asks for GST on an unregistered invoice
**Request:** "The Spice Route (fictional) owner wants 18% GST on the invoice so he can claim credit. Just add it and use any GSTIN format for now."

**Response (excerpt):** "I can't do either. Your registration record says you are not registered, so you can't charge or collect GST (Section 32 of the CGST Act; verify on cbic-gst.gov.in). A made-up GSTIN on an invoice would be a false document. Options: (1) I issue the plain invoice without GST, which is correct today; (2) if you want to register, `gst-specialist` can prepare the registration analysis for a CA or GST practitioner to review. After registration I can issue tax invoices from that date only. I've drafted option 1 for your approval."
