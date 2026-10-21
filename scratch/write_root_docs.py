# -*- coding: utf-8 -*-
"""
Script to author root documentation files for ai-team:
- QUICKSTART.md
- RESEARCH-REPORT.md
- GAPS-AND-LIMITATIONS.md
- BUILD-STATUS.md (updated)
Ensures zero em dashes across all files.
"""

import os
import sys

EM_DASH = chr(8212)

def verify_no_em_dash(content: str, filename: str):
    if EM_DASH in content:
        count = content.count(EM_DASH)
        raise ValueError(f"Found {count} em dash characters in {filename}!")
    return content

quickstart_content = """# Quickstart Guide: ai-team

Welcome to `ai-team`. This repository contains a production-grade team of 179 specialized AI agents across 26 departments, designed to run with Claude Code, the Antigravity IDE, or any compatible multi-agent framework.

The agents operate under standardized collaboration rules, strict quality rubrics, and explicit human approval boundaries.

---

## 1. Core Operating Principles

Before invoking any agent or workflow, observe these four core operating rules:

1. **The Smallest-Team Rule**: Always invoke the smallest effective subteam for the task. If a task requires only an estimation specialist, do not dispatch the entire project delivery department. Single specialists should execute simple tasks directly.
2. **Human Approval Boundaries**: AI agents produce work product drafts. Agents must never autonomously send external emails, publish social posts, deploy production code, sign agreements, or initiate financial transactions. Kiran (the human operator) maintains ultimate sign-off authority.
3. **Structured Handoffs**: Every collaboration between agents must follow the standard handoff format:
   - Source agent and target agent
   - Required inputs provided
   - Concrete deliverables produced
   - Explicit assumptions or open questions
   - Proposed next actions
4. **No Slop and No Persona Fluff**: Agents are specialized functional tools. They do not simulate fictional personal backstories, claim fake years of experience, or fabricate performance metrics.

---

## 2. Installation and Setup

### Local Project Installation
To install the 179 agents into a local project directory for use with Claude Code:

```bash
# From the ai-team repository root:
./integrations/claude-code/install.sh --project /path/to/your/project
```

This installs all agent definitions into `/path/to/your/project/.claude/agents/ai-team/` organized into 26 departmental subdirectories.

### Global Installation
To install agents globally for your user environment:

```bash
./integrations/claude-code/install.sh --global
```

This installs agents into `~/.claude/agents/ai-team/`.

### Verifying Installation
Verify that the files were correctly placed:

```bash
ls -la .claude/agents/ai-team/
```

You should see 26 department directories containing a total of 179 agent markdown definition files.

---

## 3. Validation and Tooling

The repository includes comprehensive validation and index generation utilities:

### Global Validation
Run the validator across all 179 roles, references, and roster definitions:

```bash
python3 tools/validate.py
```

Expected output:
```text
Roles checked: 179  Errors: 0  Warnings: 0
```

### Batch or Single-Role Validation
Validate a specific role or batch of roles during development:

```bash
python3 tools/validate.py --roles qa/playwright-specialist dev/backend-developer --skip-global
```

### Rebuilding Indexes and Claude Code Agents
When roster definitions, roles, or capabilities change, rebuild the indices:

```bash
python3 tools/build_indexes.py
```

This updates:
- `TEAM-INDEX.md`: Alphabetical and departmental directory of all 179 roles
- `SOURCE-MANIFEST.md`: Complete attribution and licensing record
- `evaluations/STATUS.md`: Evaluation coverage and readiness tracker
- `integrations/claude-code/agents/`: Standalone Claude Code agent files

---

## 4. Running Workflows (WF-01 to WF-09)

The repository defines nine end-to-end workflows in `workflows/`. Each workflow specifies required roles, sequential stages, artifact handoffs, and human approval gates.

Here are the standard invocation commands for all nine workflows:

### WF-01: Lead to Onboarding
- **Scope**: Outbound lead discovery, qualification, proposal drafting, contract negotiation prep, and client kickoff.
- **Example Invocation**:
  ```text
  "Run WF-01 stages 1 to 4 for home bakeries in Hyderabad. Prepare outreach drafts only; I will send them."
  ```

### WF-02: Client Build and Delivery
- **Scope**: Requirement intake, architecture, sprint planning, development, QA verification, and client delivery.
- **Example Invocation**:
  ```text
  "Run WF-02 for the salon website. Requirements are in clients/salon/requirements.md. Stop before deploy and show me the release plan."
  ```

### WF-03: Product Idea to Iteration
- **Scope**: Product discovery, user interviews, assumption mapping, lean PRD authoring, sprint backlog, and launch metrics.
- **Example Invocation**:
  ```text
  "Run WF-03 stages 1 to 4 for a QR print-shop ordering app. Budget is zero for ads."
  ```

### WF-04: Content Production
- **Scope**: Topic research, editorial drafting, visual asset specification, multi-platform adaptation, and review.
- **Example Invocation**:
  ```text
  "Run WF-04 for a carousel and a Threads post about how the school portal handles fee receipts. Draft only."
  ```

### WF-05: LinkedIn and Social Media Program
- **Scope**: Organic authority building, technical thought leadership, content calendar scheduling, and engagement synthesis.
- **Example Invocation**:
  ```text
  "Run WF-05 and create a two-week LinkedIn and Threads content plan." (Add threads-specialist in stages 3 and 4 for Threads adaptations.)
  ```

### WF-06: SEO and Organic Search Cycle
- **Scope**: Technical SEO audit, keyword opportunity mapping, content optimization, on-page fixes, and schema validation.
- **Example Invocation**:
  ```text
  "Run WF-06 for the preschool website. Audit and prioritize only; no deploys."
  ```

### WF-07: Support Issue Resolution
- **Scope**: Support triage, reproduction, incident classification, root cause analysis, fix drafting, and customer communication.
- **Example Invocation**:
  ```text
  "A parent says the fee receipt PDF is blank on their phone. Run WF-07; draft the reply but don't send."
  ```

### WF-08: Project Recovery and Architecture Audit
- **Scope**: Technical debt assessment, code quality audit, accessibility review, performance profiling, and remediation planning.
- **Example Invocation**:
  ```text
  "Audit an Angular application for accessibility, performance and test gaps." (Run stages 2 and 3 with angular-specialist, accessibility-tester, performance-tester, automation-engineer; output a prioritized gap report.)
  ```

### WF-09: Monthly Account Review
- **Scope**: Account health scoring, deliverable auditing, financial reconciliations, reporting, and QBR agenda preparation.
- **Example Invocation**:
  ```text
  "Run WF-09 for the school client for October. Draft the report and the agenda."
  ```

---

## 5. Direct Specialist Invocation

You do not need to initiate a full workflow for simple, targeted requests. You can invoke individual specialists directly:

### Backend Development Task
```text
"Act as dev/backend-developer. Review the Express route handlers in src/api/orders.ts for missing input validation and unhandled promise rejections. Provide a concise patch."
```

### India GST Tax Compliance Task
```text
"Act as finance/gst-specialist. What are the SAC codes, applicable GST rates, and reverse charge implications for cloud hosting services billed from Singapore to an Indian private limited company?"
```

### End-to-End Testing Task
```text
"Act as qa/playwright-specialist. Write an end-to-end Playwright test suite for the client login and password reset flow located at src/client/auth/."
```

---

## 6. Evaluations and Quality Assurance

Each role folder contains an `evaluation.md` file specifying:
- Core competencies evaluated
- Concrete benchmark test scenarios (inputs, instructions, mock context)
- Expected deliverables and evaluation rubrics (1 to 5 scoring scale)
- Failure thresholds and rejection criteria

To run an evaluation on a role:
1. Provide the benchmark prompt from `evaluation.md` to the agent.
2. Review the output against the quality standards in Section 7 of `AGENT.md` and the rubric in `evaluation.md`.
3. Verify that the agent adhered to all exclusions, clarify-first triggers, and formatting requirements.
"""

research_report_content = """# Research Report: Source Assessment and Roster Architecture

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
"""

gaps_limitations_content = """# Gaps, Limitations, and Operational Caveats

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

When executing multi-agent workflows (such as WF-01 through WF-09):

1. **Provider Rate Limits**:
   - Invoking large swarms of agents in parallel can quickly exhaust LLM provider token buckets (e.g., Anthropic tier rate limits).
   - **Mitigation**: Workflows must be executed sequentially stage-by-stage. Apply the Smallest-Team Rule: do not invoke secondary or optional specialists unless explicitly required by stage deliverables.
2. **Context Window Degradation**:
   - Passing cumulative conversational histories across more than 4 agents causes context pollution and diminished instruction adherence.
   - **Mitigation**: Enforce the standard handoff format. Each handoff passes only the synthesized deliverables, explicit assumptions, and inputs required for the next stage.

---

## 5. Tooling and Connector Fallbacks

While agent definitions specify recommended tools (such as GitHub, Playwright, Supabase, or WhatsApp BSPs):
- Agents do not have hard-coded software dependencies.
- In environments where MCP servers or API connectors are unavailable, agents automatically degrade gracefully to text-based prompts, requesting file uploads or raw text pasting.

---

## 6. Formatting Integrity: Zero Em Dash Policy

To ensure uniform rendering across all terminal pagers, headless CI environments, and markdown viewers, this repository enforces a strict zero-tolerance policy against the Unicode em dash character (U+2014). All markdown documents must use hyphens, colons, semicolons, or parentheses instead.
"""

build_status_content = """# Build Status

Last updated: October 2026  
Status: COMPLETE (100% of roles built and validated)

---

## 1. Summary Metrics

- **Total Departments**: 26
- **Total Functional Roles**: 179
- **Files per Role**: 4 (`AGENT.md`, `checklist.md`, `examples.md`, `evaluation.md`)
- **Total Role Files**: 716
- **Validation Status**: `python3 tools/validate.py` passes with **0 errors and 0 warnings** across all 179 roles.
- **Index Status**: `TEAM-INDEX.md`, `SOURCE-MANIFEST.md`, and `evaluations/STATUS.md` fully generated and up to date.
- **Claude Code Integration**: 179 subagents generated in `integrations/claude-code/agents/` and verified with `install.sh`.

---

## 2. Department Breakdown (179 Roles)

| Department | Roles | Status |
|---|---|---|
| `analytics` | 6 | Complete (6/6) |
| `client-onboarding` | 4 | Complete (4/4) |
| `content` | 8 | Complete (8/8) |
| `customer-success` | 5 | Complete (5/5) |
| `data-ai` | 9 | Complete (9/9) |
| `design` | 13 | Complete (13/13) |
| `dev` | 14 | Complete (14/14) |
| `devops` | 8 | Complete (8/8) |
| `finance` | 7 | Complete (7/7) |
| `knowledge-management` | 4 | Complete (4/4) |
| `leadership` | 4 | Complete (4/4) |
| `legal-compliance` | 8 | Complete (8/8) |
| `marketing` | 12 | Complete (12/12) |
| `operations` | 6 | Complete (6/6) |
| `orchestration` | 2 | Complete (2/2) |
| `partnerships` | 4 | Complete (4/4) |
| `people-hr` | 6 | Complete (6/6) |
| `product` | 6 | Complete (6/6) |
| `project-delivery` | 10 | Complete (10/10) |
| `qa` | 10 | Complete (10/10) |
| `research` | 5 | Complete (5/5) |
| `sales` | 12 | Complete (12/12) |
| `security` | 8 | Complete (8/8) |
| `social-media` | 8 | Complete (8/8) |
| `strategy` | 5 | Complete (5/5) |
| `support` | 5 | Complete (5/5) |
| **Total** | **179** | **100% COMPLETE** |

---

## 3. Workflows and Governance

- **Nine End-to-End Workflows**: Fully defined in `workflows/` (WF-01 to WF-09).
- **Core Governance**: `AGENTS.md` establishes team-wide operating standards, human sign-off gates, and structured handoff protocols.
- **Capability Matrix**: `CAPABILITY-MATRIX.md` maps every role to core capabilities and records the 8 resolved architectural boundaries.
- **Research and Provenance**: `RESEARCH-REPORT.md`, `sources/repos.json`, and `SOURCE-MANIFEST.md` record complete provenance across all 22 assessed repositories.
- **Operational Boundaries**: `GAPS-AND-LIMITATIONS.md` documents untested baseline status, Indian regulatory specifics, and license splits.

---

## 4. Verification and Packaging

- Global validation passed: `python3 tools/validate.py` (Roles checked: 179, Errors: 0, Warnings: 0).
- Claude Code installer verified via simulated project installation.
- Repository packaged and archived for distribution.
"""

def write_root_docs():
    files = {
        'QUICKSTART.md': quickstart_content,
        'RESEARCH-REPORT.md': research_report_content,
        'GAPS-AND-LIMITATIONS.md': gaps_limitations_content,
        'BUILD-STATUS.md': build_status_content
    }
    
    for filename, content in files.items():
        verify_no_em_dash(content, filename)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content.strip() + '\n')
        print(f"Successfully wrote {filename} ({len(content)} chars)")

if __name__ == '__main__':
    write_root_docs()
