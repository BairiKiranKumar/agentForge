# Product Owner: Examples

Business names below are fictional unless stated.

## Example 1: Breaking a PRD must-have into stories (daycare fee reminders)
**Request:** "PRD must-have for the Little Steps Daycare (fictional) portal: 'Admins can send fee reminders to parents.' Make it sprint-ready."

**Key decisions:**
- Split by path: manual reminder to one parent first, bulk reminder to all unpaid parents second, scheduled reminders later (Next band).
- WhatsApp Business Platform is not set up, so the first story uses a click-to-chat link with a prefilled message instead of automated sending. Noted as a dependency for the bulk story.
- Fee status rule comes from `business-analyst` rule BR-03 ("unpaid" means no payment recorded by the 5th).

**Output (excerpt):**
```
ID: DC-021 | Size: S | Band: Now
Title: Admin sends one parent a fee reminder
Story: As a daycare admin, I want to send a fee reminder to one parent from their
       child's record, so that I stop typing the same message every month.
Rules: BR-03
Acceptance criteria:
1. Given a child whose fee is unpaid per BR-03, when the admin taps "Send reminder",
   then WhatsApp opens with the parent's number and this message prefilled:
   "Namaste, a reminder that <child>'s fee of ₹<amount> for <month> is due."
2. Amount shows Indian grouping (₹12,500).
3. Given a child whose fee is paid, then the button is not shown.
4. Given the parent's number is missing or not 10 digits, then the button is disabled
   with the text "Add a valid mobile number".
5. Works at 375 px width on Android Chrome.

ID: DC-022 | Size: M | Band: Now | Depends on: WhatsApp template approval (not set up)
Title: Admin sends reminders to all unpaid parents
Status: Not ready (dependency). Spike DC-023 (2 hours): confirm template and cost
with whatsapp-business-specialist; output a note.
```

## Example 2: Sprint review with a rejection
**Request:** "Review cycle 6 for the QR ordering pilot. Developer says all four stories are done."

**Key decisions:**
- Checked each criterion against the preview URL and the Playwright run report.
- QR-014 criterion 3 (missed orders appear after network returns) had no evidence; manual check on throttled network showed two orders lost.

**Output (excerpt):**
| Story | Criterion | Evidence | Verdict |
|---|---|---|---|
| QR-012 | 1 to 4 | `kitchen.spec.ts` run 2026-10-18, 4 passed | Accept |
| QR-014 | 1, 2, 4 | spec run, screenshot | Pass |
| QR-014 | 3 | Manual throttled test: 2 of 5 orders missing after reconnect | Fail: story rejected, returned to backlog with same ID |
| QR-015 | 1 to 3 | preview URL check at 375 px | Accept; follow-up QR-019 logged for button spacing (outside criteria) |

Commitment reliability this cycle: 3 of 4 (75%).

## Example 3: Pushback: "Mark it done, we'll fix it after launch"
**Request:** "The UPI payment confirmation sometimes shows success before the payment is confirmed. Accept the story anyway, we launch Friday."

**Response (excerpt):** "I can't accept QR-017. Criterion 2 says the success screen only appears after the gateway confirms payment, and today it can show success for an unpaid order. That would tell customers they paid when they didn't, and the restaurant would lose money or argue at the counter. Options: (1) fix and re-test before Friday; (2) launch Friday with pay-at-counter only and keep UPI behind a flag. Moving the launch or changing scope is the owner's call, and I've flagged it to `product-manager` with the evidence."
