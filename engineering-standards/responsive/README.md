# Responsive design standard (version 1.0.0)

As-of date: 2026-10-22. Machine-readable requirements: `requirements.yaml` (RESP-001 to RESP-030). Meeting these is evidence of good practice, not certification.

## Scope and non-goals

In scope: layout, sizing, images, input modes, orientation, internationalisation and testing so a web interface works across viewport sizes, input types and writing directions.

Non-goals: native app layouts, print stylesheets, performance tuning beyond image selection (see the performance area), and a fixed list of supported browsers. This standard sets a process for a support policy; it asserts no browser list.

## How to apply by product type

| Product type | Applies |
|---|---|
| website | All from the chosen profile up |
| web-app | All, with extra weight on dense components, tables, sticky UI and keyboard-open states |
| mobile-web | All, with safe areas, viewport units, touch, orientation and real-device checks |
| internal-tool | Core items (no horizontal scroll, zoom, tables, support policy); phone items only if staff use phones |
| api, ai-app without UI, library | Not applicable, except a library's components must document their responsive behaviour |

Profile intent: `lightweight` keeps only the viewport meta tag and no horizontal scroll at 320 CSS px. `standard` adds the full matrix, images, input, i18n and rendered-browser checks. `high_assurance` adds visual regression and real-device testing.

## Principles taken from sources read

- Mobile first is a design choice where simple layouts are the base and wider layouts are added. Use it where it suits; document if you choose otherwise (MDN Responsive design, read 2026-10-22).
- Breakpoints belong where the content looks bad, not at device sizes, and should use relative units. Flexible grids and relative units can work without media queries (MDN).
- Mobile browsers need the viewport meta tag or they render at a default desktop-like width (MDN).
- Default `vh` equals the large viewport; small, large and dynamic viewport units behave differently as browser bars show and hide. The dynamic unit can resize during scroll (MDN CSS length).
- Safe area inset variables report distances from the edges of the viewport to the safe area, with fallbacks (MDN env). Edge-to-edge opt-in via `viewport-fit=cover` was not on the MDN page read. [Unverified] from this page; confirm on the MDN viewport meta reference before relying on it.
- `pointer` reports only the primary input; `any-pointer` covers all available inputs (MDN).
- `orientation` describes the viewport, so an on-screen keyboard can switch a portrait phone to landscape styles (MDN).
- Logical properties let one stylesheet serve left-to-right, right-to-left and vertical writing modes (MDN).
- `srcset` with `sizes` handles resolution switching; `picture` handles art direction (MDN Responsive images).
- Reflow target is 320 CSS px wide for vertical scrolling and 256 CSS px high for horizontal scrolling; data tables, maps and similar can be excepted (WCAG 2.2 Understanding).

## Methods and measurement procedure

1. Write the viewport matrix: at minimum a 320 px wide viewport, a large phone, tablet portrait and landscape, a laptop width, a desktop width and an ultrawide width. Record exact sizes in the project plan.
2. Resize continuously from 320 px upward in a rendered browser and record every width where the layout breaks. Those are the breakpoint candidates.
3. Run the overflow and clipping script at each matrix width: compare element scroll width against client width, and flag text with hidden overflow.
4. Test content stress: long words, long names, no items, many items, translated strings, right-to-left.
5. Test input: touch device, mouse, keyboard, and a hybrid device if available.
6. Test browser UI states on a real phone or emulator: address bar expanded and retracted, on-screen keyboard open, notch or rounded corners, landscape.
7. For high-visibility interfaces, capture rendered screenshots per viewport and browser and have a person review them.

A high-visibility interface is one where a layout failure has outsized cost: landing pages, sign-up, checkout, payment, primary dashboards, and anything named in a client commitment. Rendered-browser checks are mandatory for these and cannot be replaced by code review or unit tests.

## Test matrix

P = primary, S = supporting, - = not useful.

| Requirement area | Resize in desktop browser | Emulator | Real device | Automated overflow script | Visual regression | Screen reader or keyboard |
|---|---|---|---|---|---|---|
| Viewport meta and zoom | S | P | P | - | - | - |
| Reflow, no horizontal scroll | P | S | S | P | S | - |
| Breakpoints and layout | P | S | S | S | P | - |
| Tablet and ultrawide | P | S | S | - | P | - |
| Dynamic viewport units, safe areas | - | S | P | - | - | - |
| Touch, pointer, hover | S | S | P | - | - | S |
| Orientation | S | P | P | - | S | - |
| Images and density | P | S | S | - | S | - |
| Overflow and clipping | S | - | - | P | S | - |
| i18n, RTL, text expansion | P | - | S | S | P | S |
| Zoom, large text, text spacing | P | - | S | S | S | - |
| Reduced motion | P | S | S | - | - | - |
| Sticky and overlay elements | P | S | P | - | S | S |
| Tables and dense components | P | S | S | - | S | P |
| Browser support policy | S | - | P | - | S | - |

## Severity classification

| Severity | Definition | Examples |
|---|---|---|
| critical | Reserved for a layout failure that blocks a task or hides data; none of the current requirements default to critical, but any project may raise one | Sign-in button covered by a fixed bar on every phone; payment form unusable when keyboard opens |
| major | Task is harder or content is lost or unreachable on some viewports or inputs | Horizontal scroll at 320 px; text clipped at 200 percent zoom; touch target under 24 px; header hidden behind notch |
| minor | Visual or efficiency issue with workarounds | Awkward gap on a tablet; oversized image downloaded to a phone; inconsistent spacing at one width |

## Recording planned versus executed checks

Record per template and viewport: planned (yes or no), executed (date, browser and version, device), result, evidence link. Never claim a viewport was tested because it should work. Emulator results are recorded as emulator, not as real device. Automated script output and manual review are recorded separately.

## What automated tools cannot prove

An overflow script can flag a wide element but cannot say whether a layout is balanced, readable or intentional. Visual regression detects change, not correctness. Emulators do not reproduce real browser bar behaviour, notches, keyboards or touch accuracy faithfully [Inference]. Responsive checks complement, and do not replace, accessibility checks for zoom, reflow and touch targets.

## Tools

Free first: browser developer tools device and responsive modes, a small custom overflow script, a screenshot capture script in any scripted browser runner, and real devices. Visual regression services and device farms are optional paid options and are not evaluated here. No vendor page for them was read, so no claims about them are made.

## Limitations

- Source pages read in part: MDN CSS length (first 100000 of about 145750 characters), MDN env (first 100000 of about 144600), MDN orientation, pointer and logical properties (each partial).
- Not read and not cited: browser compatibility tables, Can I Use, container query documentation, scroll snap and print documentation, playwright viewport emulation docs.
- No numeric size thresholds apart from WCAG 320 px, 256 px and 24 by 24 CSS px are asserted. Matrix widths are chosen per project.
- Browser behaviour changes with releases. Re-verify viewport unit and safe area behaviour when the support policy is refreshed.

## References (retrieved 2026-10-22)

MDN Responsive design; MDN CSS length (viewport units); MDN env() and safe-area-inset; MDN pointer media feature; MDN orientation media feature; MDN CSS logical properties; MDN Responsive images; MDN prefers-reduced-motion; Understanding WCAG 2.2 pages for reflow, orientation, target size and text spacing. URLs are in `requirements.yaml`.

## Assumptions and open questions

- Assumption: mobile-first is the default for content sites and phone-heavy apps, and desktop-first is acceptable for dense internal tools when stated.
- Open: which browsers and devices each project supports; the project must fill in the support policy (RESP-026).
