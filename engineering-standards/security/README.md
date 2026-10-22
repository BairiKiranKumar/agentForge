# Security standard (v1.0.0)

Verified on 2026-10-22. Requirements: `requirements.yaml` (SEC-001 to SEC-035). Meeting them is evidence of good practice, not a security certification. No agent is a certified security professional.

## Authorization warning (mandatory)
Do not run destructive or intrusive security tests (active scanning, fuzzing, exploitation, load or brute-force attempts, credential attacks) against real environments without written authorization from the system owner, stating scope, targets, method and time window. Default to a dedicated test environment with synthetic data. SEC-035 enforces this. Without authorization, stop at preparing the test plan.

## Scope and non-goals
In scope: application-level controls for web products and APIs, secure delivery pipeline and supply chain. Non-goals: network and physical security, formal penetration testing, certification, legal compliance, AI-specific risks (see `ai-security`), personal data governance (see `privacy`).

## Applying by product type
- `website`: headers and CSP, XSS, transport, cookies if any, dependencies, secrets, supply chain.
- `web-app`, `mobile-web`, `internal-tool`: everything, with authentication, authorization, sessions and CSRF central.
- `api`: authentication, authorization, token validation, input validation, rate limiting, headers, errors, logging.
- `library`: dependencies, secrets, supply chain, input handling, secure CI/CD.
- `ai-app`: all that apply plus `ai-security`.
- Profiles: `lightweight` covers the critical basics (auth, authorization, injection, XSS, transport, secrets, dependencies, authorization of testing). `standard` adds access-control test matrices, CSP, CSRF depth, rate limits, logging protection and pipeline controls. `high_assurance` adds supply-chain assessment.

## ASVS mapping (what was and was not verified)
The OWASP ASVS GitHub README states the latest stable version is 5.0.0 (May 2025), and the OWASP project page lists 5.0.0 as stable. Chapter names below were read from the file names in the v5.0.0 tag (directory `5.0/en`). The text of the chapters and individual requirement ids (such as `6.2.1`) were not read, so mapping is chapter-level only and the choice of chapter for each topic is [Inference].

| Chapter | Name |
|---|---|
| V1 | Encoding and Sanitization |
| V2 | Validation and Business Logic |
| V3 | Web Frontend Security |
| V4 | API and Web Service |
| V5 | File Handling |
| V6 | Authentication |
| V7 | Session Management |
| V8 | Authorization |
| V9 | Self-contained Tokens |
| V10 | OAuth and OIDC |
| V11 | Cryptography |
| V12 | Secure Communication |
| V13 | Configuration |
| V14 | Data Protection |
| V15 | Secure Coding and Architecture |
| V16 | Security Logging and Error Handling |
| V17 | WebRTC |

Where a requirement cites a cheat sheet or MDN instead of an ASVS chapter, the chapter was not confirmed for that topic. For example file upload (V5), sessions (V7) and tokens (V9) have likely chapters, but SEC-009, SEC-015 and SEC-017 cite the sources actually read. Dependency and supply-chain topics are not mapped to a chapter. OWASP Top 10:2025 categories read (A01 Broken Access Control, A02 Security Misconfiguration, A03 Software Supply Chain Failures, A04 Cryptographic Failures, A05 Injection, A06 Insecure Design, A07 Authentication Failures, A08 Software or Data Integrity Failures, A09 Security Logging and Alerting Failures, A10 Mishandling of Exceptional Conditions) are used for awareness; they are a risk list, not a verification standard.

## Methods
1. Threat model new features (SEC-034).
2. Design review against the requirement list; record each requirement as met, not met, or not applicable with reason.
3. Static checks: code scanner, secret scan, dependency scan in CI.
4. Dynamic checks in a test environment: header capture, TLS scan, authenticated scan, targeted manual tests.
5. Manual access-control testing: build a role-by-endpoint matrix; for each, test own objects, other users' objects, higher-privilege functions and skipped workflow steps; record request, expected, actual.
6. Review: an independent role verifies the evidence (owner and reviewer differ).

## Tools evaluated (free first; facts from official repositories read 2026-10-22)
| Tool | Purpose | Licence as read | Notes |
|---|---|---|---|
| Ecosystem audit commands (npm audit, pip-audit, cargo audit, etc.) | dependency vulnerabilities | not checked | [Unverified]; pick the one for your ecosystem and check its page |
| OSV-Scanner | dependency vulnerability scan with OSV data | Apache-2.0 | sends package names, versions, ecosystems and file hashes to the OSV.dev API, per its README; not source code |
| Gitleaks | secret scanning | MIT | README says feature complete, security patches only, maintainer moving focus to another tool; evaluate before long-term adoption |
| Semgrep (Community Edition) | static analysis | repository LGPL-2.1; registry rule licence not stated on the page | single function or file analysis only, so cross-file flows can be missed; Pro rules are proprietary |
| OWASP ZAP | dynamic web scanner | Apache-2.0 | free; use only in a test environment or with written authorization; its README did not carry an authorization warning, that rule is this standard's |
| OpenSSF Scorecard | project security-practice checks | Apache-2.0 | automated scores per check; heuristic, not proof |
| SLSA | build integrity levels framework | not a tool | only the retired v1.0 levels page was read (L0 to L3); v1.2 is stated as current, details not read |
Optional paid scanners and bug-bounty platforms are not evaluated.

## Test matrix
| Area | Check type | Where | Authorization needed |
|---|---|---|---|
| Authentication and sessions | manual and scripted | test environment | none for own test env |
| Access control | manual matrix | test environment | none for own test env |
| Injection and XSS | scanner plus manual | test environment | written for anything shared or real |
| Headers, CSP, TLS | automated capture | deployed test or production read-only requests | passive requests only; intrusive needs written approval |
| Dependencies, secrets | automated in CI | repository | none |
| Pipeline | manual review | CI settings | owner access |

## Severity classification
Critical: exposes users or data or lets an attacker take over accounts or bypass authorization (authentication, authorization, injection, XSS, secrets exposure, transport, authorization of testing). It blocks release in every profile that includes it and is never averaged away. Major: weakens a defence layer (headers, CSP, rate limits, logging). Minor: hygiene.

## What automated tools cannot prove
Scanners miss business-logic flaws, broken access control across roles, chained issues and anything behind unexercised flows. A clean scan is not proof of security. Secret scanners miss encoded or non-pattern secrets. Dependency scanners flag known vulnerabilities only, and reachability needs judgement. Header scans do not show whether a CSP actually blocks injection.

## Recording planned versus executed checks
Per release, list each SEC id with planned check, executed flag, tool and version, environment, date, build, result and evidence link. Not executed means not passed. Record authorization references next to any intrusive test.

## References (retrieved 2026-10-22)
Read: OWASP ASVS GitHub and project page, OWASP Top 10:2025 page, OWASP cheat sheets (CSP, CSRF, file upload, session management, secrets management, logging, REST security), MDN CSP, cookies guide and Strict-Transport-Security, SLSA v1.0 levels (retired page), and the repositories of OpenSSF Scorecard, OSV-Scanner, Gitleaks, Semgrep and ZAP.
Not read: ASVS chapter content, the OWASP cheat sheets for XSS, authentication, input validation, SQL injection and others, MDN header guide (URL returned 404), SLSA v1.2, tool documentation beyond repository READMEs.

## Limitations and as-of dates
As of 2026-10-22. Versions and recommendations change; recheck ASVS version, OWASP lists and tool licences before reuse. Header values and timeouts are decisions per project, not fixed here.
