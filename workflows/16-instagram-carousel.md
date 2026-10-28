# WF-16: Instagram Carousel Production

Produce one carousel: research, storyboard, slides, caption, and an honest export status.

## Inputs
- Brand id and the one claim.
- Proof or an explicit method-only instruction.
- Output folder owned by this workflow.
- Authorization. Default is files on disk, not a post.

## Specialists
`instagram-carousel-maker` leads and builds the HTML/SVG. `instagram-specialist` can supply the framework and write the caption in parallel with the slides once the storyboard is fixed. `editor` reviews words. `design-reviewer` reviews a public visual. Lead integrates.

## Parallel and sequential stages
Brand reading and research share the first wave. The storyboard waits for both. Slide art and the caption then share a wave because they use different files. QA waits for both files. See `examples/plans/instagram-carousel.yaml`.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| Brand | `instagram-carousel-maker` | none | Research | note of colors, type, CTA | profile file was read | stop if two brands are named |
| Research | `instagram-specialist` | none | Brand | sources and the claim | nothing invented | `editor` |
| Storyboard | `instagram-carousel-maker` | Brand, Research | none | slide table | 6 to 10 slides, one idea each | `editor` for the headlines |
| Slides | `instagram-carousel-maker` | Storyboard | Caption | `index.html` at 1080 by 1350 | file exists, SVG inline | `design-reviewer` |
| Caption | `instagram-specialist` | Storyboard | Slides | `caption.md` | CTA from the profile | `editor` |
| QA | `design-reviewer` | Slides, Caption | none | QA note | export lines match disk | brand owner to publish |

## Deliverables
Storyboard, HTML artboard, caption, hashtags, alt text, and export status.

## Validations
Open the HTML and confirm the canvas size in the file. PNG and PDF count as done only when those files exist. A sample that states "PNG export was not run" is a valid draft.

## Approval gates
Publishing, collabs, and boosted posts need the brand owner.

## Exit criteria
The HTML and caption exist, the brand matches, and the export status is true.

## Example invocation
"Run WF-16 for example-brand on what makes a website feel premium. HTML draft only."

Sample artifact: `examples/campaigns/example-brand/instagram-carousel/index.html`.
