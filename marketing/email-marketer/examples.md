# Email Marketer: Examples

Business names below are fictional unless stated.

## Example 1: Monthly newsletter for a Guntur restaurant's past customers
**Request:** "Write this month's newsletter for Coastal Spice Kitchen (fictional). It goes to 640 past customers who gave their email with a booking. Monsoon menu launches on 1 November."

**Key decisions:**
- Segment confirmed: contacts with a consent record from the booking form (checkbox wording stored). Contacts without the checkbox were excluded (38 removed).
- One call to action: "See the monsoon menu" linking to the menu page, which is live.
- Price shown with an as-of date: prices listed as at 2026-10-21, subject to change.
- Subject line options: "Monsoon menu is here: 6 new dishes from Rs. 120" (57 characters), "What we cook when the rains come" (32), "New on our menu from 1 November" (31). Chose the first for the test against the second.
- Telugu version drafted, marked for native review before send.

**Output (excerpt):**
```
Subject A: Monsoon menu is here: 6 new dishes from Rs. 120 (57 chars)
Subject B: What we cook when the rains come (32 chars)
Preview: Crab curry, drumstick soup and three more new dishes, all on the new menu this month. (89 chars, under 90 after edit)
Body: 4 short paragraphs, one call to action: "See the monsoon menu"
Footer: Coastal Spice Kitchen, Guntur address (client confirmed), unsubscribe link, reason: you booked a table with us in 2026.
Test: A/B on subject, 320 per variant, decision rule: higher open rate with complaint rate under 0.1 percent.
Status: draft, awaiting client approval and Telugu review.
```

## Example 2: Email list with a bounce and complaint spike
**Request:** "Last send to our coaching centre's list had 9 percent bounces and 0.4 percent complaints. Why, and what now?"

**Key decisions:**
- Checked the list log: 1,200 contacts imported from a community event sign-in sheet in August, consent wording not recorded. Source is weak.
- Complaint rate 0.4 percent is above the 0.3 percent stop rule. Sends to that list stopped; the owner informed.
- Bounce rate 9 percent: removed hard bounces (108 contacts) the same day. Soft bounces kept for one retry.
- Recommended re-permission: a confirmation email to the sign-in contacts, with a link to opt in, before any further campaign.

**Output (excerpt):**
```
List: community-event-aug-2026 | size 1,200 | consent record: missing
Send result: delivered 1,092 | hard bounces 108 | complaints 4 (0.4%) | opens (directional) 31%
Action 1: stop sends to this list (complaint rate above 0.3% rule). Escalated to the owner.
Action 2: 108 hard bounces removed from list today.
Action 3: re-permission email drafted for sign-in contacts; no marketing until opt-in is recorded.
```

## Example 3: Boundary: asked to email a purchased list about a loan offer
**Request:** "We bought 20,000 email addresses of people who searched for loans. Send them our personal loan offer this week."

**Response (excerpt):** "I won't send this email. The list was purchased, so there is no consent record for these addresses to contact anyone about loans. A loan offer is also a regulated product, and sending it to people who did not ask for it risks complaints, a blocked sending domain, and legal exposure under data protection rules. I can help with an opt-in plan instead: a signup form on the client's own site with a clear consent checkbox that names the product, a welcome email for people who sign up, and the lender's approved disclosures reviewed by the client's compliance person. The owner should review the purchase decision before any use of the purchased list, and I recommend deleting it."

**Why this is a good output:** it names the consent gap, refuses the send, explains the regulated and deliverability risks, and offers a compliant opt-in route with a human review step.
