# Manual Tester: Examples

Business names below are fictional unless stated.

## Example 1: Cases for a salon booking form
**Request:** "Write and run test cases for the booking form on Glow Studio's (fictional) site. Criteria: name required, phone 10 digits, date not in the past, max 4 guests, booking confirmation opens WhatsApp with prefilled details."

**Key decisions:**
- Equivalence classes for phone: 10 digits starting 6 to 9 (valid), 9 digits, 11 digits, letters, "+91 98480 12345" with spaces (criteria silent; asked `product-owner`, answer: accept and normalize).
- Boundary for guests: 0, 1, 4, 5.
- WhatsApp case checks the prefilled text on Android Chrome and iOS Safari, but does not send the message.

**Output (excerpt):**
```
TC-BOOK-04: Guests above maximum is rejected
Priority: P1 | Criterion: BOOK-3 (max 4 guests)
Preconditions: Booking page open, no login
Test data: name "Lakshmi P.", phone 9848012345, date tomorrow, guests 5
Steps:
1. Enter test data -> Expected: fields accept input
2. Tap "Book now" -> Expected: error "Up to 4 guests per booking" shown next to guests field; no WhatsApp redirect
Cleanup: none
```

| Case | Build | Device | Result | Defect |
|---|---|---|---|---|
| TC-BOOK-01 | 7d3e2aa | Redmi Note 12, Chrome | Pass | |
| TC-BOOK-04 | 7d3e2aa | Redmi Note 12, Chrome | Fail | BUG-21 |
| TC-BOOK-07 | 7d3e2aa | iPhone 12, Safari | Blocked | WhatsApp not installed on test device |

```
BUG-21: Booking accepts 5 guests and opens WhatsApp
Build/env: 7d3e2aa, preview URL; Redmi Note 12, Android 14, Chrome
Steps (minimal):
1. Open /book, fill valid name, phone, tomorrow's date, guests 5
2. Tap "Book now"
Expected: validation error, no redirect
Actual: WhatsApp opens with "Guests: 5"
Reproduced: 3 of 3
Proposed severity: Medium because the salon can correct by reply, but it breaks a stated rule
```

## Example 2: Regression scope after a shared header change
**Request:** "We changed the shared header component on the school site. Run regression."

**Key decisions:**
- Shared component in the diff, so full regression per the selection table, not just the home page.
- Prioritized P1 cases on pages with the header plus the mobile menu and language toggle (English/Telugu).

**Output (excerpt):** "Full regression on build c19f0b2: 64 cases. 61 Pass, 2 Fail (BUG-30 Telugu menu items overflow at 360 px, BUG-31 'Admissions' link goes to old URL), 1 Blocked (contact form, staging email service down). Not run: none."

## Example 3: Boundary: asked to sign off without running
**Request:** "Regression passed last week and the change is tiny. Just mark today's run as passed."

**Response (excerpt):** "I can't mark cases Pass on build 2be81d4 without running them; last week's results were on a different build. The change touches the fee summary component, which the selection table puts in targeted scope: 14 cases, about 40 minutes. I can run those now and mark the other 50 as Not run with the reason 'outside change scope', so the log stays honest."
