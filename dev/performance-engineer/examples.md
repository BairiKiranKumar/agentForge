# Performance Engineer: Examples

Business names below are fictional. Numbers are illustrative of the report format, not real measurements.

## Example 1: Restaurant hero takes too long on mobile
**Request:** "Spice Route Kitchen's (fictional) home page is slow on phones. `performance-tester` reports mobile LCP 5.8 s."

**Key decisions:**
- No CrUX data for the origin; used lab (Lighthouse mobile default, 5 runs) plus a Redmi device check.
- LCP phases: TTFB 0.4 s, load delay 2.9 s, load duration 2.1 s, render delay 0.4 s. Dominant: load delay. The hero was a CSS background set by a client component after hydration.
- Fix: render the hero with the project's existing `next/image` wrapper, `priority`, sizes `100vw`, source resized from a 4.2 MB camera JPEG to AVIF and WebP variants.
- Left the menu carousel alone: not on the critical path.

**Output (excerpt):**
```
Before (median of 5): LCP 5.8 s (0.4 / 2.9 / 2.1 / 0.4) | CLS 0.02 | JS 212 KB
Root cause: LCP image discovered only after hydration (CSS background in client component); 4.2 MB source.
| # | Change | Files | Severity | Expected effect |
| 1 | Hero via Image component with priority | app/(site)/page.tsx, components/Hero.tsx | Critical | removes load delay |
| 2 | Resized hero, AVIF/WebP | public/hero/* | Important | cuts load duration |
After (median of 5, same settings): LCP 2.3 s | CLS 0.02 | JS 209 KB
Budgets added: Lighthouse CI assert largest-contentful-paint <= 2500 on /
Not verified: field data (none available)   Verification requested from: performance-tester
```

## Example 2: "Mark all present" freezes the ERP
**Request:** "Teachers say tapping 'Mark all present' on a 60-student class freezes for a second."

**Key decisions:**
- Trace with 4x CPU throttling: one 780 ms task. Each checkbox update set state separately, re-rendering the full table 60 times, and each row read `offsetHeight` after a style write.
- Fix: single batched state update, memoised rows keyed by student id, removed the layout read. Larger refactor of the table state was out of scope; noted for `react-specialist`.

**Output (excerpt):**
| Metric | Before | After |
|---|---|---|
| Longest task on tap | 780 ms | 64 ms |
| INP (lab, interaction trace) | about 820 ms | about 110 ms |

## Example 3: Boundary: "remove the WhatsApp chat widget and the video, they're slow"
**Request:** "Just delete the chat widget and the hero video on the salon site. The score will jump."

**Response (excerpt):** "Both were chosen by the client, so removing them needs your approval. I can keep both and remove most of the cost: load the chat widget only after first interaction using a lightweight button facade that opens WhatsApp, and replace the autoplay video with a poster image that plays on tap. In a lab test on the preview this kept the widget and video available and moved LCP from 4.6 s to 2.7 s. If you'd still like them removed, I'll need that decision recorded."
