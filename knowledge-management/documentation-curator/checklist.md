# Documentation Curator Checklist

## Before starting
- [ ] Review knowledge base repository structure and identify target documentation folders
- [ ] Verify that automated Markdown link checkers and frontmatter linters are operational
- [ ] Check active roles and department listings in `orchestration/roster.yaml`
- [ ] Inspect recent commit logs and pull requests to identify newly introduced documentation
- [ ] Determine scope of audit (full repository vs specific departmental folder)

## While working
- [ ] Verify that every Markdown file has valid metadata frontmatter (owner, status, review date)
- [ ] Check for broken internal markdown links (`[text](file:///path)`) and fix invalid paths
- [ ] Identify stale documents (last verified date >90 days ago) and flag for review
- [ ] Scan for conflicting guidelines across related documents and note reconciliation items
- [ ] Catalog newly accepted Architectural Decision Records (ADRs) in the master index
- [ ] Relocate superseded or deprecated documents to the `archive/` directory
- [ ] Add prominent deprecation banners with links to active replacement documents
- [ ] Validate that all role mentions use valid roster slugs in backticks
- [ ] Check document text for compliance with zero em dash standard

## Before handoff
- [ ] Compile quarterly Documentation Health Scorecard with freshness metrics
- [ ] Issue documentation recertification notices to relevant department leads
- [ ] Ensure all navigation sidebars, index pages, and search tags are synchronized
- [ ] Archive audit logs and commit clean documentation fixes to repository
- [ ] Format handoff according to `orchestration/handoff-format.md` standards

## Stop and escalate if
- [ ] Department leads persistently refuse to review or maintain stale mission-critical documents
- [ ] Repository restructuring threatens to break automated agent execution pipelines or CI/CD
- [ ] Severe data privacy or security leakage detected in public or unencrypted documentation
