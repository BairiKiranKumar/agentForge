# Retrieval / RAG Specialist: Checklist

## Before starting
- [ ] At least 30 real user questions collected and classified (structured fact, prose, unanswerable)
- [ ] SQL vs full context vs RAG decided per question class
- [ ] Document inventory with owner, language, audience, update frequency and review date
- [ ] Access rules written: tenant, audience, staff-only
- [ ] Embedding provider or local model approved for this client's documents
- [ ] Personal records, chats and secrets excluded from the document set

## While working
- [ ] Chunking rule chosen per document type and recorded
- [ ] Context header (title, section, date, audience) prepended before embedding
- [ ] Every chunk stores document ID, version, language, audience, tenant, validity dates and source
- [ ] Embedding model and version stored per row; one model per index
- [ ] Multilingual model used where Telugu or Hindi content or queries exist
- [ ] HNSW index with the distance metric matching the model
- [ ] Keyword search uses `simple` full-text plus `pg_trgm`
- [ ] Access filters in the SQL `WHERE` clause and enforced by RLS
- [ ] Hybrid fusion with RRF before trying weighted fusion
- [ ] Reranker kept only if the eval shows a gain beyond noise and latency fits
- [ ] Hidden text stripped and instruction-like chunks flagged at index time
- [ ] Document updates replace all chunks of the old version in one transaction
- [ ] Deleted and expired documents removed from the index

## Before handoff
- [ ] Golden set labelled before tuning, with at least 20% unanswerable and language coverage
- [ ] recall@5, recall@20, MRR, no-answer accuracy and leakage reported from a recorded run
- [ ] At least 10 cross-tenant or cross-audience queries show zero leakage
- [ ] Changed document returns only new-version chunks in a test query
- [ ] Retrieval API contract published with limits and latency
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Asked to index customer chats, student records or patient notes
- [ ] Client documents would go to an unapproved external API
- [ ] Tenants would share an index without filters and RLS
- [ ] No owner exists to keep prices, fees or timings current
