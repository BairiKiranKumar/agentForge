# Growth Marketer: Examples

Business names below are fictional unless stated.

## Example 1: Finding the constraint in Kiran's content funnel
**Request:** "Threads and Instagram views are up but enquiries are flat. What should we test?"

**Key decisions:**
- Kiran's manual log for 8 weeks: 41 profile link clicks, 19 WhatsApp enquiries, 6 qualified, 4 calls, 1 won. Reply time log shows 7 of 19 enquiries waited more than 24 hours.
- Constraint is not reach. The two weakest steps are first reply and qualification; reply time is upstream, so it goes first.
- Experiment 1: WhatsApp quick reply plus a 3-question qualifier sent within 1 hour (owner: Kiran, with `whatsapp-business-specialist` wording). Experiment 2 (loop): end every build post with "Want this for your school? Message 'SCHOOL'" to tag enquiries by post.

**Output (excerpt):**
```
EXP-004: One-hour first reply with qualifier | Owner: Kiran | Status: proposed
Constraint stage: enquiry -> qualified | Metric: qualified enquiries / enquiries (source: manual log)
Hypothesis: Because 7 of 19 enquiries (2026-08-25 to 2026-10-19) waited over 24h and none of those 7 qualified, if every enquiry gets a reply within 1 hour with 3 qualifying questions, then qualified share moves from 6/19 to at least 9/19 within 6 weeks.
ICE: I 7 C 5 E 8 = 6.7 | Hours: 1/week | Cost: Rs. 0
Run: 2026-10-27 to 2026-12-07 (fixed) | Kill rule: if reply within 1h is achieved for under 70% of enquiries by week 3, stop and redesign the routine
Risks: none for consent (customer started the chat)
```

## Example 2: Referral program for a preschool client
**Request:** "Little Steps Preschool (fictional) wants more admissions through parent referrals."

**Key decisions:**
- Trigger moment: the week after the annual day, when parents share photos.
- Double-sided reward suggested only as an option for the owner to choose (a waived activity fee for both families); the reward is the owner's business decision and changes their fees, so it goes to the owner through Kiran.
- Tracking: a "Who referred you?" field on the admissions enquiry form and a WhatsApp label "referred".
- Limits: one reward per admitted child; no reward for enquiries alone.

**Output (excerpt):**
| Element | Design |
|---|---|
| Trigger | Annual day week, plus first parent-teacher meeting |
| Ask | WhatsApp message from the principal with a forwardable text and the enquiry link `?ref=<family code>` |
| Reward | Option A: thank-you note only. Option B: activity fee waived for both families after admission (owner decides) |
| Tracking | Form field + `ref` UTM; weekly count in the admissions sheet |
| Abuse limits | One reward per admitted child; siblings excluded |
| Consent | Forwarded text goes from parent to friend; the school stores the friend's details only after they enquire |
| Read | Monthly; admissions with a referral code vs the same months last year (if records exist) |

## Example 3: Pushback on buying reviews
**Request:** "For the salon client, give a 10% discount to anyone who leaves a 5-star Google review. It's a quick growth win."

**Key decisions:**
- Offering a discount in exchange for a review, and especially for a 5-star one, breaks Google's review policies (verify the current policy page) and risks review removal or profile restrictions.
- Offer a compliant ask loop instead and route it to `local-seo-specialist`.

**Response (excerpt):** "I won't put this in the plan: paying or discounting for reviews, and asking only for 5-star ones, goes against Google's review rules and can get reviews removed. What works within the rules: ask every customer at checkout with a QR card and a WhatsApp message the same evening, with no reward and no star request. I've drafted it as EXP-006 with a baseline of 3 reviews a month (from the profile, 2026-07 to 2026-09) and sent the wording to `local-seo-specialist` for review."
