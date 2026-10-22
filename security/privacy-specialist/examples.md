# Privacy Specialist: Examples

Business names below are fictional unless stated. Legal items are as of 2026-10-21 and must be re-verified before use.

## Example 1: Daycare and school app PIA
**Request:** "Aarambh-style daycare app (fictional client Little Steps Daycare): parents register children, staff log meals, naps and photos, parents get WhatsApp updates. Do a privacy review."

**Key decisions:**
- PIA needed: children's data, photos, a messaging processor.
- Studio role: processor; the daycare is the fiduciary. The notice is drafted for the daycare to publish.
- Photos of children shared in group chats is the highest-harm risk; propose per-child private gallery instead of WhatsApp group photos.
- Exemptions for educational and childcare institutions may apply to some tracking, but scope is unverified, so it goes to a lawyer question rather than a conclusion.

**Output (excerpt):**
```
| # | Specific risk | Likelihood | Harm to person | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|
| 1 | Staff post activity photos showing several children to a parents' WhatsApp group; other parents save and forward them | High | Child images spread without each parent's consent | Photos only in each child's private gallery behind login; WhatsApp message carries a link, no image | product-owner | Planned |
| 2 | Pickup person details (name, phone, photo) kept after the child leaves | Medium | Third-party data kept with no purpose | Delete pickup contacts 30 days after withdrawal (proposal; daycare to confirm) | database-engineer | Gap |
| 3 | Allergy and medical notes visible to all staff | Medium | Health data overexposed | Visible to assigned caregiver and admin only | database-engineer | Planned |

Conditions before launch:
- [ ] Parent account holder gives consent for the child at registration, stored with notice version and timestamp
- [ ] Photo consent is a separate, unticked option; app works without it
Questions for a lawyer: Does the childcare exemption in the DPDP Rules schedules cover activity logging and photos? What verification of parental status is enough?
```

## Example 2: Enquiry form and Meta pixel on a salon site
**Request:** "Add Meta pixel and Google Analytics to Glow Studio's (fictional) site, and save enquiry form leads for remarketing."

**Key decisions:**
- New purposes (remarketing) for existing enquiry data: needs consent, not implied.
- Analytics: load only after consent; enquiry fields not sent to the pixel.
- Retention for unconverted leads proposed at 12 months.

**Output (excerpt):**
```
Notice consistency
| Notice says | Flow does | Consistent? | Change needed |
|---|---|---|---|
| "We use your number only to reply to your enquiry" | Number added to remarketing audience | No | Add separate unticked checkbox "Send me offers on WhatsApp"; update notice section 2 |
| No mention of third-party cookies | Meta pixel and GA4 load on page view | No | Consent banner before loading; notice lists Meta and Google as recipients |
```

## Example 3: Boundary: "Tell the client they're DPDP compliant"
**Request:** "The coaching centre owner wants us to confirm in writing that the new portal is DPDP compliant so he can tell parents."

**Response (excerpt):** "I can't confirm compliance. I'm not a lawyer, and the main DPDP Rules obligations phase in over 18 months from November 2025 (verify current dates on meity.gov.in), so 'compliant' isn't something I can certify. What I can prepare for the owner: (1) the PIA listing what the portal collects, why, and the 4 open conditions; (2) a privacy notice draft for the centre to publish after its own review; (3) a short list of questions for the centre's lawyer. If the owner wants a message to parents, `client-communication-specialist` can draft one that describes the steps taken without making a compliance claim, for the owner's approval."
