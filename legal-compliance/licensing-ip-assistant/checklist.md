# Licensing and IP Assistant: Checklist

## Before starting
- [ ] Scope confirmed: build, campaign, handover, or ai-team audit
- [ ] Delivery model recorded (client-hosted, studio-hosted, app store, social post)
- [ ] Manifest and lockfile received for code reviews
- [ ] Asset sources listed (font files, stock downloads, music, AI tools and plans)
- [ ] Contract IP clause or summary available for handovers

## While working
- [ ] Licence text read, not just metadata; location recorded
- [ ] Licence file vs header conflicts flagged
- [ ] Version pinned and checked for licence changes
- [ ] Transitive dependencies classified where a lockfile exists
- [ ] AGPL and GPL checked against the delivery model
- [ ] Source-available licences flagged as not open source
- [ ] Unknown licences marked needs review
- [ ] Apache-2.0 NOTICE requirements captured
- [ ] CC assets: no NC or ND in commercial work; TASL attribution written
- [ ] Fonts: licence type (desktop, web, app), licensee and transferability recorded
- [ ] Stock: commercial use, releases and sensitive-use limits checked; licence URL and date saved
- [ ] Music: platform-only vs off-platform use checked
- [ ] AI assets: tool, plan, terms URL and date logged
- [ ] ai-team audit: each adapted source checked against `sources/repos.json` reuse, commit and licence

## Before handoff
- [ ] Asset rights log complete with status per item
- [ ] THIRD-PARTY-NOTICES or attribution page generated where required
- [ ] Needs-review list with reasons sent to the owner
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] An asset has no traceable source or licence
- [ ] A client claims exclusive rights to a non-exclusively licensed asset
- [ ] An infringement claim or takedown notice arrives
- [ ] Asked to remove licence notices or adapt from a reference-only repo
