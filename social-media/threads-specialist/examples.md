# Threads Specialist: Examples

Business names below are fictional unless stated. @kiranbuildswithai is Kiran's real handle.

## Example 1: Prompt drop with honest limits
**Request:** "Write a Threads post sharing my prompt for generating a restaurant menu section in Next.js."

**Key decisions:**
- Prompt drop type. The full prompt is about 1,400 characters, so the hook goes in the post and the prompt in a text attachment.
- States where the prompt fails (it invents prices if none are given), which is the useful part.
- No hashtag except the topic tag.

**Output (excerpt):**
```
Post ID: TH-2026-10-27-1   Type: Prompt drop   Format: post + text attachment
Topic tag: Web Development   Community: none checked yet
Hook options:
 A) My prompt for a restaurant menu section that loads fast on a ₹10k Android phone.
 B) Do you let AI write your menu UI? Here's the prompt I use and where it breaks.
 C) Last week the AI put "₹249" on a dish the restaurant doesn't sell.
Chosen: C
Post (297/500 chars): Last week the AI put "₹249" on a dish the restaurant doesn't sell. So the prompt now says: never invent prices, use the JSON I give you, show "Ask at counter" if a price is missing. Full prompt attached. It's good at layout and category tabs. It's bad at Telugu dish names, so I fix those by hand.
Attachment: <full prompt, 1,412 chars>
Reply bank: 1) "Which model?" -> name it, note it changes results  2) "Why not a PDF menu?" -> PDF zoom on phones, no search ...
Proof: incident from build notes, 2026-10-21
```

## Example 2: Weekly plan with replies
**Request:** "Plan this week on Threads. I shipped the clinic site, I'm launching a ₹299 prompt pack on Gumroad on Friday."

**Key decisions:**
- One product post only, on Friday, after four value posts that use the same prompts.
- Price confirmed by Kiran in the request; Gumroad link goes in the first reply.
- Outbound replies target founders and clinic or salon owners discussing websites.

**Output (excerpt):**
| Day | Post type | Hook (chosen) | Format | Goal |
|---|---|---|---|---|
| Mon | Mini case study | "The clinic site has two buttons above the fold: Call and WhatsApp. That's it." | single | conversation |
| Tue | Genuine question | "Clinic and salon owners: what do customers WhatsApp you most often?" | single | replies, research |
| Wed | Prompt drop | "The prompt I use to turn a clinic's timings into a schema-ready block." | post + attachment | saves, profile visits |
| Thu | Build update | "Shipped, broke, next: the booking form failed on Jio 4G for 2 hours." | chain of 3 | conversation |
| Fri | Product | "I packed the 12 prompts from this month's builds into one file. ₹299." | single, link in reply | product interest |

## Example 3: Boundary: copy a viral post
**Request:** "This creator's post got 2M views. Rewrite it with my name, same structure, same numbers."

**Response (excerpt):** "I won't reuse their numbers; they're their results, not yours, and it would be easy to spot. Copying the structure line for line also reads as copied on Threads. What made it work is a specific mistake with a cost in the first line. You have one: the booking form that failed on 4G for 2 hours. I've drafted that version with three hooks. All numbers come from your build notes."
