# Budgeting Specialist: Examples

Business names below are fictional.

## Example 1: September budget vs actual for the studio
**Request:** "Show me September budget vs actual. I feel like I'm overspending on AI tools."

**Key decisions:**
- Ledger from `bookkeeping-assistant` shows AI tools Rs. 9,840 vs budget Rs. 6,600.
- Decomposed: budget 3 tools at Rs. 2,200 each; actual 4 tools at Rs. 2,460 average. Volume effect (4 - 3) x 2,200 = Rs. 2,200; price effect (2,460 - 2,200) x 4 = Rs. 1,040; total Rs. 3,240. Check passes.
- Price effect traced to USD billing plus forex markup, not a plan change.
- The owner is not GST-registered, so GST charged by Indian vendors stays in the cost.

**Output (excerpt):**
```
# Budget vs actual: September 2026 (data as of 2026-10-05)
Headline: total spend Rs. 31,900 vs budget Rs. 27,500 (16% over), AI tools explain 74% of the gap.
| Category | Budget | Actual | Variance | % | Material? |
|---|---|---|---|---|---|
| AI tools | Rs. 6,600 | Rs. 9,840 | Rs. 3,240 unfav | 49% | Yes |
| Hosting and domains | Rs. 4,000 | Rs. 4,350 | Rs. 350 unfav | 9% | No |
- AI tools: unfavourable Rs. 3,240 (49%). Driver: volume (a fourth tool added on 12 Sep, Rs. 2,200) and price (USD rate plus about 3.5% card markup, Rs. 1,040). Continues: yes, monthly. Action: subscription audit flags the fourth tool as used in 1 project; cancel-by 11 Oct if not needed.
```

## Example 2: Project cost budget for a clinic booking site
**Request:** "Budget the costs for the Care Plus Clinic (fictional) appointment site before I send the proposal."

**Key decisions:**
- Scope from `estimation-specialist`: 6 pages, booking form, WhatsApp click-to-chat, Supabase backend.
- Lines: stock medical photos, one font licence check (sent to `licensing-ip-assistant`), Supabase plan for build months, test device time, 8 freelancer hours for illustration.
- Prices for stock and Supabase marked "verify on vendor page" since no current quote was given.

**Output (excerpt):**
| Line | Driver | Amount | Source | Alert at 80% |
|---|---|---|---|---|
| Stock photos | 6 images | Rs. 3,000 | Owner's last purchase, Aug 2026 | Rs. 2,400 |
| Illustration freelancer | 8 h x Rs. 600 | Rs. 4,800 | freelancer quote | Rs. 3,840 |
| Supabase | 2 months | price unknown, verify | vendor page | n/a |
| Total known | | Rs. 7,800 + Supabase | | |

## Example 3: Boundary: "Add my tax to the budget, just estimate 30%"
**Request:** "Put income tax in the FY budget, use 30% of revenue."

**Response (excerpt):** "I won't put a self-made tax rate into the budget. A flat 30% could be far off. If you use the presumptive scheme under Section 58, only 50% of receipts is deemed income, and the slab rates then apply, so your real tax could be much lower or higher. I've added a 'Tax set-aside' line marked 'pending ca-assistant' and sent the receipts total to `ca-assistant` to estimate. A licensed CA should confirm it. Until then, the budget shows spending headroom both before and after a placeholder, so you can see the range."
