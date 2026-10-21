# Estimation Specialist Checklist

## Before starting
- [ ] Review product requirements documents, user stories, and wireframes for completeness
- [ ] Consult with `technical-lead` to clarify technology stack choices and architectural constraints
- [ ] Identify integration touchpoints, third-party APIs, and external hardware dependencies
- [ ] Review historical velocity and past actual hours for similar feature modules
- [ ] Confirm whether a preliminary research spike is required for novel technologies

## While working
- [ ] Decompose project scope into a hierarchical Work Breakdown Structure (WBS)
- [ ] Ensure all work packages are sized between 4 and 24 hours of effort
- [ ] Assign Three-Point estimates: Optimistic (O), Most Likely (M), and Pessimistic (P)
- [ ] Calculate PERT expected hours: (O + 4M + P) / 6 for every work package
- [ ] Calculate standard deviation and 95% confidence intervals for the overall project
- [ ] Apply appropriate uncertainty contingency buffers (15% to 35%) based on technical clarity
- [ ] Document explicit technical, operational, and client prerequisite assumptions
- [ ] Compile a comprehensive list of out-of-scope exclusions to prevent scope boundary disputes
- [ ] Validate that non-coding activities (testing, code reviews, DevOps) are explicitly estimated

## Before handoff
- [ ] Compile complete Effort Estimation Dossier with WBS, PERT tables, and confidence ranges
- [ ] Review estimation dossier with `technical-lead` for feasibility and sanity check
- [ ] Transmit effort baselines to `pricing-strategist` and `delivery-manager`
- [ ] Ensure all role and tool mentions use valid roster slugs in backticks
- [ ] Confirm zero em dashes are present in any estimation documentation
- [ ] Format handoff according to `orchestration/handoff-format.md` standards

## Stop and escalate if
- [ ] Requirements are too vague or contradictory to produce a defensible estimate
- [ ] Sales team demands cutting estimate hours without an equivalent reduction in functional scope
- [ ] Critical third-party dependency lacks documentation or technical proof of feasibility
