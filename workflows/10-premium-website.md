# WF-10: Premium Website Development

Build a marketing or brochure website with a distinct research, content, design, implementation, and QA path.

## Inputs
- Brand or client brief, audience, pages, and the offer.
- Proof the copy may use. No invented metrics.
- Stack constraints, or permission for the technical lead to choose.
- Deadline and authorization. Production deploy is off unless the brief allows it.

## Specialists
`competitor-researcher` and `ux-researcher` when the audience is unclear, `copywriter`, `ui-designer`, `frontend-developer`, `nextjs-specialist` only if that framework is chosen, `accessibility-tester`, `performance-tester` when the page is media-heavy, `code-reviewer`, `design-reviewer`. Lead: `frontend-developer` for the build, `ui-designer` for the visual system until handoff. `orchestrator` integrates.

## Parallel and sequential stages
Research and content may run together. They write different files. Design starts when both exist. Implementation starts when the design and the copy for the first template exist. QA starts after a reviewable build. Code review and accessibility review can run in the same wave if they read the build and write separate reports.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| Research | `competitor-researcher` | none | Content | `research.md` with sources | Claims sourced | `research-lead` if the findings change the offer |
| Content | `copywriter` | none | Research | page copy | One offer, no fake proof | `editor` |
| Design | `ui-designer` | Research, Content | none | UI for the templates | Phone and desktop, brand profile if any | `design-reviewer` |
| Implementation | `frontend-developer` | Design | none | working pages | builds locally | `code-reviewer` |
| QA | `accessibility-tester` | Implementation | `code-reviewer` | QA notes | checks that were actually run | `qa-lead` |
| Integrate | `orchestrator` | QA, code review | none | one report | evidence per criterion | Kiran before any production deploy |

## Deliverables
Page copy, UI, implemented templates, review notes, and a report that separates what was run from what was not.

## Validations
Local build or the project's documented check. Accessibility pass on the templates that were built. No claim of Lighthouse scores without a run log.

## Approval gates
Client-facing copy and visual direction need the client or Kiran. DNS, hosting, and production deploy need explicit authorization. Default is a local or preview build.

## Exit criteria
The agreed pages exist in the build, reviews are filed, and anything not verified is listed as not verified.

## Example invocation
"Run WF-10 for a five-page site for a clinic. Draft copy and a local build. Do not deploy."
