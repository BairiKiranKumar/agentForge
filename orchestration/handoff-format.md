# Handoff Format

Every transfer of work between agents, departments or workflow stages uses this format. It is the contract that lets a receiving agent start without re-asking for context. Copy `templates/handoff.template.md` to start one.

## Required fields

```yaml
handoff:
  id: HO-<workflow>-<number>            # e.g. HO-WF2-007
  workflow: <workflow file or "ad hoc">
  stage: <stage name from the workflow>
  from: <role slug>
  to: <role slug>
  date: <YYYY-MM-DD>

  task: <one sentence: what the receiver must do>
  objective: <why: the outcome this serves>

  context:
    summary: <3 to 6 lines of relevant background only>
    approved_decisions:                 # decisions the receiver must not reopen
      - id: D-<n>
        decision: <text>
        approved_by: <person or role>
    constraints: [<budget, deadline, brand, tech, legal constraints>]

  inputs:                               # artifacts the receiver needs
    - path: <file path or URL>
      description: <what it is, version>

  completed_work:
    - <what has been done already, so it is not redone>

  evidence:                             # proof, not claims
    - check: <test, review, source, measurement>
      result: <pass/fail/value, as observed>
      location: <log, report or file path>

  assumptions:
    - <assumption> (owner to confirm: <role or person>)

  open_questions:
    - <question> (who can answer, by when)

  risks:
    - <risk> (likelihood, impact, mitigation)

  blockers:
    - <blocker> (what unblocks it)

  next_owner: <role slug>
  acceptance_criteria:
    - <specific, checkable condition>
  authorization: none                   # or the explicit consequential actions allowed, with who approved
  due: <date or "no deadline">
```

## Rules
1. **No silent context loss.** If the receiver would need to ask "why" or "where", the handoff is incomplete.
2. **Evidence over adjectives.** "Tests pass" must point to a run log. "Client approved" must point to a message or record.
3. **Approved decisions are closed.** The receiver may raise a concern, but does not reverse an approved decision without escalation.
4. **Acceptance criteria are checkable.** "Looks good" is not acceptance criteria. "Lighthouse mobile performance at or above 85 on the home page" is.
5. **Authorization travels explicitly.** If `authorization` is `none`, the receiver may not send, publish, spend, deploy or sign.
6. **One owner.** `next_owner` is a single role. Contributors are listed in the task brief, not in the handoff owner field.
7. **Return path.** A receiver that rejects a handoff returns it to `from` with the missing items listed under `open_questions` or `blockers`.

## Minimal handoff (for small internal steps)
For quick steps inside one workflow stage, the minimum is: `task`, `inputs`, `completed_work`, `evidence`, `open_questions`, `next_owner`, `acceptance_criteria`, `authorization`.
