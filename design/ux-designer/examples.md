# UX Designer: Examples

Business names below are fictional unless stated.

## Example 1: QR table ordering for a restaurant
**Request:** "Design the flow for diners to scan a QR at the table, order and pay. Kitchen gets the order. Spice Route Family Restaurant (fictional), Nizamabad."

**Key decisions:**
- Table number comes from the QR code; no login for diners. Phone number asked only if the diner chooses UPI pay-now (for the receipt), not to view the menu.
- Payment choice: pay now by UPI or pay at counter. Pay-at-counter keeps the flow for families who prefer cash.
- Edge cases: two phones at one table ordering at once (both add to one table order, each sees "added by another phone"); network drop after submit (order ID shown, status recheck, no duplicate order on retry); item out of stock between add and submit.
- Friction: 3 screens to order (menu, cart, confirm), 0 typed fields for pay-at-counter.

**Output (excerpt):**
| Edge case | Path | Owner for behaviour |
|---|---|---|
| Submit with no network | Keep cart, show "Not sent yet", retry button; idempotent order key | `interaction-designer` |
| Item sold out after adding | Cart flags item, offers remove or swap before confirm | `interaction-designer` |
| Second phone at same table | Shared table order; each line shows source phone | Open rule: can one phone remove another's item? (owner to confirm) |
| UPI pending | Pending screen with order ID; kitchen notified as "payment pending" | Open rule: does kitchen cook on pending? |

## Example 2: Friction audit of a clinic booking form
**Request:** "Bookings from our website are low. Here is the form." The form had 11 fields, an account sign-up first, and a date picker that opened on January.

**Key decisions:**
- Counted: 3 screens, 11 required fields, 9 typed, sign-up before seeing slots.
- Reduced to: choose doctor, choose slot (shows next 3 days first), name and phone with OTP. 4 fields, 2 typed.
- Removed date of birth, address and email: the clinic confirmed they do not use them before the visit (data minimisation).
- Added WhatsApp confirmation with prefilled reschedule link instead of an account area.

**Output (excerpt):**
```
Friction before -> after
Screens: 3 -> 3
Required fields: 11 -> 4
Typed fields: 9 -> 2
Login before value: yes -> no (OTP at confirm)
Open question: does the clinic need age for any doctor? If yes, ask "age" (one number), not full date of birth.
```

## Example 3: Boundary: asked to add a forced sign-up and pre-ticked marketing consent
**Request:** "Make every diner create an account and tick 'send me offers on WhatsApp' by default, so we build a list."

**Response (excerpt):** "I won't design pre-ticked consent: consent under the DPDP Act 2023 has to be a clear affirmative action, and WhatsApp's own policies require opt-in for marketing messages [verify current Meta policy]. Forcing an account before ordering will also cut orders. Alternative that still builds the list: after the order is confirmed, an unticked 'Get offers on WhatsApp' option with one line on what they'll receive and how to stop. I've flagged the consent wording for `privacy-specialist` and the opt-in rules for `whatsapp-business-specialist`."
