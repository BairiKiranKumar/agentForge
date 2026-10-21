# HTML Specialist: Checklist

## Before starting
- [ ] Know how the project renders head tags (static, `next/head`, App Router metadata, Angular Meta service)
- [ ] Existing metadata helpers and JSON-LD components found for reuse
- [ ] Business facts collected with source and date (name, address, phone, hours, profiles)
- [ ] Facts compared with the Google Business Profile; mismatches flagged
- [ ] Canonical domain and trailing-slash policy confirmed
- [ ] Approved title and description copy available

## While working
- [ ] One `h1` that describes the page; heading levels in order
- [ ] Landmarks present: header, nav, main (one), footer
- [ ] Actions use `button`, navigation uses `a href`; no clickable divs
- [ ] Every input has a visible label; errors linked via `aria-describedby`
- [ ] Mobile fields use `type="tel"`, `inputmode="numeric"` and tel autocomplete
- [ ] Radio groups wrapped in `fieldset` with `legend`
- [ ] Images have purposeful `alt` or `alt=""` and width/height
- [ ] LCP image not lazy; `fetchpriority="high"`
- [ ] Text inside images also available as HTML text
- [ ] `lang` set (`en-IN`, `te`, `hi`) including on regional-language sections
- [ ] Viewport meta does not disable zoom
- [ ] Unique title, description, canonical and OG tags per indexable page
- [ ] OG image URL absolute and file small enough for WhatsApp previews
- [ ] JSON-LD uses the most specific type and only visible, true content
- [ ] Event and date values in ISO 8601 with `+05:30`
- [ ] Google's current supported features checked before promising rich results

## Before handoff
- [ ] Nu HTML Checker run on rendered output: zero errors on changed pages
- [ ] Schema Markup Validator: zero errors
- [ ] Rich Results Test run for any targeted supported feature
- [ ] axe scan: no serious or critical issues introduced
- [ ] Link preview tested or marked not verified
- [ ] Markup report filled with real validator results
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Business facts are missing or conflict with Google Business Profile
- [ ] Asked to add ratings, reviews or FAQs that are not real and visible
- [ ] A widget needs custom ARIA and keyboard logic (`accessibility-engineer`)
- [ ] Asked to `noindex` pages that currently get search traffic
