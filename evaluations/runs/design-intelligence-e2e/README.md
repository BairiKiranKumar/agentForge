# Design Intelligence end-to-end evaluation (WF-21, Tier M, small)

Date: 2026-10-22. One small run of the new workflow with real outputs. Model: Claude Sonnet 5.5 for lead and workers. This is a smoke evaluation, not a scored pass of any role; role statuses stay `untested`.

## Stages and actual outputs
| Stage | Role as run | Output | Note |
|---|---|---|---|
| Research | `design-researcher` (subagent, fetch only) | `design-research-brief.md` | 2 new references (Metabase, Mixpanel) plus 3 KB references. Self-reported shortfalls: one discovery channel instead of three, 5 shortlist items instead of 8 to 12, breadth rule unmet, text-extract inspection, freshness not run |
| Build | `ui-designer` plus `frontend-developer` (subagent) | `candidate/index.html`, `candidate/direction-note.md` | Fictional product, placeholders labelled |
| Control | lead | `control/index.html` | Deliberately generic page (gradient, pills, emoji, glass cards) to test discrimination |
| Capture | lead, headless Chrome (tool tier 2, static) | `captures/*.png` | 375 via iframe; see pitfalls in the browser guide |
| Review | `design-reviewer` (independent subagent, blind: pages named A and B, A = control) | `review/review-A.md`, `review-B.md`, `scores-*.json`, `comparison.md` | Scores computed by `tools/design_kb.py score` |

## Results (as reported by the reviewer, tool output in the review files)
| Page | Weighted | Verdict (high_visibility) | Notes |
|---|---|---|---|
| A (control, generic) | 31.5% | Rethink | Blocker: no demo CTA; 8 anti-slop signals failed the justification test |
| B (candidate) | 68.5% | Revise | Floor missed: accessibility 2 (conservative, static captures only) |

The rubric and tool separated the generic page from the considered one in the expected direction. One sample, one reviewer, so this says nothing about calibration or reliability.

## Reviewer finding that did not hold up
Review B listed a Major: chart bars did not match their values (North 41 filled about 18 percent, others empty). The reviewer hedged that it might be an uncaptured animation. It was: the bars animate in over about a second and the first capture was taken at load. Re-captured with `--virtual-time-budget=3000` (`captures/candidate-settled-*.png`) the bars are correct. The score sheet was not edited; the false positive stays on record. Lesson added to `guides/browser-research-and-qa.md` section 9.

## What this run does not show
- Not a pass for any role. One task each, no second grader, graders were the same model family as the producers.
- The reviewer saw no states below the first screen for page A, no 320 or 1024 widths, no keyboard, motion or measured contrast.
- The researcher stage fell short of its own AGENT.md standards (channels, breadth). That is evidence the role needs a rendering tool and a stronger fetch tool, not a pass.
- `human_approval_required` prints `false` for non-Ship verdicts by design; approval applies only to a Ship verdict.
