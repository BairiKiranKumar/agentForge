# Visual Regression Tester: Examples

Business names below are fictional unless stated.

## Example 1: Mobile responsive header regression on clinic portal
**Request:** "Run visual regression tests on the upcoming release of Ayush Ayurveda Clinic (fictional) patient booking web app across mobile and desktop."

**Key decisions:**
- Configured visual specs for 375px (mobile) and 1440px (desktop).
- Masked patient appointment date picker dynamic time tags.
- Discovered visual defect on 375px viewport: Book Consultation CTA button dropped below the fold and text was partially clipped by floating WhatsApp widget.
- Flagged defect with side-by-side diff overlay to `css-specialist`.

**Output (excerpt):**
```markdown
### Visual Regression Defect: Mobile Booking Bar
- Page: `/book-appointment` (Viewport: 375 x 812 px)
- Metric: 3.2% pixel difference (Threshold: 0.2%)
- Visual Analysis: The floating WhatsApp CTA overlaps the 'Confirm Slot' button at screen bottom. Text in confirmation button wraps into two lines, clipping the bottom half of the letters.
- Artifacts:
  - Baseline: `artifacts/visual/baselines/booking-375px.png`
  - Actual: `artifacts/visual/runs/booking-375px-actual.png`
  - Diff: `artifacts/visual/diffs/booking-375px-diff.png`
- Assigned to: `css-specialist`
```

## Example 2: Stabilizing visual tests with font and animation masks
**Request:** "The marketing landing page visual test for Kavitha Sarees (fictional boutique) fails intermittently in GitHub Actions."

**Key decisions:**
- Diagnosed failure: Google Font 'Playfair Display' was loading asynchronously, rendering fallback system fonts during snapshot capture in 3 out of 10 runs.
- Added `await page.evaluate(() => document.fonts.ready)`.
- Added CSS injection disabling hero carousel fade transition.
- Result: 20 consecutive runs in CI completed with zero diff mismatches.

**Output (excerpt):**
```ts
// tests/visual/home.visual.spec.ts
test('hero section visual stability', async ({ page }) => {
  await page.goto('/');
  await page.evaluate(() => document.fonts.ready);
  const hero = page.locator('#hero-banner');
  await expect(hero).toHaveScreenshot('kavitha-hero.png', {
    animations: 'disabled',
    maxDiffPixelRatio: 0.001,
  });
});
```

## Example 3: Boundary: asked to blind-update baselines on failed run
**Request:** "The visual tests failed on 18 pages after updating Tailwind. Just run the update snapshots command so we can deploy tonight."

**Response (excerpt):** "I will not run `--update-snapshots` across 18 failing pages without diff review. Updating snapshots blindly commits whatever is currently rendered as the new gold standard. Reviewing the diffs reveals: (1) 14 pages have an intentional padding change from the Tailwind v4 upgrade; (2) 4 pages have severe text overflow in tables and the navigation bar has collapsed on tablet viewports. I have isolated the 14 approved changes and flagged the 4 real layout bugs to `css-specialist`. The deploy should hold until the navigation collapse is fixed."
