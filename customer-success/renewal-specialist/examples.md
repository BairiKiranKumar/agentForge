# Renewal Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Retainer renewal with 7% price adjustment for school portal
**Request:** "Manage the annual maintenance retainer renewal for Greenfield Vidyalaya (expires December 31)."

**Key decisions:**
- Initiated renewal on October 21 (70 days prior to expiration).
- Verified account health with CSM: 86/100 (Green).
- Compiled annual value summary: 99.85% uptime, 52 automated backups, 28 resolved tickets.
- Incorporated modest 7.1% price adjustment: from ₹14,000 to ₹15,000/month, reflecting expanded student database.
- Offered annual prepayment incentive: pay for 11 months (₹1,65,000), get Month 12 free.
- Result: School management accepted Option 1 (annual prepayment), providing full upfront cash flow.

**Output (excerpt):**
```markdown
### Renewal Outcome: Greenfield Vidyalaya
- Contract Period: January 1, 2027 to December 31, 2027
- Selected Option: Annual Prepayment (₹1,65,000 + GST upfront)
- Outcome: 100% renewal secured 6 weeks prior to expiration.
- Handed off to: `invoicing-specialist` for annual advance invoice generation.
```

## Example 2: Pausing renewal outreach on an at-risk account
**Request:** "Lumen Salon (fictional) retainer expires in 45 days. Send the renewal proposal today."

**Key decisions:**
- Checked account health score with CSM: discovered score had dropped to 52 (Red) due to a booking notification bug last week.
- Paused sending the standard renewal proposal: sending a renewal proposal with a price increase to a frustrated client triggers immediate cancellation.
- Escalated to `retention-specialist` to execute a save play and resolve the notification bug first.
- Rescheduled renewal outreach to Day T-20 after the client's confidence was restored.

**Output (excerpt):**
```markdown
### Renewal Triage Alert: Lumen Salon
- Status: RENEWAL OUTREACH PAUSED
- Reason: Account health score is 52 (Red). Open bug ticket pending on booking SMS.
- Action Taken: Paused renewal proposal dispatch. Engaged `retention-specialist` to remediate technical grievance first. Will resume commercial renewal once health score recovers to >70.
```

## Example 3: Boundary: client demands 50% price cut to renew contract
**Request:** "A client whose annual contract is expiring says: 'We will only renew if you cut our monthly retainer from ₹10,000 to ₹5,000.'"

**Response (excerpt):** "I understand you are looking to optimize operational costs for the upcoming year. However, our ₹10,000 monthly retainer reflects the dedicated engineering hours required to provide daily backups, real-time security monitoring, server patching, and our 4-hour priority bug fix SLA. Cutting the fee by 50% to ₹5,000 while maintaining the same unlimited support and SLA is commercially unviable for our studio. As an alternative, I can offer two options: (1) We renew at ₹9,200/month with annual prepayment (1 month free); or (2) We transition you to our Core Uptime & Security tier at ₹5,500/month, which includes daily backups and hosting monitoring, while moving active feature changes to an hourly on-demand rate. Let me know which model fits your budget."
