# Ideal Customer Profile Researcher: Examples

Business names below are fictional.

## Example 1: First ICP from seven past clients
**Request:** "Write our ICP for local business websites. Here are my seven past clients." the owner pasted a table: 3 schools, 2 salons, 1 restaurant, 1 boutique, with area, source, payment notes and revision counts.

**Key decisions:**
- n = 7, so the profile is labelled judgment-based. The four-signal ranking still runs to show direction.
- The top three (two schools and one salon) all came by referral, paid milestones on time and had 2 revision rounds or fewer. The restaurant (aggregator-heavy, asked for 6 revisions) and the boutique (paid 40 days late) were the bottom group.
- Schools become the beachhead: highest pain (admissions season April to June), two portfolio pieces, dense referral network among school owners in the town.
- "60 or more Google reviews" is kept as a starting size proxy but marked `[Inference]`.

**Output (excerpt):**
```markdown
# ICP v1 (2026-10-20), approved by: pending
Evidence base: 7 paying clients, 0 recorded losses. Judgment-based, n = 7

## Profile A: Private K-12 schools, the town and Hyderabad
Statement: Private CBSE or state-board schools with an active admissions push and no working website on mobile.
| Criterion | Pass if | Check on | Confidence |
|---|---|---|---|
| Type | Private K-12 school | Maps category, signage | High |
| Activity | Instagram or Facebook post in last 30 days | Public profile | High |
| Digital gap | No site, or site fails on a mid-range Android phone | Exact-name search, phone check | High |
| Size proxy | 60+ Google reviews or 2+ branches | Google Business Profile | Low [Inference] |
| Geography | Within the town or Hyderabad | Address | High |
Triggers: admissions campaign | Jan to Jun | "Admissions open" posts and banners
Hard disqualifiers: no activity in 12 months; reachable only via a personal number; group school whose site is run by head office
Proof the owner can show: two school sites (Example School A, Example School B)
```

## Example 2: Separating a B2B product profile
**Request:** "Add product companies to the ICP, I want more React contract work."

**Key decisions:**
- A separate Profile B, so review counts and presence audits do not apply.
- Criteria: startup or SME with a live web product, frontend in React, Next.js or Angular (visible from job posts or public tech pages), currently hiring a frontend role, founder or engineering lead reachable on a public channel.
- Hiring a frontend role is the trigger and the budget signal; posts older than 60 days are treated as stale.

**Output (excerpt):**
```markdown
## Profile B: Product companies needing frontend capacity
| Criterion | Pass if | Check on | Confidence |
|---|---|---|---|
| Live web product | Public app or product site | Website | High |
| Stack match | React, Next.js or Angular | Job post or careers page | Medium |
| Budget signal | Frontend role posted in last 60 days | Job boards, careers page | Medium |
Hard disqualifiers: requires full-time relocation; agency reselling to its own clients without disclosure
```

## Example 3: Pushback on profiling owners personally
**Request:** "Make the ICP owners who are young, from our community, and recently got married, they spend more."

**Response (excerpt):** "I won't build segments on community, age or family events. Those are personal traits, not business attributes, and using them to target people is a privacy and fairness problem under India's DPDP Act, 2023 and our outreach rules. What I can do is capture the business signal you are probably reaching for: businesses that are investing right now. Observable versions: opened in the last 12 months, new branch, rebrand or new menu posted, active ad or offer posts. I've added these as triggers in Profile A, marked `[Inference]` until your wins confirm them."
