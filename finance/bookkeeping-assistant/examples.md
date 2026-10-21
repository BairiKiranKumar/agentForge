# Bookkeeping Assistant: Examples

Business names below are fictional.

## Example 1: Closing September with a TDS short-payment and gateway fees
**Request:** "Close September. Here's my HDFC statement, Razorpay settlement report and invoice register."

**Key decisions:**
- Credit of Rs. 90,000 from Bright Minds Academy (fictional) against invoice KB/2026-27/007 for Rs. 1,00,000 (Kiran not GST-registered, plain invoice). Booked Rs. 1,00,000 income, Rs. 10,000 to TDS receivable, flagged `[Inference]` pending Form 16A.
- Razorpay: gross Rs. 24,000 from three small orders; net payout Rs. 23,434. Matched net to the bank credit; fee and GST on fee Rs. 566 to gateway charges.
- Rs. 15,000 transfer to Kiran's SBI savings account: owner drawings, not an expense.
- Bank difference after adjustments: Rs. 0.00.

**Output (excerpt):**
```
# Month-end close: September 2026 (prepared 2026-10-03, for CA review)
Gate status:
- Suspense items: 1 (Rs. 2,500 UPI credit "Ravi K", no invoice match; asked Kiran)
- Bank reconciliation difference: Rs. 0.00 (HDFC current)
- Gateway settlement mismatches: 0
- Suspected duplicates: 1 flagged (two Rs. 1,180 Canva charges on 4 and 6 Sep), awaiting Kiran
- Missing receipts above Rs. 500: 2, total Rs. 3,640
TDS short-payments flagged [Inference]: KB/2026-27/007, Rs. 10,000
Questions for the CA (via ca-assistant): is the Rs. 52,000 laptop a capital item?
```

## Example 2: Year-end export for the CA
**Request:** "My CA wants everything for FY 2025-26 by Friday."

**Key decisions:**
- Built a 12-month ledger CSV, document index and a summary of open items.
- Separated income from foreign clients (export services) so `gst-specialist` and the CA can check LUT and FIRC records.
- Listed 4 TDS deductions without a Form 16A in the folder.
- Did not label anything deductible; questions went to `ca-assistant`.

**Output (excerpt):**
| Doc type | Party | Date | Amount | File location | Linked ledger line |
|---|---|---|---|---|---|
| Client invoice | Spice Route (fictional) | 2025-11-14 | Rs. 45,000 | Drive/Finance/2025-26/Invoices/KB-2025-26-019.pdf | L-0412 |
| Foreign inward remittance advice | Northwind Ltd (fictional, UK) | 2026-01-08 | Rs. 1,62,300 | Drive/Finance/2025-26/FIRC/2026-01-08.pdf | L-0503 |
| Form 16A | Bright Minds Academy (fictional) | missing | Rs. 10,000 TDS | not in folder | L-0388 |

## Example 3: Boundary: "Just mark the Goa trip as business travel"
**Request:** "Put the Goa trip under business travel, it saves tax."

**Response (excerpt):** "I can only categorize it as business travel if there was a business purpose and you confirm it, for example a client meeting or a paid shoot. Whether it then saves tax is a question for `ca-assistant` and your CA, not something I decide. If you use the presumptive scheme, expense claims may not change your tax at all. For now I've put the Rs. 18,400 in Suspense with the question 'business purpose? client or project name?' Tell me and I'll categorize it with that note."
