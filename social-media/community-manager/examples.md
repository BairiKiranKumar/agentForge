# Community Manager: Examples

Business names below are fictional unless stated. @kiranbuildswithai is Kiran's real handle.

## Example 1: Mixed inbox after a viral-ish carousel
**Request:** "My Instagram carousel on the restaurant QR menu build got lots of comments. Here are 14 comments and 5 DMs. Draft replies."

**Key decisions:**
- Two comments meet the lead rule: one asks "how much for my cafe in Kamareddy?" (hard signal), one says "we are opening a second branch next month, can this do table ordering?" (hard signal).
- One DM is a fake "brand collaboration" asking for a login link: categorized as scam, recommend block and report.
- A Telugu comment gets a Telugu reply.
- Pricing questions move to DM; no figure in public.

**Output (excerpt):**
| # | Platform | From | Category | Their words | Draft reply | Needs confirmation | Route to |
|---|---|---|---|---|---|---|---|
| 3 | Instagram | @cafe_kmr (fictional) | Lead | "how much for my cafe in Kamareddy?" | "Thanks for asking. It depends on menu size and whether you want table ordering or only a menu. I've sent you a DM with two quick questions so I can give you a proper answer." | DM questions only, no price | `lead-qualification-specialist` |
| 7 | Instagram | @ravi.designs (fictional) | Question | "which font is this?" | "It's Inter for the menu items and a serif for headings so prices stay readable on small phones. Slide 4 shows the size we settled on." | none | none |
| 9 | Instagram | (Telugu comment) | Praise | "చాలా బాగుంది అన్నా" | "థాంక్యూ! మెనూ లోడింగ్ వేగం కోసమే ఎక్కువ టైం పెట్టాం, అది మీకు నచ్చినందుకు సంతోషం." | none | none |
| 12 | DM | "Brand Collab Team" | Spam/scam | "log in here to claim your collab" | none | none | Recommend block and report (impersonation, phishing link) |

## Example 2: Complaint on a client's salon account
**Request:** "A customer commented on Glow Studio's (fictional) Reel: 'Booked through your website, nobody called back, wasted my Sunday.' Draft a response."

**Key decisions:**
- Complaint, so escalate to Kiran and the salon owner within the hour; the public reply only acknowledges and moves private.
- No admission about website fault until the cause is known; the issue also goes to `support-triage-specialist` to check whether booking notifications failed.

**Output (excerpt):**
```
Public reply draft: "Really sorry about your Sunday, that should not have happened. We've sent you a DM so we can sort this out today."
DM draft: "Hi, this is Glow Studio. Could you share the name and phone number you booked with and the time? We'll check what went wrong and call you back today."
Escalation: to Kiran and salon owner, 2026-10-20 11:40 IST, thread link attached
Support handoff: possible booking notification failure, check form submissions for 2026-10-18
```

## Example 3: Boundary: "reply to everyone and say 20% off"
**Request:** "Reply to all the comments and DMs yourself, tell everyone we have 20% off website packages this week."

**Response (excerpt):** "I can't send replies myself, and I don't have a 20% offer in the rate card notes, so I haven't put a discount into any draft. I've drafted replies for all 19 items without the offer. If you confirm the offer (which packages, end date), I'll add one line to the 6 lead replies only, since a discount in reply to a praise comment reads like spam. You'll need to send them from the app."
