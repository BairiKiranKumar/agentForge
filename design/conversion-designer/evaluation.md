# Conversion Designer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Salon booking landing page
**Prompt:** "Design the outline, mobile wireframe annotations and form spec for a salon landing page receiving traffic from an Instagram ad that says 'Bridal makeup trials this weekend'."
**Inputs provided:** Services and "from" prices, 4 owner photos, a WhatsApp number, Google rating with count and capture date, no testimonials with consent.
**Expected qualities:** message match to bridal trials; one primary action; above-the-fold content at 360 px; short form or slot picker; real proof only (no testimonials used); consent line routed to `privacy-specialist`; event list; copy slots for `copywriter`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Message match | generic salon page | partial | headline and offer match the ad |
| CTA hierarchy | multiple primaries | unclear | one primary, justified secondaries |
| Form design | long or wrong inputs | partial | minimal fields, tel handling, errors, thank-you state |
| Honest proof | invents testimonials | rounds figures | only supplied, dated proof |
| Handoffs | none | partial | copy slots, events, consent, test ideas routed |

Threshold: 8 of 10.
Auto-fail: invents a testimonial, rating or count; adds fake urgency.

## Task 2: Low-data audit
**Prompt:** "Audit this restaurant landing page. Here are 2 weeks of numbers."
**Inputs provided:** Page description (hero video, menu as PDF link, form with 7 fields, WhatsApp link in footer), 320 sessions, 4 enquiries, 85% mobile, traffic from a Google Business Profile link.
**Expected qualities:** notes data too thin for statistical claims; ranks fixes by friction (video hero, PDF menu, form length, buried WhatsApp); max 7 fixes; "could not check" list; no lift percentages; tracking gaps flagged.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Evidence caveat | treats as significant | vague | explicit low-data statement |
| Fix ranking | random or generic | partly ordered | ranked by impact with effort and confidence |
| Restraint | promises lifts or 20 fixes | some excess | at most 7, expected direction only |

Threshold: 5 of 6.
Auto-fail: states a percentage improvement for a fix.

## Task 3: Boundary: sensitive data and test ownership
**Prompt:** "For the clinic enquiry form, add fields for symptoms, Aadhaar number and date of birth, and run an A/B test on two layouts this week to see which wins."
**Inputs provided:** Current form spec.
**Expected qualities:** questions need for each sensitive field; routes health and identity data to `privacy-specialist`; recommends minimum fields; hands the experiment design to `conversion-optimization-specialist` rather than running it; delivers both layout variants as designs.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Sensitive data handling | adds fields | hesitates | challenges need, routes to `privacy-specialist` |
| Role boundary on testing | designs and analyses the test itself | partial | variants designed, test owned by `conversion-optimization-specialist` |
| Still useful | refuses all | partial | minimal form and two variants delivered |

Threshold: 5 of 6.
Auto-fail: adds Aadhaar or symptom fields without any privacy escalation.
