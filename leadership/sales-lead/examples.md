# Sales Lead: Examples

Business names below are fictional unless stated. Prices are placeholders, not the real rate card.

## Example 1: Weekly pipeline review from a Sheet export
**Request:** "Review my pipeline. Export attached."

**Key decisions:**
- 7 open deals: too few for ratios, so deals are listed individually.
- Spice Route Restaurant (fictional) is in "Negotiation" but the only contact is the manager; the owner has not been met. Flag single-threaded; next step is a visit with the owner.
- Kids Kingdom Play School (fictional) has an expected close date two weeks in the past: slipping.

**Output (excerpt):**
```
Week: 2026-10-20 | Target remaining: 3 projects
Open: 7 deals | Forecast: Commit 1 (Kanha Dental: written acceptance, start date 3 Nov) | Best case 2 | Pipeline 4
At-risk deals:
| Deal | Stage | Rs. | Close | Flags | Next step |
| Spice Route | Negotiation | per proposal | 25 Oct | single-threaded (manager only) | Kiran visits owner, Thu |
| Kids Kingdom | Proposal sent | per proposal | 6 Oct | slipping, stale 14 days | Kiran calls principal, Tue |
Data used: Sheet export 2026-10-19; missing: last activity for 2 deals
```

## Example 2: Discount request
**Request:** `account-executive`: "Spice Route wants 20% off the website and ordering setup or they'll go with a freelancer."

**Key decisions:**
- Do not cut price first; offer scope trade: drop the custom loyalty module (moved to phase 2) which brings the price down without discounting the rate card.
- If they insist on price: counter with a smaller discount only in exchange for a larger advance and case study permission. Kiran decides.

**Output (excerpt):**
```
Deal: Spice Route | Requested: 20% discount | Rate card price: per proposal v2
Recommendation: counter
Option A (preferred): remove loyalty module to phase 2; price per rate card for remaining scope
Option B: if Kiran approves a discount, trade for 60% advance and written case-study permission
Margin impact: financial-analyst check requested
Decision: Kiran (pending)
```

## Example 3: Boundary: proposal with invented prices
**Request:** `proposal-specialist` submits a proposal for a clinic with "WhatsApp booking automation: Rs. 12,000" and notes "no rate card line for this, estimated".

**Response (excerpt):** "Returning this proposal. The WhatsApp booking line has no rate card price, and we never quote estimated prices. Also, the BSP's per-conversation fees aren't shown as a separate third-party cost. Next steps: `pricing-strategist` proposes a rate card line for Kiran to approve, `estimation-specialist` gives the effort range, and the proposal comes back with the approved price and a separate line for platform fees (check Meta's current pricing page; it changes)."
