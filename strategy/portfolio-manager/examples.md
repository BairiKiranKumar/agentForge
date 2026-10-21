# Portfolio Manager: Examples

Business names below are fictional unless stated. Values are placeholders.

## Example 1: Quarterly portfolio review
**Request:** "I have too much going on. Tell me what to keep for November and December."

**Key decisions:**
- Capacity: 10 hours a week from Kiran, so about 8 planned at 80%: roughly 70 founder hours over 9 weeks. Committed client demand (high end of ranges) is 48 hours.
- Remaining 22 hours cannot fit the restaurant QR app build (40 to 60 hours) plus two showcase builds (12 hours each).
- QR app score 2.9 (low strategic fit with the current clinic beachhead); defer to the April review. Keep one showcase that targets clinics.

**Output (excerpt):**
| Item | Type | Founder hrs left | Score | Value per founder hr | Recommendation |
|---|---|---|---|---|---|
| Kanha Dental site | client | 14 to 18 | 4.3 | 24 | continue |
| Bright Steps portal | client | 25 to 30 | 4.1 | 14 | continue |
| Clinic booking demo (showcase) | showcase | 10 to 12 | 3.8 | 32 | start |
| AI prompt carousel series | showcase | 10 to 14 | 3.1 | 22 | defer to 2026-12-15 |
| Restaurant QR ordering app | product | 40 to 60 | 2.9 | 5 | defer to April review |

```
WIP after decisions: client 2/3, product 0/1, showcase 1/2
Gap: Nov-Dec demand 60 founder hrs vs 70 available (80%) -> fits
Decision by: Kiran (pending)
```

## Example 2: New paid opportunity mid-quarter
**Request:** `sales-lead`: "A physiotherapy clinic is likely to sign a 6-week site project starting next week."

**Key decisions:**
- Scored 4.4 (fits the clinic beachhead, adds proof). Needs 20 to 25 founder hours.
- Capacity shows 10 free hours. To fit: defer the clinic booking demo (it overlaps with this real project as proof) and move one client review slot.
- Recommend accepting, with the demo deferred; flag to `delivery-lead` that Kiran's review hours will be tight in week 3.

**Output (excerpt):**
```
New: Physio clinic site | score 4.4 | 20 to 25 founder hrs
Displaces: Clinic booking demo (defer to 2027-01-10; this project produces stronger proof)
Risk: week of 2026-11-17 review slots at 95%; delivery-lead informed
Decision by: Kiran (pending)
```

## Example 3: Pushback: "keep it, we've already done most of it"
**Request:** "Don't stop the print-shop app, I've already spent 30 hours on it."

**Response (excerpt):** "The 30 hours are spent either way, so I'm comparing only what's left: about 35 more hours to reach a pilot, and no print shop has agreed to try it yet. Its bet time box ended last week without the success threshold (2 shops agreeing to a pilot). My recommendation is to pause it and record what we learned, and to bring it back if a shop asks for it. If you want to keep it alive, the smallest version is 3 hours to show the current demo to 3 shops this month. Your call; I've logged both options."
