# AI Evaluation Specialist: Checklist

## Before starting
- [ ] System under test and baseline identified with versions (prompt, model, settings, retrieval config)
- [ ] Acceptance criteria and severity of each failure type agreed with the owner
- [ ] Thresholds and decision rule written before any run
- [ ] Real inputs anonymized (names, phones, emails, ID numbers)
- [ ] Grader independence confirmed: not grading your own or the same instance's output
- [ ] Run cost estimated (cases x trials x systems) and within budget

## While working
- [ ] Cheapest discriminating check chosen per criterion
- [ ] Dataset mix covers typical, edge, adversarial and unanswerable cases
- [ ] Adversarial cases include injection in user text and in retrieved or uploaded content
- [ ] Language split matches the audience (Telugu, Hindi, mixed script where relevant)
- [ ] Every case tagged with category, language and severity
- [ ] Dataset version frozen; held-out slice kept from prompt authors
- [ ] Rubric criteria binary or 0 to 2 with written anchors
- [ ] Each assertion passes 3 known-good and fails 3 known-bad outputs
- [ ] Judge used only where code checks cannot work
- [ ] Judge calibrated on 30 to 50 human labels; kappa recorded
- [ ] Pairwise comparisons run in both orders
- [ ] Same dataset, settings and trial count for baseline and candidate

## Before handoff
- [ ] Results by category and language, with 95% intervals
- [ ] Per-case diff lists newly failing and newly passing cases
- [ ] Critical regressions stated explicitly (or "none")
- [ ] Cost and latency per case taken from run logs
- [ ] Recommendation: ship, do not ship, or needs human review, with reason
- [ ] Eval weaknesses found are listed for the owner
- [ ] For ai-team agents: raw outputs saved under `evaluations/runs/`, row added to `evaluations/STATUS.md`
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Asked to declare a pass before a run completes or to lower thresholds after results
- [ ] Asked to grade your own output
- [ ] Eval data would include unanonymized customer or children's data
- [ ] Run cost would exceed the approved budget
