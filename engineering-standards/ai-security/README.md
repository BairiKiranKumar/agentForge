# AI security standard (v1.0.0)

Verified on 2026-10-22. Requirements: `requirements.yaml` (AISEC-001 to AISEC-028). Evidence of good practice, not certification or a guarantee against attack.

## Scope and non-goals
In scope: products that use an LLM or agent at runtime (`ai-app`): prompt injection, excessive agency, unsafe tool use, sensitive data leakage, model and supply-chain risk, improper output handling, retrieval and memory risks, consumption abuse, human approval for consequential actions. Non-goals: model training safety research, content policy and bias evaluation (owned by evaluation roles), general application security (see `security`), personal data governance (see `privacy`).

## Applying
- Applies to `ai-app`. Other product types that embed AI-generated content should still apply AISEC-009 (treat output as untrusted).
- Profiles: `lightweight` has the must-haves (external content as data, permissions outside the model, human approval, output handling, no secrets in prompts, authorized red teaming). `standard` adds retrieval controls, supply-chain inventory, consumption limits, logging and adversarial suites. `high_assurance` adds memory and inter-agent controls and AI incident response.

## Lists used and their verification status
- OWASP Top 10 for LLM Applications, 2025 edition: the GenAI Security Project page shows 2025 as current and links the earlier 2023-24 version. Ids and titles read: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption. The per-item descriptions were not read, so mappings in the YAML use ids and titles only and the fit is [Inference].
- OWASP Top 10 for Agentic Applications for 2026: a resource page exists and shows publication date 2025-12-09. That page did not list the risks. Secondary summaries gave ASI01 to ASI10 names (for example goal hijack, tool misuse, identity and privilege abuse, memory and context poisoning, insecure inter-agent communication, cascading failures, rogue agents), but these are [Unverified] against the primary document. The YAML cites the resource page only where memory, inter-agent and cascading-failure controls are described.
- OWASP LLM Prompt Injection Prevention cheat sheet: read; drives AISEC-003, 004, 007, 008, 022. Its main points: filters are not a boundary, enforce permissions outside the model, approvals must bind to the exact operation, treat model output and external content as untrusted, run measured smoke tests and report their limits.

## Methods
1. Draw the data and trust-boundary diagram: every input that reaches the model, every tool it can call, every sink for its output.
2. Assume injection will sometimes succeed; limit what a hijacked model can do (scoped tools, no standing credentials, approvals, sandbox, caps).
3. Test with a versioned adversarial suite in a non-production setup. State the violation definition, run repeatedly, record model version and prompt version, measure false positives on benign requests, and report the sample size and limits.
4. Review human-approval screens for exact target and arguments.
5. Re-test after model, prompt, retrieval or tool changes.

## Tools evaluated
No AI security scanner was installed or run for this standard. Free options to evaluate per project (not verified here): general scanners from the `security` standard (secret scan, dependency scan), custom test harnesses written for your tools, and open-source LLM test frameworks [Unverified: names, licences and maintenance not checked]. Guardrail classifiers are one layer and can themselves be attacked, add latency and cost, and need logging and drift monitoring (per the prompt-injection cheat sheet).

## Test matrix
| Risk | Test | Environment |
|---|---|---|
| Direct and indirect injection | hostile text in user input, documents, web pages, tool results | test with synthetic data |
| Excessive agency | request forbidden tools and arguments; check refusal in code | test |
| Output handling | hostile output into each sink (HTML, SQL, shell, path) | test |
| Data leakage | cross-user and cross-tenant retrieval; secret extraction attempts | test |
| Consumption | loops, long inputs, tool-call storms | test with caps |
| Approval bypass | alter arguments after approval | test |

## Severity classification
Critical: an attacker-controlled input can cause an unapproved consequential action, leak another user's data, expose secrets, or run code. Major: weak controls that make those outcomes likelier. Minor: hygiene, documentation. Critical failures block release in every profile that includes them.

## What automated tools and evals cannot prove
A passing suite shows resistance to those cases only. Models are non-deterministic, attackers rephrase, encode or use other languages, and rate limits do not stop eventual success. Evals do not prove absence of injection, hallucination or leakage. Provider behaviour changes with model updates.

## Recording planned versus executed checks
For each AISEC id log: planned test, executed (yes/no), model and prompt version, date, suite version, violations found, evidence link. Unexecuted tests are reported as unexecuted.

## References (retrieved 2026-10-22)
Read: OWASP Top 10 for LLM Applications page (2025 edition), OWASP agentic resource page (title and date only), OWASP LLM Prompt Injection Prevention cheat sheet, OWASP logging and secrets cheat sheets. Not read: full LLM Top 10 item pages, the agentic Top 10 document, any NIST or vendor AI risk framework.

## Limitations and as-of dates
This area changes quickly. Both OWASP lists are recent editions as of 2026-10-22; recheck for newer editions. No tests were executed to produce this document.
