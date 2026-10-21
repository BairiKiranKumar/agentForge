# Quickstart Guide: agentForge

The repository root is the system. There is no extra `ai-team/` wrapper. Parallel scheduling is in `orchestration/parallel-execution.md`. Routing and planning commands are in `README.md`.

# Quickstart Guide: ai-team

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
