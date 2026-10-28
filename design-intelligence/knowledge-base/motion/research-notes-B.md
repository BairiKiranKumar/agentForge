# Research notes B (motion-researcher)

Date: 2026-10-22. Tool: WebFetch (text via a summarising model) and one WebSearch. No page was rendered, no animation viewed.

## Opened and read
- GSAP: pricing, ScrollTrigger, SplitText, Flip, ScrollSmoother, Observer, matchMedia docs.
- MDN: scroll-driven animations overview, animation-timeline, animation-range, View Transition API, prefers-reduced-motion, clip-path, canvas optimisation.
- web.dev: animations guide, optimize CLS, INP, LCP.
- W3C WCAG 2.2 Understanding: SC 2.2.2, SC 2.3.3.
- Lenis README on GitHub; Motion docs index, animate, scroll.
- Inspiration sites: motionsites.ai, awwwards.com, godly.website (redirected to recent.design).

## Failed or limited
- tympanus.net/codrops home and one tutorial: HTTP 403. Used a web search for titles only.
- web.dev scroll-driven-animations article: 404.
- threejs.org manual pages: two 404s; manual root gave nav only.
- godly.website: 301 to recent.design, a different domain.
- Several MDN pages were longer than 100000 characters; only the first part was summarised.

## Caveats
- WebFetch passes pages through a summariser, so statements such as the GSAP free claim are paraphrases. Where the summariser said it was using general knowledge (browser behaviour, reduced-motion CSS for view transitions, clip-path interpolation) the entries mark those as unverified.
- Browser support levels for View Transitions and exact versions for scroll-driven animations were not captured.
- GSAP docs conflict: ScrollTrigger page says ScrollSmoother is members-only; pricing page says the whole library is free. Unresolved.
- Inspiration sites were used to confirm categories, not to extract techniques. Techniques come from official docs.
- Numeric mobile performance budgets were not found in any fetched source; entries mark such numbers as inference.
