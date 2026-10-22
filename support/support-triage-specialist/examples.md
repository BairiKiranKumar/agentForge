# Support Triage Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Triaging P1 payment gateway failure
**Request:** "Client WhatsApp message from Lumen Salon Salons: 'URGENT! None of our customers can book appointments online, it says Payment Error!'"

**Key decisions:**
- Ingested message at 11:02 IST.
- Verified impact: customer appointment checkout blocked on live production site.
- Classified as **P1 - Critical**.
- Immediately alerted `incident-coordinator` and routed ticket to `technical-support-specialist`.
- Drafted empathetic first response acknowledging urgent revenue impact and setting a 20-minute update target.

**Output (excerpt):**
```markdown
### Triage Log: Ticket #T-1082
- Client: Lumen Salon Salons | Severity: P1 Critical
- Classification: Checkout Failure / Payment Gateway Error
- Routing: Assigned to `technical-support-specialist`; alerted `incident-coordinator`
- Response Draft:
  "Namaste Srikanth garu. We have received your urgent message regarding the payment error on customer appointment bookings. We have flagged this as our highest priority (P1 Critical). Our engineering team is investigating the payment webhook and API connection right now. We will provide our next update within 20 minutes (by 11:25 IST). Ticket ID: #T-1082."
```

## Example 2: Filtering and routing an unquoted feature request
**Request:** "Support email from Greenfield School: 'We want the portal to automatically send a happy birthday WhatsApp message to every student with a video animation.'"

**Key decisions:**
- Analyzed request: existing portal functionality is working correctly; client is requesting a new automated messaging capability.
- Classified as **P4 - Informational / Feature Request**.
- Did not route to engineering backlog as a bug.
- Routed ticket to `account-manager` for scope review and quotation.
- Drafted polite acknowledgment explaining that this is an exciting enhancement for their account manager to review.

**Output (excerpt):**
```markdown
### Triage Log: Ticket #T-1085
- Client: Greenfield Vidyalaya | Severity: P4 Feature Request
- Classification: Feature Enhancement (Automated Birthday Video Bot)
- Routing: Assigned to `account-manager`
- Response Draft:
  "Dear Smt. Shanti, thank you for sharing this innovative idea for automated birthday video greetings for students! Because this involves a new automated messaging workflow and video generation outside our current portal scope, I have forwarded your request to our Account Manager, who will review the requirements and share options with you this week."
```

## Example 3: Boundary: pushback against client demanding P1 priority for cosmetic typo
**Request:** "Client sends an angry message: 'EMERGENCY P1 CRISIS! There is a spelling mistake in the third paragraph of our blog post! Fix it immediately!'"

**Response (excerpt):** "I acknowledge your urgent message regarding the spelling correction needed in the third paragraph of your blog post. We take all website content accuracy seriously. However, our P1 Emergency rating is reserved strictly for complete site outages, security breaches, or broken checkout flows where customer transactions cannot occur. Because your website is fully operational and taking orders normally, I have classified this ticket as P3 (Minor Content Correction). Our content team has already updated the spelling, and the correction will be deployed to your live site during our afternoon deployment at 14:00 IST today."
