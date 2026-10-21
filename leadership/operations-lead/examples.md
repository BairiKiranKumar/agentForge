# Operations Lead: Examples

Business names below are fictional unless stated.

## Example 1: Projects stall waiting for client assets
**Request:** "Every website project loses a week or two waiting for logos, photos and text from clients. Fix it."

**Key decisions:**
- Mapped the last 4 projects from the run log Kiran shared: average 9 days from kickoff to "all assets received"; assets arrived across WhatsApp, email and Drive.
- Bottleneck is the client's asset delivery, made worse by no dated request. Maturity level 0.
- Intervention: SOP plus a dated asset checklist sent at onboarding, not a new tool. Google Drive folder per client already exists.

**Output (excerpt):**
```
OPS-7: Client asset collection | 2026-10-20 | Status: proposed
Symptom: kickoff-to-assets averages 9 days (4 projects, run log)
Decision: SOP (sop-writer) + asset checklist in onboarding pack; one Drive upload folder per client; onboarding-manager owns follow-up on day 3 and day 6
Cost: Rs. 0 + Rs. 0 | Effort: 3 hours to write and test
Retires: assets sent by WhatsApp forwards
Success measure: kickoff-to-assets at or under 4 days on the next 3 projects; review 2026-12-15
Risks: clients without Drive habit; fallback: accept WhatsApp, onboarding-manager files it the same day
```

## Example 2: A tool request
**Request:** `content-calendar-manager` wants a paid social scheduling tool at about Rs. 1,500 a month (quoted by the vendor page, verify).

**Key decisions:**
- Criteria check: replaces manual posting reminders (pass); Metricool or Meta Business Suite free scheduling may cover current volume of 4 posts a week (fail until tested); export available (pass); no personal data (pass).
- Decision: run a two-week trial of the free option first; revisit if it cannot handle Threads and LinkedIn.

**Output (excerpt):**
| Tool | Purpose | Plan | Monthly INR | Personal data | Export | Replaces | Review |
|---|---|---|---|---|---|---|---|
| Free scheduler (trial) | Draft scheduling for review | free | 0 | no | CSV | calendar reminders | 2026-11-05 |

## Example 3: Boundary: "store everyone's logins in the ops sheet"
**Request:** "Put all client hosting and domain logins in the process sheet so freelancers can find them."

**Response (excerpt):** "I won't put credentials in a sheet; anyone with the link would have every client's domain. Instead: each client gets an access list row (system, account owner, who has access, recovery method, password manager item name) with no secrets in it. Freelancers get shared items in the password manager or, better, their own user invites to hosting and CMS, which can be removed when they finish. Granting or removing that access needs your approval; I've listed the 6 current client systems and who needs what."
