# Privacy audit: file-level findings

Generated from the pre-sanitization snapshot of the working tree on 2026-10-22. Values are not reproduced. Each row lists the file, the classification, the finding categories with occurrence counts, and the action taken on the `public-ready/architecture-and-standards` branch.

Classifications: PUBLIC_SAFE, ANONYMIZE, MOVE_TO_PRIVATE_WORKSPACE, REMOVE_FROM_PUBLIC_HISTORY, NEEDS_HUMAN_REVIEW. History findings are in [privacy-audit.md](privacy-audit.md).

Files with findings: 689

| Classification | Files |
|---|---|
| PUBLIC_SAFE | 4 |
| ANONYMIZE | 680 |
| MOVE_TO_PRIVATE_WORKSPACE | 5 |
| REMOVE_FROM_PUBLIC_HISTORY | 0 |
| NEEDS_HUMAN_REVIEW | 0 |

| Finding category | Files |
|---|---|
| owner-first-name (approver) | 611 |
| personal-handle/brand | 127 |
| local-market-city | 85 |
| client-style-project-names | 66 |
| showcase-project-name | 16 |
| studio-concept | 8 |
| repo-owner-username (URL) | 4 |
| email-address | 2 |
| maintainer-full-name-or-path | 1 |

## Files

| File | Classification | Findings (counts) | Action |
|---|---|---|---|
| `AGENTS.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `BUILD-STATUS.md` | ANONYMIZE | showcase-project-name: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `CAPABILITY-MATRIX.md` | ANONYMIZE | owner-first-name (approver): 66 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `QUICKSTART.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `README.md` | ANONYMIZE | personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `UPGRADE-STATUS.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `agentforge.lock` | PUBLIC_SAFE | repo-owner-username (URL): 1 | Canonical upstream repository coordinates. Public project metadata; owner may still choose a different location (see human-review list). |
| `analytics/marketing-analyst/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `analytics/marketing-analyst/examples.md` | ANONYMIZE | client-style-project-names: 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `analytics/web-analytics-specialist/AGENT.md` | ANONYMIZE | client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `analytics/web-analytics-specialist/examples.md` | ANONYMIZE | client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `brands/SCHEMA.md` | ANONYMIZE | personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `brands/_template/README.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `brands/_template/brand.yaml` | ANONYMIZE | personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `brands/<private-brand>/README.md` | MOVE_TO_PRIVATE_WORKSPACE | owner-first-name (approver): 3, personal-handle/brand: 1 | Moved to ignored workspace/private. Replaced by templates or fictional example. |
| `brands/<private-brand>/brand.yaml` | MOVE_TO_PRIVATE_WORKSPACE | owner-first-name (approver): 5, personal-handle/brand: 3, studio-concept: 1 | Moved to ignored workspace/private. Replaced by templates or fictional example. |
| `client-onboarding/client-communication-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 12, client-style-project-names: 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `client-onboarding/client-communication-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `client-onboarding/client-communication-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `client-onboarding/client-communication-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 3, client-style-project-names: 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `client-onboarding/kickoff-facilitator/AGENT.md` | ANONYMIZE | owner-first-name (approver): 6, client-style-project-names: 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `client-onboarding/kickoff-facilitator/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `client-onboarding/kickoff-facilitator/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `client-onboarding/onboarding-manager/AGENT.md` | ANONYMIZE | owner-first-name (approver): 19 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `client-onboarding/onboarding-manager/checklist.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `client-onboarding/onboarding-manager/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `client-onboarding/onboarding-manager/examples.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `client-onboarding/requirements-specialist/AGENT.md` | ANONYMIZE | client-style-project-names: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `client-onboarding/requirements-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/brand-voice-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 12, personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/brand-voice-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/brand-voice-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/case-study-writer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 16 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/case-study-writer/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/case-study-writer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/case-study-writer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/content-calendar-manager/AGENT.md` | ANONYMIZE | owner-first-name (approver): 11 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/content-calendar-manager/checklist.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/content-calendar-manager/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/content-calendar-manager/examples.md` | ANONYMIZE | owner-first-name (approver): 3, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/content-repurposing-specialist/AGENT.md` | ANONYMIZE | personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/content-repurposing-specialist/evaluation.md` | ANONYMIZE | personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/content-repurposing-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/content-strategist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 12, personal-handle/brand: 3, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/content-strategist/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/content-strategist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/content-strategist/examples.md` | ANONYMIZE | owner-first-name (approver): 5, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/copywriter/AGENT.md` | ANONYMIZE | owner-first-name (approver): 7, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/copywriter/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/copywriter/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/editor/AGENT.md` | ANONYMIZE | owner-first-name (approver): 6, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/editor/evaluation.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/editor/examples.md` | ANONYMIZE | owner-first-name (approver): 6, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/localization-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 7, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/localization-specialist/examples.md` | ANONYMIZE | local-market-city: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/proofreader/AGENT.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/proofreader/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/proofreader/examples.md` | ANONYMIZE | owner-first-name (approver): 2, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/proposal-writer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 19, studio-concept: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/proposal-writer/checklist.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/proposal-writer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/scriptwriter/AGENT.md` | ANONYMIZE | owner-first-name (approver): 15, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/scriptwriter/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/scriptwriter/examples.md` | ANONYMIZE | owner-first-name (approver): 2, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/technical-writer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/technical-writer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/technical-writer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/ux-writer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/ux-writer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `content/ux-writer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `customer-success/customer-feedback-analyst/examples.md` | ANONYMIZE | client-style-project-names: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `customer-success/customer-success-manager/AGENT.md` | ANONYMIZE | client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `customer-success/customer-success-manager/examples.md` | ANONYMIZE | client-style-project-names: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `customer-success/implementation-specialist/AGENT.md` | ANONYMIZE | client-style-project-names: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `customer-success/implementation-specialist/examples.md` | ANONYMIZE | client-style-project-names: 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `customer-success/renewal-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 6, client-style-project-names: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `customer-success/renewal-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `customer-success/renewal-specialist/examples.md` | ANONYMIZE | client-style-project-names: 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `customer-success/retention-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 6, client-style-project-names: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `customer-success/retention-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `customer-success/retention-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `customer-success/retention-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/agent-workflow-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/agent-workflow-engineer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/agent-workflow-engineer/examples.md` | ANONYMIZE | owner-first-name (approver): 2, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/ai-application-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/ai-application-engineer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/ai-evaluation-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/ai-evaluation-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/ai-evaluation-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/analytics-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/analytics-engineer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/analytics-engineer/examples.md` | ANONYMIZE | owner-first-name (approver): 3, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/data-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/data-engineer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/data-engineer/examples.md` | ANONYMIZE | local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/data-scientist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/data-scientist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/data-scientist/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/model-operations-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/model-operations-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/model-operations-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/prompt-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/prompt-engineer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/prompt-engineer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/rag-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/rag-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `data-ai/rag-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 2, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design-intelligence/README.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design-intelligence/REPORT.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design-intelligence/design-researcher/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design-intelligence/design-skill-researcher/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design-intelligence/guides/research-run.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design-intelligence/motion-researcher/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design-intelligence/motion-researcher/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design-intelligence/rubric/design-review-rubric.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design-intelligence/skill-registry/policy.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/accessibility-designer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/accessibility-designer/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/brand-designer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/brand-designer/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/brand-designer/examples.md` | ANONYMIZE | owner-first-name (approver): 1, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/brand-strategist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/brand-strategist/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/canva-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/canva-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/conversion-designer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/creative-director/AGENT.md` | ANONYMIZE | owner-first-name (approver): 6, personal-handle/brand: 2, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/creative-director/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/creative-director/examples.md` | ANONYMIZE | owner-first-name (approver): 2, personal-handle/brand: 1, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/design-reviewer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/design-reviewer/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/design-reviewer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/design-systems-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/design-systems-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/illustrator/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 1, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/illustrator/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/illustrator/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/illustrator/examples.md` | ANONYMIZE | owner-first-name (approver): 3, personal-handle/brand: 1, local-market-city: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/information-architect/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/information-architect/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/interaction-designer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/interaction-designer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/motion-designer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/motion-designer/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/motion-designer/examples.md` | ANONYMIZE | owner-first-name (approver): 2, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/presentation-designer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 6, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/presentation-designer/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/presentation-designer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/presentation-designer/examples.md` | ANONYMIZE | owner-first-name (approver): 6, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/ui-designer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/ui-designer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/ux-designer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `design/ux-designer/examples.md` | ANONYMIZE | local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/accessibility-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/angular-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/api-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/api-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/backend-developer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/backend-developer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/backend-developer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/cms-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 7 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/cms-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/code-reviewer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/code-reviewer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/code-reviewer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/css-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/database-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/database-engineer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/ecommerce-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/ecommerce-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/frontend-architect/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/frontend-architect/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/html-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/html-specialist/examples.md` | ANONYMIZE | local-market-city: 2, client-style-project-names: 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/integration-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/integration-engineer/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/integration-engineer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/integration-engineer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/maintenance-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/maintenance-engineer/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/maintenance-engineer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/maintenance-engineer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/mobile-developer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/mobile-developer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/nextjs-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/nextjs-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/nextjs-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/performance-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/solution-architect/AGENT.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/solution-architect/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `dev/solution-architect/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/cicd-engineer/examples.md` | ANONYMIZE | client-style-project-names: 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/cloud-architect/AGENT.md` | ANONYMIZE | owner-first-name (approver): 2, client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/cloud-architect/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/cloud-architect/examples.md` | ANONYMIZE | client-style-project-names: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/devops-engineer/examples.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/incident-coordinator/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3, client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/incident-coordinator/examples.md` | ANONYMIZE | client-style-project-names: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/infrastructure-engineer/AGENT.md` | ANONYMIZE | client-style-project-names: 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/infrastructure-engineer/examples.md` | ANONYMIZE | client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/observability-specialist/AGENT.md` | ANONYMIZE | client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/observability-specialist/examples.md` | ANONYMIZE | client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/release-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/release-engineer/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/release-engineer/examples.md` | ANONYMIZE | client-style-project-names: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/site-reliability-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `devops/site-reliability-engineer/examples.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `docs/INSTALL.md` | PUBLIC_SAFE | personal-handle/brand: 1, repo-owner-username (URL): 1 | Canonical upstream repository coordinates. Public project metadata; owner may still choose a different location (see human-review list). |
| `evaluations/runs/2026-10-22-parallel/REPORT.md` | ANONYMIZE | personal-handle/brand: 1 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/2026-10-22-parallel/linkedin.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 3 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/2026-10-22-parallel/review.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 4, studio-concept: 1 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/2026-10-22-parallel/threads.md` | ANONYMIZE | owner-first-name (approver): 5, personal-handle/brand: 3 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/design-intelligence-e2e/review/review-A.md` | ANONYMIZE | owner-first-name (approver): 1 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/design-intelligence-e2e/review/review-B.md` | ANONYMIZE | owner-first-name (approver): 2 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/v1.1-evals/SCORES.md` | ANONYMIZE | personal-handle/brand: 3 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/v1.1-evals/reels-task1/captions.md` | ANONYMIZE | owner-first-name (approver): 2 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/v1.1-evals/reels-task1/export.md` | ANONYMIZE | owner-first-name (approver): 1 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/v1.1-evals/reels-task1/hook.md` | ANONYMIZE | owner-first-name (approver): 2, personal-handle/brand: 2 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/v1.1-evals/reels-task1/script.md` | ANONYMIZE | owner-first-name (approver): 8, personal-handle/brand: 2 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/v1.1-evals/reels-task1/shot-list.md` | ANONYMIZE | owner-first-name (approver): 3 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/v1.1-evals/reels-task1/storyboard.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 1 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/v1.1-evals/repurpose-task1/digest.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 2 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/v1.1-evals/repurpose-task1/linkedin.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 1 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/v1.1-evals/repurpose-task1/matrix.md` | ANONYMIZE | owner-first-name (approver): 3, personal-handle/brand: 1 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/v1.1-evals/repurpose-task1/reel/script.md` | ANONYMIZE | owner-first-name (approver): 2, personal-handle/brand: 1 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `evaluations/runs/v1.1-evals/repurpose-task1/threads.md` | ANONYMIZE | owner-first-name (approver): 2, personal-handle/brand: 1 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/campaigns/<private-brand>/instagram-carousel/caption.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 4 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/campaigns/<private-brand>/instagram-carousel/index.html` | ANONYMIZE | personal-handle/brand: 7 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/plans/instagram-carousel.yaml` | ANONYMIZE | personal-handle/brand: 3 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/plans/showcase-campaign.yaml` | ANONYMIZE | personal-handle/brand: 1, showcase-project-name: 8 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/BRIEF.md` | ANONYMIZE | owner-first-name (approver): 2, personal-handle/brand: 2, local-market-city: 2, showcase-project-name: 3 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/execution-report.md` | ANONYMIZE | showcase-project-name: 9 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/index.html` | ANONYMIZE | local-market-city: 5, showcase-project-name: 4 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/instagram-carousel/caption.md` | ANONYMIZE | owner-first-name (approver): 2, personal-handle/brand: 2, local-market-city: 2, showcase-project-name: 4 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/instagram-carousel/index.html` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 7, local-market-city: 2, showcase-project-name: 1 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/linkedin.md` | ANONYMIZE | owner-first-name (approver): 5, personal-handle/brand: 3, local-market-city: 3, showcase-project-name: 6 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/reel/captions.md` | ANONYMIZE | showcase-project-name: 1 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/reel/export.md` | ANONYMIZE | showcase-project-name: 3 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/reel/hook.md` | ANONYMIZE | personal-handle/brand: 2, local-market-city: 1, showcase-project-name: 1 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/reel/script.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 1, local-market-city: 1, showcase-project-name: 3 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/reel/shot-list.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 1, local-market-city: 1, showcase-project-name: 3 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/reel/storyboard.md` | ANONYMIZE | owner-first-name (approver): 2, local-market-city: 2, showcase-project-name: 11 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/review.md` | ANONYMIZE | personal-handle/brand: 1, local-market-city: 1, showcase-project-name: 5 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `examples/projects/<showcase-project>/threads.md` | ANONYMIZE | owner-first-name (approver): 5, personal-handle/brand: 2, local-market-city: 6, showcase-project-name: 8 | Renamed and fictionalized (neutral owner, fictional brand, town and project). |
| `finance/bookkeeping-assistant/AGENT.md` | ANONYMIZE | owner-first-name (approver): 21 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/bookkeeping-assistant/checklist.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/bookkeeping-assistant/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/bookkeeping-assistant/examples.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/budgeting-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 18 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/budgeting-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/budgeting-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/budgeting-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/ca-assistant/AGENT.md` | ANONYMIZE | owner-first-name (approver): 17 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/ca-assistant/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/ca-assistant/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/ca-assistant/examples.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/collections-coordinator/AGENT.md` | ANONYMIZE | owner-first-name (approver): 31 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/collections-coordinator/checklist.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/collections-coordinator/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/collections-coordinator/examples.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/financial-analyst/AGENT.md` | ANONYMIZE | owner-first-name (approver): 11 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/financial-analyst/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/financial-analyst/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/financial-analyst/examples.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/gst-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 18 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/gst-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/gst-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/gst-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/invoicing-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 28 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/invoicing-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/invoicing-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `finance/invoicing-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 7 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `integrations/claude-code/agents/analytics/marketing-analyst.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/analytics/web-analytics-specialist.md` | ANONYMIZE | client-style-project-names: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/client-onboarding/client-communication-specialist.md` | ANONYMIZE | owner-first-name (approver): 12, client-style-project-names: 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/client-onboarding/kickoff-facilitator.md` | ANONYMIZE | owner-first-name (approver): 6, client-style-project-names: 4 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/client-onboarding/onboarding-manager.md` | ANONYMIZE | owner-first-name (approver): 19 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/client-onboarding/requirements-specialist.md` | ANONYMIZE | client-style-project-names: 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/brand-voice-specialist.md` | ANONYMIZE | owner-first-name (approver): 12, personal-handle/brand: 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/case-study-writer.md` | ANONYMIZE | owner-first-name (approver): 16 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/content-calendar-manager.md` | ANONYMIZE | owner-first-name (approver): 11 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/content-repurposing-specialist.md` | ANONYMIZE | personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/content-strategist.md` | ANONYMIZE | owner-first-name (approver): 12, personal-handle/brand: 3, local-market-city: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/copywriter.md` | ANONYMIZE | owner-first-name (approver): 7, local-market-city: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/editor.md` | ANONYMIZE | owner-first-name (approver): 6, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/localization-specialist.md` | ANONYMIZE | owner-first-name (approver): 7, local-market-city: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/proofreader.md` | ANONYMIZE | owner-first-name (approver): 6 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/proposal-writer.md` | ANONYMIZE | owner-first-name (approver): 19, studio-concept: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/scriptwriter.md` | ANONYMIZE | owner-first-name (approver): 15, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/technical-writer.md` | ANONYMIZE | owner-first-name (approver): 5 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/content/ux-writer.md` | ANONYMIZE | owner-first-name (approver): 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/customer-success/customer-success-manager.md` | ANONYMIZE | client-style-project-names: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/customer-success/implementation-specialist.md` | ANONYMIZE | client-style-project-names: 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/customer-success/renewal-specialist.md` | ANONYMIZE | owner-first-name (approver): 6, client-style-project-names: 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/customer-success/retention-specialist.md` | ANONYMIZE | owner-first-name (approver): 6, client-style-project-names: 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/data-ai/agent-workflow-engineer.md` | ANONYMIZE | owner-first-name (approver): 4 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/data-ai/ai-application-engineer.md` | ANONYMIZE | owner-first-name (approver): 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/data-ai/ai-evaluation-specialist.md` | ANONYMIZE | owner-first-name (approver): 4 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/data-ai/analytics-engineer.md` | ANONYMIZE | owner-first-name (approver): 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/data-ai/data-engineer.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/data-ai/data-scientist.md` | ANONYMIZE | owner-first-name (approver): 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/data-ai/prompt-engineer.md` | ANONYMIZE | owner-first-name (approver): 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/data-ai/rag-specialist.md` | ANONYMIZE | owner-first-name (approver): 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design-intelligence/design-researcher.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design-intelligence/design-skill-researcher.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design-intelligence/motion-researcher.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/accessibility-designer.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/brand-designer.md` | ANONYMIZE | owner-first-name (approver): 5 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/brand-strategist.md` | ANONYMIZE | owner-first-name (approver): 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/canva-specialist.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/conversion-designer.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/creative-director.md` | ANONYMIZE | owner-first-name (approver): 6, personal-handle/brand: 2, local-market-city: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/design-reviewer.md` | ANONYMIZE | owner-first-name (approver): 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/design-systems-specialist.md` | ANONYMIZE | owner-first-name (approver): 4 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/illustrator.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 1, local-market-city: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/information-architect.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/interaction-designer.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/motion-designer.md` | ANONYMIZE | owner-first-name (approver): 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/presentation-designer.md` | ANONYMIZE | owner-first-name (approver): 6, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/ui-designer.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/design/ux-designer.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/accessibility-engineer.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/angular-specialist.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/api-specialist.md` | ANONYMIZE | owner-first-name (approver): 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/backend-developer.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/cms-specialist.md` | ANONYMIZE | owner-first-name (approver): 7 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/code-reviewer.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/css-specialist.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/database-engineer.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/ecommerce-specialist.md` | ANONYMIZE | owner-first-name (approver): 4 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/frontend-architect.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/html-specialist.md` | ANONYMIZE | owner-first-name (approver): 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/integration-engineer.md` | ANONYMIZE | owner-first-name (approver): 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/maintenance-engineer.md` | ANONYMIZE | owner-first-name (approver): 5 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/mobile-developer.md` | ANONYMIZE | owner-first-name (approver): 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/nextjs-specialist.md` | ANONYMIZE | owner-first-name (approver): 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/performance-engineer.md` | ANONYMIZE | owner-first-name (approver): 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/dev/solution-architect.md` | ANONYMIZE | owner-first-name (approver): 5 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/devops/cloud-architect.md` | ANONYMIZE | owner-first-name (approver): 2, client-style-project-names: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/devops/incident-coordinator.md` | ANONYMIZE | owner-first-name (approver): 3, client-style-project-names: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/devops/infrastructure-engineer.md` | ANONYMIZE | client-style-project-names: 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/devops/observability-specialist.md` | ANONYMIZE | client-style-project-names: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/devops/release-engineer.md` | ANONYMIZE | owner-first-name (approver): 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/devops/site-reliability-engineer.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/finance/bookkeeping-assistant.md` | ANONYMIZE | owner-first-name (approver): 21 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/finance/budgeting-specialist.md` | ANONYMIZE | owner-first-name (approver): 18 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/finance/ca-assistant.md` | ANONYMIZE | owner-first-name (approver): 17 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/finance/collections-coordinator.md` | ANONYMIZE | owner-first-name (approver): 31 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/finance/financial-analyst.md` | ANONYMIZE | owner-first-name (approver): 11 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/finance/gst-specialist.md` | ANONYMIZE | owner-first-name (approver): 18 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/finance/invoicing-specialist.md` | ANONYMIZE | owner-first-name (approver): 28 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/leadership/chief-of-staff.md` | ANONYMIZE | owner-first-name (approver): 32 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/leadership/delivery-lead.md` | ANONYMIZE | owner-first-name (approver): 10 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/leadership/design-lead.md` | ANONYMIZE | owner-first-name (approver): 6 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/leadership/marketing-lead.md` | ANONYMIZE | owner-first-name (approver): 11, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/leadership/operations-lead.md` | ANONYMIZE | owner-first-name (approver): 12 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/leadership/research-lead.md` | ANONYMIZE | owner-first-name (approver): 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/leadership/sales-lead.md` | ANONYMIZE | owner-first-name (approver): 24 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/leadership/technical-lead.md` | ANONYMIZE | owner-first-name (approver): 4 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/legal-compliance/compliance-research-assistant.md` | ANONYMIZE | owner-first-name (approver): 8 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/legal-compliance/contract-review-assistant.md` | ANONYMIZE | owner-first-name (approver): 15 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/legal-compliance/licensing-ip-assistant.md` | ANONYMIZE | owner-first-name (approver): 5 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/marketing/email-marketer.md` | ANONYMIZE | owner-first-name (approver): 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/marketing/growth-marketer.md` | ANONYMIZE | owner-first-name (approver): 12 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/marketing/lifecycle-marketer.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/marketing/local-seo-specialist.md` | ANONYMIZE | owner-first-name (approver): 4 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/marketing/marketing-strategist.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 1, local-market-city: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/marketing/paid-ads-specialist.md` | ANONYMIZE | owner-first-name (approver): 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/marketing/seo-specialist.md` | ANONYMIZE | owner-first-name (approver): 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/marketing/technical-seo-specialist.md` | ANONYMIZE | owner-first-name (approver): 5 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/orchestration/orchestrator.md` | ANONYMIZE | owner-first-name (approver): 4 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/partnerships/partnership-manager.md` | ANONYMIZE | owner-first-name (approver): 34, local-market-city: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/product/business-analyst.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/product/product-manager.md` | ANONYMIZE | owner-first-name (approver): 8, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/product/product-owner.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/product/service-designer.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/qa/accessibility-tester.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/qa/api-tester.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/qa/exploratory-tester.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/qa/manual-tester.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/qa/mobile-tester.md` | ANONYMIZE | client-style-project-names: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/qa/performance-tester.md` | ANONYMIZE | owner-first-name (approver): 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/qa/qa-lead.md` | ANONYMIZE | owner-first-name (approver): 7 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/qa/release-validation-specialist.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/qa/security-testing-specialist.md` | ANONYMIZE | owner-first-name (approver): 3, client-style-project-names: 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/research/competitor-researcher.md` | ANONYMIZE | owner-first-name (approver): 4 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/research/customer-interview-specialist.md` | ANONYMIZE | owner-first-name (approver): 6 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/research/market-researcher.md` | ANONYMIZE | owner-first-name (approver): 4, local-market-city: 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/research/research-operations-specialist.md` | ANONYMIZE | owner-first-name (approver): 7, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/research/research-synthesis-specialist.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/research/usability-researcher.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/research/ux-researcher.md` | ANONYMIZE | owner-first-name (approver): 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/account-executive.md` | ANONYMIZE | owner-first-name (approver): 25 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/account-manager.md` | ANONYMIZE | owner-first-name (approver): 21 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/business-development-representative.md` | ANONYMIZE | owner-first-name (approver): 32, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/crm-operations-specialist.md` | ANONYMIZE | owner-first-name (approver): 13 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/discovery-specialist.md` | ANONYMIZE | owner-first-name (approver): 16 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/icp-researcher.md` | ANONYMIZE | owner-first-name (approver): 21, local-market-city: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/lead-qualification-specialist.md` | ANONYMIZE | owner-first-name (approver): 16 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/negotiation-prep-specialist.md` | ANONYMIZE | owner-first-name (approver): 37 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/objection-handling-specialist.md` | ANONYMIZE | owner-first-name (approver): 10 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/outreach-copywriter.md` | ANONYMIZE | owner-first-name (approver): 26 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/pricing-strategist.md` | ANONYMIZE | owner-first-name (approver): 30 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/proposal-specialist.md` | ANONYMIZE | owner-first-name (approver): 36, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/prospect-researcher.md` | ANONYMIZE | owner-first-name (approver): 11 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/sales-development-representative.md` | ANONYMIZE | owner-first-name (approver): 36 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/sales/sales-engineer.md` | ANONYMIZE | owner-first-name (approver): 16 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/security/application-security-engineer.md` | ANONYMIZE | owner-first-name (approver): 4 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/security/privacy-specialist.md` | ANONYMIZE | owner-first-name (approver): 6 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/security/threat-modeling-specialist.md` | ANONYMIZE | owner-first-name (approver): 3 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/community-manager.md` | ANONYMIZE | owner-first-name (approver): 20, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/creator-partnerships-specialist.md` | ANONYMIZE | owner-first-name (approver): 18, local-market-city: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/instagram-carousel-maker.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/instagram-specialist.md` | ANONYMIZE | owner-first-name (approver): 6, personal-handle/brand: 3, local-market-city: 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/linkedin-specialist.md` | ANONYMIZE | owner-first-name (approver): 20, local-market-city: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/reels-producer.md` | ANONYMIZE | personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/short-form-video-strategist.md` | ANONYMIZE | owner-first-name (approver): 12, personal-handle/brand: 2, local-market-city: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/social-listening-specialist.md` | ANONYMIZE | owner-first-name (approver): 16, personal-handle/brand: 3, local-market-city: 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/social-media-manager.md` | ANONYMIZE | owner-first-name (approver): 18, personal-handle/brand: 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/threads-specialist.md` | ANONYMIZE | owner-first-name (approver): 20, personal-handle/brand: 1, local-market-city: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/whatsapp-business-specialist.md` | ANONYMIZE | owner-first-name (approver): 6 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/x-specialist.md` | ANONYMIZE | owner-first-name (approver): 25, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/social-media/youtube-strategist.md` | ANONYMIZE | owner-first-name (approver): 13, personal-handle/brand: 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/strategy/business-strategist.md` | ANONYMIZE | owner-first-name (approver): 14, personal-handle/brand: 1, studio-concept: 1, local-market-city: 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/strategy/portfolio-manager.md` | ANONYMIZE | owner-first-name (approver): 15, personal-handle/brand: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/support/knowledge-base-writer.md` | ANONYMIZE | client-style-project-names: 2 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/support/support-triage-specialist.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 1 | Generated file. Regenerated from sanitized role definitions. |
| `integrations/claude-code/agents/support/technical-support-specialist.md` | ANONYMIZE | client-style-project-names: 1 | Generated file. Regenerated from sanitized role definitions. |
| `knowledge-management/company-profile.md` | MOVE_TO_PRIVATE_WORKSPACE | owner-first-name (approver): 9, personal-handle/brand: 2, studio-concept: 1 | Moved to ignored workspace/private. Replaced by templates or fictional example. |
| `leadership/chief-of-staff/AGENT.md` | ANONYMIZE | owner-first-name (approver): 32 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/chief-of-staff/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/chief-of-staff/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/chief-of-staff/examples.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/delivery-lead/AGENT.md` | ANONYMIZE | owner-first-name (approver): 10 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/delivery-lead/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/delivery-lead/evaluation.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/delivery-lead/examples.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/design-lead/AGENT.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/design-lead/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/marketing-lead/AGENT.md` | ANONYMIZE | owner-first-name (approver): 11, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/marketing-lead/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/marketing-lead/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/operations-lead/AGENT.md` | ANONYMIZE | owner-first-name (approver): 12 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/operations-lead/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/operations-lead/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/research-lead/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/sales-lead/AGENT.md` | ANONYMIZE | owner-first-name (approver): 24 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/sales-lead/checklist.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/sales-lead/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/sales-lead/examples.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/technical-lead/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `leadership/technical-lead/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `legal-compliance/compliance-research-assistant/AGENT.md` | ANONYMIZE | owner-first-name (approver): 8 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `legal-compliance/contract-review-assistant/AGENT.md` | ANONYMIZE | owner-first-name (approver): 15 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `legal-compliance/contract-review-assistant/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `legal-compliance/contract-review-assistant/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `legal-compliance/contract-review-assistant/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `legal-compliance/licensing-ip-assistant/AGENT.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `legal-compliance/licensing-ip-assistant/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `legal-compliance/licensing-ip-assistant/examples.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/email-marketer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/email-marketer/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/email-marketer/examples.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/growth-marketer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 12 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/growth-marketer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/growth-marketer/examples.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/lifecycle-marketer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/local-seo-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/marketing-strategist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 1, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/marketing-strategist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/marketing-strategist/examples.md` | ANONYMIZE | owner-first-name (approver): 2, local-market-city: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/paid-ads-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/paid-ads-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/seo-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/technical-seo-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/technical-seo-specialist/evaluation.md` | ANONYMIZE | local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `marketing/technical-seo-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `orchestration/orchestrator/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `orchestration/orchestrator/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `orchestration/orchestrator/examples.md` | ANONYMIZE | owner-first-name (approver): 3, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `orchestration/roster.yaml` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `partnerships/partnership-manager/AGENT.md` | ANONYMIZE | owner-first-name (approver): 34, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `partnerships/partnership-manager/checklist.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `partnerships/partnership-manager/evaluation.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `partnerships/partnership-manager/examples.md` | ANONYMIZE | owner-first-name (approver): 9, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `product/business-analyst/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `product/business-analyst/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `product/product-manager/AGENT.md` | ANONYMIZE | owner-first-name (approver): 8, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `product/product-manager/evaluation.md` | ANONYMIZE | local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `product/product-owner/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `product/product-owner/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `product/product-owner/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `product/service-designer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `product/service-designer/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `project-delivery/client-training-specialist/examples.md` | ANONYMIZE | client-style-project-names: 2, email-address: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `project-delivery/handover-specialist/examples.md` | ANONYMIZE | client-style-project-names: 3, email-address: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/accessibility-tester/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/api-tester/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/exploratory-tester/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/manual-tester/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/mobile-tester/AGENT.md` | ANONYMIZE | client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/performance-tester/AGENT.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/qa-lead/AGENT.md` | ANONYMIZE | owner-first-name (approver): 7 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/qa-lead/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/qa-lead/evaluation.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/qa-lead/examples.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/release-validation-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/release-validation-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/release-validation-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/security-testing-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3, client-style-project-names: 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/security-testing-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `qa/security-testing-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 3, client-style-project-names: 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/competitor-researcher/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/competitor-researcher/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/competitor-researcher/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/competitor-researcher/examples.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/customer-interview-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/customer-interview-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/customer-interview-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/customer-interview-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/market-researcher/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4, local-market-city: 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/market-researcher/examples.md` | ANONYMIZE | owner-first-name (approver): 1, local-market-city: 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/research-operations-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 7, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/research-operations-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/research-operations-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/research-operations-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/research-synthesis-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/usability-researcher/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/ux-researcher/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/ux-researcher/evaluation.md` | ANONYMIZE | local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `research/ux-researcher/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `runtime/discover.py` | PUBLIC_SAFE | repo-owner-username (URL): 1 | Canonical upstream repository coordinates. Public project metadata; owner may still choose a different location (see human-review list). |
| `sales/account-executive/AGENT.md` | ANONYMIZE | owner-first-name (approver): 25 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/account-executive/checklist.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/account-executive/evaluation.md` | ANONYMIZE | owner-first-name (approver): 8 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/account-executive/examples.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/account-manager/AGENT.md` | ANONYMIZE | owner-first-name (approver): 21 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/account-manager/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/account-manager/examples.md` | ANONYMIZE | owner-first-name (approver): 3, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/business-development-representative/AGENT.md` | ANONYMIZE | owner-first-name (approver): 32, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/business-development-representative/checklist.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/business-development-representative/examples.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/crm-operations-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 13 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/crm-operations-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/crm-operations-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/crm-operations-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 4, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/discovery-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 16 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/discovery-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/discovery-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/icp-researcher/AGENT.md` | ANONYMIZE | owner-first-name (approver): 21, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/icp-researcher/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/icp-researcher/evaluation.md` | ANONYMIZE | local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/icp-researcher/examples.md` | ANONYMIZE | owner-first-name (approver): 2, local-market-city: 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/lead-qualification-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 16 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/lead-qualification-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/lead-qualification-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/lead-qualification-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 1, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/negotiation-prep-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 37 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/negotiation-prep-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 8 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/negotiation-prep-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/negotiation-prep-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 15 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/objection-handling-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 10 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/objection-handling-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/objection-handling-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/objection-handling-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 4, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/outreach-copywriter/AGENT.md` | ANONYMIZE | owner-first-name (approver): 26 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/outreach-copywriter/checklist.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/outreach-copywriter/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/outreach-copywriter/examples.md` | ANONYMIZE | owner-first-name (approver): 8, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/pricing-strategist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 30 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/pricing-strategist/checklist.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/pricing-strategist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 7 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/pricing-strategist/examples.md` | ANONYMIZE | owner-first-name (approver): 13 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/proposal-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 36, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/proposal-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/proposal-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/proposal-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 6, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/prospect-researcher/AGENT.md` | ANONYMIZE | owner-first-name (approver): 11 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/prospect-researcher/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/prospect-researcher/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/prospect-researcher/examples.md` | ANONYMIZE | owner-first-name (approver): 1, local-market-city: 2, client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/sales-development-representative/AGENT.md` | ANONYMIZE | owner-first-name (approver): 36 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/sales-development-representative/checklist.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/sales-development-representative/evaluation.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/sales-development-representative/examples.md` | ANONYMIZE | owner-first-name (approver): 8, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/sales-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 16 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/sales-engineer/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/sales-engineer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `sales/sales-engineer/examples.md` | ANONYMIZE | owner-first-name (approver): 5, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `scratch/package_zip.py` | MOVE_TO_PRIVATE_WORKSPACE | maintainer-full-name-or-path: 4 | Moved to ignored workspace/private. Replaced by templates or fictional example. |
| `scratch/write_root_docs.py` | MOVE_TO_PRIVATE_WORKSPACE | owner-first-name (approver): 1 | Moved to ignored workspace/private. Replaced by templates or fictional example. |
| `security/application-security-engineer/AGENT.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `security/application-security-engineer/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `security/application-security-engineer/evaluation.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `security/application-security-engineer/examples.md` | ANONYMIZE | owner-first-name (approver): 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `security/privacy-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `security/privacy-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `security/privacy-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `security/privacy-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `security/threat-modeling-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `security/threat-modeling-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `security/threat-modeling-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/community-manager/AGENT.md` | ANONYMIZE | owner-first-name (approver): 20, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/community-manager/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/community-manager/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 1, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/community-manager/examples.md` | ANONYMIZE | owner-first-name (approver): 3, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/creator-partnerships-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 18, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/creator-partnerships-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/creator-partnerships-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/creator-partnerships-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 1, local-market-city: 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/instagram-carousel-maker/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/instagram-carousel-maker/evaluation.md` | ANONYMIZE | personal-handle/brand: 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/instagram-carousel-maker/examples.md` | ANONYMIZE | owner-first-name (approver): 2, personal-handle/brand: 5 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/instagram-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 6, personal-handle/brand: 3, local-market-city: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/instagram-specialist/evaluation.md` | ANONYMIZE | personal-handle/brand: 1, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/instagram-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 2, local-market-city: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/linkedin-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 20, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/linkedin-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/linkedin-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/linkedin-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/reels-producer/AGENT.md` | ANONYMIZE | personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/reels-producer/evaluation.md` | ANONYMIZE | personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/reels-producer/examples.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/short-form-video-strategist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 12, personal-handle/brand: 2, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/short-form-video-strategist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/short-form-video-strategist/examples.md` | ANONYMIZE | owner-first-name (approver): 2, personal-handle/brand: 2, local-market-city: 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/social-listening-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 16, personal-handle/brand: 3, local-market-city: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/social-listening-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/social-listening-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 5, personal-handle/brand: 4, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/social-media-manager/AGENT.md` | ANONYMIZE | owner-first-name (approver): 18, personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/social-media-manager/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/social-media-manager/evaluation.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/social-media-manager/examples.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 3, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/threads-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 20, personal-handle/brand: 1, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/threads-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/threads-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/threads-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 2, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/whatsapp-business-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/whatsapp-business-specialist/evaluation.md` | ANONYMIZE | local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/whatsapp-business-specialist/examples.md` | ANONYMIZE | local-market-city: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/x-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 25, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/x-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/x-specialist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/x-specialist/examples.md` | ANONYMIZE | owner-first-name (approver): 4, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/youtube-strategist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 13, personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/youtube-strategist/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/youtube-strategist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `social-media/youtube-strategist/examples.md` | ANONYMIZE | owner-first-name (approver): 3, personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `strategy/business-strategist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 14, personal-handle/brand: 1, studio-concept: 1, local-market-city: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `strategy/business-strategist/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `strategy/business-strategist/evaluation.md` | ANONYMIZE | owner-first-name (approver): 2, studio-concept: 3, local-market-city: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `strategy/business-strategist/examples.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `strategy/portfolio-manager/AGENT.md` | ANONYMIZE | owner-first-name (approver): 15, personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `strategy/portfolio-manager/checklist.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `strategy/portfolio-manager/evaluation.md` | ANONYMIZE | owner-first-name (approver): 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `strategy/portfolio-manager/examples.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `support/knowledge-base-writer/AGENT.md` | ANONYMIZE | client-style-project-names: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `support/knowledge-base-writer/examples.md` | ANONYMIZE | client-style-project-names: 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `support/support-triage-specialist/AGENT.md` | ANONYMIZE | owner-first-name (approver): 1, client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `support/support-triage-specialist/checklist.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `support/support-triage-specialist/examples.md` | ANONYMIZE | client-style-project-names: 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `support/technical-support-specialist/AGENT.md` | ANONYMIZE | client-style-project-names: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `templates/AGENT.template.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `templates/examples.template.md` | ANONYMIZE | personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `tests/test_discover.py` | PUBLIC_SAFE | repo-owner-username (URL): 2 | Canonical upstream repository coordinates. Public project metadata; owner may still choose a different location (see human-review list). |
| `tests/test_system.py` | ANONYMIZE | personal-handle/brand: 6 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/01-lead-to-onboarding.md` | ANONYMIZE | owner-first-name (approver): 4, local-market-city: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/02-client-build-delivery.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/03-product-idea-to-iteration.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/04-content-production.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/05-linkedin-program.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/06-seo-cycle.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/07-support-issue.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/08-project-recovery.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/09-monthly-account-review.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/10-premium-website.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/11-fullstack-app.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/12-bugfix-regression.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/13-ui-ux-implementation.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/14-technical-research.md` | ANONYMIZE | owner-first-name (approver): 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/15-linkedin-content.md` | ANONYMIZE | owner-first-name (approver): 1, personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/16-instagram-carousel.md` | ANONYMIZE | personal-handle/brand: 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/17-threads-content.md` | ANONYMIZE | personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/18-reels-production.md` | ANONYMIZE | personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/19-content-repurposing.md` | ANONYMIZE | personal-handle/brand: 1 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/20-client-website-showcase.md` | ANONYMIZE | owner-first-name (approver): 3 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/21-design-first.md` | ANONYMIZE | owner-first-name (approver): 4 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
| `workflows/22-design-intelligence-refresh.md` | ANONYMIZE | owner-first-name (approver): 2 | Role, workflow or document text: personal name, handle, place or project replaced by neutral or fictional terms. |
