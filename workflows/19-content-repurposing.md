# WF-19: Cross-platform Content Repurposing

Turn one source into platform-native drafts. Do not paste one caption everywhere.

## Inputs
- Source path, brand id, and the platforms worth doing this week.
- Allowed proof and forbidden claims.
- Authorization. Default is drafts.

## Specialists
`content-repurposing-specialist` leads. Native owners: `linkedin-specialist`, `instagram-carousel-maker`, `threads-specialist`, `reels-producer`. Call only the rows in the matrix. `editor` reviews the package. `social-media-manager` receives calendar rows after review.

## Parallel and sequential stages
The digest and the matrix are sequential. After the matrix, each platform row with its own folder runs in parallel. Integration and the editorial pass wait for every row. A missing row stays missing.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| Digest | `content-repurposing-specialist` | none | none | allowed proof and the one idea | source was read | owner if permission is unclear |
| Matrix | `content-repurposing-specialist` | Digest | none | owners, hooks, paths | hooks are not identical | lead |
| Platform drafts | row owners | Matrix | other rows, different paths | native files | form matches the platform | `editor` |
| Integrate | `content-repurposing-specialist` | All rows | none | `index.md` | links resolve, proof still matches the digest | `editor` |
| Calendar | `social-media-manager` | Integrate | none | draft rows | not scheduled live | brand owner to publish |

## Deliverables
Digest, matrix, native drafts, index.

## Validations
No fact outside the digest. No shared output path. No file claimed that is absent.

## Approval gates
Publishing any row needs the brand owner. Client permission limits apply to every row.

## Exit criteria
The index lists real files, the editor has reviewed the words, and nothing is live.

## Example invocation
"Run WF-19 on a homepage build note for example-brand. LinkedIn and Threads only."
