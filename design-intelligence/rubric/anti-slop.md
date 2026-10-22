# Anti-slop standards

"Slop" is design that arrives by default: the first output a tool or a habit produces, shipped without a reason. This file gives reviewers and designers a shared way to spot it and, more important, to decide whether a choice is justified.

No technique is banned universally. A gradient, a card, a glass panel or a scroll animation can be exactly right. The question is always: does this choice serve the user, the content, the brand and the intended experience, and can you say how?

## The justification test
For any flagged choice, ask in order:
1. **Purpose**: what job does it do for the user or content?
2. **Fit**: does it come from this subject, brand and audience, or could it be pasted onto any product?
3. **Alternatives**: was another approach considered?
4. **Cost**: what does it cost in attention, performance, accessibility or maintenance?
5. **Consistency**: is it used with discipline, or sprinkled?
A flagged choice that passes 1 and 2 with evidence is acceptable. Record the reason. A flagged choice that fails 1 or 2 is a finding.

## Signals
Each signal maps to a rubric criterion in `design-review-rubric.md`. "Often fine when" lists conditions where the choice can be justified. "Evidence to cite" is what the reviewer must point to.

| Signal id | What it looks like | Often fine when | Evidence to cite | Criterion |
|---|---|---|---|---|
| repetitive-generic-layout | Same hero, three-up features, testimonial strip, CTA band on every page | The content truly is parallel and the order supports a task | Section order across pages; content that does not fit the structure | Originality, Composition |
| default-ai-visual-pattern | Output matches the tool's first-draft look: familiar palette, rounded everything, soft shadows, one accent | A conventional look is a deliberate trust choice for the audience | Direction document versus result; no decision recorded | Originality, Art direction |
| overused-gradient | Gradient backgrounds or text with no semantic role | Gradient encodes data, depth in a product image, or is the brand idea | Where gradients appear; what they communicate | Art direction |
| unnecessary-glassmorphism | Blurred translucent panels over busy backgrounds | Layering clarifies hierarchy and contrast still passes | Contrast measurement; legibility over the background | Composition, Accessibility |
| excessive-rounded-cards | Everything is a rounded card with a shadow | Cards are the right unit for browsable, comparable items | Count of cards; whether grouping adds meaning | Composition |
| weak-typography | One default family, no scale, tight or loose leading, long lines | A restrained single family with strong scale and rhythm | Measured sizes, line length, leading, fallback behaviour | Typography |
| poor-visual-hierarchy | Everything equal weight; blur test shows no focal point | Flat hierarchy is intended for a reference or list page | Blur test result; primary action location | Composition, Usability |
| generic-stock-imagery | Interchangeable stock or synthetic imagery of people at laptops | Real, relevant, rights-cleared imagery that happens to be stock | Image source and rights; relevance to the subject | Imagery |
| unnecessary-decoration | Shapes, blobs, icons and flourishes without function | Decoration carries brand identity and does not compete with content | What it adds; what happens if removed | Composition, Art direction |
| inconsistent-spacing | Gaps and paddings vary without a scale | Variation follows a visible rhythm | Measured values across components | Composition |
| predictable-section-composition | Alternating left/right image-text blocks throughout | Alternation supports comparison or narrative order | Section layouts in sequence | Originality |
| meaningless-motion | Entrance fades and slides on every element | Motion shows cause and effect or sequence | Which motions have a stated purpose | Interaction |
| excessive-animation | Many simultaneous or long animations; scroll hijacking | A single showpiece moment with a static alternative | Count, duration, performance trace, reduced-motion behaviour | Interaction, Accessibility |
| weak-mobile-layout | Shrunk desktop; tiny targets; hidden primary action | Content genuinely suits a simple stack | Captures at narrow widths; target sizes | Responsive |
| generic-copywriting | Vague, superlative or filler headlines | Plain functional labels where clarity is the goal | Quoted lines; whether they could apply to any product | Originality, Usability |
| uninspired-navigation | Default menu with no thought for the task or structure | Convention is right for the task and the audience | Navigation versus the main user journeys | Usability |
| inconsistent-components | Same component looks or behaves differently across pages | Variants are documented and purposeful | Side-by-side captures | Interaction, Composition |
| poor-footer | Link dump with no hierarchy or purpose | A simple footer fits a simple site | Footer structure versus user needs at page end | Composition, Usability |
| weak-interaction-states | Missing hover, focus, active, loading, empty or error states | None. Missing focus and error states are rarely justified | States present versus required | Interaction, Accessibility |

## How to report
Cite the signal id, the evidence, the criterion affected and the fix direction. Do not write "looks AI-generated". Write what is observable and why it fails the user or brief.

## Limits
- Signals are heuristics. Several together are stronger evidence than one.
- Absence of every signal does not prove quality. Score the rubric criteria, not only the signal list.
- The list ages. Review it when the knowledge base is refreshed and add or retire signals with evidence.
