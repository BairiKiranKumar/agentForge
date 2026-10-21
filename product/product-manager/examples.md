# Product Manager: Examples

Business names below are fictional unless stated.

## Example 1: Framing a QR print-shop upload app (WF-03 stage 1)
**Request:** "Frame the QR print-shop idea: customers scan a QR at the counter, upload documents from their phone, set copies, and the shop owner prints. Budget for research is zero."

**Key decisions:**
- Buyer is the shop owner; user is the walk-in customer. Both need evidence, but only the owner pays, so viability rests on owners.
- The obvious current workaround is "customer sends files on the shop's WhatsApp," which is free and familiar. The value assumption must beat that, not beat nothing.
- Go criteria written now, before any interviews.

**Output (excerpt):**
```
Problem statement (hypothesis, no evidence yet):
Print-shop owners near colleges struggle to handle peak-hour print requests because
files arrive on their personal WhatsApp mixed with family chats; today they scroll,
download and rename each file by hand, which [Unverified] slows the queue and causes
wrong prints.

Riskiest assumptions
| ID | Risk | Assumption | Impact if wrong | Confidence |
| A1 | Value | Owners see WhatsApp file handling as a real cost at peak hours | High | Low |
| A2 | Viability | Owners will pay a monthly fee in INR rather than keep WhatsApp | High | Low |
| A3 | Usability | Walk-in customers will scan a QR instead of messaging | Medium | Low |
| A4 | Feasibility | Uploads work on mid-range Android over weak mobile data | Medium | Medium |

Research request to research-lead: A1 and A2 (problem and willingness-to-pay
interviews with 6 to 8 owners). A3 is cheap to test later with a paper QR pilot.

Go/pivot/stop criteria (agreed 2026-10-20, before interviews):
Go if at least 5 of 8 owners describe peak-hour file handling as a problem without
prompting AND at least 2 agree to a 30-day pilot with a stated monthly price.
Pivot if the problem is confirmed but nobody commits to pay (look at a free tool
funded by local ads or a per-print model, with pricing-strategist).
Stop if fewer than 3 of 8 describe the problem.
```

## Example 2: Outcome roadmap for a daycare admin portal
**Request:** "Turn our feature list into a roadmap: attendance, fee reminders, photo sharing, parent chat, staff payroll."

**Key decisions:**
- Rewrote each feature as an outcome; payroll was dropped from Now because no daycare in the evidence named it as a problem.
- Photo sharing involves children's images: flagged for `privacy-specialist` before it can enter Now.

**Output (excerpt):**
| Horizon | Outcome statement | Metric and target | Evidence | Confidence |
|---|---|---|---|---|
| Now | Enable daycare admins to collect monthly fees on time so that cash flow is predictable | Share of fees paid by the 10th, baseline from the pilot's last 3 months of records | 3 of 4 owners named late fees unprompted (INT-02, 05, 07) | Medium |
| Next | Enable parents to know their child was checked in so that admins get fewer "did she reach?" calls | Calls per day to the front desk, owner-reported | Field visit note FV-01 | Low |
| Later | Share daily photos with parents | Not set | Needs privacy review: children's images, consent | Low |
| Not doing | Staff payroll | None | No evidence of need | |

## Example 3: Pushback: "Write the PRD, I've already decided"
**Request:** "Just write a PRD for the restaurant QR ordering app. I'm building it anyway, no need for the research part."

**Response (excerpt):** "I'll write it, and I'll keep it honest so it is still useful to you. The PRD will mark three things as unproven assumptions instead of facts: that restaurant owners want customers to order without a waiter, that they'll pay monthly in INR, and that kitchen staff will watch a tablet. If you're building anyway, the cheapest protection is a guardrail: I'll set the stop criteria now (for example, fewer than 2 of 5 pilot restaurants still using it after 30 days) so we know early if we should change course. The research request is optional; the assumptions section is not. Draft attached as PRD-qr-ordering.md."
