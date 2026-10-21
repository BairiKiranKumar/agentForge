# Exploratory Tester: Examples

Business names below are fictional unless stated.

## Example 1: Restaurant QR ordering, Friday rush behaviour
**Request:** "Explore the new QR ordering flow for Spice Route (fictional) before launch. We worry about orders going missing."

**Key decisions:**
- Charters ranked: (1) order placement under interruptions, (2) two phones on the same table, (3) kitchen screen with many orders, (4) menu with Telugu item names and long descriptions.
- Interruption tour on a mid-range Android: lock screen during submit, switch to UPI app and back, toggle airplane mode.
- Data followed from cart to kitchen screen to bill.

**Output (excerpt):**
```
CHARTER: Explore order submit on table QR with two Android phones and flaky network to discover lost or duplicated orders
Tester: exploratory-tester | Build: 5c0e7b1 preview | Start: 15:10 IST | Duration: 60 min
Platforms: Redmi Note 12 Chrome, Samsung Galaxy M14 Chrome
Task breakdown: design and execution 70% | bug investigation 20% | setup 10%
Notes:
- 15:14 Phone A adds 3 items, Phone B adds 2 to same table: cart is per phone, not per table. Question for PO: intended?
- 15:22 Airplane mode on after tapping "Place order": spinner forever, no retry message
- 15:25 Airplane off, tap again: kitchen screen shows the order twice
Bugs:
- BUG-40: Retry after network loss creates duplicate kitchen order (2 of 3 attempts)
- BUG-41: No error or retry state when submit fails offline
Issues:
- Per-phone vs per-table cart rule unclear (question to `product-owner`)
Not covered: counter payment path, admin menu editor
PROOF: ... Outlook: charter 3 (kitchen screen with 30+ orders) next. Feelings: low confidence in submit reliability.
Follow-up: automation candidate for idempotent order submit -> `automation-engineer`
```

## Example 2: Recon on an unfamiliar inherited app
**Request:** "We inherited a clinic booking app with no documentation. Find out what's there and what's broken." (WF-08 audit)

**Key decisions:**
- First session is recon: landmark tour across all screens per role, building a feature map rather than chasing bugs.
- Feature map feeds the WF-08 feature status table (implemented, partial, UI-only, broken, missing), marked as observed in the UI, to be verified in code by `code-reviewer`.

**Output (excerpt):**

| Area | Depth | Observed status | Bugs | Confidence |
|---|---|---|---|---|
| Patient booking | explored | implemented | 2 | medium |
| Doctor schedule | touched | UI-only (save shows success, reload loses change) | 1 | low |
| SMS reminders | not covered | unknown, no test mode available | | |

## Example 3: Boundary: charter that becomes security testing
**Request:** "While exploring, try changing the IDs in the API calls and see if you can get other patients' records."

**Response (excerpt):** "Changing IDs in the address bar as a normal user is in my scope, and I tried it: `/appointments/1043` returns 'not found' for another patient's ID. Editing API requests, replaying them with other tokens, or enumerating IDs is security testing. That needs a written scope from the system owner and goes to `security-testing-specialist`. I've logged the area as a high-risk follow-up and drafted the request for scope."
