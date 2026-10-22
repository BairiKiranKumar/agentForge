# Security Testing Specialist: Checklist

## Before starting
- [ ] Explicit written authorization charter signed by system owner and the owner
- [ ] Exact testing scope defined (domain, IP list, excluded endpoints, testing hours)
- [ ] Staging environment verified as non-production (no live customer data)
- [ ] Dual test accounts per role provisioned (e.g. Student 1, Student 2, Admin)
- [ ] Prohibited testing methods documented (no DoS, no destructive drops)
- [ ] Third-party service boundaries verified (payment gateways, WhatsApp APIs)

## While working
- [ ] HTTP security headers inspected (CSP, HSTS, X-Frame-Options, CORS)
- [ ] Dependency vulnerabilities audited (`npm audit` / Trivy)
- [ ] Authentication rate limiting tested on login and password reset endpoints
- [ ] Password reset token entropy and expiration evaluated
- [ ] Session invalidation verified upon logout and password update
- [ ] Horizontal access control (IDOR) tested by swapping User IDs between accounts
- [ ] Vertical access control tested by accessing Admin routes from Student account
- [ ] Input validation tested for SQL injection using non-destructive syntax
- [ ] Cross-site scripting (XSS) tested with benign proof probes (`<script>alert(1)</script>`)
- [ ] Client JavaScript bundles searched for hardcoded API keys and secrets
- [ ] Detailed curl reproduction commands captured for every confirmed finding
- [ ] Findings scored objectively using CVSS v3.1 calculator

## Before handoff
- [ ] Every vulnerability finding verified with clean, reproducible proof-of-concept
- [ ] Sensitive passwords, tokens, and PII redacted from report logs
- [ ] Remediation guidance provided for every reported vulnerability
- [ ] Executive summary written with overall risk assessment
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Target environment turns out to be live production without explicit authorization
- [ ] Unauthenticated Remote Code Execution or total database access is discovered
- [ ] Testing activities cause instability or downtime on shared staging servers
- [ ] Live customer financial or medical data is uncovered in the target environment
