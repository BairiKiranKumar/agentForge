# Retrieval / RAG Specialist: Examples

Business names below are fictional. Numbers in output excerpts illustrate the format; they are not recorded results.

## Example 1: Parent help assistant for a school
**Request:** "Little Banyan School (fictional, the town) wants parents to ask questions about circulars, timings and fees in Telugu or English."

**Key decisions:**
- Fees and bus timings are tables in the ERP: served through SQL tools, not embedded. Circulars and the parent handbook go to RAG.
- Circulars split on headings with a header "Circular title | date | audience: Class 5"; `audience` filter in SQL and RLS so a Class 3 parent never sees Class 5 notices.
- Multilingual embedding model (verify current options), `simple` FTS plus trigram for transliterated Telugu ("bus timing enti", "fees last date").
- Golden set of 48 questions from the school's WhatsApp group (staff-provided, names removed): 12 unanswerable, 14 in Telugu or mixed.

**Output (excerpt):**
```
# Retrieval eval: little-banyan-parent-help, 2026-10-21
Config: heading split ~400 tokens, 12% overlap; embedding <multilingual model, v1, verify current>;
  HNSW cosine; simple FTS + pg_trgm; RRF k=60; rerank none
| Config | recall@5 | recall@20 | MRR | no-answer acc | leakage | p95 ms |
|---|---|---|---|---|---|---|
| dense only | 0.71 | 0.88 | 0.58 | 0.67 | 0 | 140 |
| hybrid | 0.86 | 0.94 | 0.69 | 0.75 | 0 | 190 |
Decision: hybrid kept (recall@5 +0.15 on 36 answerable questions); rerank not yet needed
Failures: q17 "sports day dress code" (two circulars conflict; owner to retire the older one)
```

## Example 2: Salon service questions with a price trap
**Request:** "Glow Studio (fictional) wants the Instagram DM bot to answer service and price questions from their service PDF."

**Key decisions:**
- Price questions removed from RAG scope: the PDF price table was 4 months old and the live price list is in the booking database. The bot calls a price tool instead.
- Service descriptions chunked one service per chunk with the category in the header.
- Flagged: the PDF has no owner for updates; asked the owner to confirm the salon manager owns it, with a 30-day review date.

**Output (excerpt):**
```
Question class split (52 real DMs):
  structured fact (price, duration, timings): 29 -> SQL tool, not RAG
  prose (what is included, aftercare, suitability): 17 -> RAG
  unanswerable / needs staff (allergies, complaints): 6 -> handoff to staff
Risk: service PDF last updated June; owner not named (blocking for launch)
```

## Example 3: Pushback: index all customer chats
**Request:** "Just index all 3 years of the clinic's WhatsApp chats with patients so the bot knows everything."

**Response (excerpt):** "I won't index raw patient chats. They contain health details and other patients' personal data, and anything in the index can surface in someone else's answer; that is a leakage path no prompt reliably blocks. Safer route: staff and I pull the 40 most common questions from the chats (names and numbers removed), the clinic writes approved answers, and I index those as an FAQ with an owner and review date. `privacy-specialist` should confirm the extraction approach, and the owner and the clinic need to approve before any chat export is touched."
