# UX standard (version 1.0.0)

As-of date: 2026-10-22. Machine-readable requirements: `requirements.yaml` (UX-001 to UX-032). Meeting these is evidence of good practice, not certification.

## Scope and non-goals

In scope: information architecture, user journeys, task completion, navigation, forms, errors, states (empty, loading, success, disabled), feedback, user control, progressive disclosure, consistent components, design tokens, conversion flows, content clarity and reusable accessible interaction patterns.

Non-goals: visual brand design, market research methods in depth, analytics implementation, pricing or business model decisions, and legal compliance for consent or consumer law. Accessibility detail lives in the accessibility area; UX requirements point to it where they meet.

## How to apply by product type

| Product type | Applies |
|---|---|
| website | Journeys, IA, navigation, content, forms, conversion flows, states |
| web-app | All, with weight on states, errors, long operations, undo and consistency |
| mobile-web | As website and web-app, with the responsive area for touch and viewport concerns |
| internal-tool | Task completion, forms, errors, consistency, efficiency; conversion flows are usually not applicable |
| ai-app | Status, control, recoverability (UX-032) plus the general items |
| library | Component consistency, tokens, states, patterns (UX-020, 021, 022, 029) |
| api | Not applicable, except developer-facing documentation clarity which belongs to the documentation owners |

Profile intent: `lightweight` keeps navigation clarity, error wording, plain content, link and button labels, and a clear primary action. `standard` adds the full set of journeys, states, tokens and testing. `high_assurance` adds expert-path efficiency testing (UX-028). Usability testing (UX-004) is `standard` and applies from there up.

## Evidence base (all read 2026-10-22)

- Nielsen Norman Group ten usability heuristics: the checklist of principles used as the review lens across the requirements. They are heuristics from an expert body, not laws; use them with user testing, not instead of it.
- NN/g Usability 101: five components of usability and the guidance to test unaided with representative users in small, iterative rounds.
- NN/g progressive disclosure: defer rarely used features, base the split on evidence, keep to about two levels.
- NN/g empty states: show status instead of blank space, teach in context, provide a next step, avoid no-results while loading.
- NN/g response time limits: about 0.1 s feels instant, about 1 s keeps flow, about 10 s is the limit of attention and needs progress and cancel. These are the article's figures, and they are used as design guidance rather than hard acceptance thresholds.
- GOV.UK Design System error message: placement, wording, keep input, summary. A public-sector pattern used here as one documented example, not a mandate.
- Design Tokens Community Group format: a draft Community Group report, not a W3C standard; do not treat it as stable (the page warns against implementing the preview draft; the latest published version listed is 2025.10).
- WCAG 2.2 Understanding pages for error identification, consistent navigation, error prevention, timing and accessible authentication, cited where UX decisions meet accessibility criteria.

## Methods and measurement procedure

1. Task analysis: list users and primary tasks with success measures (UX-001).
2. Structure validation: test findability of key items with a card sort, tree test or task-based check (UX-002, 005). Use a small, honest sample and report its size.
3. Journey review: walk each journey including failure paths (UX-003).
4. State inventory: for each view and component, capture default, loading, empty, error, success and disabled states (UX-008 to 011, 022).
5. Heuristic review by a reviewer who did not design the screens, using the ten heuristics, with each finding given a severity.
6. Usability test: unaided tasks with representative users; record completion, errors, time, and quotes. Fix and retest (UX-004).
7. Content review: read labels, errors, help and confirmation copy out of context (UX-012, 024, 025).
8. Conversion flow review where applicable: count steps, check cost and consent clarity, and compare with analytics only if data exists (UX-023).

Sample sizes, benchmarks and conversion uplifts must come from a source or a measurement. Otherwise label them `[Unverified]`.

## Test matrix

P = primary, S = supporting, - = not useful.

| Requirement area | Heuristic review | Usability test with users | Content review | Analytics (if available) | Accessibility check | Design system audit |
|---|---|---|---|---|---|---|
| Task definition and journeys | S | P | - | S | - | - |
| Information architecture and navigation | S | P (findability) | S | S | S | - |
| Feedback and system status | P | S | - | - | S | - |
| Loading, empty, success, disabled states | P | S | S | - | S | S |
| Errors and recovery | P | P | P | S | P | - |
| Forms | P | P | S | S | P | - |
| User control, undo, time limits | P | P | - | - | S | - |
| Progressive disclosure | S | P | - | S | - | - |
| Consistent components and tokens | S | - | - | - | S | P |
| Conversion flows | S | P | P | P | S | - |
| Content clarity, labels | S | P | P | - | S | - |
| Accessible interaction patterns | S | S | - | - | P | P |

## Severity classification

| Severity | Definition | Examples |
|---|---|---|
| critical | Reserved for a defect that blocks a primary task for users or exposes users or data; no UX requirement defaults to critical, but a project may raise one | Checkout cannot be completed because the only confirm control is unreachable; delete runs with no confirmation and no undo on irreversible user data |
| major | Users fail or struggle with a primary task, lose data, or are misled | Generic error with no fix; input cleared after error; misleading label; no cancel in a long operation; hidden cost until the last step |
| minor | Friction or inconsistency that users overcome | Slightly different button style for the same job; empty state without a next step; unexplained disabled button on a secondary view |

## Recording planned versus executed checks

For each requirement record planned method, executed method with date and reviewer, sample size for any user test, result and evidence link. Mark expert review and user evidence separately: heuristic review is expert opinion and does not replace usability testing. Analytics observations and qualitative findings are recorded separately. Never record a test as passed without the evidence.

## What cannot be proven by these methods

- Heuristic reviews do not show real user behaviour. They find likely problems and miss some.
- A small usability test shows serious problems that occurred but cannot estimate rates in a population.
- Analytics show what happened, not why.
- Conversion benchmarks vary widely by context; no benchmark is asserted here.

## Tools

Free first: paper or whiteboard sorting, spreadsheet-based task logs, a screen and audio recording tool already available to the team, browser developer tools, and design tool prototypes. Optional paid tools for remote testing or analytics exist; none were evaluated, so no claims are made about them.

## Limitations

- The NN/g Information Architecture study guide URL returned HTTP 404 and was not read. Nothing from it is cited.
- Not read: NN/g articles on form design, navigation or conversion; Material, Carbon, or other design system documentation beyond GOV.UK error messages; WCAG 3.3.2 and 3.3.3 Understanding pages (error suggestion level not confirmed).
- The Design Tokens page was read for its first 100000 of about 114985 characters.
- The NN/g response time limits come from an older, widely cited article; its figures are treated as guidance and should be re-checked against current research before use as a contractual threshold.
- GOV.UK guidance is for public services in the UK. Its wording rules are examples, and the project must adapt them to its own audience and language.

## References (retrieved 2026-10-22)

NN/g ten usability heuristics; NN/g Usability 101; NN/g progressive disclosure; NN/g empty states; NN/g response times; GOV.UK Design System error message; Design Tokens Community Group format draft; Understanding WCAG 2.2 pages. URLs are in `requirements.yaml`.

## Assumptions and open questions

- Assumption: unless a brief says otherwise, users are the general public and plain-language content is the default.
- Open: which primary tasks and success measures apply, and whether analytics exist, are set per project in UX-001.
