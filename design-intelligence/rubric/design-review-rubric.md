# Design review rubric

The scoring standard for rendered design work. The machine-readable weights and thresholds are in `rubric.yaml`; this file explains how to apply them. Compute totals with `python tools/design_kb.py score <scores.json> --profile standard|high_visibility`.

Applies to any digital interface or experience. It names no brand, project or technology.

## Rules of use
1. Review rendered output (screenshots or a live render at stated widths), never a description. If only a description exists, the review is "not reviewable" and cannot pass.
2. The reviewer is independent of the designer and implementer (`design-reviewer` per `AGENTS.md` section 7).
3. Score each criterion 0 to 4 using the anchors below. Any score of 2 or below needs a finding with evidence: location, observation, impact, fix direction, owner.
4. Praise is also evidence. Record a Keep list.
5. Compare against the approved creative direction. A different direction is not a defect unless it breaks the brief; record it as a deviation for `creative-director` to rule on.
6. No technique is banned universally. Judge whether a choice serves the user, the content, the brand and the experience. See `anti-slop.md`.
7. Taste notes are labelled and never block.

## Criteria and anchors
Scale: 0 absent or harmful, 1 weak, 2 acceptable, 3 strong, 4 exceptional.

| Criterion (weight) | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Originality (14) | Reads as a stock template; could be any product | Competent but predictable; a known pattern with little adaptation | A distinct idea grounded in the subject; some defaults replaced | A memorable, ownable idea that could not belong to another subject, still usable |
| Art direction (12) | No consistent visual idea | Style applied unevenly | Clear, consistent direction visible across pages and sizes | Direction shapes every decision, with one deliberate signature moment |
| Composition (12) | Cluttered or flat; no focal point | Orderly but monotonous rhythm | Clear focal points, varied rhythm, purposeful whitespace | Composition guides attention and pacing across the whole journey |
| Typography (12) | Default fonts, no scale | Readable, limited scale | Intentional pairing, consistent scale, good measure and leading | Typography carries personality and hierarchy; excellent at every size and script used |
| Imagery (8) | Generic or low quality | Fine but interchangeable | Specific, well cropped, consistent treatment | Imagery is distinctive, rights-clear and integral to the idea |
| Interaction quality (10) | Missing states, feedback or confusing behaviour | Core states present | Hover, focus, active, loading, empty and error states handled; motion has purpose | Interaction feels considered; motion clarifies; reduced-motion alternative is good |
| Responsive execution (10) | Breaks or crops badly | Reflows but feels shrunk desktop | Designed per breakpoint; touch targets and content priority adapted | Each size feels native to its device; no loss of meaning |
| Usability (10) | Primary action unclear | Task completable with friction | Clear primary path, good labels, low effort | Effortless; errors prevented; content matches expectations |
| Accessibility (8) | Fails AA basics | Meets basics with gaps | Meets WCAG 2.2 AA on checked items; keyboard path works | AA throughout, strong focus design, motion and contrast handled with care |
| Technical feasibility (4) | Cannot be built as shown or ignores budgets | Buildable with unresolved cost | Buildable within stated budgets | Buildable, with fallbacks and clear performance plan |

Weights sum to 100. The weighted percentage is `sum(weight * score / 4)`.

## Acceptance
| Profile | Weighted minimum | Revise band | Floors | Human approval |
|---|---|---|---|---|
| standard | 65 | 50 to 64 | accessibility 2, usability 2 | not required |
| high_visibility | 80 | 65 to 79 | accessibility 3, usability 3, originality 3, art direction 3, typography 3, composition 3 | required (Kiran or the client) |

Verdicts map to the existing design-review verdicts:
- **Ship**: meets the profile's weighted minimum, every floor, and no gate is triggered.
- **Revise**: in the revise band, or a floor is missed, or a gate fixable without changing direction is triggered. List exact conditions for Ship.
- **Rethink**: weighted result below the revise band, or originality and art direction both 1 or lower. Return to `creative-director`.

Gates (any one prevents Ship): open Blocker finding; accessibility 1 or lower; review based on description only; reviewer not independent.

Use `high_visibility` for launches, flagship pages and public campaigns, and whenever the requester asks for it. Human approval is recorded in the handoff `authorization` field.

## Finding format
```
| ID | Severity | Criterion | Where (viewport, section) | Evidence (observed) | Impact | Fix direction | Owner |
```
Severity: Blocker, Major, Minor, Taste (as in `design-reviewer`).

## Score sheet (JSON for the scoring tool)
```json
{"originality": 3, "art_direction": 3, "composition": 3, "typography": 3, "imagery": 2,
 "interaction": 3, "responsive": 3, "usability": 3, "accessibility": 3, "feasibility": 3,
 "gates": [], "open_blockers": 0}
```

## Limits
The rubric measures craft and fit against stated criteria. It does not measure user outcomes. Pair it with usability testing when outcomes matter. Scores from different reviewers are not directly comparable until a calibration set has been scored by both (see the evaluation tasks).
