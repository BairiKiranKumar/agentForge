# SEO standards (area: seo)

As of 2026-10-22. Version 1.0.0. Requirements: `requirements.yaml` (SEO-001 to SEO-032). Search engine behaviour changes; re-read the references before relying on any detail.

## Scope and non-goals
In scope: making public pages understandable, crawlable, indexable and accurately described to search engines and link-sharing platforms.
Non-goals: guaranteeing rankings, positions, traffic or rich results (SEO-001); paid search; link buying; keyword research method; accessibility, performance and security criteria (see those areas; some SEO checks overlap with them but are not restated).

Rule: never promise rankings or traffic. Report actions, measurements and labelled inferences only.

## How to apply by product type
- `website`: all requirements apply at their profile.
- `mobile-web`: heading, link, rendering and status-code requirements apply to public pages only.
- `web-app`: only public landing or help pages are in scope. Authenticated screens should not be indexed and need no SEO work (SEO-002).
- `api`, `library`, `ai-app`, `internal-tool`: out of scope, except SEO-001, SEO-015 and SEO-031 which apply to all.

## Methods and measurement procedure
1. Inventory page templates and the indexable URL set. Record what is intentionally not indexable.
2. Crawl the site (free options below) and export titles, descriptions, headings, canonicals, status codes, directives, links and images.
3. Fetch raw HTML and compare with the rendered DOM for each template (SEO-020). Record the command and date.
4. Validate sitemap, robots.txt, structured data and hreflang with tools. Record tool name, version, date and result.
5. Review content by hand against the helpful-content questions (SEO-028, SEO-029).
6. Verify Search Console access. Use its reports as observation, not as prediction.
7. Write the report with Executed and Planned sections.

Key rules taken from the references (own wording):
- Titles: unique, brief, accurate, same language as the page, consistent site name. Meta descriptions are a hint; the engine may write its own snippet.
- Canonicals: absolute, self-referencing, one method at a time, never used for language variants. Sitemaps are a weak signal.
- Sitemaps: preferred indexable URLs only, absolute, UTF-8, at most 50,000 URLs and 50 MB uncompressed per file, honest lastmod; priority and changefreq are ignored by Google.
- Robots: robots.txt controls crawling, not indexing, and is no security control. A noindex directive is only seen if the page is crawlable.
- JavaScript: links need anchor elements with href; use the History API for routes; rendering is queued, so keep key content and metadata in initial HTML where feasible; return real error codes.
- Structured data: JSON-LD preferred, visible content only, validate, eligibility for rich results is never guaranteed.
- Images: img elements, specific alt text, descriptive filenames; CSS background images are not indexed.
- Hreflang: reciprocal, self-referencing, valid codes, x-default optional fallback, one declaration method.
- Open Graph: og:title, og:type, og:image, og:url required; add description and image alt text.

## Tools evaluated
Free first. Availability and features on the date above were not all tested by this author.
| Need | Free options | Optional paid |
|---|---|---|
| Crawl and export | Command-line fetch (curl), a headless browser script, free-tier desktop crawler | Paid crawler subscriptions |
| Structured data | The search engine's rich results test, schema.org validator | None needed |
| Index and coverage | Search Console, Bing Webmaster Tools | None |
| Sitemap/robots | XML schema validation, robots.txt tester in Search Console | None |
| Share previews | Platform debuggers and manual paste tests | Social tools |
| Hreflang | Crawler export plus script check | Paid audit suites |
[Unverified] Exact free-tier limits of third-party crawlers; check current vendor pages.

## Test matrix
| Area | Requirements | Check type |
|---|---|---|
| Titles, headings, descriptions | 003-006 | crawl + manual |
| URLs, canonicals, duplicates | 007-010 | crawl + request tests |
| Sitemap | 011-013 | validation + sweep |
| Robots and directives | 014-017 | fetch + crawl |
| Status codes, rendering, links | 018-020 | crawl, raw vs rendered |
| Internal linking, images | 021-022 | crawl + manual |
| Structured data, social | 023-025 | validators, previews |
| International | 026-027 | validation + manual |
| Content, practices | 028-029 | editorial |
| Operations | 030-032 | manual |

## Severity classification
- critical: a mistake that removes the site from search or exposes private content (robots/noindex mistakes, SEO-014, 015, 016). Blocks release.
- major: wrong or missing signals on many pages (canonicals, sitemap, rendering, status codes, titles).
- minor: refinements on limited pages.

## What automated tools cannot prove
They cannot prove content is helpful or original, that a title matches intent, that markup describes visible content truthfully, that a page will be indexed, or that rankings or traffic will change. They cannot judge alt text quality. Crawlers may differ from search engine rendering.

## Recording planned versus executed checks
Every SEO report must have two lists. Executed: check, tool and version, command or procedure, environment URL, date, result. Planned: checks not yet run. Add a list of unavailable tools, accounts (for example no Search Console access) and the checks affected.

## Roles
Owners and reviewers use roles from `orchestration/roster.yaml`: seo-specialist, technical-seo-specialist, local-seo-specialist, frontend-developer, copywriter, content-strategist, editor, web-analytics-specialist, qa-lead, code-reviewer and others where named. Owner and reviewer differ in every requirement.

## References (retrieved 2026-10-22)
All are read pages; wording here is paraphrased. See `requirements.yaml` for ids and URLs: Google SEO starter guide; title links; snippets; consolidate duplicate URLs; build a sitemap; robots.txt introduction; robots meta tag; structured data introduction; JavaScript SEO basics; localized versions; image SEO; helpful content; Search Console verification; Open Graph protocol; schema.org getting started.

Not read: Bing Webmaster guidelines (the fetched page returned no guideline text) and the individual Google feature-specific structured data pages. They are not cited; Bing guidance should be checked directly before use.

## Limitations and as-of dates
Limits such as sitemap size and statements about ignored tags reflect Google documentation read on 2026-10-22 and may change. Behaviours of other search engines may differ. This guide is evidence of good practice, not a guarantee of outcomes.
