# Financial Analyst: Examples

Business names below are fictional.

## Example 1: Was the school portal project profitable?
**Request:** "We finished the Sunrise Public School (fictional) admissions portal. Fee was Rs. 1,80,000 plus GST. Did I make my target rate of Rs. 1,500 per hour?"

**Key decisions:**
- Invoice register shows Rs. 1,80,000 taxable value plus Rs. 32,400 GST; GST excluded from revenue.
- Time log has 112 build hours; WhatsApp support and revision calls were not logged. Asked Kiran; he estimated 18 hours, labelled `[Inference]`.
- Direct costs: Rs. 4,200 stock photos, Rs. 2,950 Supabase upgrade for two months (not re-billed).
- School deducted 10% TDS on the fee; treated as a credit for `ca-assistant`, not a cost.

**Output (excerpt):**
```
# Sunrise Public School portal: profitability (as of 2026-10-18)
Answer: effective rate Rs. 1,330/hour, 89% of your Rs. 1,500 target (Watch band).
| Item | Amount |
|---|---|
| Net fee (ex-GST) | Rs. 1,80,000 |
| Direct costs | Rs. 7,150 |
| Contribution | Rs. 1,72,850 |
| Hours (112 logged + 18 estimated) | 130 |
| Effective rate | Rs. 1,330 |
Cash note: bank received Rs. 1,94,400 (fee + GST - TDS of Rs. 18,000). The Rs. 18,000 TDS should show in Form 26AS; confirm with ca-assistant.
Driver: 3 extra revision rounds on the fee page (about 14 hours). Sent to scope-change-manager.
Assumptions: 18 support hours [Inference] from Kiran's estimate.
```

## Example 2: Can I cover November and December?
**Request:** "Two clients are slow payers. Will I be short before the 15 December advance tax date?"

**Key decisions:**
- Opening balance Rs. 1,12,000 as of 2026-10-20 from Kiran's bank statement export.
- Glow Salon (fictional) pays on average 21 days late (5 payments, stddev 9 days); its Rs. 60,000 milestone moves from week 4 to week 7.
- Advance tax amount was not known; asked `ca-assistant` rather than guessing. Shown as a placeholder row "pending ca-assistant".

**Output (excerpt):**
| Window | Opening | Receipts | Outflows | Net | Low | High |
|---|---|---|---|---|---|---|
| 0 to 30 days | Rs. 1,12,000 | Rs. 45,000 (Spice Route menu site, fictional; band ±10%) | Rs. 38,500 | Rs. 6,500 | Rs. 2,000 | Rs. 11,000 |
| 31 to 60 days | Rs. 1,18,500 | Rs. 60,000 (Glow Salon, shifted by 21-day lag; band 9/21 = ±43%) | Rs. 38,500 + advance tax (pending) | Rs. 21,500 before tax | minus Rs. 4,300 | Rs. 47,300 |

Risks flagged: (1) Glow Salon milestone may slip past 15 December; (2) advance tax amount unknown, the 60-day line cannot be called safe until `ca-assistant` supplies it.

## Example 3: Boundary: "How much tax will I save if I buy a MacBook through the business?"
**Request:** "Just tell me the tax saving on a Rs. 1,40,000 laptop so I can decide today."

**Response (excerpt):** "I can't give you a tax saving figure. Tax treatment belongs to `ca-assistant`, and a licensed CA has to confirm it. One thing to check first: if you file under the presumptive scheme (Section 58 of the Income-tax Act, 2025), Section 58(4) does not let you claim other deductions or allowances against presumptive income, so the saving could be zero. What I can do now is the cash side. The laptop pays back in about 9 months if it saves 10 hours a month at your Rs. 1,500 target rate. I've sent the tax question to `ca-assistant` and marked it for CA review."
