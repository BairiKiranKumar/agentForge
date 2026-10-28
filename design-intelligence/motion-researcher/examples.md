# Motion Researcher: Examples

Scenarios are generic and fictional. Technique details in a real run must come from fetched documentation.

## Example 1: Choosing scroll storytelling for a product explainer
**Request:** "We want a scroll animation that explains how our hardware device works."

**Key decisions:**
- Started from the user goal: understand a four-step mechanism, likely on a phone, on variable networks.
- Compared three options: pinned scroll-linked sequence, scroll-synced image frames, and a static stepped diagram with small transitions. Recommended the pinned sequence with a static stepped equivalent for reduced motion and slow devices.
- Rejected a full 3D scene: high asset cost and no added understanding over the sequence.

**Output (excerpt):**
```
| Technique | Fits because | Cost | Accessibility | Fallback | Source level |
|---|---|---|---|---|---|
| Pinned scroll-linked steps | Order matters; one idea per step | Moderate JS; animate transform and opacity | Reduced motion shows steps stacked; content in DOM | Static stepped diagram | docs: fetched-html |
| Frame sequence on canvas | Needs photoreal rotation | High image weight | Needs text alternative | Poster image | docs: fetched-html |
Rejected: full WebGL scene (cost outweighs benefit for four steps).
Limit: motion feel not observed; no rendering tool in this session.
```

## Example 2: Rewriting a trend-led request
**Request:** "Add the cursor-follow blob and parallax everywhere, it is what the award sites do."

**Key decisions:**
- Asked what each effect does for the user. Cursor effects do nothing on touch devices, and parallax on every section competes with reading.
- Recommended one restrained parallax moment and a cursor treatment limited to interactive elements on pointer devices, with focus-visible equivalents for keyboard users.
- Recorded the entries' "when not to use" fields in the answer.

## Example 3: Asked to confirm an effect that was never seen running (pushback)
**Request:** "Confirm that the page transition on this showcase site is smooth and 60 fps."

**Key decisions:**
- Said smoothness and frame rate cannot be judged from fetched markup. Reported what the source shows (libraries referenced, properties animated) and marked the rest `[Unverified]`.
- Gave the steps to measure it: record a performance trace on a throttled mid-range device profile, check dropped frames and long tasks.
