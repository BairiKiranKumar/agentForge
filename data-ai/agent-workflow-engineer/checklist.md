# Agent Workflow Engineer: Checklist

## Before starting
- [ ] Two or three real working cases collected end to end
- [ ] Every external effect listed with a named approver
- [ ] Runtime known (Claude Code subagents, framework, custom server, manual)
- [ ] Requirement register started with a status per item
- [ ] For ai-team changes: roster entries read and overlap with existing `owns` checked

## While working
- [ ] Complexity ladder applied; simpler options rejected with reasons
- [ ] Topology drawn as Mermaid source
- [ ] Each agent has input schema, output schema, tool allow-list and "not responsible for" list
- [ ] IDs, approved decisions, constraints and authorization pass verbatim in state
- [ ] Code-enforced rules separated from model-decided ones
- [ ] No agent both reads untrusted content and holds send, publish or spend tools
- [ ] Handoffs validated against schema; instruction-like text quarantined
- [ ] Every loop capped; evaluator-optimizer at most 3 rounds with plateau exit
- [ ] Per-run limits set for time, spend in INR, tool calls and handoffs
- [ ] Output on limit defined (best result, unfinished items, reason)
- [ ] Failure taxonomy filled per agent, including "effect unknown" for timed-out writes
- [ ] Idempotency keys on any retried external write
- [ ] Progress ledger file defined for long runs
- [ ] Tracing defined with a shared `trace_id`

## Before handoff
- [ ] Each working case walked through on paper and run with effects stubbed
- [ ] At least 3 adversarial cases run (injection, missing input, tool failure) with results recorded
- [ ] For ai-team changes: `tools/validate.py` run with zero errors, full run checked for duplicates and links
- [ ] Capability matrix and workflows updated for changed roles
- [ ] Evaluation requested from `ai-evaluation-specialist`; status left unchanged
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] An agent would approve its own external action
- [ ] Someone asks to remove a human gate on sending, spending, publishing or deleting
- [ ] A new role duplicates an existing role's ownership
- [ ] Agents would connect to live client systems without authorization
