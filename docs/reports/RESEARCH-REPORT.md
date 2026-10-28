# Research Report: Source Assessment and Roster Architecture

Date of completion: October 2026  
Scope: Architecture, sourcing, evaluation, and provenance for the 179-role `ai-team` repository.

---

## 1. Executive Summary

The `ai-team` repository represents a comprehensive multi-agent operational team consisting of 179 distinct functional roles across 26 departments. To construct this system with high domain rigor, we conducted an exhaustive investigation of 22 public open-source agent repositories, skill libraries, and prompt collections.

All 22 candidate repositories were shallow-cloned, systematically read, and categorized into three distinct tiers:
1. **Selected (10 repositories)**: Permissively licensed (MIT or Apache-2.0), technically rigorous, and directly adapted with attribution.
2. **Reference (8 repositories)**: Evaluated for architectural concepts, workflows, checklists, or topic coverage, but not directly copied due to licensing limitations, derivative nature, or uneven depth.
3. **Rejected (4 repositories)**: Excluded entirely due to incompatible licenses (e.g., Commons Clause, PolyForm Noncommercial), lack of licensing (all rights reserved), or bundled vendor lock-in.

Across the 179 roles, 100 roles were directly seeded from high-quality upstream material. The remaining 79 roles (including India-specific tax, legal compliance, and localized operations) were authored cleanly from primary statutes, regulatory filings, and domain engineering standards.

---

## 2. Discovery Methodology

To identify candidate repositories, we conducted targeted queries across developer communities, GitHub repositories, and AI agent registries, focusing on:
- Multi-agent frameworks and subagent libraries (Claude Code subagents, Copilot agents, Agent Skills).
- Specialized business, legal, financial, and operational skills.
- Localized compliance standards (India GST, DPDP Act 2023, TDS, MCA rules).

Repositories were evaluated against five concrete quality gates:
1. **Legal Permissibility**: Valid open-source license (MIT, Apache-2.0, or CC-BY-4.0). Rejection of non-commercial restrictions (CC-BY-NC, PolyForm Noncommercial), Commons Clause restrictions, and unlicensed works.
2. **Methodological Depth**: Presence of actionable domain workflows, checklists, decision matrices, and edge-case handling rather than generic summaries.
3. **Absence of Fictional Personas**: Elimination of fabricated credentials (e.g., "Cassandra, 15+ years Big Four") and simulated emotional states.
4. **Tool and Vendor Independence**: Separation of functional domain methods from proprietary SaaS connectors (e.g., CRM or ERP platforms), ensuring graceful fallback to standard text and file data.
5. **Prompt Safety**: Absence of coercive triggers (e.g., "Use PROACTIVELY", "MUST BE USED") that provoke invocation conflicts, and strict containment of untrusted inputs.

---

## 3. Repositories Assessed

### 3.1 Selected Repositories (Adapted with Attribution)

1. **`anthropics/knowledge-work-plugins`** (Commit `a266ab8`, Apache-2.0)
   - *Strengths*: Premier source for business operations, legal contract review, finance, sales objection handling, and customer support triage. Features explicit gatekeeping (e.g., books must be closed before tax calculations), untrusted data handling, and structured templates.
   - *Adaptation*: Stripped US-centric tax/payroll assumptions; preserved decision criteria and escalation thresholds.
2. **`anthropics/claude-for-legal`** (Commit `4a6c651`, Apache-2.0)
   - *Strengths*: Highly rigorous legal workflows covering IP review, OSS licensing, commercial contract analysis, and data privacy impact assessments.
   - *Adaptation*: Preserved legal guardrails, practice profile concepts, and attorney routing while localizing statutory references to Indian law.
3. **`msitarzewski/agency-agents`** (Commit `4e3ac3c`, MIT)
   - *Strengths*: Broad coverage across 18 agency divisions; excellent operational frameworks for incident response, application security, and sales discovery (SPIN, Gap Selling).
   - *Adaptation*: Stripped all vibe/persona blocks, US-only tax provisions (IRS, Section 179), and China-specific marketing channels.
4. **`wshobson/agents`** (Commit `0874a27`, MIT)
   - *Strengths*: Leading source for software engineering, cloud architecture, CI/CD, postmortem analysis, and UI/accessibility foundations. Progressive disclosure structure.
   - *Adaptation*: Removed coercive "Use PROACTIVELY" description triggers; adapted reference files into core checklists.
5. **`coreyhaines31/marketingskills`** (Commit `e85f3cb`, MIT)
   - *Strengths*: Exceptional marketing playbooks, cold email deliverability guidelines, and the sole open repository providing actionable WhatsApp Business workflows.
   - *Adaptation*: Removed vendor sponsorship links; adapted FTC disclosure guidance to ASCI guidelines for the Indian market.
6. **`phuryn/pm-skills`** (Commit `07b34f6`, MIT)
   - *Strengths*: Methodologically clean product management skills (Mom Test customer interviews, lean PRDs, assumption mapping) without persona fluff.
   - *Adaptation*: Directly adapted into product, discovery, and GTM specialist roles.
7. **`alirezarezvani/claude-skills`** (Commit `19392f7`, MIT)
   - *Strengths*: Valuable operational depth in customer success health scoring, vendor management matrices, capacity planning, and RevOps.
   - *Adaptation*: Extracted unique operational logic while filtering out uncredited duplicate copies of `marketingskills` and unsupported Python CLI scripts.
8. **`github/awesome-copilot`** (Commit `613efc8`, MIT umbrella)
   - *Strengths*: In-depth accessibility instructions (WCAG 2.2 AA), modern Next.js specifications, and enterprise account planning (MEDDICC).
   - *Adaptation*: Adopted high-quality individual components while attributing per-item copyright holders (e.g., Andrew Stellman for `quality-playbook`, Smit Patel for `gtm-*`).
9. **`obra/superpowers`** (Commit `bb92a77`, MIT)
   - *Strengths*: Uncompromising software engineering discipline: systematic root-cause debugging, test-driven development, code review protocols, and subagent dispatching.
   - *Adaptation*: Formed the core execution philosophy for developer, code reviewer, and orchestrator roles.
10. **`anthropics/skills`** (Commit `dbd4588`, Apache-2.0 subset)
    - *Strengths*: Canonical reference skills for frontend aesthetics, skill creation rubrics, and brand voice guidelines.
    - *Adaptation*: Adapted Apache-2.0 components; strictly excluded proprietary document skills (`docx`, `pdf`, `pptx`, `xlsx`).

### 3.2 Reference Repositories (Consulted for Concepts)

1. **`VoltAgent/awesome-claude-code-subagents`** (Commit `408d3c9`, MIT): Evaluated as a topic checklist. Rejected body text due to uniform keyword checklists and fabricated delivery metrics (e.g., claims of saving millions in risk).
2. **`lst97/claude-code-sub-agents`** (Commit `96f5a50`, MIT): Thin derivative of `wshobson/agents` with hard-coded MCP dependencies; consulted for role scoping.
3. **`vijaythecoder/awesome-claude-agents`** (Commit `2050f3c`, MIT): Useful multi-agent routing limits (e.g., maximum two parallel agents), but overly narrow dev focus.
4. **`0xfurai/claude-code-subagents`** (Commit `9236d10`, MIT): Generic 50-line framework checklists; partly dated (recommends React PropTypes).
5. **`iannuttall/claude-agents`** (Commit `f7df2c3`, MIT): Clean but small PRD and content writing templates; superseded by `phuryn/pm-skills`.
6. **`deanpeters/Product-Manager-Skills`** (Commit `cfcb697`, CC-BY-NC-SA-4.0): High-quality PM discovery playbooks, but non-commercial license legally prevents direct reuse in a commercial agency repository. Consulted for structural ideas only.
7. **`openaccountants/openaccountants`** (Commit `e1d91b6`, AGPL-3.0 / Guide License): Contains 1,000+ lines on Indian GST and tax mechanics. Custom guide license prohibits embedding in commercial AI products. Used strictly as a topic checklist to locate primary Indian government statutes.
8. **`basecamp/handbook`** (Commit `c953606`, NOASSERTION): Informative policy prose (moonlighting boundaries, title ladders), but repository lacks an explicit open-source license.

### 3.3 Rejected Repositories (Excluded)

1. **`davepoon/claude-code-subagents-collection`** (Commit `868d035`): Marketplace aggregator with mixed nested licenses, including non-commercial code (`PolyForm-Noncommercial-1.0.0`). Unclear per-file copyright provenance.
2. **`contains-studio/agents`** (Commit `a5a480c`): No license file in repository; default copyright applies (all rights reserved). Persona-heavy and stale.
3. **`ComposioHQ/awesome-claude-skills`** (Commit `be2a406`): Lacks a repository LICENSE file. Bundles proprietary Anthropic files without clear rights, and 95% of content consists of vendor-specific connection stubs.
4. **`borghei/Claude-Skills`** (Commit `4a698e8`): Governed by Commons Clause (restricting commercial sale) and contains relicensed upstream MIT material without clear separation.

---

## 4. Departmental Source Mapping

| Department | Primary Upstream Source | Secondary / Reference Source | Adaptation Strategy |
|---|---|---|---|
| `leadership` | `anthropics/knowledge-work-plugins` | `msitarzewski/agency-agents` | Focus on governance, decision logs, and delegation |
| `strategy` | `phuryn/pm-skills` | `wshobson/agents` | Market sizing, strategic defensibility, lean canvas |
| `product` | `phuryn/pm-skills` | `anthropics/knowledge-work-plugins` | Problem-first discovery, lean PRDs, assumption grids |
| `research` | `phuryn/pm-skills` | `anthropics/knowledge-work-plugins` | Mom Test user interviews, qualitative synthesis |
| `design` | `wshobson/agents` | `anthropics/skills` | WCAG 2.2 AA, token systems, anti-generic design |
| `content` | `coreyhaines31/marketingskills` | `anthropics/knowledge-work-plugins` | Direct copywriting, readability, brand voice |
| `dev` | `wshobson/agents` | `obra/superpowers` | TDD, strict root-cause debugging, clean modularity |
| `data-ai` | `wshobson/agents` | `anthropics/skills` | Evaluation pipelines, RAG architecture, LLM guardrails |
| `qa` | `obra/superpowers` | `github/awesome-copilot` | Deterministic Playwright tests, accessibility audits |
| `security` | `msitarzewski/agency-agents` | `wshobson/agents` | STRIDE threat modeling, OWASP Top 10, SAST |
| `devops` | `wshobson/agents` | `msitarzewski/agency-agents` | CI/CD pipelines, containerization, incident runbooks |
| `marketing` | `coreyhaines31/marketingskills` | `alirezarezvani/claude-skills` | Deliverability, landing page conversion, funnel math |
| `social-media` | `coreyhaines31/marketingskills` | Primary platform specs | Platform constraints, WhatsApp BSPs, LinkedIn hooks |
| `sales` | `anthropics/knowledge-work-plugins` | `msitarzewski/agency-agents` | MEDDICC qualification, objection handling, proposals |
| `customer-success` | `alirezarezvani/claude-skills` | `anthropics/knowledge-work-plugins` | Weighted health scoring, retention, onboarding |
| `finance` | `anthropics/knowledge-work-plugins` | Indian primary statutes | Books-closed gate, GST SAC codes, advance tax |
| `legal-compliance` | `anthropics/claude-for-legal` | Indian primary statutes | DPDP Act 2023, Indian Contract Act, not-legal-advice |
| `people-hr` | `anthropics/knowledge-work-plugins` | `wshobson/agents` | Structured scoring rubrics, Shops and Establishments |
| `operations` | `msitarzewski/agency-agents` | `alirezarezvani/claude-skills` | VSM, SIPOC, vendor scorecards, standard SOPs |
| `support` | `anthropics/knowledge-work-plugins` | `msitarzewski/agency-agents` | P1 to P4 severity classification, ticket triage |
| `project-delivery` | `alirezarezvani/claude-skills` | `obra/superpowers` | PERT estimation, scope change control, UAT sign-off |
| `orchestration` | `obra/superpowers` | `vijaythecoder/awesome-claude-agents` | Smallest-team dispatching, loop prevention |

---

## 5. Licensing and Legal Compliance

To ensure complete copyright and license compliance:
1. **Verbatim Licenses Maintained**: Clean copies of all upstream licenses are stored in `sources/licenses/`.
2. **Machine-Readable Metadata**: Every role in `orchestration/roster.yaml` records upstream provenance, and `SOURCE-MANIFEST.md` provides an itemized index.
3. **In-File Attribution**: Every `AGENT.md` includes Section 12 ("Provenance and adaptation notes"), citing upstream repositories, commits, and modifications.
4. **Derivative Cleanliness**: Where upstream files contained non-commercial clauses, proprietary code, or missing licenses, clean-room authoring was performed based solely on public technical standards and government publications.
