# CSS Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Fee table scrolls sideways on phones
**Request:** "Green Valley School (fictional) admin: the fees page scrolls horizontally on a 360 px phone. styled-components."

**Key decisions:**
- Found the cause: the grid uses `grid-template-columns: 1fr 1fr 1fr` and a student email cell with a long unbroken address; `1fr` minimum is `auto`, so the column grows past the viewport.
- Fix: `minmax(0, 1fr)` columns and `overflow-wrap: anywhere` on the email cell; below 640 px (existing `theme.breakpoints.sm`) each row stacks as a labelled card.
- Did not add `overflow-x: hidden` to the page wrapper.

**Output (excerpt):**
```
Root cause: .FeeRow grid columns 1fr (min auto) + unbroken email string
Fix: features/fees/FeeTable.styles.ts; tokens used: theme.space[3], theme.breakpoints.sm; new tokens: none
Width matrix: 320 ok | 360 ok | 390 ok | 768 ok | 1024 ok | 1440 ok
Font scale 1.3x: ok   Telugu student names: ok
Commands: npm run lint pass; npm test 64 passed; npm run build pass
```

## Example 2: Dark mode for a restaurant template sold to several clients
**Request:** "Add dark mode and per-client brand colours to the restaurant template (Tailwind v4)."

**Key decisions:**
- One token source: semantic tokens in `@theme`; per-client brand values as a small override file per client; dark values under `prefers-color-scheme` plus a `data-theme` attribute for the toggle.
- Asked `design-systems-specialist` for dark surface and text values instead of inventing them; contrast checked for both themes.
- Components use only semantic tokens; replaced 14 hardcoded hex values in the touched components.

**Output (excerpt):**
```css
@theme {
  --color-surface: var(--brand-surface, oklch(99% 0.01 80));
  --color-text: var(--brand-text, oklch(22% 0.02 60));
  --color-accent: var(--brand-accent);
}
:root[data-theme="dark"] {
  --color-surface: oklch(20% 0.01 60);
  --color-text: oklch(95% 0.01 80);
}
```
```
Contrast: body text 12.1:1 light, 13.4:1 dark; accent button text 4.8:1 (pass AA)
```

## Example 3: Boundary: "just put !important and hide the overflow"
**Request:** "The salon booking modal is cut off on iPhones. Add `overflow: hidden !important` on body and move on."

**Response (excerpt):** "That would hide the symptom and make the rest of the page unscrollable on iOS while the modal is open. The real cause is the modal height set to `100vh`, which on iOS Safari includes the area behind the browser toolbar. I changed it to `max-height: 100dvh` with a `100vh` fallback and let the modal body scroll inside. Checked at 375 and 390 px in WebKit emulation; a real iPhone check is still needed because I couldn't run Safari here."
