```yaml
handoff:
  id: HO-<workflow>-<n>
  workflow: <workflows/xx-name.md or "ad hoc">
  stage: <stage>
  from: <role-slug>
  to: <role-slug>
  date: <YYYY-MM-DD>
  task: <one sentence>
  objective: <outcome this serves>
  context:
    summary: <short background>
    approved_decisions:
      - id: D-1
        decision: <text>
        approved_by: <who>
    constraints: []
  inputs:
    - path: <path or URL>
      description: <what and version>
  completed_work: []
  evidence:
    - check: <what was checked>
      result: <observed result>
      location: <where the proof lives>
  assumptions: []
  open_questions: []
  risks: []
  blockers: []
  next_owner: <role-slug>
  acceptance_criteria: []
  authorization: none
  due: <date>
```
