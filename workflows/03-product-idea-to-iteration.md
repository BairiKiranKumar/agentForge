# WF-03: Product Idea to Iteration

Product idea, validation, MVP, launch, measurement, iteration.

## Entry requirements
- An idea statement: who has what problem, and why now.
- Constraints: time, budget, tech preferences.
- Authorization: spending (ads, paid tools), launch announcements and outreach need approval.

## Roles
`product-manager` (lead), `market-researcher`, `competitor-researcher`, `customer-interview-specialist`, `research-synthesis-specialist`, `business-strategist`, `pricing-strategist`, `ux-designer`, `ui-designer`, `solution-architect`, developers, `qa-lead`, `marketing-strategist`, `web-analytics-specialist`, `product-analyst`, `design-reviewer`, `code-reviewer`.

## Stages
| # | Stage | Owner | Deliverables | Quality gate | Reviewer |
|---|---|---|---|---|---|
| 1 | Frame | `product-manager` | Problem statement, riskiest assumptions list | Assumptions ranked by risk and ease of testing | `business-strategist` |
| 2 | Market and competition | `market-researcher`, `competitor-researcher` (parallel) | Market notes with sources, competitor teardown | Every number sourced and dated | `research-lead` |
| 3 | Customer validation | `customer-interview-specialist` | 5 to 10 problem interviews, evidence table | Evidence on problem frequency, current workaround, willingness to pay | `research-synthesis-specialist` |
| 4 | Decision | `product-manager` | Go / pivot / stop memo | Decision tied to pre-agreed criteria from stage 1 | Owner |
| 5 | MVP scope | `product-manager` with `pricing-strategist` | MVP PRD (must-haves only), success metrics, pricing hypothesis | Each feature traces to a validated need; metrics defined with targets | `product-owner` |
| 6 | Design | `ux-designer`, `ui-designer` | Core flow designs | Usable in a 5-person test (`usability-researcher` optional) | `design-reviewer` |
| 7 | Build | developers led by `solution-architect` | MVP on a preview environment | Tests pass; analytics events implemented per measurement plan | `code-reviewer`, `qa-lead` |
| 8 | Measurement plan | `web-analytics-specialist` | Event spec, dashboards | Events fire correctly in preview | `product-analyst` |
| 9 | Launch | `marketing-strategist` | Launch plan and drafts | Claims match what is built | Owner approves launch |
| 10 | Measure | `product-analyst` | Weekly metrics readout | Data quality checked before conclusions | `product-manager` |
| 11 | Iterate | `product-manager` | Next-cycle backlog | Changes tied to evidence | `product-owner` |

## Human authorization points
Go/stop decision, any spend, launch, pricing published to customers.

## Exit criteria
Either a stop decision with learnings recorded, or an MVP live with a measurement readout and a next-cycle plan.

## Example invocation
"Run WF-03 stages 1 to 4 for a QR print-shop ordering app. Budget is zero for ads."
