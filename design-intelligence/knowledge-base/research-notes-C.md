# Research notes C (design-researcher worker, 2026-10-22)

Scope: folders references, patterns, typography, color, accessibility, anti-slop. Not motion, not critiques.

## Method
- Candidate discovery: Awwwards Sites of the Day list page (text extraction via WebFetch, 31 entries, Sep 22 to Oct 22, 2026; no industry column shown). Other discovery came from well-known live sites chosen to cover industries.
- Evidence for references: WebFetch returns rendered page text, not source, so it could not show CSS or script tags. The raw HTML and linked stylesheets were therefore fetched with curl using a plain identifying user agent, saved to the session scratchpad, and searched with grep for font-family, custom properties, script src, landmarks and media features. Linked CSS was sampled (first four stylesheets) for linear.app, charitywater, tate, odyssee, monzo, stripe, allbirds, butter, riotters.
- No page was rendered; no screenshots. Every reference entry has method fetched-html, viewports_checked empty.
- Contrast ratios and OKLCH numbers in entries were computed by this worker with small scripts from declared hex values or the published Oklab matrices. They are not from an external checker and are marked as such.
- Principles: WCAG 2.2 Understanding pages (W3C), MDN, web.dev, NN/g, Utopia, Every Layout, plus two opinion blogs for anti-slop.

## Sources opened (all retrieved 2026-10-22)
Awwwards SOTD list; linear.app; stripe.com; charitywater.org; monzo.com; tate.org.uk; pudding.cool; odysseeclinic.com.au; allbirds.com; butter.video; drone.riotters.com; signal-a.studio; overworldaudio.com; W3C WCAG 2.2 Understanding pages for 1.4.3, 1.4.11, 2.5.8, 2.4.11, 2.4.13, 2.3.3; web.dev vitals, optimize-lcp, optimize-cls, optimize-inp, responsive-web-design-basics; MDN clamp, oklch, prefers-color-scheme, prefers-reduced-motion, :focus-visible, variable fonts guide; utopia.fyi/type; every-layout.dev modular-scale; NN/g carousels, hamburger-menus, footers, mobile-navigation-patterns; world.hey.com Spot the Slop; superdesign.dev why-ai-design-looks-generic.
Also opened but unused: ascension.pegassi.be, belgradearbor.rs, santionispirits.com (raw HTML fetched, not written up for lack of time to cover them).

## Failures and limits
- frame.work and aesop.com returned HTTP 403 with a bot-challenge page ("Just a moment..."). Skipped. No attempt to bypass. A WebFetch text extraction of frame.work did work earlier, but without source it could not support a fetched-html entry, so it was not written up.
- cartier.com Le Choeur des Pierres returned HTTP 403 (empty-ish body). Skipped.
- Material Design 3 navigation bar, M3 window size classes (404) and Apple HIG tab bars returned no body text (script-rendered or missing). Not cited as sources. Platform-specific mobile numbers are [Unverified].
- WebFetch truncated long MDN pages and monzo.com text at 100,000 characters; only that portion was read, and entries say so.
- Many sites keep fonts and tokens in external or JS-injected CSS; absence of a declaration in HTML is not evidence the site lacks it.
- pudding.cool: no stylesheet link found; fonts not observed.
- signal-a.studio: only script tags were examined, not CSS.
- Pages are served by region and A/B tests (stripe.com returned en-IN; tate.org.uk contains an A/B script), so another visitor may see different content.

## Untrusted content
Fetched pages contained no instructions directed at this worker that were acted on. The NN/g pages are 2013 to 2019 articles with review dates; the hamburger study is from 2016.

## Not verified
Anything visual or behavioural: layout at any width, type sizes in use, motion, contrast as rendered, Core Web Vitals of any listed site, accessibility of any listed site, mobile behaviour.
