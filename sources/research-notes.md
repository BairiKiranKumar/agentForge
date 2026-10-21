# Source research notes for ai-team

Date of inspection: 2026-10-20. All repositories were shallow-cloned (`git clone --depth 1`) into `/root/src/<owner>_<repo>` and only read. No install scripts, package managers, Makefiles, Python or shell files from any repo were run. Commits and dates below come from `git rev-parse --short HEAD` and `git log -1 --format=%cs` on those clones. I did not record star counts because I did not look them up.

Companion files:

- `sources/repos.json`: one object per assessed repo (22 repos).
- `sources/role-source-candidates.yaml`: all 179 roster slugs mapped to 0 to 3 permissively licensed source files.
- `sources/licenses/`: verbatim LICENSE copies for every repo marked adapt-with-attribution, plus item-level licenses where a file carries its own.

## 1. How discovery was done

Web searches I ran:

1. `github Claude Code subagents collection sales marketing finance legal agents`
2. `github Agent Skills SKILL.md collection business finance legal HR`
3. `github anthropics knowledge-work-plugins sales finance legal customer support plugins`
4. `github UX research skills claude agent usability testing interview synthesis`
5. `github product manager skills claude PRD agent skills repository`
6. `github open source company SOP templates HR policies playbook repository`
7. `deanpeters product-manager-skills github`
8. `github claude skills sales account executive discovery call MEDDIC skill`
9. `github claude skills legal contract review NDA skill open source license`
10. `github "basecamp handbook" OR "clef handbook" company handbook open source license`
11. `phuryn pm-skills github product management skills`
12. `github crewai multi-agent role definitions marketing agency team yaml agents tasks`
13. `github claude skill GST India invoice tax compliance agent`
14. `github claude skills customer success churn renewal QBR skill repository`
15. `github DPDP Act India compliance checklist open source repository`
16. `github MIT license India startup compliance GST TDS checklist markdown agent skills`

Two listing pages were fetched to find source repos: an mcpmarket.com listing (pointed to openaccountants) and a claudskills.com listing for `india-gst` (pointed to `openaccountants/openaccountants`, `agent-skills/india-gst/SKILL.md`).

What the searches produced beyond the named candidates: `anthropics/knowledge-work-plugins`, `anthropics/claude-for-legal`, `phuryn/pm-skills`, `deanpeters/Product-Manager-Skills`, `borghei/Claude-Skills`, `openaccountants/openaccountants`, `basecamp/handbook`. Searches for India compliance (DPDP Act, GST) returned blog posts and WordPress plugins, not reusable agent material, except openaccountants. The CrewAI search returned framework docs and blog posts, not role libraries worth cloning.

All 22 repositories were available: 3 were already cloned and 19 new clones succeeded. None failed.

Inspection method: list every agent/skill file, read at least 3 representative files per repo, then grep across all clones by keyword for each roster role, and measure candidate files (line count, tables, numbered steps, reference files). Quality calls in the mapping come from reading, not just from those counts.

## 2. Repositories assessed

Decision legend: **selected** (adapt with attribution), **reference** (read for ideas; for MIT repos copying is allowed but not recommended), **rejected** (do not use).

### 2.1 Selected

**anthropics/knowledge-work-plugins** (a266ab8, 2026-10-19, Apache-2.0). Selected. The best business-function source. Plugins for sales, customer-support, legal, finance, human-resources, operations, product-management, marketing, design, data, engineering, enterprise-search and small-business, 252 skills in total. Files I read: `legal/skills/review-contract`, `sales/skills/handle-objection`, `customer-support/skills/ticket-triage`, `small-business/skills/tax-prep`, `design/skills/user-research`, `human-resources/skills/interview-prep`. The skills have the things the brief asks for. They have gates (no tax estimate until the books are reconciled), decision tables (P1 to P4 priority, clause review points), explicit assumptions and "not legal/tax advice" framing. They also treat emails and transcripts as untrusted data. The weak parts: the HR skills are short (30 to 40 lines), and the small-business tax and payroll math is US-only (the skill says so and stops for non-US businesses). The repo assumes paid connectors, but every skill states a paste or upload fallback. One license oddity: the root LICENSE has a few lines of stray non-license text after the Apache appendix. The plugin-level LICENSE files are clean. Partner sub-plugins have their own licenses: brand-voice is MIT by Tribe AI, slack is MIT by Slack Technologies, zoom is MIT by Zoom, apollo is MIT by Apollo.io, and common-room is Apache-2.0.

**anthropics/claude-for-legal** (4a6c651, 2026-07-23, Apache-2.0). Selected for legal, privacy and IP. 151 skills across commercial, corporate, employment, IP, privacy, product, regulatory and litigation practice areas. I read `ip-legal/oss-review`, `privacy-legal/dpa-review`, `commercial-legal/nda-review` and `product-legal/marketing-claims-review`. They are the most rigorous files in the whole survey. They load a practice profile first, require primary-source citations for jurisdictional rules, route contested questions to an attorney, and `oss-review` explicitly says Commons Clause, BUSL and SSPL are not open source. The law content is US and EU (GDPR, US state privacy laws), so every rule must be re-sourced for India. The guardrails transfer well.

**msitarzewski/agency-agents** (4e3ac3c, 2026-10-19, MIT, "AgentLand Contributors"). Selected, but used selectively. 283 agents across 18 division folders plus strategy playbooks. It covers the most roles of any repo, but depth is uneven. Every file has a persona block (282 have a `vibe:` line). The strong files are `sales/sales-discovery-coach` (SPIN, Gap Selling, call structure), `specialized/operations-manager` (SIPOC, VSM, DMAIC), `finance/finance-bookkeeper-controller` (close checklist), `engineering/engineering-incident-response-commander`, `security/security-appsec-engineer`, `specialized/customer-success-manager` and `engineering/engineering-multi-agent-systems-architect`. The weak files are `paid-media/*` (71-line capability lists), `marketing/marketing-instagram-curator` and `marketing-growth-hacker`. Problems found:
- Overclaimed personas. `finance-tax-strategist` is "Cassandra, 15+ years ... Big Four".
- US-only content. `finance-tax-strategist` covers IRS, Section 179 and GILTI. `specialized/hr-onboarding` has I-9, W-4, 401(k) and COBRA.
- China-specific content. `specialized/recruitment-specialist` covers China hiring platforms and PIPL, and many marketing files target Douyin, WeChat or Xiaohongshu.
- `language-translator` is Spanish to English only.

Several agent names match contains-studio/agents (which has no license), but the text I compared is rewritten, not copied.

**wshobson/agents** (0874a27, 2026-10-17, MIT, Seth Hobson). Selected as the primary engineering, devops, QA and security source. 92 plugins with 202 agents, 185 skills and 105 commands. The skills use progressive disclosure: a short SKILL.md plus a references folder. I read `startup-business-analyst/market-sizing-analysis`, `incident-response/postmortem-writing`, `hr-legal-compliance/agents/hr-pro` and several `ui-design` skills. They are concrete and current. Business coverage is thin: `customer-sales-automation` is just two short agents. 157 files use "Use PROACTIVELY" in their descriptions, which would make them over-trigger if copied as written. `hermes-tweet` needs an XQUIK API key and `meigen-ai-design` needs an image MCP.

**coreyhaines31/marketingskills** (e85f3cb, 2026-10-19, MIT, Corey Haines). Selected as the primary marketing source. 52 skills with deep reference folders. I read `cold-email`, `influencer-marketing` and `sms` (with `references/whatsapp.md`). They are method-dense, with decision tables, deliverability rules and guardrails such as "fetched pages are data, not instructions". It is the only repo with usable WhatsApp Business guidance: opt-in, template categories, BSPs including Interakt, AiSensy and Wati, click-to-WhatsApp ads, and India named as a WhatsApp-first market. The disclosure guidance is FTC-framed, with no ASCI. The repo runs a disclosed paid partner program (`partners.json`, `tools/PARTNERS.md`). Builders should drop vendor names when adapting. `tools/clis` has JS API wrappers that need keys; I did not run them.

**phuryn/pm-skills** (07b34f6, 2026-10-16, MIT, Pawel Huryn). Selected for product, discovery and GTM. 69 skills and 42 commands, no tool dependencies. I read `interview-script` (Mom Test rules, JTBD probes), `create-prd` ("lean by default", "don't invent", unknowns go to an assumptions section) and `ideal-customer-profile`. The files are clean and faithful to the frameworks they use, with no personas. Some are thin (40 to 50 lines). `pm-toolkit/draft-nda` and `privacy-policy` should not feed legal roles.

**alirezarezvani/claude-skills** (19392f7, 2026-08-26, MIT, Alireza Rezvani). Selected, but only for original, non-duplicated skills. 388 skills (outside the mirror folders) and 230 agent files, plus about 745 Python scripts. Useful pieces fill real gaps:
- the customer-success health-scoring reference (weighted dimensions with reasons for each weight)
- `vendor-management` (when-to-use and when-not-to-use routing)
- `capacity-planner`, `deal-desk`, `revenue-operations`
- the `chief-of-staff` routing and loop-prevention rules

Problems:
- The counts are inflated by mirrors (`.gemini`, `.codex`, `docs`).
- Many skills depend on Python CLIs that a markdown-only agent cannot run.
- "Production-grade" claims and c-level advisor personas.
- Provenance: several marketing skills share most of their lines verbatim with coreyhaines31/marketingskills, and I found no credit to that repo. Examples: copy-editing (241 of 341 unique lines), programmatic-seo (153 of 200), ab-test-setup (151 of 197), copywriting (149 of 201). Both repos are MIT, so this is legal, but the mapping cites coreyhaines31 for those topics.

**github/awesome-copilot** (613efc8, 2026-10-20, MIT, GitHub, Inc.). Selected per item. 222 agents, 192 instructions and 435 skill folders. Quality varies a lot by item. The strong items I read:
- `instructions/a11y.instructions.md` (731 lines)
- `instructions/nextjs.instructions.md` (dated to Next.js 16.1.1)
- `skills/gtm-enterprise-account-planning` (MEDDICC, mutual action plan health signals)
- `skills/web-design-reviewer`
- `skills/quality-playbook`

Weak items include `agents/playwright-tester.agent.md` (14 lines). Some items carry their own license and author: quality-playbook (Apache-2.0, Andrew Stellman), anti-ui-slop (Apache-2.0), phoenix-tracing (Apache-2.0, Arize), agent-architecture (MIT, Stanislav Bankovskii), and the gtm-* skills (MIT, Smit Patel, from beingsmit/technical-product-gtm). Credit those authors. Several workshop and CLI docs encourage `--yolo` or allow-all modes; that must not be carried over.

**obra/superpowers** (bb92a77, 2026-10-09, MIT, Jesse Vincent). Selected for engineering process. 15 process skills: systematic-debugging, TDD, brainstorming, receiving and requesting code review, verification-before-completion, dispatching-parallel-agents and subagent-driven-development. They are opinionated and enforceable ("no fixes without root cause investigation first"). Coverage is narrow, but these are the best inputs for code-reviewer, maintenance-engineer, QA and the orchestrator.

**anthropics/skills** (dbd4588, 2026-10-09). Selected, Apache-2.0 skills only. There is no repo-level LICENSE. 14 skills ship an Apache-2.0 LICENSE.txt. docx, pdf, pptx and xlsx are "(c) 2025 Anthropic, PBC. All rights reserved" source-available, and `doc-coauthoring` has no license file. Treat those 5 as reference-only. I read `frontend-design`, `skill-creator`, `internal-comms`, `brand-guidelines` and `claude-api`. They are small and high quality.

### 2.2 Reference

**VoltAgent/awesome-claude-code-subagents** (408d3c9, 2026-10-11, MIT). Reference. Of 163 agents, 105 use one template: "When invoked" steps, keyword checklists like "Sample size adequate verified", a JSON progress block, and a "Delivery notification" with made-up metrics (legal-advisor: "Reviewed 89 contracts identifying $2.3M in risk reduction"). I read ux-researcher, legal-advisor and angular-architect. They cover topics but not methods. A few newer short files are fine (`assumption-mapping`, `growth-loops`, `docs-drift-editor`) and are cited in the mapping.

**lst97/claude-code-sub-agents** (96f5a50, 2025-08-15, MIT). Reference. Its README says it is built on the wshobson scaffold. Thinner than wshobson, hard-codes MCP servers (context7, 21st magic), and is stale.

**vijaythecoder/awesome-claude-agents** (2050f3c, 2025-10-29, MIT). Reference. Dev-only. `tech-lead-orchestrator` and `team-configurator` are useful patterns for the orchestrator role (fixed assignment format, cap on parallel agents). Uses "MUST BE USED" coercive descriptions.

**0xfurai/claude-code-subagents** (9236d10, 2025-10-15, MIT). Reference. 138 identical-shape 50-line technology files. Generic and partly dated (react-expert still recommends PropTypes).

**iannuttall/claude-agents** (f7df2c3, 2025-07-25, MIT). Reference. 7 agents. `prd-writer` and `content-writer` are compact and practical, but superseded by phuryn and coreyhaines.

**deanpeters/Product-Manager-Skills** (cfcb697, 2026-10-15, CC-BY-NC-SA-4.0). Reference only, do not copy. High quality (77 skills, for example `discovery-interview-prep`), but the NonCommercial license blocks use in a paid agency.

**openaccountants/openaccountants** (e1d91b6, 2026-10-19). Reference only, do not copy. Software is AGPL-3.0-only. The tax guides are under the "OpenAccountants Guide License v1.0", which is source-available and requires a commercial license to embed the guides in a commercial AI product or index them for commercial RAG. It is the only India tax source found with depth: india-gst (1,002 lines, rates from 22 September 2025 with a cited GST Council source), in-tds-freelance, in-advance-tax, in-pf-esi-employer, in-professional-tax, india-einvoice and india-payroll. All India skills are marked `review_status: pending_review`. Use it only as a list of topics and to find government primary sources.

**basecamp/handbook** (c953606, 2026-05-01). Reference only. There is no license file in the tree. An old blog post says the policies were put under Creative Commons, but the repo itself does not say so, so that cannot be relied on. It is clear policy prose (moonlighting OK and not-OK lists, title ladders) with a US employer context.

### 2.3 Rejected

**davepoon/claude-code-subagents-collection** (868d035, 2026-10-19). Top level is MIT, but it is an aggregator of 150 plugins with mixed nested licenses, including PolyForm Noncommercial (`plugins/magic-cc-codex-worker`). Per-file provenance is unclear. The business agents I read are short checklists. 146 files say "Use PROACTIVELY".

**contains-studio/agents** (a5a480c, 2025-07-28). No license file and no license statement, so all rights reserved. Persona-heavy ("virtuoso", "superpower") and stale.

**ComposioHQ/awesome-claude-skills** (be2a406, 2026-07-24). No LICENSE file. The README claims Apache-2.0, but the repo bundles Anthropic proprietary document skills. 832 of 864 skills are Composio "Rube MCP" automation stubs.

**borghei/Claude-Skills** (4a698e8, 2026-10-07). Commons Clause plus MIT. Commons Clause forbids selling a service whose value comes substantially from the software, which conflicts with an agency. Provenance flag: `business-growth/customer-success-manager/references/health-scoring-framework.md` matches the MIT original in alirezarezvani/claude-skills in its first 30 lines, so some MIT content appears to be relicensed with an extra restriction. Use the upstream instead.

## 3. Comparative conclusions

Which repo to start from, by department:

| Department | Start with | Then |
|---|---|---|
| leadership | knowledge-work-plugins (sales pipeline and forecast), agency-agents operations-manager | alirezarezvani c-level skills for routing and decision logs |
| strategy | agency-agents business-strategist, phuryn product-strategy | wshobson market-sizing |
| product | phuryn/pm-skills | knowledge-work product-management |
| research | phuryn (interviews), knowledge-work synthesize-research | agency-agents ux-researcher, alirezarezvani ux-researcher-designer |
| design | wshobson ui-design skills, knowledge-work design | anthropics/skills frontend-design, awesome-copilot web-design-reviewer |
| content | coreyhaines31 (copywriting, copy-editing, video) | knowledge-work ux-copy and brand-voice |
| dev | wshobson, awesome-copilot instructions | obra/superpowers for process |
| data-ai | wshobson llm-application-dev, anthropics/skills (claude-api, skill-creator) | agency-agents multi-agent architect |
| qa | obra/superpowers, wshobson accessibility | awesome-copilot quality-playbook |
| security | agency-agents appsec, wshobson security-scanning | claude-for-legal privacy for the privacy role |
| devops | wshobson cicd and observability | agency-agents incident commander |
| marketing, social-media | coreyhaines31 | alirezarezvani originals (local SEO, X, YouTube, LinkedIn) |
| sales, customer-success, support | knowledge-work-plugins | agency-agents sales and CSM files |
| finance | knowledge-work finance and small-business | agency-agents finance (US lens) |
| legal-compliance | claude-for-legal, knowledge-work legal | none |
| people-hr | knowledge-work human-resources and small-business hiring | wshobson hr-pro |
| operations, knowledge-management | knowledge-work operations, alirezarezvani vendor-management | |
| orchestration | obra dispatching skills | agency-agents nexus-strategy, vijaythecoder orchestrators |

Personality-heavy or weak sources: VoltAgent's templated files (fabricated delivery metrics), 0xfurai (generic), contains-studio (persona, no license), agency-agents paid-media and several social files, lst97 (derivative). These are good for topic checklists, not text.

Method-rich sources: knowledge-work-plugins, claude-for-legal, wshobson skills, coreyhaines31, phuryn and obra/superpowers.

Mapping statistics: 100 of 179 roles have at least one source rated strong. 1 role has nothing usable at all (gst-specialist). 9 roles have only weak sources.

## 4. Coverage gaps (no repo covers these well)

Roles with no source, only weak sources, or only a borrowed structure:

- **gst-specialist**: none (original). The only real GST source (openaccountants) is not reusable.
- **ca-assistant**: only the structure of the US tax-prep skill. Indian income tax, advance tax, presumptive taxation (44AD/44ADA) and TDS need original work.
- **invoicing-specialist**: no GST tax invoice, receipt voucher or credit note rules anywhere permissive.
- **localization-specialist**: no Telugu, Hindi or Indian English material. The only translator is Spanish to English.
- **threads-specialist**: only a platform-limits note. No Threads strategy.
- **negotiation-prep-specialist**: no negotiation-prep method (BATNA, concession plans) in any permissive repo.
- **estimation-specialist**: no three-point/PERT or assumptions-list method.
- **acceptance-coordinator**: no UAT plan or acceptance record source.
- **program-manager**: no cross-project dependency method.
- **mobile-tester**: only a 67-line agent.
- **case-study-writer**: only a 5-line structure. No interview, permission or proof-asset workflow.

Partial gaps worth noting:

- **research-operations-specialist**: no screener, consent form or panel content.
- **service-designer**: no real service blueprint (backstage) source.
- **angular-specialist**: no current Angular material (signals, zoneless, control flow). The best source is an AngularJS migration skill.
- **database-engineer**: no Supabase or RLS-specific source.
- **canva-specialist**: depends on the Canva connector skill only.
- **delivery-lead / delivery-manager**: thin.
- **exploratory-tester**: no charters or heuristics.
- **visual-regression-tester**: no baseline or masking policy.
- **kickoff-facilitator**: thin.

## 5. India-specific gaps

None of the reusable repos has India-specific compliance or market content apart from a few WhatsApp notes in coreyhaines31. Everything below must be written from Indian primary sources (CBIC, GST Council, Income Tax Department, MeitY, ASCI, EPFO/ESIC, state shops-and-establishments acts) and reviewed by a qualified professional:

- **GST**: registration thresholds, SAC codes for services, place of supply, LUT for exports, e-invoicing, GSTR-1/3B/9, ITC rules, reverse charge, and the rate changes from 22 September 2025. The only source is openaccountants (reference-only).
- **Indian income tax**: advance tax calendar, 44AD/44ADA presumptive schemes, TDS on professional fees (194J and related), Form 26AS/AIS, new vs old regime. Nothing reusable.
- **DPDP Act 2023 and DPDP Rules**: consent notices, consent managers, data principal rights, breach notification, children's data. Reusable privacy skills are GDPR/CCPA only. claude-for-legal gives a strong PIA/DPA structure to localize.
- **Indian contracts and IP**: Indian Contract Act and stamp duty practice, and arbitration (Arbitration and Conciliation Act). Not covered.
- **Employment**: EPF, ESI, professional tax, gratuity, leave under state shops-and-establishments acts, POSH Act committee requirements. agency-agents and wshobson are US-centric (I-9, W-4, FLSA).
- **ASCI**: influencer advertising guidelines and disclosure labels. coreyhaines31 is FTC-framed.
- **WhatsApp**: coreyhaines31 `sms/references/whatsapp.md` is a good start (opt-in, templates, BSPs). It still needs Indian context: business verification, TRAI rules for SMS and DLT that interact with WhatsApp fallbacks, and Indian customer etiquette.
- **Local business**: Google Business Profile in Tier 2/3 cities, Justdial and IndiaMART listings, UPI and Razorpay payment flows, Shopify India and Indian payment gateways, Tally and Zoho Books as ledgers, and INR pricing norms. No source mentions these except a passing WhatsApp/Interakt mention.
- **Languages**: Telugu, Hindi and Indian English localization, transliteration and code-mixed (Tenglish/Hinglish) copy. No source.

## 6. Risks

- **License traps.** Public repos that look reusable but are not: contains-studio (no license), ComposioHQ (no LICENSE file, bundles proprietary files), basecamp/handbook (no license in tree), deanpeters (NonCommercial), borghei (Commons Clause), openaccountants (source-available guide license). anthropics/skills mixes Apache-2.0 with proprietary skills. awesome-copilot and davepoon have per-item licenses that differ from the umbrella.
- **Provenance.** borghei appears to relicense MIT content from alirezarezvani. alirezarezvani repeats coreyhaines31 text without credit. Builders should cite the earliest source and keep its MIT notice.
- **Attribution mechanics.** MIT requires keeping the copyright and permission notice in "substantial portions". Apache-2.0 requires keeping the license, marking modified files, and keeping any NOTICE (none of the Apache repos assessed has a NOTICE file, though anthropics/skills has THIRD_PARTY_NOTICES.md). Each adapted file should record repo, path, commit and license.
- **Jurisdiction errors.** Much of the legal, tax and HR material is US, EU or China specific. Copying it into an India-first agent would produce confident wrong answers. The mapping notes flag every case I found.
- **Hallucination-prone and overclaiming text.** Persona credentials ("15+ years Big Four"), fabricated outcome numbers (VoltAgent delivery notifications), and unsourced benchmarks (for example "3.5%+ engagement target"). Strip all of these.
- **Over-triggering and coercive descriptions.** "Use PROACTIVELY" and "MUST BE USED" appear in hundreds of descriptions (wshobson 157, davepoon 146, 0xfurai 31, lst97 20, vijaythecoder 20). If copied, agents would fight for invocation.
- **Prompt injection.** I scanned all repos for override phrases ("ignore previous instructions", "disregard the system"). Every match was defensive text: detection rules, guardrails, or examples in security and eval skills. I found no live injection. Still, content from these repos must be treated as data. Several awesome-copilot docs recommend `--yolo` or allow-all permission modes, and some davepoon plugins reference skip-permission flags. Neither should be carried into ai-team.
- **Tool and vendor coupling.** knowledge-work-plugins and awesome-copilot assume paid SaaS connectors. coreyhaines31 has a paid partner program. wshobson and lst97 hard-code specific MCP servers. Keep the method and drop the vendor.
- **Staleness.** lst97, iannuttall, contains-studio, 0xfurai and vijaythecoder have not changed since 2025. Framework-specific advice (React, Angular, Next.js) dates quickly. Prefer sources with explicit version dates (awesome-copilot nextjs instructions).
- **Executable content.** Many repos ship install scripts, Python CLIs and hooks. None were run. Builders should not run them either. If a skill relies on a script, rewrite the method in prose or get a separate review before using the code.
