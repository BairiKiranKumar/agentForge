# WF-14: Technical Research and Documentation

Answer a technical question from sources and leave a document someone else can trust.

## Inputs
- The question, the decision it supports, and the date sensitivity.
- The codebase or the links the reader may use.
- The audience: implementer, client, or future agent.
- Authorization. This workflow does not deploy or buy services.

## Specialists
`technical-writer` leads. `solution-architect` or the relevant specialist consults when the question is a design choice. `editor` reviews. `documentation-curator` files the result if it should live in the knowledge set. Several source readers may split documents in parallel when each has a different file.

## Parallel and sequential stages
Source reading is parallel by document or module. The synthesis waits. The edit waits on the synthesis. Do not write the recommendation before the sources are in the notes.

| Stage | Owner | Depends on | Parallel with | Deliverable | Validation | Approval |
|---|---|---|---|---|---|---|
| Reading | assigned specialists | none | other readers, different files | source notes with links and dates | each claim points at a source | lead writer |
| Synthesis | `technical-writer` | Reading | none | the document | separates observed, inferred, and unknown | `editor` |
| Review | `editor` | Synthesis | none | edit notes | unsourced claims flagged | `technical-lead` if the doc sets an engineering standard |
| File | `documentation-curator` | Review | none | index update | path is real | `operations-lead` if it changes the knowledge rules |

## Deliverables
Source notes, the document, and the edit record.

## Validations
Time-sensitive claims carry an as-of date and a primary source. Unverified items are labelled. No invented benchmarks.

## Approval gates
An architecture decision that other projects must follow needs `technical-lead`. Publishing the document outside the repo needs the owner.

## Exit criteria
The question is answered, the unknowns are listed, and the file paths exist.

## Example invocation
"Run WF-14 on how this repo's contact form stores enquiries. Document only. Do not change the form."
