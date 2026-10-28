# Gaps, Limitations, and Operational Caveats

Last updated: October 2026  
Status: Production Baseline

This document provides transparent documentation of known operational boundaries, untested baselines, legal/statutory constraints, and platform dependencies across the `ai-team` repository.

---

## 1. Untested Baseline Status for 179 Roles

All 179 roles in this repository have been fully authored to the four-file standard:
- `AGENT.md`: Complete 12-section behavioral definition
- `checklist.md`: Step-by-step procedural gates and acceptance checks
- `examples.md`: Realistic input and output demonstrations
- `evaluation.md`: Benchmark test cases, scoring rubrics, and failure thresholds

### Operational Caveat:
While every role has undergone rigorous structural and cross-reference validation (0 errors, 0 warnings in `tools/validate.py`), live behavioral execution against large language model benchmarks remains an **untested baseline**.

Unlike upstream collections that published fabricated performance metrics (e.g., claiming hundreds of simulated contracts reviewed or millions saved without proof), `ai-team` deliberately reports zero fabricated benchmark results. Each agent's real-world accuracy, token efficiency, and tool execution fidelity must be measured and calibrated through live operational use.

---

## 2. Indian Business, Legal, and Regulatory Facts

A key architectural enhancement of `ai-team` is native support for Indian business operations, tax filings, and legal compliance. Users must understand the verified scope versus legal boundaries:

### Verified Primary Sources
- **Goods and Services Tax (GST)**:
  - Rates, SAC/HSN codes, GSTR-1, GSTR-3B, and GSTR-9 mechanics reflect recommendations of the GST Council as of September 2025.
  - Input Tax Credit (ITC) reconciliation and reverse charge mechanism (RCM) workflows align with CBIC statutory guidelines.
- **Direct Tax (Income Tax)**:
  - Advance tax installment schedules (June 15, September 15, December 15, March 15).
  - Presumptive taxation limits under Section 44AD (turnover up to INR 3 crore for digital receipts) and Section 44ADA (gross receipts up to INR 75 lakh).
  - TDS rates under Section 194J (2% for technical services, 10% for professional services) and Section 194C.
- **Data Privacy (DPDP Act 2023)**:
  - Workflows reflect the enacted provisions of the Digital Personal Data Protection Act, 2023, including Data Principal rights, consent notice structures, and Data Protection Board adjudication pathways.

### Unverified and Secondary Assumptions (Subject to Change)
- **Draft DPDP Implementing Rules**: Detailed procedural rules regarding Consent Managers and breach notification timelines remain subject to notifications from the Ministry of Electronics and Information Technology (MeitY).
- **State-Specific Labor Regulations**: Professional tax slabs, shop registration renewal cadences, and holiday calendars vary by state (e.g., Telangana Shops and Establishments Act vs Karnataka). Agents supply standard templates requiring local verification.

### Mandatory Legal and Tax Disclaimer:
> **IMPORTANT**: AI agents are not advocates, chartered accountants, company secretaries, or tax practitioners. Outputs produced by `legal-compliance` and `finance` roles are preliminary work-product drafts for review. All contracts, tax computations, and regulatory filings must be formally reviewed and signed off by a qualified professional licensed in the relevant jurisdiction.

---

## 3. Upstream Licensing Splits and Nuances

Users and contributors must be aware of upstream licensing boundaries:

1. **`anthropics/skills`**:
   - The majority of skills in this repository are licensed under Apache-2.0.
   - However, four document skills (`docx`, `pdf`, `pptx`, `xlsx`) carry a proprietary Anthropic source-available license (`LicenseRef-Anthropic-Proprietary`), and `doc-coauthoring` lacks an explicit license.
   - **Resolution in ai-team**: The proprietary document skills were strictly excluded from direct code or text adaptation. Document generation in `ai-team` relies on open-source libraries (e.g., Markdown, ReportLab, standard CLI tooling).
2. **`github/awesome-copilot`**:
   - Governed by an umbrella MIT license, but several nested skills carry distinct licenses (e.g., `quality-playbook` and `anti-ui-slop` are Apache-2.0).
   - **Resolution in ai-team**: Individual file licenses and original authors (such as Andrew Stellman and Smit Patel) are explicitly credited in `SOURCE-MANIFEST.md` and Section 12 of adapted agents.
3. **`openaccountants/openaccountants`**:
   - Software is AGPL-3.0; tax guides are governed by the custom OpenAccountants Guide License v1.0, which restricts commercial redistribution.
   - **Resolution in ai-team**: Zero text or code was copied from this repository. It was used solely during research to compile an inventory of relevant Indian tax topics, followed by clean-room authoring from official CBIC and Income Tax Department portals.

---

## 4. Multi-Agent Orchestration and Rate Limits

When executing multi-agent workflows (WF-01 through WF-20):

1. **Provider Rate Limits**:
   - Invoking large swarms of agents in parallel can quickly exhaust LLM provider token buckets (for example Anthropic tier rate limits).
   - **Mitigation**: Follow `orchestration/parallel-execution.md`. Run only the stages in the current wave, and only when they have separate files. Keep the team inside the size caps. A host that cannot spawn workers runs that wave in order and says so. Do not add idle specialists to look parallel.
2. **Context Window Degradation**:
   - Passing cumulative conversational histories across more than 4 agents causes context pollution and diminished instruction adherence.
   - **Mitigation**: Enforce the standard handoff format. Each handoff passes only the synthesized deliverables, explicit assumptions, and inputs required for the next stage.

---

## 5. Tooling and Connector Fallbacks

While agent definitions specify recommended tools (such as GitHub, Playwright, Supabase, or WhatsApp BSPs):
- Agents do not have hard-coded software dependencies.
- In environments where MCP servers or API connectors are unavailable, agents automatically degrade gracefully to text-based prompts, requesting file uploads or raw text pasting.

---

## 6. agentForge 1.0 runtime limits

- `runtime/router.py` matches keywords. It is not a semantic judge. Unknown tasks fall back to `orchestrator`.
- `runtime/scheduler.py` orders stages and can run command workers concurrently. It does not call a model and does not produce specialist prose by itself.
- `runtime/discover.py` will not invent a file it cannot fetch, cache, or find locally. Fetched text does not override safety rules or the user.
- PNG, PDF, and video export are real only when the file is on disk. The sample Instagram carousel is HTML and SVG. Its caption records that PNG and PDF export were not run.
- New and existing roles stay `status: untested` until `evaluation.md` is scored into `evaluations/STATUS.md`.
- The role count in older sections of this file described the pre-1.0 handbook. The generated count is `registry/agents.json`.

## 7. Formatting Integrity: Zero Em Dash Policy

To ensure uniform rendering across all terminal pagers, headless CI environments, and markdown viewers, this repository enforces a strict zero-tolerance policy against the Unicode em dash character (U+2014). All markdown documents must use hyphens, colons, semicolons, or parentheses instead.
