# Compliance Research Assistant: Examples

Business names below are fictional.

## Example 1: School portal storing student photos and attendance
**Request:** "Sunrise Public School wants parents to see their child's photos and attendance in the portal. What rules apply?"

**Key decisions:**
- Children's personal data: DPDP Act and Rules identified as the main regime; parental consent provisions noted with in-force date.
- Only a secondary source for the phased dates was fetched; confidence medium; lawyer question added.
- Separated design actions (role-based access, retention) from legal conclusions.

**Output (excerpt):**
```
RESEARCH, NOT LEGAL ADVICE. As of 2026-10-20.
Summary: proceed with conditions; lawyer review recommended for children's data consent design.
| Rule | Source and tag | In force from | Applies? | Confidence | Requires |
|---|---|---|---|---|---|
| DPDP Act 2023, children's data provisions and Rules | AZB update [secondary source, verify]; meity.gov.in to confirm | 13 May 2027 (most substantive provisions) | Applies (school as data fiduciary) | Medium | Verifiable parental consent, no tracking of children (verify exact rule text) |
Checklist:
- [ ] Parent sees only own child's records (frontend-developer, test by playwright-specialist)
- [ ] Retention period agreed with school (privacy-specialist)
Questions for a lawyer: 1) Is the school or the studio the data fiduciary for hosted data? 2) What consent evidence must the portal keep?
```

## Example 2: Monthly change watch
**Output (excerpt):**
| Item | Source | Tier | Action |
|---|---|---|---|
| Consent manager provisions commence 13 Nov 2026 | AZB update [secondary source, verify] | Watch (not relevant unless we integrate a consent manager) | Log |
| New ASCI guideline on AI-generated ads (claimed in a blog) | blog [secondary source] | Bumped to FYI until found on ascionline.in | Trace to primary |

## Example 3: Boundary: "Just say we're DPDP compliant on the website"
**Request:** "Write 'Fully DPDP compliant' in the clinic site footer."

**Response (excerpt):** "I can't support that claim. I'm not a lawyer, compliance is a legal conclusion, and the main DPDP obligations commence on 13 May 2027 per the source I found (verify on meity.gov.in). An unsupported claim could also count as a misleading statement. I can give `privacy-specialist` a list of what the site does today (consent checkbox, privacy notice, data minimisation) so the footer links to an accurate privacy notice instead."
