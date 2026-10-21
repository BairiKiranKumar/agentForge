# Conversion Designer: Examples

Business names below are fictional unless stated.

## Example 1: Admissions landing page for Instagram ads
**Request:** "Sri Vidya High School (fictional) is running Instagram ads for 'Admissions open for 2027-28, book a campus visit'. Design the landing page."

**Key decisions:**
- Primary action: Book a visit (form, 3 fields: parent name, mobile, class applying for). Secondary: WhatsApp the office. Prospectus download is a text link lower down.
- Headline slot repeats the ad promise: admissions open plus campus visit.
- Trust cue above the fold: the school's Google rating as shown on its profile on the capture date, linked; no rounding.
- FAQ answers the questions the office says parents ask: fee range, transport routes, medium of instruction, timings.

**Output (excerpt):**
```
## Outline: admissions-2027
| # | Section | Job | Proof used | CTA |
|---|---|---|---|---|
| 1 | Hero (360 px: headline, area, CTA, rating) | Match ad promise | Google rating x.x (n reviews, captured 2026-10-20) | Book a visit (primary) |
| 2 | Visit in 3 steps | Remove uncertainty | - | - |
| 3 | Campus photos (owned) | Show the real place | 6 owner photos | Book a visit |
| 4 | Fees and transport | Answer cost question | Fee range supplied by school | - |
| 5 | FAQ (6 real questions) | Objections | Office's list | Book a visit, WhatsApp |
Form: Parent name | Mobile (+91 ok, 10 digits) | Class applying for (chips Nursery to Class 5)
Purpose line: "The office will call you within one working day to fix a visit time." + privacy notice link (wording: privacy-specialist)
Events: cta_book_tap, form_start, form_submit, whatsapp_tap, call_tap
```

## Example 2: Audit of a clinic page with low calls
**Request:** "Sunrise Dental (fictional) gets traffic from Google search but few calls. Audit the page."

**Key decisions:**
- Got 30 days of data: about 640 sessions and 11 call taps [figures supplied by client export]. Under the 1,000-session threshold, so ranking is first-principles, not statistical.
- The phone number sits in the footer; the hero is a slider with three images; timings are only in an image.

**Output (excerpt):**
```
Verdict: The page hides the action that search visitors want (call now). Offer and audience look fine.
Fix now:
1. Hero | no call button above fold at 360 px -> add Call (primary) and WhatsApp (secondary) in first screen | S | high
2. Hero slider | delays LCP and hides message -> single static photo of the clinic | S | high
3. Timings | image of text, not readable or searchable -> HTML timings with "Open now" logic | S | med
4. Mobile | no sticky contact -> bottom bar Call / WhatsApp / Directions | S | med
Not a problem: services list, doctor profile section
Could not check: call-tracking accuracy (no event on tel: links) -> web-analytics-specialist
```

## Example 3: Pushback: fake urgency and borrowed ratings
**Request:** "Add a countdown timer saying 'Offer ends in 2 hours' that resets for every visitor, and show '4.9 stars, 1,000+ happy customers'. The salon is new, so just use a number that looks good."

**Response (excerpt):** "I won't design a resetting countdown or a rating the salon doesn't have. Both mislead customers, are the kind of dark pattern Indian consumer regulators have issued guidance on [verify current guidance], and the salon would lose trust the first time someone checks Google. Options that still create a reason to act: a real launch offer with a real end date ('Opening offer till 30 November'), an honest new-salon cue ('Opened October 2026, book your first visit'), and photos of the stylists' real work with their consent. When reviews come in, we show the exact rating and count with the date."
