## Design review: Page B (Tallyfield), round 1, stage pre-launch
Reviewer independence: did not produce this artefact (yes)
Lens: finance and operations leads at mid-size companies; job: decide whether the product's answers can be trusted; primary action: request a demo. Profile: high_visibility.
Inputs reviewed: brief.md; page-B-375.png, page-B-768.png, page-B-1440.png (headless Chrome static captures).

### Evidence tier
Tier 2 style, static captures supplied by others (not captured by me). Widths seen: 375, 768, 1440. Not seen: 320, 1024, content below the first screen (1440 shows only the start of a dark band at the foot), hover, focus, active, loading, error states, keyboard, motion, reduced motion, measured contrast. Contrast and size notes are by eye and labelled [Inference]. Page source not read. No approved art-direction document; judged against the brief.

Verdict: Revise. The direction is distinctive and fits the brief; the chart encoding, visible internal placeholder wording and unverified accessibility keep it below the high_visibility floors.
Conditions to reach Ship: fix the chart bars (B1); replace placeholder wording and proof slots with approved real content (B2, B3); evidence the section below the hero; measure contrast and small mono text (B4); show focus, hover and reduced-motion behaviour; record human approval (Kiran or client).

### Scores (0 to 4)
| Criterion | Score | Basis |
|---|---|---|
| Originality | 3 | Idea grounded in the subject: "Every answer shows its working", the query shown beside the result, tally-mark logo. Hero-left, product-card-right is a known pattern, so not 4 |
| Art direction | 3 | Paper ground, ink, deep green, rust accent, mono plus serif, consistent at three widths; hard offset shadow on the card is a repeated motif. No separate signature moment beyond the query card |
| Composition | 3 | 1440: two columns with a strong focal card, rule-separated proof row, dark band beginning. 375: logical stack. Purposeful whitespace. Proof row is thin |
| Typography | 3 | Serif display with italic emphasis plus mono for data; consistent scale; body measure about 70 to 80 characters at 1440 (slightly long); some mono text looks about 10 to 11 px [Inference] |
| Imagery | 2 | No photography; the query card is the image and is on idea, but its chart bars are visibly wrong (B1) |
| Interaction | 2 | Cannot be judged from statics. Scored conservatively; primary and secondary buttons are visually distinct, but hover, focus and loading were not observed |
| Responsive | 3 | Structure changes per width: 1440 two columns, 768 stacked with an extra nav item, 375 nav reduced to the CTA and buttons full width; targets look 44 px or more [Inference] |
| Usability | 3 | "Request a demo" is dominant in header and hero at every width; "Try the sample data" is clearly secondary. The placeholder note disrupts trust (B2) |
| Accessibility | 2 | Dark ink on cream and white on green look strong by eye; small mono text, grey body text and the rust label are unmeasured; focus and keyboard unseen. Capped at 2 for lack of evidence, not for a found failure |
| Feasibility | 3 | Plain layout; two families plus mono is a mild cost. Judged from captures |

### Findings
| ID | Severity | Criterion | Where | Evidence (observed) | Impact | Fix direction | Owner |
|---|---|---|---|---|---|---|---|
| B1 | Major | Imagery, Usability | 375, 768, 1440, chart card | "Average days to pay, by region": North (41) fills about 18 percent of its track; East 33, West 27, South 22 show no bar fill | The page's idea is "every answer shows its working", yet the chart does not match its own numbers; undermines trust. If the fill is an animation not captured, statics cannot settle it | Scale bar fill to value and capture a settled final state | frontend-developer |
| B2 | Major | Usability | 375 to 1440, under hero buttons | Visible note: "Placeholder wording: your security and legal owners must supply the real data-handling statement before launch." | Internal production note on a launch candidate; not launch copy | Replace with an approved data-handling statement | content owner, legal owner (Kiran to confirm) |
| B3 | Major | Usability | 1440, proof row | "CUSTOMER PROOF: PLACEHOLDER SLOTS, NONE CLAIMED" with dashed bracket boxes | Honest, no fake proof, but empty slots carry no persuasion on a launch page | Fill with real, permitted proof or remove the row until it exists | content owner |
| B4 | Minor | Accessibility, Typography | 375 to 1440 | Mono captions ("ILLUSTRATIVE PAGE...", chart footnote, chart header) look about 10 to 11 px; rust label on cream [Inference] | Possible AA and legibility gap | Measure size and contrast; raise captions toward 12 px or more and verify 4.5:1 | ui-designer |
| B5 | Minor | Responsive | 375, chart card | Card header "sample_workspace / illustrative" and "placeholder data" each wrap to two lines; the offset shadow shows a notch at the right edge | Slight clutter at the primary width | Stack or shorten header labels at 375 | ui-designer |
| B6 | Minor | Typography | 1440, hero | Body about 70 to 80 characters per line | Mild readability cost | Cap measure near 65 characters | ui-designer |
| B7 | Minor | Composition | 768, 1440 | The brief's further section is only a proof row and the start of a dark band; nothing below is captured | Cannot confirm the second section | Provide full-page captures | ui-designer |
| B8 | Taste | Composition | 375 | Hero text, two buttons and the note fill more than one screen before the chart appears | Chart is below the first screen at 375; purely order preference | Consider chart earlier; optional | ux-designer |

### Anti-slop signals (justification test applied)
| Signal id | Evidence | Test | Result |
|---|---|---|---|
| repetitive-generic-layout | Hero left, product card right at 1440 | Purpose: shows the differentiator beside the claim; fit: the card is the product's own idea | Acceptable, recorded |
| excessive-rounded-cards | One card with square corners and a hard offset shadow | Not a pattern here | Not flagged |
| overused-gradient | None seen | | Not flagged |
| generic-copywriting | "Every answer shows its working" | Specific and tied to the subject | Not flagged |
| generic-stock-imagery | No imagery besides the chart | | Not flagged; imagery thin (B1) |
| unnecessary-decoration | Tally-mark logo, dashed proof slots | Logo ties to the "working" idea; slots mark missing content (B3) | Acceptable for logo |
| weak-interaction-states | Not observable | Cannot be judged from statics | Interaction scored conservatively |
No unjustified signal found. Absence of signals does not prove quality.

### Taste notes (non-blocking)
Italic green "working" is effective; the offset shadow is a strong motif. B8 is taste.

### Keep
- Headline with italic emphasis.
- Query plus chart card as the product proof (ASK and SQL lines above the result).
- Single dominant "Request a demo" CTA in header and hero at every width with a clear secondary style.
- Honest labelling ("illustrative", "placeholder data", no invented proof).
- Palette and type pairing; 375 nav reduced to the CTA.

### Not reviewed / could not check
320 and 1024 widths; content below the first screen; interaction states; keyboard; motion; measured contrast; performance.

### Assumptions, open questions, risks
Assumes the empty chart bars are static, not mid-animation. Scores reflect captures only. Placeholder items may be deliberate for a draft; for a launch candidate they are open. The tool reports human_approval_required false even for high_visibility; the rubric requires recorded human approval before delivery regardless.

### Score tool output (real output)

```
python tools/design_kb.py score scores-B.json --profile high_visibility
{
  "profile": "high_visibility",
  "weighted_percent": 68.5,
  "weighted_min": 80,
  "floors_missed": [
    "accessibility"
  ],
  "gates_triggered": [],
  "verdict": "Revise",
  "human_approval_required": false
}
```
