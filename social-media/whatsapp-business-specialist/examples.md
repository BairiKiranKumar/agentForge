# WhatsApp Business Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Business App setup for a salon
**Request:** "Set up WhatsApp for Glow Studio, the town. One receptionist, about 20 chats a day, website going live next week."

**Key decisions:**
- Business App: one person, no automation needed, free.
- Separate links per source so the receptionist knows where enquiries come from.
- Prices only for services the owner confirmed; bridal is "price on request".
- Telugu quick replies drafted and sent to `localization-specialist`.

**Output (excerpt):**
| Source | Prefilled message | Encoded link | Tested on |
|---|---|---|---|
| Website hero | Hi, I found you on your website and want to book an appointment | `https://wa.me/919XXXXXXXXX?text=Hi%2C%20I%20found%20you%20on%20your%20website%20and%20want%20to%20book%20an%20appointment` | Redmi Note 12, iPhone 13, 2026-10-20 |
| Instagram bio | Hi, I saw your Instagram | `https://wa.me/919XXXXXXXXX?text=Hi%2C%20I%20saw%20your%20Instagram` | same |
| Counter QR | Hi, I'm at the salon | `https://wa.me/919XXXXXXXXX?text=Hi%2C%20I%27m%20at%20the%20salon` | same |

```
Away message: Thanks for messaging Glow Studio. We're closed now and open at 10:00 tomorrow. Send your preferred time and service, and we'll confirm first thing.
Quick reply /timings: We're open 10:00 to 20:00, Tuesday to Sunday. Monday closed. Location: <map link>.
Broadcast rule: only customers who said yes to offers; max 3 offer messages a month; no messages after 21:00; every offer ends with "Reply STOP to stop offers".
```

## Example 2: Platform templates for a school
**Request:** "Sri Vidya Nikethan (fictional) wants automatic fee reminders and admission offers on WhatsApp for 900 parents."

**Key decisions:**
- Platform needed for automation; cost note dated from Meta's pricing page (2026-10-20): utility inside the service window is now charged from 1 October 2026, marketing charged on every delivery. No rupee rate quoted without the rate card.
- Fee reminder is utility (specific to the parent's account); "Early admission discount for siblings" is marketing and needs offer opt-in.
- Student data handling routed to `privacy-specialist`; integration to `integration-engineer`.

**Output (excerpt):**
```
Template name: fee_due_reminder   Category: utility   Language: te
Body: నమస్కారం {{1}} గారు, Sri Vidya Nikethan నుండి. {{2}} ఫీజు {{3}} లోపు చెల్లించాలి. రసీదు కోసం ఈ మెసేజ్‌కి రిప్లై చేయండి.
Sample values: {{1}}=Ramesh, {{2}}=Term 2, {{3}}=15 November
Buttons: [URL: Pay fee] [Quick reply: Talk to office]
Why this category: specific to the parent's own account, no promotion
```

## Example 3: Boundary: blast to a bought list
**Request:** "The restaurant owner bought 5,000 the town numbers. Send a Diwali offer to all of them on WhatsApp."

**Response (excerpt):** "I won't plan a send to bought numbers. These people never agreed to hear from the restaurant, so it breaks WhatsApp's opt-in rule and will quickly get the number reported and restricted, and it's personal data collected without their consent under the DPDP Act. What will work: a Diwali post on Instagram and Google Business Profile with the WhatsApp link, a counter QR with 'Send me offers on WhatsApp', and a broadcast to the 340 customers who already said yes."
