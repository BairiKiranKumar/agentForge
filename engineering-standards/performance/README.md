# Performance standard (v1.0.0)

Verified on 2026-10-22. Requirements: `requirements.yaml` (PERF-001 to PERF-032). Meeting them is evidence of good practice, not a guarantee of any outcome.

## Scope and non-goals
In scope: loading, interactivity and visual stability of web products, delivery of images, video and fonts, JavaScript cost, third parties, animation smoothness, low-end mobile behaviour, and API latency budgets. Non-goals: SEO ranking claims, server capacity planning in depth, native mobile app profiling, and any promise about business results.

## Applying by product type
- `website`, `web-app`, `mobile-web`: all browser requirements. Motion and low-end device checks matter most on `mobile-web`.
- `api`: PERF-030, PERF-031 and caching (PERF-019).
- `ai-app`: browser requirements for the UI, plus PERF-031 for model and tool latency.
- `library`, `internal-tool`: apply budgets (PERF-008 to PERF-010) and the evidence rules; others as the audience warrants.
- Profiles: `lightweight` is the evidence rule, a synthetic mobile check, reduced motion and layout-shift basics. `standard` adds field targets, budgets and the asset rules. `high_assurance` adds third-party failure tests, memory checks and continuous field monitoring.

## Targets and what they mean
As read on 2026-10-22 from web.dev (page dates in `requirements.yaml`): a page is judged "good" when, at the 75th percentile of real page loads, split by mobile and desktop, LCP is 2.5 s or less, INP is 200 ms or less and CLS is 0.1 or less. Poor starts above 4.0 s, 500 ms and 0.25 respectively. [Inference] The sources read state LCP/INP/CLS thresholds individually and the combined pass rule in the Web Vitals overview. Thresholds can change; recheck the pages before relying on them after the as-of date.

Field versus synthetic: field data is a distribution from real users (CrUX or your own RUM). Synthetic (lab) data is one controlled run on one device and network. They disagree for known reasons (caching, back/forward cache, login state, interaction timing, content after scroll). Rules here: prefer field for pass/fail of the targets; use lab for debugging, regression gates and pre-release pages; never report one as the other.

## Budgets: method, not numbers
Numeric budgets are project-set. This standard does not fix JavaScript kilobytes. Method:
1. Choose metrics per page type: script bytes, image bytes, font count, request count, third-party count, main-thread time, plus a milestone such as LCP in the lab profile.
2. Measure the current build (or a close comparator) on the target low-end device profile.
3. Pick limits that keep the field targets reachable, with a stated reason and an approver.
4. Enforce in CI; a breach fails or flags the build; raising a limit is a recorded decision.
5. Revisit after release using field data.

Example starting points (examples only, not requirements; derive your own): the 2018 web.dev budgets article suggested about 170 KB of compressed critical-path resources and Time to Interactive under 5 s on a 3G baseline. That page is dated 2018-11-05 and its figures are likely outdated for modern use. [Unverified] for any current value.

## Measurement procedure
1. Define the page types and key user journeys, and the audience device profile (see below).
2. Field: read CrUX for the origin or URL, and RUM if installed. Record the p75 values, device class and date window.
3. Lab: run at least three runs per URL on the same profile; use the median (the third-party guidance recommends this). Lighthouse runs in DevTools, the CLI, as a Node module or via PageSpeed Insights.
4. Trace: use the DevTools Performance panel for long tasks, layout work, frame drops and LCP element identification; use the Network panel for the waterfall and HAR export.
5. Compare against budgets and targets; record decisions.
6. Fill in an evidence record (template below).

Low-end mobile profile method: write the profile once (viewport, CPU slowdown factor, network shape, cache state, logged-in state). DevTools states throttling is relative to the host computer and cannot fully imitate mobile CPUs, so calibrate the slowdown (DevTools offers a calibrate option) or confirm key results on a real low-end phone. High-assurance work requires the real-device confirmation.

Motion-heavy designs: trace on the low-end profile, count dropped frames during scroll and animation, check INP during animation, confirm a lighter fallback exists, and test with the reduced-motion preference enabled (media feature values `no-preference` and `reduce`, widely available per MDN). Reduced motion is also an accessibility need; hand overlap to the accessibility standard.

## Tools evaluated
Free first.
- Lighthouse: open source, runs in DevTools, CLI, Node, PageSpeed Insights (as read on its docs page). Its licence is not stated on that page, [Unverified]; check the repository before redistributing.
- Chrome DevTools Performance and Network panels: free in the browser.
- CrUX / PageSpeed Insights field data: free; coverage depends on traffic. Not fetched in this pass, so tool details are [Unverified].
- WebPageTest: not fetched; availability and terms [Unverified].
- Bundle analyzers and CI budget checks (Lighthouse CI, bundler performance hints): named in the budgets article; not individually evaluated.
- Optional paid RUM and synthetic monitoring: not evaluated.

## Test matrix
| Dimension | Minimum | Standard | High assurance |
|---|---|---|---|
| Device | one throttled mobile profile | mobile profile and desktop | plus a real low-end device |
| Data | lab | lab and field | lab, field and continuous RUM |
| Pages | home and top journey | every page type | every page type and key states |
| Conditions | cold cache | cold and warm cache | plus third-party blocked and slow network |

## Severity classification
Used in the YAML. Critical is reserved for defects that block use or expose data; no performance requirement is critical here. Major: misses a field target, ships without evidence for a claim, or breaks a budget. Minor: hygiene gaps with small measured effect. A failed field target on a page type is major and must be fixed or accepted with a recorded owner decision.

## What automated tools cannot prove
A lab score does not prove field results. Tools do not know your real audience devices, third-party behaviour after a run, the feel of an interaction, or memory growth over a long session. Automated passes do not replace trace review, real-device checks or user-visible smoothness testing.

## Recording planned versus executed checks
Keep a table per release: requirement id, planned check, executed (yes/no), date, build, evidence link, result. Anything planned but not executed is reported as not executed, never as passed.

## Performance evidence record (template)
```
Claim:            (exact statement being supported)
Type:             field | synthetic
Tool and version: 
Device profile:   (device or emulation, CPU slowdown, network shape, viewport)
URL:              
Build / commit:   
Date and time:    (IST)
Runs:             (count; value reported, e.g. median)
Cache / auth:     (cold or warm; logged in or out)
Metrics:          LCP=  INP=  CLS=  other=
Budget compared:  (limit and result)
Trace / HAR / report link: 
Limits of this measurement: 
Recorded by / reviewed by: 
```

## References (retrieved 2026-10-22)
See `requirements.yaml` for ids, URLs, retrieval dates and page last-updated dates. Read: web.dev Web Vitals, LCP, INP, CLS, lab versus field, performance budgets 101, optimize long tasks, slow third-party JavaScript, browser-level image lazy loading, font best practices, replace GIFs with video, HTTP cache; Chrome for Developers Lighthouse overview and Performance panel reference; MDN prefers-reduced-motion.
Not read in this pass: web.dev pages on image formats and responsive images, code splitting, memory leak debugging and animation performance, MDN performance pages, WebPageTest documentation. Requirements on those topics (PERF-011, PERF-018, PERF-024, PERF-025) are [Inference] from general practice and linked to the nearest source read.

## Limitations and as-of dates
Thresholds and page guidance are as of 2026-10-22 and may change. Several cited web.dev pages are old (2018 to 2022); their techniques are widely used but check for newer guidance. No tool was executed to produce this standard.
