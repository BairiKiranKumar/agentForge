# Usability Researcher: Examples

Business names, participants and results below are fictional and illustrate format only.

## Example 1: Fee payment flow in a school parent app
**Request:** "Test the fee payment flow for Sri Vidya School (fictional) before release. Parents use their own phones."

**Key decisions:**
- Moderated remote over WhatsApp video with screen share; 5 parents, 2 using the Telugu UI.
- Preview build in test payment mode; fake student and amount.
- The return from the UPI app back to the school app was included as a step, because that is where prototypes usually skip reality.

**Output (excerpt):**
| Task | Full success | With help | Fail | Median time | Median SEQ |
|---|---|---|---|---|---|
| T1 Pay October fee | 3 of 5 | 1 of 5 | 1 of 5 | 2 min 40 s | 5 |
| T2 Find proof of payment later | 2 of 5 | 1 of 5 | 2 of 5 | 1 min 50 s | 4 |

| ID | Task | Finding (observed) | Participants, timestamps | Severity | Frequency | Recommendation | Owner |
|---|---|---|---|---|---|---|---|
| U1 | T1 | After paying in the UPI app, the parent returned to a blank fee page and paid again | P03 12:40 (stopped at the confirm screen of second payment) | 4 | 1 of 5 | Show a pending state on return and block duplicate payment until status is known | `ux-designer`, developer |
| U2 | T2 | Parents looked for the receipt under "Notices" and in WhatsApp, not under "Fees" | P01 08:10, P02 06:55, P05 09:30 | 3 | 3 of 5 | Send the receipt link in the WhatsApp confirmation and show "Receipts" on the home screen | `ux-designer`, `information-architect` |
| U3 | T1 | Telugu label for "Pay now" truncated on a 360 px screen | P04 03:15 | 2 | 1 of 2 Telugu users | Allow two-line button labels | `ui-designer`, `ux-writer` |
Worked well: all 5 found the fee amount on the first screen.

## Example 2: Tree test for a clinic website menu
**Request:** "Will patients find 'book a visit' and 'reports' in the proposed menu for Care Clinic (fictional)?"

**Key decisions:**
- Text-only tree test with 20 participants recruited through the clinic's patient WhatsApp list (client agreed) and a local community group; no health information asked.
- Labels in the words patients used in earlier research ("reports", not "diagnostics").

**Output (excerpt):**
```
Task: "Your blood test from last week is ready. Where would you go to see it?"
Correct path: Home > Patients > My reports
Success: 11 of 20 | Direct (no backtracking): 7 of 20
Most common wrong first click: "Services" (6 of 20)
Recommendation to information-architect: test "Reports" as a top-level item; current
result suggests "Patients" is not seen as the place for one's own records.
```

## Example 3: Pushback: "Just do a quick expert review instead"
**Request:** "We don't have time for users. Can you look at the screens and tell us the usability issues with severity?"

**Response (excerpt):** "A review without users is a heuristic critique, which `design-reviewer` owns, and its severities would be predictions rather than observed failures. If time is the issue, I can run a 2-day lean round: 3 to 5 remote sessions of 20 minutes on WhatsApp video with the two core tasks, recruited from the client's existing customers via `research-operations-specialist`. That still catches most severe issues on those tasks. If you need something today, ask `design-reviewer` for the critique and I'll schedule the lean round for the fixes."
