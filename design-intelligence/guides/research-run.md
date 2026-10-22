# Design intelligence refresh run

A repeatable research cycle that an external scheduler can trigger. See `workflows/22-design-intelligence-refresh.md` for the workflow table.

## Honesty about automation
agentForge does not run itself. This repository contains the procedure, the validation tooling and the report format. Nothing here is a scheduler. A refresh happens only when a human or an external runner (for example a cron job, a CI schedule or a scheduled agent session in your runtime) starts it. Do not state that monitoring is active unless a real scheduler is configured and its run history exists. Record the runner and the last run date in `design-intelligence/guides/refresh-log.md`.

## What one run does
1. **Discover.** `design-researcher` finds new references; `motion-researcher` finds new techniques and documentation changes; `design-skill-researcher` finds new or updated skills. Three workers, separate output paths.
2. **Verify.** Re-fetch sources; check URLs resolve; confirm metadata (licence, version, dates); record the method used.
3. **Compare.** Search existing entries and registry records. Mark duplicates, near-duplicates, supersessions.
4. **Select.** Keep only meaningful additions: new technique, new evidence, better source, corrected fact.
5. **Evaluate skills.** New or changed skills get the ten-criterion review. A changed pinned skill gets a diff review.
6. **Propose.** Write proposed changes to the knowledge base and registry on a branch or in a `proposals/` folder. Nothing merges without review.
7. **Flag.** List stale (over 365 days since verification), broken (source fails) and obsolete (superseded) entries.
8. **Report.** One concise run report.

## Commands
```
python tools/design_kb.py validate          # schema and registry checks
python tools/design_kb.py freshness         # stale and broken candidates (offline: dates only)
python tools/design_kb.py freshness --check-urls   # also tries each source URL (network)
python tools/design_kb.py index             # regenerate INDEX.md and REGISTRY.md
python tools/design_kb.py search <term>     # dedup check before adding
```
`--check-urls` makes outbound requests. Run it only where that is allowed. It sends a HEAD request per unique URL with a polite delay and does not follow login walls.

## Deduplication
- Key on normalized URL and on `id`. Same URL, different date: update the existing entry and bump `verified_on`.
- Near duplicates: compare titles and tags; merge into the stronger entry; add a `superseded` note to the other.

## Version history
Version history is git history. Each run's changes are a reviewed commit with the run report in the message or beside it. Do not rewrite history. Registry entries carry `registry_version` and a pinned ref; skill upgrades are new reviews.

## Run report (`design-intelligence/reports/refresh-<YYYY-MM-DD>.md`)
```
# Design intelligence refresh: <date>
Runner: <who or what started it> | Tool tier: <0-3> | Tools: <names>
Scope: <categories searched>
Added (proposed): <ids with one line each>
Updated: <ids and what changed>
Flagged stale / broken / obsolete: <ids>
Skills: new <ids> | changed <ids, diff reviewed yes/no> | status changes <ids>
Verified how: <methods; what was not verified>
Failures and blocked sources: <list>
Needs human decision: <list>
```

## Approval
Autonomous: reading public sources, writing proposals and the report. Needs Kiran: merging proposals into the shared base when the change alters an approved skill's status, any installation, paid sources, publishing.

## Cadence suggestion
Quarterly for the full run, monthly for skills and motion library documentation. Adjust to your needs. This is a suggestion, not a schedule that exists.
