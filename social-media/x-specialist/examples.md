# X (Twitter) Specialist: Examples

Business names below are fictional unless stated. @example_brand is the owner's real handle.

## Example 1: Build breakdown thread with code
**Request:** "Turn my notes on making the restaurant QR menu fast on 4G into an X thread."

**Key decisions:**
- How-to with steps, so a thread of 7 posts. Standard account, 280 characters each.
- Code shown as images with the code in alt text; the repo link goes in the first reply.
- Numbers from the owner's own throttled test (Chrome DevTools "Fast 4G" profile, 2026-10-18).

**Output (excerpt):**
```
ID: X-2026-10-29-1   Format: thread (7)   Tier: standard
Opening A: A restaurant's QR menu should open before the customer gives up and asks the waiter. Mine went from 6.2 s to 1.8 s on throttled 4G. 6 changes:
Opening B: Most QR menus in Indian restaurants are a 4 MB PDF. Here's how I built one that opens in under 2 s on a ₹10k phone.
1/ A restaurant's QR menu should open before the customer gives up and asks the waiter. Mine went from 6.2 s to 1.8 s on throttled 4G. 6 changes: (142/280)
2/ Setup: Next.js, Supabase for menu data, tested in Chrome DevTools on "Fast 4G" with CPU 4x slowdown. (100/280)
3/ 1. Menu data at build time, revalidated when the owner edits it. No client fetch on first load. [code image] (108/280)
...
7/ If you build for local businesses, test on the slowest phone in the room, not your laptop. I post these breakdowns every week. (126/280)
First reply: repo link (demo branch, no client data)
Media: 3 code images, alt text contains the code
Proof: build notes, DevTools runs on 2026-10-18
```

## Example 2: Timely commentary
**Request:** "A big AI coding tool just shipped a new feature. Write something about it, everyone's posting."

**Key decisions:**
- The owner tried it for 40 minutes on the school portal repo and found it handled Telugu labels badly; that is the basis.
- Quote post on the official announcement with one specific observation; no claims about speed or benchmarks.

**Output (excerpt):**
```
ID: X-2026-10-30-2   Format: quote post   Tier: standard
Timely basis: The owner tested on the school portal repo, 2026-10-30, 40 minutes
1/ Tried this on a Next.js school portal for 40 minutes. Good at splitting a 600-line form into components. It rewrote Telugu labels into English transliteration twice. If you build bilingual UIs, review every string it touches. (225/280)
```

## Example 3: Boundary: growth hack and benchmark claim
**Request:** "Post that this tool is '10x faster than Copilot' and join a follow-for-follow group so we hit 5k by December."

**Response (excerpt):** "I can't write '10x faster' because you haven't benchmarked it and anyone can ask for the numbers. Follow-for-follow groups bring followers who never read your posts and can get an account flagged for inauthentic behaviour, so I won't plan that either. What I can do: a post with your actual 40-minute test notes, and a reply plan for 15 conversations a day in AI coding and frontend circles. I'll review follows weekly against your current median."
