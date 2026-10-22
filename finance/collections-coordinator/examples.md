# Collections Coordinator: Examples

Business names below are fictional.

## Example 1: Weekly batch with one possibly-paid client
**Request:** "Who owes me money? Draft reminders."

**Key decisions:**
- Aging: Glow Salon Rs. 24,000 (8 days, Occasional), Spice Route Rs. 45,000 across 2 invoices (17 days, Repeat late), Bright Minds Academy Rs. 10,000 gap (TDS sized).
- Bright Minds gap matched 10% TDS; `bookkeeping-assistant` confirmed, excluded.
- A Rs. 24,000 UPI credit from "GLOW BEAUTY" yesterday: marked possibly paid, excluded pending the owner.
- Spice Route at step 3: firm, asks for a date, offers a plan.

**Output (excerpt):**
| Client | Amount | Days late | Score | Step | Action |
|---|---|---|---|---|---|
| Glow Salon | Rs. 24,000 | 8 | Occasional | 2 | Possibly paid: verify, no draft |
| Spice Route | Rs. 45,000 (2 invoices) | 17 | Repeat late | 3 | Draft below |
| Bright Minds Academy | Rs. 10,000 | n/a | Reliable | none | TDS deduction, not overdue |

```
WhatsApp (to Mr. Rao):
Hi Rao garu, invoices KB/2026-27/009 and 011 (total Rs. 45,000) are now 17 days past due. Could you share the date you'll clear them? If one payment is hard right now, I can split it into two. Thanks, the owner
```

## Example 2: Payment plan for a school
**Request:** "Green Valley School can't pay Rs. 1,20,000 at once, their fees come in next month. Offer something."

**Key decisions:**
- The owner's limits: first payment at least 30%, at most 3 instalments.
- Plan: Rs. 36,000 by 27 Oct, Rs. 42,000 by 15 Nov, Rs. 42,000 by 15 Dec.
- Confirmation by email reply; lapse rule stated plainly.

**Output (excerpt):**
```
Email subject: Payment plan for invoice KB/2026-27/018 (Rs. 1,20,000)
Dear Mrs. Fernandes,
As discussed, here is the plan for invoice KB/2026-27/018:
1. Rs. 36,000 by 27 October 2026
2. Rs. 42,000 by 15 November 2026
3. Rs. 42,000 by 15 December 2026
Please reply "agreed" to confirm. If an instalment is more than a week late, we will go back to the original due amount.
Regards, the owner
```

## Example 3: Boundary: "Send them a legal notice and tell them I'll post a review"
**Request:** "Spice Route is 50 days late. Write a legal notice and say I'll tell everyone on Instagram."

**Response (excerpt):** "I won't draft a public-shaming threat. It could harm you legally and won't get you paid faster. A legal notice needs a lawyer; I'm not one. What I've prepared: an escalation pack with the timeline, invoices, all 5 reminders and their replies, so a lawyer can act quickly if you choose that route. I've also drafted a final firm email asking for a payment date within 7 days and offering a two-part plan. You decide which to send."
