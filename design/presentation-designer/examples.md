# Presentation Designer: Examples

Business names below are fictional unless stated.

## Example 1: Website proposal deck for a school principal
**Request:** "Turn the proposal for Sri Vidya High School (fictional) into a deck the owner presents on Google Meet, then sends as a PDF on WhatsApp."

**Key decisions:**
- Two densities: a presented version (12 slides, 24 pt minimum) and a read version (10 slides, 16 pt minimum, with the spoken points written in).
- Titles written as assertions from `proposal-writer`'s narrative; pricing slide is the table from `proposal-specialist`, unchanged.
- Proof uses screenshots of a real school portal the owner built, with the client's permission recorded by `case-study-writer`.

**Output (excerpt):**
```
## Storyline: sri-vidya-website-proposal (presented, 12 slides, 20 minutes)
Audience and decision: principal and correspondent; approve the website project and a start date
Setting: live Google Meet, then PDF on WhatsApp
| # | Assertion title | Pattern | Evidence | Source | Owner of copy |
|---|---|---|---|---|---|
| 1 | Parents decide on admissions from their phones | Big statement + photo of the school gate | School's own photo | School | proposal-writer |
| 2 | Today the fee details and admission form are hard to find on mobile | Before screenshot, 375 px | Current site screenshot, 2026-10-18 | Owner | proposal-writer |
| 3 | A new site puts admissions, fees and contact one tap from the home page | Three-step process | Wireframe from ux-designer | Owner | proposal-writer |
| 9 | The project runs in four stages over the timeline below | Timeline | Milestones from proposal-specialist | proposal-specialist | proposal-specialist |
| 10 | Investment and payment schedule | Table (unchanged) | Pricing table | proposal-specialist | proposal-specialist |
Missing content: approval to show the portal client's name (case-study-writer, by 2026-10-22)
QA: overflow 0, overlaps 0, unique titles yes, alt text 7/7, min font 24 pt, PDF 4.2 MB
```

## Example 2: LinkedIn document carousel from a build
**Request:** "Make a 7-page LinkedIn carousel from the owner's post about building a QR ordering app for restaurants."

**Key decisions:**
- Carousel type: 1080 x 1350 pages, 28 pt minimum, under 25 words per page [platform spec verified on the day before export].
- Hook page uses the real problem, not a stat that was never measured.
- Proof page is a real screenshot of the order screen with test data, no customer names.

**Output (excerpt):**
```
| # | Assertion title | Pattern | Evidence |
|---|---|---|---|
| 1 | Waiters in busy the town restaurants miss orders at peak hours | Hook, big type | Owner's quote, used with permission |
| 2 | Customers scan, order and the kitchen sees it instantly | 3-step process | Diagram |
| 4 | This is the kitchen screen | Screenshot, cropped to order list | Test data screenshot |
| 7 | Want this for your restaurant? Message me | CTA | WhatsApp link text |
```

## Example 3: Pushback: "add some impressive numbers"
**Request:** "The results slide looks empty. Add something like '300% more enquiries' and a few client logos to make it look established."

**Response (excerpt):** "I can't put a number on the slide without data behind it, and I can't add client logos without each client's permission. Both would be seen by the prospect as facts. What I can do: if `marketing-analyst` can pull enquiry counts before and after the salon site launch, I'll chart the real change with the date range and source. If there's no data yet, the slide can show the real before and after screenshots with the owner's quote, which the owner already has permission to use. I've left a labelled placeholder: 'Enquiry data: awaiting marketing-analyst'."
