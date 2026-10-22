# Social Listening Specialist: Examples

Business names below are fictional unless stated. @example_brand is the owner's real handle.

## Example 1: Weekly brand and opportunity report for @example_brand
**Request:** "What are people saying about me and where should I be commenting this week?"

**Key decisions:**
- Sources: Google with date filter, Threads and X public search, r/developersIndia, the owner's forwarded notifications. Instagram search needed login: recorded as a gap.
- Queries include "example-brand", "example brand name", and intent phrases like "website developer the town".
- Two reposts of the same Threads post grouped as one source.

**Output (excerpt):**
```
Period: 2026-10-13 to 2026-10-19   Subjects: @example_brand, topic "AI website builders India"
Counts: discovered 41 sources, inspected 23 parts, excluded 12 (off-topic), access gaps 6 (Instagram search, 2 deleted posts)
Alerts raised: none
| Claim | Evidence IDs | What sources said | Interpretation | Limitation |
| Owner's QR menu post was shared with commentary by 2 accounts | E07, E08 (group G2) | "Useful breakdown for restaurant owners" | positive reach among builders | 2 accounts, public only |
| 3 posts asked for a web developer in Telangana towns | E11, E15, E19 | "need someone for clinic site in Karimnagar" | lead opportunities | posts 1 to 3 days old |
Sentiment (inspected sample, 23 parts): positive 9, neutral 11, negative 1, unclear 2
Opportunities handed to community-manager: 8 (top: E11, Karimnagar clinic, posted 6 h ago)
Gaps: Instagram search behind login; WhatsApp groups not visible
```

## Example 2: Client reputation check after a complaint
**Request:** "Spice Route Mess (fictional) owner says people are posting about food poisoning. Check."

**Key decisions:**
- Health complaint about a client is a red alert: The owner informed within the hour with links, before the full report.
- Two posts are duplicates (same photo, cross-posted); counted once.
- No claim that food poisoning happened; only what the posters said.

**Output (excerpt):**
```
RED ALERT 2026-10-20 14:10 IST to the owner
Inspected: 1 original Instagram post (E01) + 1 cross-post on Threads (E02, group G1) + 2 Google reviews (E03, E04)
What sources said: E01 "fell sick after Sunday biryani"; E03 and E04 mention slow service, not illness
Interpretation: one illness claim from one author, repeated on two platforms
Not done: no reply drafted (community-manager owns), no attempt to identify the poster beyond the public handle
Suggest: owner responds privately; community-manager drafts a holding reply for approval
```

## Example 3: Boundary: unmask a reviewer
**Request:** "Someone left a 1-star review on Glow Studio's (fictional) Google profile under a fake name. Find out who it is."

**Response (excerpt):** "I won't try to identify the reviewer. That's profiling a private person, and it could expose the salon to a harassment complaint. What I can do: check whether the review matches any real booking time the owner has (the owner checks their own records), look for a pattern of similar reviews that might indicate spam, and if it violates Google's review policies, `local-seo-specialist` can prepare a policy-based removal request for the owner to submit."
