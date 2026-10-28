# Design research brief: hero section for a B2B data-analytics landing page

Date: 2026-10-22. Author role: design-researcher. Status: evaluation run, no knowledge-base entries added.

## 1. Research question
Which hero approaches work for a B2B data-analytics product whose main action is "request a demo", and what can be reused without copying?

Audience (stated assumption): data and business leads evaluating a tool, often with a buyer and a hands-on evaluator reading the same page. Context: first visit, usually from search or outbound, desktop-heavy with mobile traffic. Baseline: WCAG 2.2 AA.

Excellence criteria for this context:
1. The visitor can say what the product does and who it is for within one screen.
2. The demo action is unmistakable, and a lower-commitment alternative exists for people not ready.
3. Proof or risk-reducers sit near the action.
4. The product is shown or described concretely, not as abstract imagery.
5. The hero stays light enough to load fast on mid-range phones.

## 2. Inspection level and tools (read this first)
- Tools available: WebFetch (page text extraction), shell. No rendering browser, no screenshot tool.
- Inspection level for the two new references: text extraction through WebFetch. The tool returned a text rendering summarised by a small model, not raw HTML. This is below the full `fetched-html` level in the AGENT.md table: no fonts, CSS variables, scripts or markup were returned. I use the nearest schema label, `fetched-html`, with this caveat. No visual claim is made about any reference. Statements about layout, size, colour, emphasis or motion are not made.
- Existing KB references were not re-fetched. They carry `fetched-html` evidence dated 2026-10-22 from the knowledge base.
- Duplicate search: `python tools/design_kb.py search hero` returned one pattern (hero-patterns-and-when-each-fits) and references ref-allbirds-store, ref-charitywater-org, ref-linear-app-homepage and ref-monzo-homepage as hero-tagged or matching. Neither new site exists in `knowledge-base/references/`.
- Discovery channels: only one channel was used (category knowledge of well-known B2B analytics and BI products, then direct fetch). The three-channel rule in AGENT.md was not met; this is a scoped Tier M run. The shortlist is 5 items, not 8 to 12.
- PostHog (posthog.com) was also fetched and dropped: the extract showed one CTA and no proof, so it added little for a demo-led hero.

## 3. Shortlist table
Retrieved 2026-10-22 for the two new rows. Inspection level for new rows: `fetched-html` (text extraction only, see section 2).

| Reference | Industry | Style | Channel | Inspection level | Why it works (observed, then inference) | Borrow | Do not copy | Feasibility |
|---|---|---|---|---|---|---|---|---|
| NEW: Metabase, https://www.metabase.com/ | BI and analytics, open source | Not judged (no render) | Category search then direct fetch | fetched-html (text extract) | Observed: the headline claims a verifiable property ("open source AI analytics you can verify") and the subhead backs it with a concrete mechanism (inspect the query behind every answer). Two CTAs for two readiness levels (cloud trial, self-host), a "Trusted by 100,000+ companies" line with eight named logos, and a "Watch a 1-minute demo" link with a length stated. Product UI appears as real labels (chart titles, a chat prompt). [Inference] The headline turns a trust objection into the value claim, and the stated demo length lowers the cost of clicking. | A claim that answers the buyer's main doubt; a timed low-commitment option beside the main action; proof with named logos right after the action | Their wording, the verify claim itself (it is their product fact), logo set, announcement bar content | Low. Text, logos and a link row. No heavy media was identifiable in the extract. [Unverified] for page weight |
| NEW: Mixpanel, https://mixpanel.com/ | Product analytics, SaaS | Not judged (no render) | Category search then direct fetch | fetched-html (text extract) | Observed: "Book a Demo" listed first and "Get Started Free" second, both repeated in the hero block; a rating line ("4.5 / 5.0 score with 1300+ reviews"); a "Contact Sales" item in the nav; product tabs (AI, Analytics, Session Replay, Experiments, Metric Trees) linking to scroll anchors. No logo strip or hero media identified in the extract. [Inference] Pairing a sales action with a self-serve action lets both buyer types act without a second page. The rating is third-party-style proof, but its source is not stated in the extract, so treat as [Unverified]. | Demo plus self-serve pair with the demo first; repeating the same two actions at the hero and page bottom; product-area anchors that let evaluators jump | Their headline, tab names, rating figure, any review-site claim | Low for the structure. Scroll-anchored sections may add scripts [Unverified] |
| EXISTING: Stripe, ref-stripe-homepage | Fintech, SaaS | Not judged (fetched-html only in KB) | KB | fetched-html (per KB) | KB evidence: nav with Start now and Contact sales, one sentence-case statement in the hero, then a customer logo row; prefixed design tokens. [Inference] Two-tier actions plus logos directly under the hero is a known B2B structure. | Order of elements: statement, actions, logo row; token-based consistency | Gradient art, licensed typeface, bar-chart style stat graphics | Medium to high effort at their scale; the structure alone is cheap |
| EXISTING: Linear, ref-linear-app-homepage | SaaS, product tool | Dark, per KB class and attribute evidence only | KB | fetched-html (per KB) | KB evidence: one headline, an announcement badge, short feature titles, a closing row of four actions, theme set by root attribute. [Inference] A closing action row repeats the conversion after the evidence has been read. | Repeat the main action at the page end; keep feature titles short | Grain texture, screenshots, copy | Low |
| EXISTING: Monzo, ref-monzo-homepage | Consumer banking | Not judged | KB | fetched-html (per KB) | KB evidence: trust badges and a terms line sit next to the sign-up action. [Inference] Answering the safety question at the decision point lifts confidence where trust gates the click, a pattern that transfers to analytics tools that touch company data. | Place security or compliance statements beside the demo action, wording supplied by the client's compliance owner | Badges, brand colour, typefaces, autoplay video | Low |

The KB pattern entry hero-patterns-and-when-each-fits (statement plus one action, product visual, proof first, index) is the frame used below. It is a synthesis labelled inference in the KB.

## 4. Patterns across the set
All pattern statements below are [Inference] from text-level evidence, not visual observation.
1. **Two actions at two readiness levels.** Metabase (trial and self-host), Mixpanel (demo and free start) and Stripe (start and contact sales) all pair a committed action with a lighter one. For a demo-led product the lighter option is the valve for visitors not ready to talk to sales.
2. **Proof close to the action.** Named logos (Metabase, Stripe), a review score (Mixpanel), regulator badges (Monzo). Three different proof types; which one fits depends on what the client can substantiate.
3. **The headline carries a claim, not a category.** Metabase states a checkable property. Mixpanel states an outcome. [Unverified] whether either claim drives conversion; no outcome data was read.
4. **The product appears as specifics.** Metabase's extract shows real chart and prompt labels instead of generic imagery. [Inference] This matters more for analytics, where the product is the evidence.
5. **Conversion repeats.** Mixpanel and Linear repeat actions lower on the page.

## 5. Gaps
- No rendered inspection: nothing is known about hierarchy, emphasis, type, colour, spacing, motion, mobile layout or what is actually primary versus secondary. Both new sources' extracts said styling was not visible.
- Visual-style breadth rule not met. The set has no verified styles at all, and only SaaS, fintech and BI industries. Missing: editorial or data-journalism heroes, light-theme enterprise (for example large data platforms), and heroes with interactive or live-data demos.
- Single discovery channel; no gallery, no practitioner write-up, no official guideline for form or CTA design.
- No conversion data. Nothing here shows that any hero performs well. Treat patterns as plausible, not proven.
- Demo-form design (fields, scheduling embeds, qualification) was not researched.
- Other regions and Indian-market B2B examples not covered.
- Geo-variation of fetched content is possible [Unverified].

## 6. Limits
- Text-extraction summaries came through a small model, so wording of descriptions could be incomplete or paraphrased. Quotes above are short phrases only.
- Site content changes often; retrieval date 2026-10-22.
- Licensing: logos, copy, typefaces and imagery on all references are not reusable. Only principles above are carried forward.
- Not added to the knowledge base by instruction.

## 7. Direction recommendations
Three principles for the hero, original and independent of any reference layout. All [Inference] pending a rendered check and, ideally, user testing.
1. **Lead with a checkable claim about the data, then show one real artefact.** State one concrete thing the product does with a visitor's own data (a number, a time, a question answered) and place a real-looking chart or query result from a believable scenario in the hero, instead of abstract graphics. Use only claims the client can substantiate; mark unsupported ones before launch.
2. **Make "Request a demo" the one primary action and give the unready a timed alternative.** Pair it with a short, clearly labelled option, such as a watch-through of known length or an interactive sample dataset, so nobody has to choose between a sales call and leaving. Repeat the pair at the end of the page.
3. **Put the risk answer at the point of action.** Next to the demo button, add one line addressing the likely objection for analytics buyers (for example how data is handled, what the demo involves, how long it takes), written with the client's security and legal owners. Add named customer proof directly beneath only if permission and substantiation exist.

## 8. Assumptions, open questions, risks
- Assumptions: B2B buyers with a sales-assisted process; desktop-first with mobile support; India market defaults unless the brief says otherwise (not verified, no brief inputs on region).
- Open questions: product maturity (is there a trial or sandbox for the lighter action?), what proof the client can substantiate, regulatory or security claims allowed, stack and performance budget.
- Risks: pattern fit is judged from text only; a rendered pass (1440, 1024, 768, 375 px) by a tool-equipped session or `design-reviewer` is needed before these become design decisions.

## 9. Handoff note
To: creative-director. Inspection level per reference given in table. Tool used: WebFetch (text extraction). Entries added: none (by instruction). Stale or broken entries found: none (freshness not run). Gaps: section 5.
