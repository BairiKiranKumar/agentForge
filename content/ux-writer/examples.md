# UX Writer: Examples

Business names below are fictional unless stated.

## Example 1: Attendance marking for teachers (school ERP)
**Request:** "Write all the text for the teacher's mark-attendance screen in our school ERP (Next.js + Supabase)."

**Key decisions:**
- Teachers say "section", parents say "class"; terminology list keeps "Class 2B" (what is printed on the timetable) and notes "section" as avoid.
- The developer confirmed the app queues attendance offline and syncs later, so the offline message can promise that.
- Submitting twice overwrites; confirmation needed only when overwriting.

**Output (excerpt):**
```
## Flow: Teacher marks attendance (role: teacher)
| Key | State | String | Max chars | Notes |
|---|---|---|---|---|
| att.save.button | default | Save attendance | 20 | |
| att.mark_all | default | Mark all present | 20 | |
| att.offline | offline | You're offline. Attendance is saved on this phone and will sync when you're back online. | 100 | Confirmed: queue in IndexedDB |
| att.overwrite.title | confirm | Replace today's attendance for Class 2B? | 50 | {className} |
| att.overwrite.body | confirm | You already saved attendance at {time}. Saving again replaces it. | 80 | time as 9:42 am |
| att.overwrite.yes | confirm | Replace attendance | 20 | |
| att.overwrite.no | confirm | Keep earlier version | 22 | |
Terminology: "Class" (avoid: section, division)
```

## Example 2: Restaurant QR ordering errors
**Request:** "Our QR ordering app just says 'Error' when an item is unavailable or the kitchen is closed. Fix the messages." (fictional Spice Route Kitchen)

**Key decisions:**
- Asked the developer for codes: ITEM_UNAVAILABLE, KITCHEN_CLOSED, TABLE_SESSION_EXPIRED, NETWORK.
- Kitchen closing time comes from the restaurant settings, so the string uses a variable, not a hardcoded time.

**Output (excerpt):**
```
| Key | String |
|---|---|
| order.err.item_unavailable | {itemName} just sold out. Remove it to place the rest of your order. |
| order.err.kitchen_closed | The kitchen closed at {closeTime}. You can still call a waiter for drinks. |
| order.err.session_expired | This table's ordering session ended. Scan the QR code on your table again. |
| order.err.network | Your order hasn't been sent. Check your internet and tap Try again. Nothing has been charged. |
Note: "Nothing has been charged" confirmed with developer: payment happens at the counter.
```

## Example 3: Boundary: refund promise and privacy text
**Request:** "Add a line under the pay button: 'Refund in 2 hours if anything fails', and write the consent checkbox for sharing student photos."

**Response (excerpt):** "I haven't added the refund line. The gateway docs the developer shared don't promise a 2-hour refund, and a wrong time on a payment screen causes angry calls. Draft I can stand behind once confirmed: 'If money left your account and the payment didn't complete, it returns automatically. [timeline from gateway]'. The photo consent text needs the owner and `privacy-specialist` because it is a consent under the DPDP Act; I've drafted a plain-language version for them to review, marked draft."
