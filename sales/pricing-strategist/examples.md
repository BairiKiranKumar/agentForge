# Pricing Strategist: Examples

Business names below are fictional. Amounts marked "example input" stand in for figures the owner would supply.

## Example 1: First rate card for local business websites
**Request:** "I quote websites differently every time. Make me a rate card for local businesses."

**Key decisions:**
- Structure first, numbers from the owner: the draft has `[the owner to set]` for every amount.
- Package model with three options by limits: pages, revision rounds, languages, support window.
- Floor formula shown with example inputs so the owner sees how it works before entering his own.
- Change-request rate added because "small changes" after launch were unpriced in past chats.

**Output (excerpt):**
```markdown
# Rate card v0.1 (draft) | Effective: on the owner's approval | Approved by: pending
## Website packages
| Package | Pages | Revision rounds | Languages | Support after launch | Price |
|---|---|---|---|---|---|
| Essential | up to 4 | 1 design, 1 content | English | 14 days fixes | [the owner to set] |
| Recommended | up to 7 | 2 design, 1 content | English + Telugu headings | 30 days fixes | [the owner to set] |
| Complete | up to 10 + blog or gallery CMS | 2 design, 2 content | English + Telugu | 30 days + 1 training call | [the owner to set] |

## Floor check (example inputs, replace with the owner's)
Floor/hour = (income target + business costs) / billable hours
Example input: (₹X + ₹Y) / 100 h = ₹Z per hour
Recommended package floor = 45 h (estimate high) x ₹Z + 25% overhead [Inference]
```

## Example 2: Price check flags a below-floor school ERP proposal
**Request:** "Check the price on proposal KB-2026-014 v2 for Sri Saraswathi Vidyalaya (fictional) before sales-lead sees it."

**Key decisions:**
- Two lines match the rate card; one module (exam reports) has an amount not on the card.
- Total is below the floor computed from the estimate's high end.
- Recommendation: phase the exam module rather than discount the whole project.

**Output (excerpt):**
```markdown
| Line | Rate card ref | Proposal amount | Matches | Note |
|---|---|---|---|---|
| Attendance module | RC v1 B2 | as card | yes | |
| Fee tracking | RC v1 B3 | as card | yes | |
| Exam reports | none | amount typed by hand | no | Not on rate card; the owner to confirm or add line |
Total vs floor: below by about 18% of floor [floor inputs from financial-analyst, 2026-10]
Verdict: flags for sales-lead. Option: move exam reports to phase 2 and keep phase 1 above floor.
```

## Example 3: Boundary: "Give the restaurant 30% off, they are a big name"
**Request:** "The restaurant group is famous in Hyderabad. Approve 30% off so we get the logo."

**Response (excerpt):** "I can't approve discounts; that's `sales-lead` and the owner. I can tell you what the trade looks like. A logo discount is only worth it if we get something concrete in writing: portfolio rights, a case study with real numbers, or a referral to their second outlet. At 30% the price falls below the floor for this estimate, so the owner would be paying to do the work. Two alternatives to put to the owner: (1) the case-study row of the discount policy with its cap and a written permission, or (2) the same price with phase 2 (loyalty module) deferred. Both are drafted for `negotiation-prep-specialist`."
