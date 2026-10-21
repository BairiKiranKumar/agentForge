# Technical SEO Specialist: Checklist

## Before starting
- [ ] Production and staging URLs confirmed, and the environment for this audit stated
- [ ] Platform identified (WordPress, Next.js, Shopify, Webflow, plain HTML or other)
- [ ] Search Console read access confirmed, or a crawl export from a client-owned tool obtained
- [ ] Sitemap URL and robots.txt content captured with the access date
- [ ] List of intentional noindex pages obtained from the client
- [ ] Approval owner named for any live change

## Crawl and index
- [ ] robots.txt does not block CSS, JavaScript or images needed for rendering
- [ ] No blanket Disallow on production (checked against the approved file)
- [ ] Sitemap contains only 200, indexable, canonical URLs
- [ ] Sitemap URL count compared with Search Console indexed count, gap explained if above 20 percent
- [ ] Key pages reachable within three clicks of the homepage
- [ ] Filter, sort and session parameter URLs controlled by canonical or robots rules

## Canonicals and redirects
- [ ] One preferred host (https, www or non-www) with all other variants redirecting in one hop
- [ ] Self-referencing canonical on each indexable page
- [ ] No product or article page canonicalised to the homepage or a category by default
- [ ] Redirect chains (more than one hop) counted and listed
- [ ] Soft 404 pages identified and fixed or returned as 404 or 410

## Rendering and structured data
- [ ] Key content and structured data confirmed in the rendered DOM, not only raw HTML
- [ ] Structured data type matches the business (for example Restaurant or Dentist for a local business)
- [ ] Every structured data value appears in the visible page (no hidden ratings or prices)
- [ ] No invented GSTIN, address, phone or rating in markup
- [ ] Validation run with the rich results test; date and result recorded

## Speed and mobile
- [ ] Field data checked first and its availability stated
- [ ] Lab tests run on a mid-range Android profile with CPU and network throttling, at least 3 runs, median reported
- [ ] Hero image above 300 KB on mobile flagged
- [ ] First-load JavaScript above 1 MB flagged
- [ ] Third-party scripts measured before and after addition

## Handoff and stop
- [ ] Every failed check has evidence, an impact, an effort and an owner
- [ ] Change requests written in the section 6 format with a rollback step
- [ ] Re-check dates set at 7 and 28 days
- [ ] Stop and escalate if robots.txt, redirects or sitemaps on a live site must change without written approval
- [ ] Stop and escalate on any Search Console manual action or security notice
