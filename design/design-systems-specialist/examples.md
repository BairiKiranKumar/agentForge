# Design Systems Specialist: Examples

Business names below are fictional unless stated.

## Example 1: One component kit, three client themes
**Request:** "We keep rebuilding buttons and forms for every local business site. Set up a shared kit that can take each client's colours. Projects use Next.js and Tailwind v4."

**Key decisions:**
- Source of truth: `tokens/tokens.json`, generated to a Tailwind v4 `@theme` block and CSS variables.
- Semantic roles fixed across clients; each client theme only remaps semantics to its primitives.
- Contrast check per theme: the salon's rose #D9849B fails as text on white (2.7:1), so added `color-rose-700: #9C3F58` (6.4:1) and mapped `color-action-primary-bg` to it; the light rose stays decorative.
- Scope: Button, Input, Select, Textarea, Checkbox, Alert, Toast for v1.0.0; cards deferred until two projects need the same one.

**Output (excerpt):**
```css
/* themes/glow-grace.css (generated) */
@theme {
  --color-text-primary: var(--color-ink-900);
  --color-action-primary-bg: var(--color-rose-700);
  --color-action-primary-text: var(--color-white);
  --color-decor-accent: var(--color-rose-400);
  --font-family-body: "Source Sans 3", system-ui, sans-serif;
  --radius-control: 6px;
}
```
| Pair | Ratio | Pass |
|---|---|---|
| action-primary-text on action-primary-bg | 6.4:1 | AA |
| text-primary on surface-default | 16.9:1 | AA |
[Second row: ink-900 assumed #1A1D21 on white; recompute when values lock.]

## Example 2: Parity audit on the school ERP
**Request:** "Developers say the Figma file and the app don't match anymore."

**Key decisions:**
- Grepped components for raw hex and off-scale px; compared Figma variables (via Figma MCP read) with `theme.ts`.
- Prioritised drift by number of screens affected.

**Output (excerpt):**
| Category | In Figma only | In code only | Hard-coded instances | Priority |
|---|---|---|---|---|
| Colour | 3 (status-info variants) | 2 (`#f5a623`, `#e8e8e8`) | 14 in `src/components/attendance/*` | High |
| Spacing | 0 | 1 (`18px` gap) | 9 | Medium |
| Button variants | `ghost-danger` | none | n/a | Low |
Recommendation: map `#f5a623` to `color-status-warning`, remove `ghost-danger` from Figma (unused in code), release as 1.4.1 (patch).

## Example 3: Boundary: "Add a special purple gradient button just for the homepage"
**Request:** "Client wants one big gradient button on the hero. Add it as a new Button variant."

**Response (excerpt):** "It's used on one screen of one project, so by our admission rule it stays a project pattern, not a system variant. Also, purple-blue gradients are on the company's avoid list, so `creative-director` should confirm the direction first. If it goes ahead, `ui-designer` can specify it in the project with existing tokens for size, radius and focus, and I'll check its text contrast across the gradient's lightest point. If a second project needs it, we'll revisit."
