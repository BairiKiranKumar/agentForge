# Team Orchestrator: Examples

Business names are fictional unless stated.

## Example 1: "Assemble a team to design and build a restaurant ordering product"
**Brief score:** goal 2, deliverables 1 (product unspecified: QR table ordering? delivery?), audience 1, deadline 0, constraints 0, authorization 0 = 4. Ask first.

**Questions sent (with defaults):**
1. Is this QR table ordering inside the restaurant, online delivery, or both? Default: QR table ordering only for v1.
2. Target launch date and one pilot restaurant? Default: 6 weeks, one pilot in Nizamabad.
3. Payments in v1 or pay at counter? Default: pay at counter, UPI later.

**After answers (QR ordering, 6 weeks, pay at counter), workflow:** `workflows/03-product-idea-to-iteration.md` stages 1 to 5.

**Team plan (excerpt):**
| Role | Responsibility | L/C/R | Output | Model |
|---|---|---|---|---|
| product-manager | Problem, scope, success metrics | Lead (product) | PRD | opus |
| customer-interview-specialist | 5 owner and staff interviews | C | Interview notes | sonnet |
| ux-designer | Order and kitchen flows | Lead (design) | Wireframes | sonnet |
| ui-designer | Hi-fi mobile screens | C | Screens | sonnet |
| solution-architect | Architecture, data model | Lead (tech) | ADR | opus |
| nextjs-specialist | Build | C | App | sonnet |
| database-engineer | Schema, RLS | C | Migrations | sonnet |
| playwright-specialist | E2E for order flow | C | Specs | sonnet |
| design-reviewer | Review before build | R | Review | opus |
| code-reviewer | PR reviews | R | Reviews | opus |

10 roles, phased: discovery (3 active), design (3 active), build and test (5 active). Not activated: marketing, sales, payments roles (out of v1 scope).

## Example 2: Small task, small team
**Request:** "Fix the mobile layout of the pricing table on the salon site."

**Decision:** Workflow none needed. Team: `css-specialist` (lead) and `visual-regression-tester` only if a baseline suite exists; no design or QA lead. Two roles, one handoff each way. Acceptance: no horizontal scroll at 375 px, all columns readable, before/after screenshots.

## Example 3: Disagreement and boundary
**Situation:** `conversion-designer` wants a sticky "Book a Visit" bar on mobile; `design-reviewer` rejects it because an approved decision (D-3) says the floating CTA is WhatsApp only.

**Handling:**
1. D-3 is approved by Kiran, so it is closed for this task.
2. Asked `conversion-designer` for evidence. They cite a general CRO article, no data from this site.
3. Decision: keep D-3. Logged the proposal as an idea for a future A/B test, owner `conversion-optimization-specialist`, needing Kiran's approval to reopen D-3.

**Log entry:**
```
D-7 Keep floating CTA as WhatsApp only (D-3 approved by Kiran). Proposal for sticky Book a Visit bar parked as experiment idea EXP-2; requires approval to reopen D-3.
```
