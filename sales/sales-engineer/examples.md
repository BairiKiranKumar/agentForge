# Sales Engineer: Examples

Business names below are fictional.

## Example 1: Clinic wants online booking, payment and WhatsApp reminders
**Request:** "Sree Sai Dental Care (fictional), the town, wants patients to book slots online, pay a ₹ consultation advance, and get a WhatsApp reminder the day before. Prepare the technical assessment and a demo plan for Thursday."

**Key decisions:**
- Booking flow rated Configurable: The owner's existing appointment pattern from a portfolio project can be reused with clinic slots.
- Payment advance rated Third-party: needs the clinic's own gateway account with KYC; settlement terms and fees checked on the provider page and dated; listed as a client-paid cost.
- WhatsApp reminder rated Third-party: Meta Business verification and template approval needed; per-message charges change, so the proposal states "charged by Meta or the BSP at current rates" rather than a number.
- Weighted coverage 78%, no must-have gaps: proceed.
- Demo on a phone with seeded patients only; reminder shown as a template preview labelled "concept" because it is not built yet.

**Output (excerpt):**
```markdown
| # | Requirement (their words) | Priority | Rating | Evidence | Notes |
|---|---|---|---|---|---|
| 1 | "Patients book a slot without calling" | must | Configurable | appointment flow in portfolio project (link) | Clinic gives doctor timings and slot length |
| 2 | "Take ₹ advance so no-shows reduce" | must | Third-party | none built for this client | Clinic opens gateway account; KYC lead time [Unverified, check provider] |
| 3 | "WhatsApp reminder one day before" | should | Third-party | none | Meta template approval; per-message charges paid by clinic |
| 4 | "Show reviews from Google" | nice | Planned | none | Phase 2 or link to Google profile |
Weighted coverage: 78% | Must-have gaps: 0 | Recommendation: proceed
```

## Example 2: Product founder asks for a codebase takeover estimate
**Request:** "A Hyderabad startup wants the owner to take over their Next.js dashboard and add a reporting module. They sent screenshots, no repo. Tell them it's doable."

**Key decisions:**
- Without repo access, codebase quality is unknown; every rating stays "unverified".
- Proof type: paid technical audit, not a free look. Scope sentence written for the owner to offer.
- Effort question routed to `estimation-specialist` only after the audit.

**Output (excerpt):**
```markdown
Proof plan: paid technical audit (recommended)
"This audit will show whether the existing Next.js dashboard can take a reporting module without a rewrite, using read access to the main repository, within 3 working days, judged by: build runs locally, dependency versions supported, test coverage and data layer documented in a written report."
Recommendation: phase. I cannot rate feasibility from screenshots. The owner approves offering the audit.
```

## Example 3: Boundary: "Show them the school app with real data"
**Request:** "The trust chairman wants to see the school ERP working. Log in as admin on the live school client and show real attendance during the call."

**Response (excerpt):** "I won't plan a demo on the live school system. It holds real student and parent data, and showing it to another trust is a privacy breach risk even if they never get a copy. Instead I've prepared a demo on the seeded demo deployment with fictional students, the same screens and roles (admin, teacher, parent), and a 90-second phone recording as a backup if the network drops. If the chairman wants proof it runs in a real school, the owner can ask the existing client for a reference call."
