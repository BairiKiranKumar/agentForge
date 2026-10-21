# WF-13: UI/UX Design and Implementation

Design a flow and implement that flow. Research and content structure can proceed together. Visual design and code do not.

## Inputs
- The job the user is trying to finish, the screens involved, and the content.
- Brand profile or an existing design system in the repo.
- Accessibility target. Default is WCAG 2.2 AA as the aim, verified only where tested.
- Authorization for any user-facing release. Default is a local implementation.

## Specialists
`ux-designer`, `ui-designer`, `ux-writer`, `frontend-developer`, `accessibility-designer` when the flow is complex, `design-reviewer`, `accessibility-tester`. Lead: `ux-designer` until the flow is accepted, then `frontend-developer`.

## Parallel and sequential stages
User-flow notes and interface copy can be drafted together. High-fidelity UI depends on the flow. Implementation depends on the UI for the screens in this slice. Design review and accessibility review of the build share a wave.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| Flow | `ux-designer` | none | Interface copy | flow and states | empty, error, and success states named | `design-reviewer` |
| Copy | `ux-writer` | none | Flow | microcopy | no filler, errors say what to do | `editor` |
| UI | `ui-designer` | Flow, Copy | none | screen spec | type, space, and contrast described | `design-reviewer` |
| Build | `frontend-developer` | UI | none | implemented screens | matches the spec or lists gaps | `code-reviewer` |
| QA | `accessibility-tester` | Build | `design-reviewer` | findings | tool or method named | `qa-lead` |
| Integrate | `orchestrator` | QA, design review | none | one implementation report | open gaps listed | client or Kiran before release |

## Deliverables
Flow, copy, UI spec, code, and QA notes.

## Validations
Keyboard path on the built screens if a browser is available. If it is not, the report says the keyboard path was not run.

## Approval gates
A new visual direction needs the client or Kiran. Shipping to users needs authorization.

## Exit criteria
The slice is implemented, reviewed, and the untested parts are named.

## Example invocation
"Run WF-13 for the contact flow on an existing marketing site. Local only."
