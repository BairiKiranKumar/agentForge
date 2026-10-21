# Visual Regression Tester: Checklist

## Before starting
- [ ] Target preview environment or local build verified and accessible
- [ ] Approved design mocks or existing baseline snapshots available for reference
- [ ] Viewport matrix defined (standard 375px, 768px, 1440px)
- [ ] Dynamic widgets identified (timestamps, live counters, random hero images)
- [ ] Test harness configured with Docker or consistent headless browser environment

## While working
- [ ] CSS animations and transitions disabled in test setup (`reducedMotion: reduce`)
- [ ] `document.fonts.ready` verified prior to screenshot capture
- [ ] Dynamic regions masked with `mask: [...]` locators
- [ ] Text cursors and focus rings stabilized (`caret-color: transparent`)
- [ ] Scrollbar presence forced to prevent horizontal layout shift
- [ ] Element scrolled into view and settled before screenshot trigger
- [ ] Pixel tolerance threshold (`maxDiffPixelRatio`) set strictly per component type
- [ ] Visual diffs reviewed side-by-side against original design comps
- [ ] Anti-aliasing noise separated from true structural layout changes
- [ ] Broken images, clipped text, and container overflows highlighted
- [ ] Viewports tested on mobile portrait (375px) to catch mobile responsive flaws

## Before handoff
- [ ] Visual regression test suite passes cleanly with zero false positives
- [ ] All diffs documented with baseline, actual, and difference images attached
- [ ] Intentional design updates confirmed by `design-systems-specialist` or frontend developer
- [ ] Baseline snapshot updates committed cleanly without collateral changes
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Developer requests running `--update-snapshots` without reviewing visual diffs
- [ ] Critical landing page or checkout button is truncated or pushed off-screen
- [ ] Brand colors or primary typography deviate without approved design change
- [ ] Inconsistent cross-OS font rendering renders automated visual diffs unusable
