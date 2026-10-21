# Operations Lead: Checklist

## Before starting
- [ ] Symptom or goal stated with at least one measure (count, wait time, cost)
- [ ] Current process described as it is actually done, not as intended
- [ ] Monthly volumes known or a two-week run log proposed
- [ ] Tool register read; monthly INR spend known
- [ ] Client-facing steps in the process identified

## While working
- [ ] SIPOC written before any fix is proposed
- [ ] Each step has an owner, a tool and a wait time
- [ ] Maturity level assigned using the 0 to 4 scale
- [ ] Bottleneck named with evidence (where work waits longest)
- [ ] Single points of failure listed (person, account, device)
- [ ] Intervention chosen with the SOP / automation / agent / nothing table
- [ ] No automation proposed below maturity level 2
- [ ] New tool passes all five criteria, including export path and DPDP check
- [ ] Tool addition names what it retires; register stays at or under the cap
- [ ] GST or reverse charge treatment of foreign SaaS flagged for `gst-specialist` instead of assumed
- [ ] Capacity planned at 80% or less of available hours

## Before handoff
- [ ] Operating decision record has baseline, target and review date
- [ ] Cost shown as one-time and monthly INR
- [ ] Process map updated with owner and maturity
- [ ] SOP brief, purchase need or automation spec routed to the right role
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] The change requires buying a tool or upgrading a plan
- [ ] Credentials, OTPs or passwords appear in any document or message
- [ ] The change alters what clients see or do
- [ ] Client data would move between systems
