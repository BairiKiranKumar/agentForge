# WF-20: Client Website Showcase Campaign

Turn a permissioned website project into a small campaign: a case-study draft and the social cuts that the permission allows.

## Inputs
- The project, what the client allows in public, and what is forbidden.
- Brand id for the studio channel, separate from the client's brand.
- Screenshots or a URL the client said can be shown.
- Authorization. Default is drafts. Sending the draft to the client for permission is still a send and needs approval.

## Specialists
`case-study-writer` owns the study. `content-repurposing-specialist` owns the cuts. `ui-designer` or `instagram-carousel-maker` produces visuals from approved screenshots only. `editor` reviews. `client-communication-specialist` drafts the permission request if one is still needed. Lead: `content-repurposing-specialist` for the campaign, `case-study-writer` for the study text.

## Parallel and sequential stages
The permission note is blocking. After it exists, the case-study draft and a visual inventory can run together. Social cuts wait for the study's allowed facts. They then run in parallel by platform. Nothing is sent to the client or posted without a gate.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| Permission | `client-communication-specialist` | none | none | what may be public | forbidden items listed | Kiran before any message is sent |
| Study | `case-study-writer` | Permission | Visual inventory | case-study draft | only allowed facts | `editor` |
| Visual inventory | `ui-designer` | Permission | Study | list of screens that are allowed | no extra screens | `design-reviewer` |
| Cuts | `content-repurposing-specialist` | Study | platform rows after the matrix | native drafts | proof stays inside the study | `editor` |
| Integrate | `orchestrator` | Cuts, visuals | none | campaign folder | every public claim traces to the permission | Kiran to send or publish |

## Deliverables
Permission record, case-study draft, visual list, social drafts, and a status that nothing was sent unless authorization said so.

## Validations
Compare every public sentence to the permission note. Client brand and studio brand are not mixed in one voice.

## Approval gates
Messages to the client, posts, and ads need Kiran. A draft folder does not.

## Exit criteria
The campaign folder matches the permission, reviews are filed, and sends are either done with authorization or still waiting.

## Example invocation
"Run WF-20 for a school site. Permission: city and page list, no fees and no student data. Drafts only. Do not email the school."
