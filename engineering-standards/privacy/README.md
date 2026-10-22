# Privacy standard (v1.0.0)

Verified on 2026-10-22. Requirements: `requirements.yaml` (PRIV-001 to PRIV-028).

## Not legal advice, not compliance
These checklists are engineering good practice. A passed checklist never equals legal compliance. Whether a law applies, what lawful basis or consent is needed, notification duties and retention periods are legal questions that need review by a qualified lawyer or privacy professional. No agent holds that credential. PRIV-027 and PRIV-028 enforce this.

## Scope and non-goals
In scope: engineering controls for personal data in web products, APIs and AI applications: minimisation, purpose, consent mechanics, encryption, logging and redaction, retention and deletion, access control, backups, third-party sharing, privacy by design. Non-goals: drafting policies or contracts, legal basis selection, regulator filings, data protection officer duties.

## Applying
- `website`, `mobile-web`: notices, consent and tracker control, cookies, third parties.
- `web-app`, `internal-tool`, `api`: inventory, RBAC, encryption, logging, retention, deletion, backups.
- `ai-app`: all plus PRIV-025 and the `ai-security` standard.
- `library`: minimise what it collects or emits; no telemetry by default.
- Profiles: `lightweight` is inventory, purpose, minimisation, transport encryption, log hygiene, RBAC, no real data in test, and the regulation applicability note. `standard` adds consent flows, retention, deletion, backups, third parties and breach procedure. `high_assurance` adds access logging of sensitive data.

## Regulations as examples only
Mention a regulation only when project context (users' location, data type, sector) justifies it. Verification status as of 2026-10-22:
- CCPA (California): the California Attorney General page was read. It states consumer rights to know, delete, correct, opt out of sale or sharing and limit use of sensitive information, business duties such as notice and request response, and applicability thresholds (revenue, volume of consumers' data, share of revenue from selling data). The page shows it was last updated 2026-08-28. The "CPRA" amendments and the exact thresholds should be confirmed on the page itself.
- GDPR (EU), India's Digital Personal Data Protection Act 2023, and HIPAA (US health): primary sources could not be read in this pass (the EUR-Lex fetch returned no content; the India and HHS pages returned HTTP 403). Any statement about their content is [Unverified]. Use them only as names of regimes that may be relevant, and obtain the primary text and legal review before relying on them. AGENTS.md section 5 also states that the DPDP Act applies to personal data of people in India; that is a repository rule, not independently verified here.

## Principles used in requirements
Data inventory and purpose (PRIV-001, 002); minimisation (003); privacy by design (004); consent mechanics where chosen (005); notice (006); preference signals where applicable (007); encryption in transit and at rest and key separation (008 to 010); logging and redaction (011, 012); retention and deletion (013 to 015); RBAC and access logging (016, 017); backups and recovery (018); third-party sharing and trackers (019, 020); non-production data (021); sensitive categories (022); transfers (023); breach procedure (024); AI data (025); browser exposure (026); regulation applicability and claims (027, 028).

## Methods
1. Build the data inventory from code, schema, logs, analytics configuration and vendor list; confirm with the product owner.
2. For each field record purpose, basis owner (legal decides), retention and recipients.
3. Inspect a clean browser session: cookies, storage, requests to third parties, URLs.
4. Sample logs and error reports for personal data; run a pattern scan for identifiers.
5. Test deletion across stores and a restore from backup (re-apply deletions).
6. Test access with each role.
7. Record regulation applicability and escalate to legal review where flagged.

## Tools evaluated
No privacy tool was run for this standard. Free options to evaluate per project (not verified here): browser DevTools for cookies, storage and network; the secret and pattern scanners listed in the `security` standard for finding identifiers in logs; database queries for deletion checks. Any consent-management or privacy-scanning product is optional, paid status and licence [Unverified].

## Test matrix
| Check | Method | Evidence |
|---|---|---|
| Collection vs purpose | field review | purpose map |
| Trackers and cookies | clean-session network inspection | inventory |
| Logs | sampling and pattern scan | scan output |
| Deletion | per-store query after request | test record |
| Backups | restore drill | drill report |
| Access | role-based tests | matrix |

## Severity classification
Critical: exposes personal data to unauthorized parties (no encryption in transit, uncontrolled access to personal data) or sensitive/children's data collected with no review. Major: missing retention, deletion, consent mechanics where chosen, unmanaged third parties, personal data in logs. Minor: documentation gaps. Failed critical items block release.

## What automated tools cannot prove
Tools cannot decide lawful basis, whether consent is valid, whether a retention period is lawful, whether a third-party contract is adequate, or whether all personal data was found. Pattern scans miss unstructured and encoded data. A clean scan is not proof of absence.

## Recording planned versus executed checks
For each PRIV id log planned check, executed flag, date, environment, evidence link, reviewer, and whether legal review is pending, requested or done. Unexecuted checks are not passed.

## References (retrieved 2026-10-22)
Read: California Attorney General CCPA page, OWASP Logging, Secrets Management and Session Management cheat sheets, OWASP ASVS directory listing (chapter names V12 and V14 only), MDN Strict-Transport-Security, AGENTS.md section 5. Not read: GDPR text, DPDP Act 2023 text, HIPAA Security Rule pages, any regulator guidance, ISO or NIST privacy frameworks.

## Limitations and as-of dates
As of 2026-10-22. Laws and regulator guidance change; thresholds, timelines and definitions must be rechecked from primary sources with legal review. This standard sets no retention periods or notification deadlines.
