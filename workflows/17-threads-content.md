# WF-17: Threads Content Creation

Draft short conversational posts for Threads. The owner is `threads-specialist` (alias Threads Content Creator).

## Inputs
- Brand id and the week's material: builds, mistakes, questions, or a method.
- The goal: conversation, profile visits, or a later enquiry. Not a fake viral target.
- Any offer, with the price confirmed by the owner if a price is mentioned.
- Authorization. Default is drafts.

## Specialists
`threads-specialist` writes. `proofreader` checks. `editor` joins for a chain or a text attachment. `social-media-manager` may place the approved draft on the calendar. No second writer on the same post file.

## Parallel and sequential stages
Several posts in one week can be drafted together only when each post has its own file and its own proof. The proofreader wave waits for the drafts. Do not parallelize two agents into one post.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| Select | `threads-specialist` | none | none | 5 to 7 ideas or fewer if the source is thin | one idea each | owner if a post names a person |
| Drafts | `threads-specialist` | Select | one file per post, same owner, sequential writes | post files with three hooks | under 500 characters, one topic tag | `proofreader` |
| Proof | `proofreader` | Drafts | none | marked files | bait and unsourced numbers flagged | `editor` if a chain is long |
| Stage | `social-media-manager` | Proof | none | draft calendar rows | not live | brand owner to publish |

## Deliverables
Hooks, the posts, reply notes, and character counts.

## Validations
Counts are shown. Distribution claims are labelled as hypotheses. No rage bait and no copied viral post.

## Approval gates
Publishing and outbound replies that mention a private person need the owner. Default authorization is none.

## Exit criteria
Drafts the proofreader has seen, or a shorter set because the source could not fill a week.

## Example invocation
"Run WF-17 for example-brand. Three posts about a homepage decision. Draft only."
