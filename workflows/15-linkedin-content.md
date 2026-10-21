# WF-15: LinkedIn Content Creation

Draft a LinkedIn post, article, or document-post script for one brand profile. The owner is `linkedin-specialist` (alias LinkedIn Content Creator).

## Inputs
- Brand id. Use `kiranbuildswithai` only for that handle.
- The idea, the proof, and the format: text, article, document, or single image.
- Audience and the ask.
- Authorization. Default is a draft. Posting needs the brand owner.

## Specialists
`linkedin-specialist` leads. `case-study-writer` joins when the piece is a permissioned case study. `editor` reviews. `canva-specialist` or `presentation-designer` produces a designed document only when the brief asks for a designed file rather than a script. `marketing-analyst` is not in the draft wave.

## Parallel and sequential stages
Proof check and the graphic brief can run together after the angle is chosen. They write different files. The final copy waits if it must mention a number from the proof check. Editorial review is last.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| Angle | `linkedin-specialist` | none | none | two hooks and the format choice | first lines fit the fold | `content-strategist` only if the angle fights the pillar |
| Proof | `linkedin-specialist` | Angle | Graphic brief | proof lines with sources | no unsourced numbers | `editor` |
| Graphic brief | `linkedin-specialist` | Angle | Proof | slide or image script | one idea per slide | `design-reviewer` if a designed file will be public |
| Draft | `linkedin-specialist` | Proof | none | post or article draft | one idea, one CTA | `editor` |
| Stage for review | `social-media-manager` | Draft | none | calendar row in draft | not live | Kiran or the brand owner to publish |

## Deliverables
Hook options, the draft, alt text if there is an image, and the proof list.

## Validations
Character and fold checks are labelled with the date they were last verified. Client names appear only with permission.

## Approval gates
Publishing and messaging people from the post need the owner. Default authorization is none.

## Exit criteria
A draft the editor has seen, or a blocked note that names the missing proof.

## Example invocation
"Run WF-15 for kiranbuildswithai. Text post on removing sliders. Draft only."
