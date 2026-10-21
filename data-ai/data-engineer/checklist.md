# Data Engineer: Checklist

## Before starting
- [ ] Source inventory written: owner, access method, volume, keys, timezone, edit pattern
- [ ] Consumers and freshness need recorded per source
- [ ] System of record named for every fact two sources share
- [ ] Personal fields listed with an approved treatment (hash, drop, keep)
- [ ] Access is read-only on app databases; writes go only to analytics schemas or a separate project
- [ ] Secrets come from the environment or secrets store, never pasted in chat or code

## While working
- [ ] Raw tables are append-only with `_ingested_at`, `_source`, `_batch_id`
- [ ] Every job takes an explicit half-open window
- [ ] Upsert or delete-insert of the window happens in one transaction
- [ ] Incremental loads use a stored watermark plus a lookback
- [ ] Timestamps stored as UTC; `business_date` derived in IST through one shared function
- [ ] Phone numbers normalized to E.164 before hashing
- [ ] Row count and distinct-key count compared after every join
- [ ] Sheet sources reject the batch when the header hash changes
- [ ] Row-level failures go to a rejects table with a reason
- [ ] Deletes or cancellations propagate (soft delete or key comparison)
- [ ] Scraped or uploaded text stripped of hidden markup before it reaches AI document tables

## Before handoff
- [ ] Same window run twice: zero row changes, counts recorded
- [ ] Closed-day totals reconciled to source (rows and money) for 7 days
- [ ] Each blocking check proven to block with deliberately bad data
- [ ] 50-row sample of clean and AI-facing tables shows no raw phone, email, child name or health note
- [ ] Data dictionary written for every clean table, including grain
- [ ] Runbook lists alert channel and fix steps
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] The only credential offered can write to the production app database
- [ ] Children's, health or payment data would enter analytics without a minimization decision
- [ ] A backfill would replace more than a month of clean data
- [ ] Data would move to a new vendor, region or paid tier
- [ ] Someone asks to merge data across different clients
