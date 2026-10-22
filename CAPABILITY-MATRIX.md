# Capability Matrix (Responsibility Matrix)

Business activities mapped to who does the work, who decides, and who reviews. The orchestrator uses this to pick the smallest sufficient team.

- **Owner (R)**: does the work and produces the deliverable. Exactly one.
- **Approver (A)**: makes the final call. "Kiran" means a human decision is required.
- **Reviewer**: independent check before approval. Never the owner.
- **Consulted (C)**: gives input when needed; not activated by default.
- **WF**: workflow in `workflows/` where the activity appears.

Rule: any activity that sends, publishes, spends, deploys, signs or tests live systems has Kiran (or the system owner) as approver, per `AGENTS.md` section 3.

## Leadership, strategy and operations
| Activity | Owner (R) | Approver (A) | Reviewer | Consulted | WF |
|---|---|---|---|---|---|
| Weekly priorities and decision log | `chief-of-staff` | Kiran | | department leads | |
| Assemble a team for a brief | `orchestrator` | Kiran (for large or consequential work) | | `chief-of-staff` | all |
| Business strategy, offers, segments | `business-strategist` | Kiran | `marketing-strategist` | `market-researcher`, `financial-analyst` | 03 |
| Portfolio prioritization (client, product, showcase work) | `portfolio-manager` | Kiran | `chief-of-staff` | `resource-planner`, `financial-analyst` | |
| Operating model and tool stack | `operations-lead` | Kiran | `financial-analyst` | `vendor-manager` | |
| Engineering standards and stack choices | `technical-lead` | Kiran | `solution-architect` | `frontend-architect` | |
| Design standards and design sign-off policy | `design-lead` | Kiran | `design-reviewer` | `creative-director` | |
| Research strategy and method choice | `research-lead` | `research-lead` | `research-synthesis-specialist` | `product-manager` | 02, 03 |
| Marketing targets and channel budget | `marketing-lead` | Kiran | `marketing-analyst` | `marketing-strategist` | |
| Sales targets, pipeline review, discount approval | `sales-lead` | Kiran | `crm-operations-specialist` | `pricing-strategist` | 01 |
| Delivery standards and project health reviews | `delivery-lead` | Kiran | `risk-manager` | `delivery-manager` | 02, 08 |
| SOPs | `sop-writer` | `operations-lead` | `editor` | process owner | |
| Tool and service purchases | `procurement-specialist` | Kiran | `budgeting-specialist` | `licensing-ip-assistant` | |
| Vendor and subscription management | `vendor-manager` | `operations-lead` | `financial-analyst` | | |
| Knowledge base structure and stale-doc reviews | `documentation-curator` | `operations-lead` | | all owners | |

## Product and research
| Activity | Owner (R) | Approver (A) | Reviewer | Consulted | WF |
|---|---|---|---|---|---|
| Problem framing and PRD | `product-manager` | Kiran | `product-owner` | `business-analyst` | 03 |
| Backlog and acceptance criteria | `product-owner` | `product-manager` | `qa-lead` | `business-analyst` | 03 |
| Process and business rules modelling | `business-analyst` | `product-owner` | `requirements-specialist` | | |
| Service blueprint | `service-designer` | `product-manager` | `ux-designer` | `operations-lead` | |
| Market sizing and trends | `market-researcher` | `research-lead` | `business-strategist` | | 03 |
| Competitor teardown | `competitor-researcher` | `research-lead` | `marketing-strategist` | | 03 |
| Generative user research | `ux-researcher` | `research-lead` | `research-synthesis-specialist` | `research-operations-specialist` | 02 |
| Recruiting, consent, scheduling participants | `research-operations-specialist` | `research-lead` | `privacy-specialist` | | 02, 03 |
| Problem-validation interviews | `customer-interview-specialist` | `product-manager` | `research-synthesis-specialist` | | 03 |
| Usability testing | `usability-researcher` | `research-lead` | `design-reviewer` | `ux-designer` | 02 |
| Research synthesis and insight reports | `research-synthesis-specialist` | `research-lead` | `ux-researcher` | | 02, 03 |
| Product metrics and experiment readouts | `product-analyst` | `product-manager` | `data-scientist` | `analytics-engineer` | 03 |

## Design
| Activity | Owner (R) | Approver (A) | Reviewer | Consulted | WF |
|---|---|---|---|---|---|
| Creative concept and art direction | `creative-director` | Kiran or client | `design-lead` | `brand-strategist` | 02 |
| Brand positioning and naming | `brand-strategist` | Kiran or client | `marketing-strategist` | `copywriter` | |
| Visual identity and brand guidelines | `brand-designer` | Kiran or client | `design-reviewer` | `brand-strategist` | |
| Sitemap, navigation, content model | `information-architect` | `ux-designer` | `usability-researcher` | `cms-specialist` | 02 |
| User flows and wireframes | `ux-designer` | client | `design-reviewer` | `ux-writer` | 02, 03 |
| High-fidelity UI | `ui-designer` | client | `design-reviewer` | `accessibility-designer` | 02, 03 |
| Interaction and state specs | `interaction-designer` | `ux-designer` | `design-reviewer` | `frontend-developer` | 02 |
| Design tokens and component library | `design-systems-specialist` | `design-lead` | `frontend-architect` | `brand-designer` | |
| Accessibility annotations | `accessibility-designer` | `design-lead` | `accessibility-tester` | `accessibility-engineer` | 02 |
| Motion, scroll and 3D specs | `motion-designer` | `creative-director` | `performance-engineer` | `frontend-developer` | 02 |
| Illustrations and image direction | `illustrator` | `creative-director` | `licensing-ip-assistant` | | 04 |
| Slide decks | `presentation-designer` | requester | `editor` | `proposal-writer` | 01, 04 |
| Conversion-focused page layouts | `conversion-designer` | client | `conversion-optimization-specialist` | `copywriter` | 02 |
| Design review before build or ship | `design-reviewer` | `design-lead` | | `accessibility-designer` | 02 |
| Canva production | `canva-specialist` | requester | `design-reviewer` (high visibility) | `brand-designer` | 04 |
| Visual reference research and design knowledge base | `design-researcher` | `design-lead` | `creative-director` | `ux-researcher` | 21, 22 |
| Design skill discovery, vetting and registry | `design-skill-researcher` | Kiran (for approved status or install) | `technical-lead` | `licensing-ip-assistant` | 21, 22 |
| Motion reference research and pattern library | `motion-researcher` | `design-lead` | `motion-designer` | `performance-engineer`, `accessibility-designer` | 21, 22 |
| Design direction approval before major implementation | `creative-director` | Kiran or client (high-visibility) | `design-reviewer` | `design-researcher` | 21 |
| Rubric-scored visual QA of rendered work | `design-reviewer` | `design-lead` | `accessibility-tester` | `performance-engineer` | 21 |

## Content
| Activity | Owner (R) | Approver (A) | Reviewer | Consulted | WF |
|---|---|---|---|---|---|
| Content strategy and pillars | `content-strategist` | `marketing-lead` | `brand-voice-specialist` | `seo-specialist` | 04 |
| Editorial calendar, briefs, content library | `content-calendar-manager` | `content-strategist` | | `social-media-manager` | 04 |
| Website and marketing copy | `copywriter` | client or Kiran | `editor` | `brand-voice-specialist` | 02, 04 |
| UI microcopy | `ux-writer` | `ux-designer` | `editor` | `localization-specialist` | 02 |
| Technical and admin documentation | `technical-writer` | `technical-lead` | `editor` | developers | 02 |
| Structural and line editing | `editor` | content owner | | | 04 |
| Final proofreading | `proofreader` | content owner | | | 04 |
| Voice and tone guide | `brand-voice-specialist` | `marketing-lead` | `editor` | `brand-strategist` | |
| Video scripts over 90 seconds, explainers, and ads | `scriptwriter` | Kiran | `editor` | `short-form-video-strategist` | 04 |
| Case studies | `case-study-writer` | Kiran and client permission | `editor` | `delivery-manager` | 04 |
| Proposal narrative | `proposal-writer` | `sales-lead` | `editor` | `proposal-specialist` | 01 |
| Telugu, Hindi and regional adaptation | `localization-specialist` | client or Kiran | native-speaker human check | `copywriter` | 04 |

## Development, data and AI
| Activity | Owner (R) | Approver (A) | Reviewer | Consulted | WF |
|---|---|---|---|---|---|
| Solution design and ADRs | `solution-architect` | `technical-lead` | `application-security-engineer` | `cloud-architect` | 02 |
| Frontend architecture | `frontend-architect` | `technical-lead` | `performance-engineer` | framework specialists | 02 |
| UI feature implementation | `frontend-developer` | `product-owner` | `code-reviewer` | framework specialists | 02, 03 |
| Angular-specific work | `angular-specialist` | `technical-lead` | `code-reviewer` | | 08 |
| React-specific work | `react-specialist` | `technical-lead` | `code-reviewer` | | |
| Next.js-specific work | `nextjs-specialist` | `technical-lead` | `code-reviewer` | `performance-engineer` | 02 |
| Semantic HTML and structured data | `html-specialist` | `frontend-developer` | `technical-seo-specialist` | `accessibility-engineer` | 06 |
| CSS layout and responsive fixes | `css-specialist` | `frontend-developer` | `visual-regression-tester` | `design-systems-specialist` | |
| Backend logic and auth | `backend-developer` | `technical-lead` | `code-reviewer` | `application-security-engineer` | 02 |
| API contracts | `api-specialist` | `solution-architect` | `api-tester` | | |
| Schema, migrations, RLS | `database-engineer` | `solution-architect` | `application-security-engineer` | | 02 |
| Mobile apps and PWAs | `mobile-developer` | `technical-lead` | `code-reviewer` | `mobile-tester` | |
| CMS implementation | `cms-specialist` | `solution-architect` | `code-reviewer` | `information-architect` | 02 |
| Shopify and e-commerce builds | `ecommerce-specialist` | client | `code-reviewer` | `integration-engineer` | |
| Third-party integrations (payments, WhatsApp, CRM) | `integration-engineer` | `solution-architect` | `application-security-engineer` | `api-specialist` | |
| Performance fixes | `performance-engineer` | `technical-lead` | `performance-tester` | | 06, 08 |
| Accessibility fixes in code | `accessibility-engineer` | `technical-lead` | `accessibility-tester` | `accessibility-designer` | 08 |
| Code review | `code-reviewer` | `technical-lead` | | | 02, 07, 08 |
| Maintenance, upgrades, small fixes | `maintenance-engineer` | `delivery-manager` | `code-reviewer` | | 07 |
| Premium marketing website | `frontend-developer` | Kiran (production deploy) | `design-reviewer` | `ui-designer`, `copywriter` | 10 |
| Application slice across UI and API | `solution-architect` | `technical-lead` | `code-reviewer` | `frontend-developer`, `backend-developer` | 11 |
| Defect reproduction, fix, and regression check | `maintenance-engineer` | `technical-lead` | `code-reviewer` | `manual-tester`, `playwright-specialist` | 12 |
| UI flow design and implementation | `ux-designer` | client or Kiran | `design-reviewer` | `ui-designer`, `frontend-developer` | 13 |
| Technical research write-up | `technical-writer` | `technical-lead` | `editor` | relevant specialist | 14 |
| Data pipelines | `data-engineer` | `technical-lead` | `analytics-engineer` | | |
| Metric models | `analytics-engineer` | `product-analyst` | `data-engineer` | | |
| Statistical analysis and models | `data-scientist` | `product-manager` | `product-analyst` | | 03 |
| LLM features | `ai-application-engineer` | `technical-lead` | `ai-evaluation-specialist` | `prompt-engineer` | |
| Agent workflows (including this ai-team) | `agent-workflow-engineer` | Kiran | `ai-evaluation-specialist` | `documentation-curator` | |
| Retrieval systems | `rag-specialist` | `ai-application-engineer` | `ai-evaluation-specialist` | | |
| Prompts and system instructions | `prompt-engineer` | feature owner | `ai-evaluation-specialist` | | |
| AI and agent evaluations | `ai-evaluation-specialist` | `technical-lead` | role's department lead | | all |
| AI cost, latency and model ops | `model-operations-specialist` | `technical-lead` | `financial-analyst` | | |

## QA, security and DevOps
| Activity | Owner (R) | Approver (A) | Reviewer | Consulted | WF |
|---|---|---|---|---|---|
| Test strategy and quality gates | `qa-lead` | `delivery-manager` | `technical-lead` | `automation-engineer` | 02 |
| Scripted and regression testing | `manual-tester` | `qa-lead` | | | 02, 07 |
| Exploratory testing | `exploratory-tester` | `qa-lead` | | | 02 |
| Test pyramid and CI test infrastructure | `automation-engineer` | `qa-lead` | `code-reviewer` | `cicd-engineer` | 08 |
| E2E browser tests | `playwright-specialist` | `qa-lead` | `automation-engineer` | | 02, 07 |
| API testing | `api-tester` | `qa-lead` | `api-specialist` | | 02 |
| Accessibility audits | `accessibility-tester` | `qa-lead` | `accessibility-engineer` | | 02, 08 |
| Performance testing | `performance-tester` | `qa-lead` | `performance-engineer` | | 02, 08 |
| Visual regression | `visual-regression-tester` | `qa-lead` | `ui-designer` | | 02 |
| Mobile device testing | `mobile-tester` | `qa-lead` | | `css-specialist` | 02 |
| Authorized security testing | `security-testing-specialist` | system owner (Kiran or client) | `application-security-engineer` | | 08 |
| Release readiness checks | `release-validation-specialist` | `qa-lead` | `release-engineer` | | 02 |
| Secure design and remediation | `application-security-engineer` | `technical-lead` | `security-testing-specialist` | | 02, 08 |
| Threat models | `threat-modeling-specialist` | `solution-architect` | `application-security-engineer` | | |
| Personal data handling and privacy notices (drafts) | `privacy-specialist` | Kiran (lawyer for legal opinion) | `compliance-research-assistant` | `contract-review-assistant` | |
| Hosting and cloud design | `cloud-architect` | `technical-lead` | `financial-analyst` | | 02 |
| Environments, secrets, deploy config | `devops-engineer` | `technical-lead` | `application-security-engineer` | | 02 |
| CI/CD pipelines | `cicd-engineer` | `technical-lead` | `devops-engineer` | | |
| Infrastructure, DNS, domains | `infrastructure-engineer` | Kiran (production) | `devops-engineer` | | 02 |
| SLOs and reliability | `site-reliability-engineer` | `technical-lead` | `observability-specialist` | | |
| Logging, monitoring, alerts | `observability-specialist` | `technical-lead` | `site-reliability-engineer` | | |
| Live incident command | `incident-coordinator` | Kiran | `site-reliability-engineer` | `client-communication-specialist` | 07 |
| Release execution and rollback | `release-engineer` | Kiran (production) | `release-validation-specialist` | | 02 |

## Marketing, social and analytics
| Activity | Owner (R) | Approver (A) | Reviewer | Consulted | WF |
|---|---|---|---|---|---|
| Positioning, messaging, go-to-market | `marketing-strategist` | `marketing-lead` | `brand-strategist` | `competitor-researcher` | 03 |
| Growth experiments | `growth-marketer` | `marketing-lead` | `marketing-analyst` | | |
| Keyword and content SEO | `seo-specialist` | `marketing-lead` | `technical-seo-specialist` | `copywriter` | 06 |
| Technical SEO | `technical-seo-specialist` | `technical-lead` | `seo-specialist` | `html-specialist` | 06 |
| Local SEO and Google Business Profile | `local-seo-specialist` | Kiran or client | `seo-specialist` | | 06 |
| Paid ads | `paid-ads-specialist` | Kiran (spend) | `marketing-analyst` | `copywriter` | |
| Newsletters and campaign emails | `email-marketer` | Kiran (send) | `editor` | | |
| Lifecycle journeys | `lifecycle-marketer` | `marketing-lead` | `privacy-specialist` | `whatsapp-business-specialist` | |
| CRO audits and A/B tests | `conversion-optimization-specialist` | `marketing-lead` | `product-analyst` | `conversion-designer` | |
| Social calendar and scheduling for review | `social-media-manager` | Kiran (publish) | `content-calendar-manager` | platform specialists | 04, 05 |
| Replies, DMs, community | `community-manager` | `social-media-manager` | | `sales-development-representative` | 05 |
| LinkedIn profile, posts, articles, and graphic-post scripts | `linkedin-specialist` | Kiran (publish) | `editor` | `case-study-writer` | 05, 15 |
| Instagram content plans and captions | `instagram-specialist` | Kiran (publish) | `editor` | `instagram-carousel-maker` | 04 |
| Instagram carousel artboards | `instagram-carousel-maker` | Kiran (publish) | `design-reviewer` | `instagram-specialist`, `editor` | 16 |
| Threads posts and discussion starters | `threads-specialist` | Kiran (publish) | `proofreader` | | 04, 05, 17 |
| X content | `x-specialist` | Kiran (publish) | `proofreader` | | 04 |
| YouTube channel strategy | `youtube-strategist` | Kiran | `marketing-analyst` | `scriptwriter` | 04 |
| Reels and Shorts concepts and series | `short-form-video-strategist` | Kiran | `instagram-specialist` | `reels-producer` | 04 |
| Reels and Shorts production packages | `reels-producer` | Kiran (publish) | `editor` | `short-form-video-strategist` | 18 |
| One-source multi-platform adaptation | `content-repurposing-specialist` | Kiran (publish) | `editor` | platform specialists | 19 |
| Client website showcase campaign | `content-repurposing-specialist` | Kiran | `editor` | `case-study-writer` | 20 |
| Brand and topic monitoring | `social-listening-specialist` | `marketing-lead` | | `community-manager` | |
| Creator collaborations and disclosure | `creator-partnerships-specialist` | Kiran (spend, contracts) | `compliance-research-assistant` | `contract-review-assistant` | |
| WhatsApp Business setup and messaging rules | `whatsapp-business-specialist` | Kiran or client | `privacy-specialist` | `integration-engineer` | |
| Marketing reporting and attribution | `marketing-analyst` | `marketing-lead` | `web-analytics-specialist` | | 04, 06, 09 |
| Tracking plans and tags | `web-analytics-specialist` | `marketing-lead` | `privacy-specialist` | `frontend-developer` | 03, 06 |

## Sales and partnerships
| Activity | Owner (R) | Approver (A) | Reviewer | Consulted | WF |
|---|---|---|---|---|---|
| Ideal customer profile | `icp-researcher` | `sales-lead` | `marketing-strategist` | | 01 |
| Prospect lists and personalization notes | `prospect-researcher` | `sales-lead` | `lead-qualification-specialist` | | 01 |
| Lead scoring and qualification | `lead-qualification-specialist` | `sales-lead` | | | 01 |
| Inbound lead response | `sales-development-representative` | Kiran (send) | `outreach-copywriter` | | 01 |
| Outbound prospecting plan | `business-development-representative` | `sales-lead` | | `prospect-researcher` | 01 |
| Outreach message drafts | `outreach-copywriter` | Kiran (send) | `sales-lead` | | 01 |
| Discovery calls | `discovery-specialist` | `account-executive` | | `sales-engineer` | 01 |
| Deal management and close plan | `account-executive` | `sales-lead` | | | 01 |
| Technical sales support and demos | `sales-engineer` | `account-executive` | `solution-architect` | | 01 |
| Proposal assembly, scope and terms | `proposal-specialist` | `sales-lead`, then Kiran (send) | `delivery-manager` (feasibility) | `estimation-specialist` | 01 |
| Rate cards and packages | `pricing-strategist` | Kiran | `financial-analyst` | | 01 |
| Objection library | `objection-handling-specialist` | `sales-lead` | | `case-study-writer` | 01 |
| Negotiation preparation | `negotiation-prep-specialist` | Kiran | `sales-lead` | | 01 |
| CRM hygiene and sales reports | `crm-operations-specialist` | `sales-lead` | | | 01 |
| Upsell and referral plans for existing clients | `account-manager` | `sales-lead` | `customer-success-manager` | | 09 |
| Partnerships and referral agreements (drafts) | `partnership-manager` | Kiran | `contract-review-assistant` | | |

## Client onboarding, delivery, success and support
| Activity | Owner (R) | Approver (A) | Reviewer | Consulted | WF |
|---|---|---|---|---|---|
| Client onboarding checklist and access collection | `onboarding-manager` | `delivery-manager` | | `privacy-specialist` | 01 |
| Requirements elicitation | `requirements-specialist` | client | `business-analyst` | `solution-architect` | 01, 02 |
| Kickoff meeting | `kickoff-facilitator` | `delivery-manager` | | `project-manager` | 01 |
| Client status updates and difficult messages (drafts) | `client-communication-specialist` | Kiran (send) | `delivery-manager` | | 02, 07, 08 |
| Project plan, schedule, status | `project-manager` | `delivery-manager` | | | 02 |
| Multi-project programs | `program-manager` | `delivery-lead` | | `project-manager` | |
| Engagement ownership | `delivery-manager` | `delivery-lead` | | | 02, 08 |
| Capacity and allocation | `resource-planner` | `delivery-lead` | | `portfolio-manager` | |
| Estimates | `estimation-specialist` | `delivery-manager` | `technical-lead` | | 01, 08 |
| Change requests | `scope-change-manager` | client and Kiran | `delivery-manager` | `pricing-strategist` | 02, 08 |
| Risk register | `risk-manager` | `delivery-manager` | `delivery-lead` | | 02, 08 |
| Client UAT and acceptance | `acceptance-coordinator` | client | `qa-lead` | | 02 |
| Handover pack and go-live checklist | `handover-specialist` | `delivery-manager` | `release-validation-specialist` | | 02 |
| Client training | `client-training-specialist` | `delivery-manager` | `ux-writer` | | 02 |
| Success plans and account reviews | `customer-success-manager` | Kiran (send) | `account-manager` | | 09 |
| Product or platform implementation | `implementation-specialist` | `customer-success-manager` | | | |
| Churn risk and save plays | `retention-specialist` | `customer-success-manager` | | | 09 |
| Renewals | `renewal-specialist` | Kiran | `financial-analyst` | | 09 |
| Feedback themes | `customer-feedback-analyst` | `product-manager` | `research-synthesis-specialist` | | 09 |
| Ticket triage | `support-triage-specialist` | `delivery-manager` | | | 07 |
| Issue reproduction | `technical-support-specialist` | `support-triage-specialist` | developer | | 07 |
| Help articles | `knowledge-base-writer` | `customer-success-manager` | `editor` | | 07 |

## Finance, legal, people
| Activity | Owner (R) | Approver (A) | Reviewer | Consulted | WF |
|---|---|---|---|---|---|
| Profitability and cash-flow analysis | `financial-analyst` | Kiran | `budgeting-specialist` | | |
| Budgets and budget vs actual | `budgeting-specialist` | Kiran | `financial-analyst` | | |
| Bookkeeping and reconciliation prep | `bookkeeping-assistant` | licensed CA | `ca-assistant` | | |
| Invoices, receipt vouchers, credit notes | `invoicing-specialist` | Kiran (issue) | `gst-specialist` | | 02 |
| Receivables follow-up | `collections-coordinator` | Kiran (send) | `financial-analyst` | `client-communication-specialist` | 09 |
| GST obligations analysis and calendar | `gst-specialist` | licensed CA or GST practitioner | `ca-assistant` | `invoicing-specialist` | |
| Income tax, TDS and advance tax preparation | `ca-assistant` | licensed CA | `financial-analyst` | `bookkeeping-assistant` | |
| Contract summaries and clause flags | `contract-review-assistant` | Kiran (lawyer if material) | `compliance-research-assistant` | | 01 |
| Compliance research memos | `compliance-research-assistant` | Kiran (lawyer if material) | `privacy-specialist` | | |
| Licensing, attribution and asset rights | `licensing-ip-assistant` | Kiran | `compliance-research-assistant` | | |
| Hiring process and interview kits | `recruiting-specialist` | Kiran | `people-operations-specialist` | | |
| People policies and records | `people-operations-specialist` | Kiran | `compliance-research-assistant` | | |
| New team member onboarding | `employee-onboarding-specialist` | `people-operations-specialist` | | | |
| Skills and learning plans | `learning-development-specialist` | `operations-lead` | | department leads | |

## Resolved architectural and ownership decisions

### 1. Survey design ownership
- User experience, usability, and product surveys are owned by `ux-researcher`.
- Market sizing, brand awareness, and competitor surveys are owned by `market-researcher`.
- Recurring post-launch customer satisfaction (CSAT) and Net Promoter Score (NPS) surveys are owned by `customer-feedback-analyst`.

### 2. Change-request pricing ownership
- Rate cards, standard hourly pricing tiers, and discounting parameters are owned by `pricing-strategist`.
- Effort hour calculations and operational Change Order drafting are owned by `scope-change-manager`.
- Commercial fee quotes for change requests are reviewed by `delivery-manager` and `pricing-strategist`.

### 3. Next.js metadata and sitemap ownership
- Structural sitemap, URL taxonomy, and content hierarchy are owned by `information-architect`.
- Metadata strategy, OpenGraph/Twitter social cards, and schema.org JSON-LD specs are owned by `seo-specialist`.
- Code-level implementation in Next.js (`app/sitemap.ts`, `app/robots.ts`, dynamic `generateMetadata()`) is owned by `frontend-developer`.

### 4. Motion designer aliases
- Official aliases added to `orchestration/roster.yaml` for `motion-designer`: `animator`, `animation designer`, and `motion graphics designer`.

### 5. Licensing and IP assistant tool permissions
- Least-privilege tools preserved: `licensing-ip-assistant` uses Read, Write, Edit, Glob, Grep, WebSearch, WebFetch (no direct Bash tool).
- Automated CLI repository license scanning is executed by `devops-engineer` or `automation-engineer`, passing generated lockfiles and inventories to `licensing-ip-assistant` for legal compliance analysis.

### 6. WF-01 Stage 6 account executive input
- `account-executive` provides commercial deal strategy, client budget constraints, and stakeholder decision criteria into Stage 6 (Proposal) alongside `proposal-specialist`, ensuring seamless continuity into Stage 7 (Close).

### 7. Instagram vs short-form video boundary
- `instagram-specialist` owns channel curation, static carousels, feed aesthetics, stories, bio/links, captions, and community engagement on Instagram.
- `short-form-video-strategist` owns video-first conceptualization, hook scripts, pacing, audio direction, and cross-platform vertical video scripting (Reels, Shorts, TikTok).

### 8. Research synthesis vs research lead review protocol
- `research-synthesis-specialist` performs peer data validation and evidence cross-checking (ensuring findings are anchored in raw interview notes).
- `research-lead` provides executive governance on methodology compliance and decision recommendations. For small research engagements, `research-lead` signs off directly with peer review marked optional.

