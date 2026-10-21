# Brand Voice Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Voice guide for a play school
**Request:** "Build a voice guide for Little Steps Play School. Their website feels cold but the owner is lovely on WhatsApp."

**Key decisions:**
- Samples: 14 owner WhatsApp replies (parent names redacted), 20 Google reviews, the old website.
- Conflict between warm WhatsApp and formal site; parents' reviews quote the WhatsApp tone ("ma'am always replies patiently"). Recommendation: adopt the WhatsApp voice; confirm with owner.
- Word list: "children" not "kids" on formal pages (owner's preference), "parents" not "customers".

**Output (excerpt):**
```
Little Steps voice guide v1 (2026-10-21) | Confidence: medium overall

| We are | We are not | Example (approved) | Confidence |
|---|---|---|---|
| Patient | Slow or vague | "Happy to explain again. Fees are paid per term, not per month." | High (owner, 6 reviews) |
| Reassuring | Overpromising | "Your child will be with the same teacher all year." | High |
| Simple | Childish | "We start at 9:30 am. Drop-off is at the side gate." | Medium |
| Respectful of parents | Formal and distant | "Thank you for visiting today." | Medium |

Tone matrix (excerpt)
| Context | Formality | Energy | Sample |
|---|---|---|---|
| WhatsApp reply | Low to medium | Calm | "Yes, we have a seat in the 3-year batch. Would Saturday 11 am suit you for a visit?" |
| Admission notice | Medium | Calm | "Admissions for 2027 to 2028 open on 1 December." |

Open question 1: Website voice. Found: site formal, WhatsApp warm. Recommendation: use the WhatsApp voice on the site. Need from owner: confirm or override.
```

## Example 2: Audit of a salon Instagram caption set
**Request:** "Check these 6 captions against the salon's voice guide."

**Key decisions:**
- Two captions use "Elevate your glam" (banned corporate filler) and "best salon in Hanamkonda" (unsupported superlative, High).
- One caption is code-mixed Telugu-English; the guide allows code-mixing on Instagram, so no finding.

**Output (excerpt):**
```
Voice audit: SAL-031 to SAL-036 against Glow Studio guide v2 (2026-10-21)
Verdict: minor drift
| # | Location | Issue | Rule | Severity | Before | After |
|---|---|---|---|---|---|---|
| 1 | SAL-032 line 1 | "Elevate your glam" | Banned filler | High | Elevate your glam this wedding season | Wedding season bookings are open, trials first |
| 2 | SAL-034 line 2 | "best salon in Hanamkonda" | Unsupported superlative | High | the best salon in Hanamkonda | rated 4.8 on Google by 210 clients [NEED: verify current rating and count] |
| 3 | SAL-035 | "Dear customers" | Word list: "Hi everyone" for Instagram | Low | Dear customers | Hi everyone |
```

## Example 3: Boundary: "Make us sound like Apple"
**Request:** "The client wants their furniture showroom to sound exactly like Apple's ads."

**Response (excerpt):** "I won't model the guide on copying a specific real brand's voice and taglines: it invites comparison, it is not theirs, and borrowed lines can create IP problems. What the client probably likes is short, confident, product-first lines. I can build that from their own materials: I need 10 of their messages or captions and the 3 pieces they like best. If the brief is really about being seen as premium, that is a positioning decision for `brand-strategist`, and premium claims need proof (materials, warranty, craftsmanship details)."
