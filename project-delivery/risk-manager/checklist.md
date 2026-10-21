# Risk Manager Checklist

## Before starting
- [ ] Review project execution plan, Statement of Work (SOW), and architectural specifications
- [ ] Identify external dependencies, third-party APIs, and client-side decision milestones
- [ ] Review historical failure modes and post-mortem notes from past studio projects
- [ ] Initialize Master Risk Register repository and configure 5x5 scoring parameters
- [ ] Schedule kickoff Risk Identification Workshop with multidisciplinary project leads

## While working
- [ ] Brainstorm delivery risks across technical, operational, and client stakeholder categories
- [ ] Formulate risk statements using standard syntax: "If [Event], then [Consequence], resulting in [Impact]"
- [ ] Score each risk on Probability (1-5) and Impact (1-5) to calculate Exposure Score (1-25)
- [ ] Assign every risk item to a single accountable role owner
- [ ] Develop proactive Mitigation Plans to reduce likelihood for all High and Medium risks
- [ ] Formulate reactive Contingency Plans for all High-severity risks
- [ ] Define measurable Early Warning Indicators and trigger thresholds for critical risks
- [ ] Facilitate bi-weekly Risk Review syncs with `project-manager` and `technical-lead`
- [ ] Track closed and retired risks to maintain an accurate active threat profile

## Before handoff
- [ ] Compile Bi-Weekly Risk Review Summary with trending exposure scores and mitigation statuses
- [ ] Verify that high-priority mitigation tasks are injected into active sprint backlogs
- [ ] Brief `delivery-manager` on critical residual risks prior to client executive reviews
- [ ] Ensure all role and tool mentions use valid roster slugs in backticks
- [ ] Confirm zero em dashes are present in any risk documentation
- [ ] Format handoff according to `orchestration/handoff-format.md` standards

## Stop and escalate if
- [ ] Unmitigated delivery risk reaches Exposure Score >= 20, threatening catastrophic project failure
- [ ] Critical third-party vendor experiences sudden insolvency or service termination
- [ ] Project leadership refuses to execute mandatory mitigation actions for a critical Red risk
