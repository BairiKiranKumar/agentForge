## Design review: Page A (DataFlow), round 1, stage pre-launch
Reviewer independence: did not produce this artefact (yes)
Lens: data and operations leads at mid-size companies; job: judge whether to request a demo; primary action: request a demo (per brief). Profile: high_visibility.
Inputs reviewed: brief.md; page-A-375.png, page-A-768.png, page-A-1440.png (headless Chrome static captures).

### Evidence tier
Tier 2 style, static captures supplied by others (not captured by me). Widths seen: 375, 768, 1440. Not seen: 320, 1024, any scroll below the first screen, hover, focus, active, loading, error states, keyboard behaviour, motion and reduced motion, measured contrast values (contrast notes are by eye and labelled [Inference]). Page source was not read. No approved art-direction document exists, so no direction comparison was possible; judged against the brief.

Verdict: Rethink. The page does not offer the brief's primary action and has no distinctive idea.
Conditions to reach Ship: a new direction from creative-director grounded in the product; a "Request a demo" primary CTA; a real second section; AA contrast verified by measurement; interaction states evidenced; human approval (Kiran or client) recorded.

### Scores (0 to 4)
| Criterion | Score | Basis |
|---|---|---|
| Originality | 1 | Violet-to-blue gradient, pill badge, three icon cards, "Unlock the power of your data": could be any product |
| Art direction | 1 | One idea (gradient) used as a default; no signature, no link to analytics or the audience |
| Composition | 1 | Centred stack and 3-up cards; at 768 and 1440 the area below the cards is an empty gradient band (the "further section" shows no content); at 375 cards are clipped at the right edge |
| Typography | 1 | One default-looking sans, bold white headline with a gradient word; no evident pairing or scale beyond headline versus body; small body on gradient |
| Imagery | 1 | No imagery; emoji as icons; no product view or data shown |
| Interaction | 1 | Cannot be judged from statics. Scored conservatively: no states evidenced. This is not a claim that none exist |
| Responsive | 2 | Reflows at all three widths, but at 375 the cards are cut off with only a fade hint and no visible scroll cue; desktop structure is largely stacked or shrunk |
| Usability | 1 | Only CTA is "Get started"; no demo request; copy gives no concrete value to data leads |
| Accessibility | 2 | Contrast borderline by eye in places; focus and keyboard not observed. Capped at 2 for lack of evidence |
| Feasibility | 3 | Simple build; gradient and cards are cheap. Judged from captures only |

### Findings
| ID | Severity | Criterion | Where | Evidence (observed) | Impact | Fix direction | Owner |
|---|---|---|---|---|---|---|---|
| A1 | Blocker | Usability | All widths, hero | The only button reads "Get started"; no "Request a demo" in any capture | The brief's primary action is absent, so the page cannot meet its goal | Make "Request a demo" the single primary CTA in hero and header | conversion-designer |
| A2 | Major | Originality | All widths | Headline "Unlock the power of your data"; subline "all-in-one platform to supercharge your insights and take your business to the next level" | Vague copy that fits any product; gives data leads no reason to act | Replace with a specific claim about what the product does for these leads | copywriter |
| A3 | Major | Composition | 768, 1440, below cards | A full-width gradient band under the cards has no content; the brief's "further section" is not visible | Looks unfinished; brief asked for a second section | Add the second section or remove the empty band; confirm with a longer capture | ui-designer |
| A4 | Major | Accessibility | 375 to 1440, cards | White body text on mid-blue translucent cards (right card lightest). [Inference] may be under 4.5:1; not measured | AA basics risk for body text | Measure; darken card fill or text backing to reach 4.5:1 | ui-designer |
| A5 | Major | Responsive | 375, cards row | "Scalable" card cut at the page edge; "Fast" and "Secure" copy truncated; no scroll cue seen | Content hidden on the primary viewing width | Stack cards at 375 or add a clear horizontal affordance | ui-designer |
| A6 | Major | Imagery | All widths | Emoji (rocket, lock, chart) as feature icons; no product visual | Generic, renders differently per platform, shows nothing of the product | Use a consistent icon set or a real product view | illustrator |
| A7 | Minor | Accessibility | 375 to 1440 | "Now with AI" pill text about 12 to 13 px on translucent violet [Inference] | Small, possibly low contrast | Raise size and contrast or drop the pill | ui-designer |
| A8 | Minor | Typography | 375 | Headline breaks to three lines; subline ends with an orphan "level." | Awkward rag | Tune size and measure at 375 | ui-designer |
| A9 | Minor | Usability | 375, nav | Three nav links sit close to the logo; targets look under 44 px high [Inference] | Touch risk | Measure target size | ui-designer |

### Anti-slop signals (justification test applied)
| Signal id | Evidence | Purpose and fit test | Result | Criterion |
|---|---|---|---|---|
| overused-gradient | Full-page violet to blue gradient; gradient on "your data" | Encodes no data or meaning; could be pasted on any product (fails 1 and 2) | Finding | Art direction |
| default-ai-visual-pattern | Gradient, pill badge, rounded translucent cards, one accent | No direction document or recorded decision (fails 2) | Finding | Originality, Art direction |
| repetitive-generic-layout | Hero then three-up features | Content (Fast, Secure, Scalable) is generic, not ordered for a task (fails 2) | Finding | Originality, Composition |
| excessive-rounded-cards | Three identical rounded translucent cards, same shadow | Grouping adds no meaning | Finding | Composition |
| unnecessary-glassmorphism | Translucent cards over gradient | Contrast unmeasured; legibility uncertain (A4) | Finding pending measurement | Composition, Accessibility |
| generic-copywriting | "Unlock the power", "supercharge", "next level" | Interchangeable (fails 2) | Finding A2 | Originality |
| unnecessary-decoration | Emoji icons, sparkle in pill | No function beyond decoration | Finding A6 | Imagery, Art direction |
| weak-mobile-layout | Clipped card row at 375 | Not a simple stack | Finding A5 | Responsive |
| weak-interaction-states | Not observable | Cannot be judged from statics | Not a defect finding; interaction scored conservatively | Interaction |

### Taste notes (non-blocking)
The warm gold gradient on "your data" gives lively contrast against the violet; some will like it.

### Keep
- Single-column hero order: headline, subline, button.
- White pill button has strong contrast against the violet.
- Header with logo left and nav right at 768 and 1440.

### Not reviewed / could not check
320 and 1024 widths; below-the-fold content; interaction states; keyboard; motion; measured contrast; performance.

### Assumptions, open questions, risks
If a demo CTA exists lower on the page, A1 drops to Major, but the hero CTA mismatch remains. Scores and verdict apply to the supplied captures only. The tool reports human_approval_required false even for high_visibility; the rubric requires recorded human approval before delivery regardless.

### Score tool output (real output)

```
python tools/design_kb.py score scores-A.json --profile high_visibility
{
  "profile": "high_visibility",
  "weighted_percent": 31.5,
  "weighted_min": 80,
  "floors_missed": [
    "accessibility",
    "usability",
    "originality",
    "art_direction",
    "typography",
    "composition"
  ],
  "gates_triggered": [
    "open blocker finding"
  ],
  "verdict": "Rethink",
  "human_approval_required": false
}
```
