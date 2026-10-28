# WF-06: SEO Cycle

SEO audit, prioritization, implementation, measurement.

## Entry requirements
- Site URL and codebase access (for implementation), target market and locations.
- Search Console and analytics access if available (read access shared by the owner); otherwise the audit relies on public crawling and is marked partial.
- Authorization: production deploys and Google Business Profile edits need approval.

## Roles
`seo-specialist` (lead for content and keywords), `technical-seo-specialist` (lead for technical audit), `local-seo-specialist` (for local businesses), `html-specialist`, `performance-engineer`, `copywriter`, `web-analytics-specialist`, `marketing-analyst`, `code-reviewer`.

## Stages
| # | Stage | Owner | Deliverables | Quality gate | Reviewer |
|---|---|---|---|---|---|
| 1 | Audit (parallel) | `technical-seo-specialist`, `seo-specialist`, `local-seo-specialist` | Technical audit (crawl, index, render, canonicals, sitemaps, structured data, CWV), keyword and content gap audit, local audit (GBP, NAP, reviews) | Each finding has evidence (URL, screenshot, tool output) and severity | each other (cross-review) |
| 2 | Prioritize | `seo-specialist` | Prioritized backlog: impact, effort, confidence, owner | Quick wins separated; nothing without evidence | `marketing-lead` |
| 3 | Implement | `html-specialist`, `performance-engineer`, `copywriter`, `local-seo-specialist` | PRs and content changes; GBP change list | Changes match backlog items; tests pass | `code-reviewer`; the owner approves deploy and GBP edits |
| 4 | Verify | `technical-seo-specialist` | Post-change checks (structured data validation, indexability, CWV) | Each implemented item verified | `seo-specialist` |
| 5 | Measure | `marketing-analyst` with `web-analytics-specialist` | Baseline and 4 to 8 week readout | Uses Search Console and analytics data; notes seasonality | `seo-specialist` |

## Exit criteria
Backlog items done or deferred with reasons, verification complete, measurement date set and baseline recorded.

## Example invocation
"Run WF-06 for the preschool website. Audit and prioritize only; no deploys."
