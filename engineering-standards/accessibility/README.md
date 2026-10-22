# Accessibility standard (version 1.0.0)

As-of date for all thresholds and tool statements: 2026-10-22. Machine-readable requirements: `requirements.yaml` (A11Y-001 to A11Y-043).

Default target: WCAG 2.2 Level AA for every applicable web project. Meeting these requirements is evidence of good practice. It is not a legal or certification statement, and no agent is a certified accessibility auditor.

## Scope and non-goals

In scope: web interfaces (public sites, authenticated apps, phone-first web, internal tools, reusable component libraries) and the content inside them (images, media, tables, charts, forms).

Non-goals: native mobile apps (only the web content on mobile is covered), PDF and office documents, legal advice on any accessibility law, and WCAG Level AAA, which is optional guidance here.

## Roles

| Role | Responsibility |
|---|---|
| accessibility-designer | Design side: contrast, focus appearance, motion, non-colour cues, chart and media alternatives |
| accessibility-engineer | Code side: semantics, ARIA, focus management, dialogs, forms, announcements |
| accessibility-tester | Independent reviewer for every requirement. Never reviews their own output |
| frontend-developer, frontend-architect, ux-designer, ui-designer, qa-lead, ux-writer, technical-writer | Own the requirements named in `requirements.yaml` |

## How to apply by product type

| Product type | Applies |
|---|---|
| website | All requirements from the chosen profile up |
| web-app | All, with extra weight on dialogs, focus management, status messages, custom widgets and charts |
| mobile-web | All, plus touch target, gesture, orientation, zoom and mobile screen reader requirements |
| internal-tool | Same as web-app. Limited audience does not remove the duty to people with disabilities on staff |
| library | Component-level items (A11Y-001, 028, 029) plus documented keyboard and ARIA behaviour per component |
| api, ai-app without UI | Not applicable, except A11Y-043 for any UI the project ships |

Profiles: `lightweight` keeps essentials (semantics, headings, alt text, contrast, reflow at 320 px, keyboard operation and no trap, visible focus, labels, language, flashing). `standard` adds the rest of WCAG 2.2 AA coverage. `high_assurance` adds mobile screen reader testing and independent re-testing on the supported browser and assistive technology matrix.

## Organisation by the four principles

| Principle | Requirements |
|---|---|
| Perceivable | A11Y-006 to 017, 038 (text alternatives, media, contrast, resize, reflow, spacing, charts) |
| Operable | A11Y-005, 018 to 023, 030 to 032, 034, 035, 039, 040 (keyboard, focus, targets, gestures, motion, timing) |
| Understandable | A11Y-004, 024 to 026, 033, 036, 041 (titles, forms, errors, authentication, language, consistency) |
| Robust | A11Y-001, 002, 003, 027 to 029, 037 (semantics, structure, name role value, status messages, ARIA) |
| Process | A11Y-042, 043 (mobile assistive technology, result recording) |

## Rule on ARIA

Prefer native HTML elements. Use ARIA and an Authoring Practices Guide (APG) pattern only when no native element fits. The APG itself warns that incorrect ARIA can mislead users more than no ARIA, that roles do not add keyboard behaviour, and that each browser and assistive technology pair needs testing (read on 2026-10-22). The APG page read did not state a native-first rule in so many words, so native-first here is project policy built on those warnings.

## Methods and measurement procedure

1. Automated pass: run an axe-based scan on every template and key state (dialog open, error shown, menu expanded). Record violations and "incomplete" items.
2. Keyboard-only pass: unplug the mouse and complete each primary task using Tab, Shift+Tab, Enter, Space, Escape and arrow keys. Note focus visibility, order, traps and hidden focus.
3. Zoom and reflow pass: set the window to 1280 CSS px wide and zoom to 400 percent (about 320 px wide); also test 200 percent text zoom and the text spacing override values below.
4. Screen reader pass: NVDA with Firefox or Chrome on Windows; VoiceOver with Safari on macOS. Check names, roles, states, headings, landmarks, forms, errors and announcements.
5. Mobile pass: VoiceOver on iOS and TalkBack on Android for mobile-first products.
6. Record, per requirement, planned method and executed method with date, tool and version.

## Thresholds verified against fetched text (as of 2026-10-22)

| Item | Value | Where read |
|---|---|---|
| Text contrast (SC 1.4.3, AA) | 4.5:1 normal text, 3:1 large text | WCAG 2.2 TR |
| Non-text contrast (SC 1.4.11, AA) | 3:1 | WCAG 2.2 TR |
| Resize text (SC 1.4.4, AA) | up to 200 percent | WCAG 2.2 TR |
| Reflow (SC 1.4.10, AA) | 320 CSS px wide for vertical scrolling, 256 CSS px high for horizontal scrolling. 320 equals 1280 at 400 percent | WCAG 2.2 TR, Understanding page |
| Text spacing (SC 1.4.12, AA) | line height 1.5, paragraph spacing 2, letter spacing 0.12, word spacing 0.16, all times font size | WCAG 2.2 TR, Understanding page |
| Target size (SC 2.5.8, AA) | 24 by 24 CSS px, with spacing, equivalent, inline, user agent and essential exceptions | Understanding page |
| Flashing (SC 2.3.1, A) | no more than 3 flashes in any one second, or below general and red flash thresholds | Understanding page |
| Focus not obscured (SC 2.4.11, AA) | focused item not entirely hidden by author content | Understanding page |
| Levels confirmed: 1.2.2 (A), 1.2.5 (AA), 1.4.1 (A), 2.2.1 (A), 2.4.1 (A), 2.5.1 (A), 2.5.7 (AA), 3.1.1 (A), 3.1.2 (AA), 3.2.3 (AA), 3.3.1 (A), 3.3.4 (AA), 3.3.8 (AA), 4.1.2 (A), 4.1.3 (AA), 1.3.4 (AA), 1.1.1 (A) | as listed | Understanding pages |

Not confirmed from text read: levels and wording for SC 1.2.1, 2.1.1, 2.1.2, 2.4.3 and 3.3.7 beyond the main-page table (3.3.7 listed as A, 3.2.6 as A, 2.4.7 as AA there). Requirements citing them are marked `[Unverified]` in `requirements.yaml`. The WCAG 2.2 main page was read only for its first 100000 of about 269700 characters.

## Test matrix

Cells show the expected primary method. P = primary, S = secondary or supporting, - = not useful. Every executed cell is recorded as planned or executed.

| Requirement area | Automated tool | Keyboard-only | NVDA + Firefox/Chrome | VoiceOver + Safari | Mobile TalkBack / VoiceOver | Zoom and reflow |
|---|---|---|---|---|---|---|
| Semantics, headings, landmarks | P | S | P | S | S | - |
| Text alternatives, decorative images | P (presence) | - | P (quality) | S | S | - |
| Captions, transcripts, audio description | - | S (player controls) | S | S | S | - |
| Contrast and non-text contrast | P | - | - | - | - | S |
| Text resize, reflow, text spacing | S | - | - | - | S | P |
| Keyboard access, no trap, focus order | S | P | S | S | S | - |
| Visible focus, focus not obscured | S | P | - | - | - | S |
| Skip links | S | P | S | - | - | - |
| Dialogs (focus in, trap, restore) | S | P | P | S | S | - |
| Forms: labels, instructions | P | P | P | S | S | - |
| Validation errors, error prevention | S | P | P | S | S | - |
| Status messages | - | S | P | P | S | - |
| Name, role, value, ARIA patterns | P | S | P | P | S | - |
| Touch target size, dragging, gestures | S | S | - | - | P | S |
| Accessible authentication | - | P | S | S | P | - |
| Reduced motion, flashing | - | - | - | - | S | - (manual review of media and animation) |
| Language attributes | P | - | S | S | - | - |
| Tables and data visualisations | S | P | P | S | S | S |

## Severity classification

Severity applies to a failure of a requirement, and `critical` is never averaged away. A failed critical requirement blocks release in every profile that includes it.

| Severity | Definition | Examples |
|---|---|---|
| critical | Blocks use of a task for a group of users, traps them, or can cause harm | Keyboard trap in a modal; checkout button not reachable by keyboard; flashing content above threshold; CAPTCHA with no alternative at login; modal that never returns focus so a keyboard user is lost |
| major | Task is possible but with serious difficulty, or key information is missed | Missing form label on a field; text contrast at 3:1 for body text; error shown only in red; focus indicator removed; chart with no text alternative |
| minor | Annoyance or inefficiency that does not block the task | Skipped heading level; redundant alt text; slightly inconsistent help placement |

## Recording planned versus executed checks

Each test run produces two separate sections in the report.

1. Automated results: tool name and version, rule set, pages and states scanned, violations, incomplete items, exclusions with reasons.
2. Manual and assistive technology results: method, tester, date, browser and screen reader versions, tasks run, findings with severity.

Do not merge them into one score. Every requirement shows planned method, executed method, result (pass, fail, not tested), and evidence link. "Not tested" is a valid, honest result.

## What automated tools can and cannot prove

- axe-core (Deque, repository text read 2026-10-22): states it finds on average 57 percent of WCAG issues automatically, and reports items it cannot decide as "incomplete" for manual review. The page also states a design goal of zero false positives; no measured data was given there, so treat that as a vendor goal. `color-contrast` is documented as not working in JSDOM.
- Playwright docs (read 2026-10-22): automated tests detect some common problems, many issues need manual testing, and passing a scan does not mean full compliance.
- Lighthouse (Chrome developers, read 2026-10-22): the accessibility score is a weighted average of automated audits, each pass or fail with no partial credit, and manual checks such as logical tab order, managed focus and visual order do not affect the score.
- Automated tools generally cannot judge whether alt text is meaningful, whether focus order makes sense, whether captions are accurate, whether language is plain, or whether a screen reader experience is usable. This is an [Inference] drawn from the vendor statements above and from the manual-check lists in them.

**An automated score never establishes WCAG conformance.** Reports must not say "WCAG compliant" or "accessible" on the basis of a Lighthouse score, an axe pass or a Pa11y exit code alone.

## Tools evaluated (free first)

| Tool | Cost | Use | Notes from pages read |
|---|---|---|---|
| axe-core (Deque) | Free, open source (licence not read) | Engine for unit, integration and browser tests; `@axe-core/playwright` for Playwright | About 57 percent of issues found automatically per vendor; returns incomplete items |
| Playwright with axe | Free | Scan states in CI; attach results | Docs recommend pairing with manual assessment |
| Accessibility Insights for Web | Free; page says open source, licence not stated | FastPass (automated plus tab stop testing) and guided manual Assessment of about 20 tests | Assessment text refers to WCAG 2.1 AA; the extension for Chrome and Edge. Check currency of its WCAG 2.2 coverage [Unverified] |
| Lighthouse | Free | Quick signal and trend; not conformance | Weighted automated audits only |
| Pa11y | Free, LGPL-3.0-only | CLI and CI runs with htmlcs or axe runner | Exit code 2 when errors found; needs recent even-numbered Node version |
| NVDA | Free, GPL v2 or later | Windows screen reader testing | Browse mode and focus mode details were not read |
| VoiceOver | Built into Apple platforms | macOS Safari and iOS testing | Page read gave no cost or setup steps |
| TalkBack | Built into Android | Android testing | Gesture list not read |
| Paid options (for example commercial audit platforms) | Not evaluated | Optional only; not assumed | Not read, no claims made |

## Limitations

- Pages that were read only in part: WCAG 2.2 main page (first 100000 of about 269700 characters), NVDA user guide (first 100000 of about 405700).
- The APG home page and the TalkBack and VoiceOver pages gave little detail; they are cited only for what was read.
- Not cited because not read: the full APG pattern set beyond the modal dialog, the Accessibility Insights licence text, Deque product pages beyond the open source repository, WCAG 2.2 Understanding pages for SC 1.2.1, 2.1.1, 2.1.2 and 2.4.3.
- WCAG 2.2 is the version targeted as of 2026-10-22. Later versions or errata should be checked before relying on thresholds.
- Assistive technology behaviour differs by version and browser pair. Record versions with every result.

## References (retrieved 2026-10-22)

See `requirements.yaml` for the list with notes: WCAG 2.2, Understanding WCAG 2.2 pages, APG modal dialog pattern and Read Me First, W3C WAI tutorials (forms, images, tables, headings), axe-core, Playwright accessibility testing, Accessibility Insights for Web, Lighthouse accessibility scoring, Pa11y, NVDA user guide, VoiceOver for Mac, TalkBack help, MDN prefers-reduced-motion.

## Assumptions and open questions

- Assumption: WCAG 2.2 AA is the target when the brief says nothing else. A project with a stated legal requirement or a different level records that in its brief.
- Open: which browser and assistive technology versions each project supports. Record in the project test plan.
