# Privacy sampling review (independent)

Reviewer scope: committed state of branch `public-ready/architecture-and-standards`, HEAD `ebae929`. No repository file was modified except this report. Date: 2026-10-22.

Method: random sample (Python `random.seed(20261022)` over sorted `git ls-files` candidates per stratum), read by eye first, then `python tools/privacy_scan.py --verbose`, then the private identity patterns (10 pattern lines, terms not reproduced here) run against the sample and against all tracked text files at HEAD, then an unguided scan (emails, phones, paths, handles, cloud ids, GitHub handles, capitalised multi-word names, ~700 most frequent). Evidence is masked: first 2 characters plus a count.

Observed results of the automated checks:
- `tools/privacy_scan.py --verbose`: 5 built-in detectors, 10 private patterns, tracked files 0 findings in 0 files.
- Private patterns on the 88 sampled files: 0 hits. On all tracked text files at HEAD: 5 hits, all the allowlisted upstream repository coordinates (`agentforge.lock`, `docs/INSTALL.md`, `runtime/discover.py`, `tests/test_discover.py` x2), masked `Ba***`.
- Key point: every Major finding below was found by eye or by the unguided scan, and none is caught by the scanner or the private patterns. The scan being green does not mean the content is neutral.

## Sample (seed 20261022, 88 files)

Strata: 12 role AGENT.md, 6 examples.md (excluding design-intelligence and engineering-standards), 6 workflows, all of `examples/` and `brands/` (29 files), 6 evaluations/docs-reports, 6 generated integrations, 6 from sources/registry/TEAM-INDEX/SOURCE-MANIFEST, 4 design-intelligence, README, AGENTS, CAPABILITY-MATRIX, config/*, templates/*. SOURCE-MANIFEST.md was not drawn by the sampler; it was covered only by the unguided scan. Files read in full: all of `examples/`, `brands/`, `config/`, `README.md`, `AGENTS.md` (first 80 lines). Role/example/generated files were read by eye at cue-line level (owner, studio, place, first person, money, contact, handles, URLs, paths) plus the persisted full text of the first three AGENT.md files; they were not each read line by line. See UNVERIFIED.

```
- social-media/whatsapp-business-specialist/AGENT.md
- leadership/sales-lead/AGENT.md
- sales/business-development-representative/AGENT.md
- devops/infrastructure-engineer/AGENT.md
- design/interaction-designer/AGENT.md
- content/copywriter/AGENT.md
- dev/integration-engineer/AGENT.md
- dev/frontend-architect/AGENT.md
- dev/html-specialist/AGENT.md
- analytics/marketing-analyst/AGENT.md
- research/competitor-researcher/AGENT.md
- data-ai/rag-specialist/AGENT.md
- content/proofreader/examples.md
- dev/angular-specialist/examples.md
- dev/accessibility-engineer/examples.md
- finance/ca-assistant/examples.md
- security/threat-modeling-specialist/examples.md
- support/knowledge-base-writer/examples.md
- workflows/22-design-intelligence-refresh.md
- workflows/20-client-website-showcase.md
- workflows/04-content-production.md
- workflows/07-support-issue.md
- workflows/05-linkedin-program.md
- workflows/17-threads-content.md
- brands/SCHEMA.md
- brands/_template/README.md
- brands/_template/brand.yaml
- brands/example-brand/README.md
- brands/example-brand/brand.yaml
- examples/campaigns/example-brand/instagram-carousel/caption.md
- examples/campaigns/example-brand/instagram-carousel/index.html
- examples/plans/bugfix-regression.yaml
- examples/plans/design-first.yaml
- examples/plans/instagram-carousel.yaml
- examples/plans/premium-website.yaml
- examples/plans/showcase-campaign.yaml
- examples/projects/brightwell-dental/BRIEF.md
- examples/projects/brightwell-dental/execution-report.md
- examples/projects/brightwell-dental/index.html
- examples/projects/brightwell-dental/instagram-carousel/caption.md
- examples/projects/brightwell-dental/instagram-carousel/index.html
- examples/projects/brightwell-dental/linkedin.md
- examples/projects/brightwell-dental/reel/captions.md
- examples/projects/brightwell-dental/reel/export.md
- examples/projects/brightwell-dental/reel/hook.md
- examples/projects/brightwell-dental/reel/script.md
- examples/projects/brightwell-dental/reel/shot-list.md
- examples/projects/brightwell-dental/reel/storyboard.md
- examples/projects/brightwell-dental/review.md
- examples/projects/brightwell-dental/threads.md
- evaluations/run-plan.md
- evaluations/runs/design-intelligence-e2e/candidate/direction-note.md
- evaluations/runs/design-intelligence-e2e/review/review-B.md
- evaluations/runs/design-intelligence-e2e/design-research-brief.md
- docs/reports/BUILD-STATUS.md
- evaluations/runs/v1.1-evals/repurpose-task1/matrix.md
- integrations/claude-code/agents/data-ai/data-engineer.md
- integrations/claude-code/agents/leadership/technical-lead.md
- integrations/claude-code/agents/design-intelligence/motion-researcher.md
- integrations/claude-code/agents/sales/account-executive.md
- integrations/claude-code/agents/leadership/design-lead.md
- integrations/claude-code/agents/project-delivery/client-training-specialist.md
- TEAM-INDEX.md
- sources/role-source-candidates.yaml
- sources/licenses/VoltAgent__awesome-claude-code-subagents.LICENSE.txt
- sources/repos.json
- sources/licenses/github__awesome-copilot__skills-agent-architecture.LICENSE.txt
- registry/agents.json
- design-intelligence/knowledge-base/INDEX.md
- design-intelligence/skill-registry/REGISTRY.md
- design-intelligence/knowledge-base/motion/horizontal-scroll-sections.md
- design-intelligence/motion-researcher/AGENT.md
- README.md
- AGENTS.md
- CAPABILITY-MATRIX.md
- config/defaults.yaml
- config/privacy-allowlist.yaml
- config/templates/organization.example.yaml
- config/templates/project.example.yaml
- config/templates/quality.example.yaml
- config/templates/stack.example.yaml
- templates/AGENT.template.md
- templates/AUTHORING-GUIDE.md
- templates/checklist.template.md
- templates/evaluation.template.md
- templates/examples.template.md
- templates/execution-report.md
- templates/handoff.template.md
```

Three PNG captures were opened: `evaluations/runs/design-intelligence-e2e/captures/candidate-1440.png`, `control-768.png`, `candidate-settled-375.png`. They show only a fictional product page ("Tallyfield", labelled "Illustrative page. Fictional product.", sample_workspace, placeholder data) and a generic "DataFlow" gradient control page. No personal names, faces, emails, phone numbers, URLs, browser chrome, tabs, local paths or account names are visible. Clean. [Unverified] whether "Tallyfield" or "DataFlow" match a real trademark.

## CONFIRMED FINDINGS

### F1. Pervasive single-person, single-region business story in role files and examples. Severity: Major
The README says the repo is project-agnostic, brand-agnostic and that "Your organization, brand, stack and clients live in your own private configuration." The role content does not match. Roles still describe one freelancer's studio, clients and region.

Evidence (all at HEAD, counts from `git grep`, generated copies under `integrations/` excluded unless stated):
- "The owner's clients are in Telangana and nearby" `content/localization-specialist/AGENT.md:18`; "For most of the owner's clients (salons, clinics, restaurants, schools, boutiques in Telangana)" `social-media/whatsapp-business-specialist/AGENT.md:22`. Four files carry the "owner's clients" phrasing including the generated copies.
- "the owner is a sole proprietor unless he says otherwise" `finance/gst-specialist/AGENT.md:54`; same assumption in `legal-compliance/contract-review-assistant/AGENT.md:60`; "individual resident, sole proprietor" `finance/ca-assistant/AGENT.md:58`.
- "The owner is a solo studio: one wasted week chasing..." `sales/lead-qualification-specialist` (generated copy line 11); "For a solo studio, SOM is often capped by capacity" `research/market-researcher/AGENT.md:77`; "defaults for a solo studio" `finance/budgeting-specialist/AGENT.md:171`. 13 lines in 7 files.
- "the owner also has deep Angular experience" `leadership/technical-lead/AGENT.md:66` (a personal skill claim about one individual).
- "the earliest start date he can honestly commit to", "the owner's rate card version" in `sales/account-executive` (generated copy lines 41 and 43). "he" for the owner also in `finance/gst-specialist/AGENT.md:54`.
- "For this studio ..." and "the owner's own service pages" (`content/copywriter/AGENT.md:26`), 13 lines in 12 files and 37 lines in 25 files for "the owner's own".
- Region: Telangana, Hyderabad, Warangal, Hanamkonda or Telugu appear in 277 non-generated, non-docs files; 103 files excluding `regional-packs/`. Examples: "best in Telangana" claims `design/brand-strategist/AGENT.md:60`; `addressRegion "Telangana"` hard-coded in `dev/html-specialist/AGENT.md:93`; Telangana-specific festival and Telugu register rules in `content/localization-specialist/AGENT.md:80,87`. Regional content belongs in `regional-packs/india/`; role bodies should stay neutral.
- Hashtag `#webdesignindia` in `examples/projects/brightwell-dental/instagram-carousel/caption.md` (Hashtags line).

Why it matters: it reads as one individual's business profile (location, client segments, tax status, skills, selling style) and contradicts the "brand-agnostic" claim. It also leaves public contributors with roles that assume a Telangana sole proprietor.

### F2. Dangling references to a removed private profile, `knowledge-management/company-profile.md`. Severity: Major
The file is not in the repo (`docs/release-readiness/privacy-audit-files.md:462` records it as moved to private). 16 references remain in 12 files, e.g. `content/brand-voice-specialist/AGENT.md:67` ("for the owner's brand, `knowledge-management/company-profile.md` voice section is the baseline"), `data-ai/prompt-engineer/AGENT.md:55`, `sales/icp-researcher/AGENT.md:60`, `social-media/community-manager/AGENT.md:50`, `social-media/social-media-manager/AGENT.md:82` ("Default pillar mix for @example_brand (proof-led funnel from `company-profile.md`)"), `leadership/technical-lead/AGENT.md:66` ("From company-profile: Next.js, React, TypeScript, Supabase ..."). Broken for users, and it signals a hidden personal profile. `AGENTS.md` itself is clean here (it points to the organization profile and `docs/configuration.md`).

### F3. Personal-looking infrastructure identifier in Terraform example. Severity: Major
`devops/infrastructure-engineer/AGENT.md:104` and `:107` (and generated copy `integrations/claude-code/agents/devops/infrastructure-engineer.md:97,100`): S3 state bucket and DynamoDB lock table names start with `ar` + 3 characters followed by `-studio-tf-...` (4 hits, 2 files). The first token reads as a person's first name or a studio handle (`ar***-studio`). It is not in the private identity patterns, which is why the scanner is green. Cloud account id in the repo is the AWS documentation value (`123456789012`, allowlisted), which is fine.

### F4. Invoice register prefix and personal-style correspondence in finance examples. Severity: Major (cannot confirm what the prefix stands for)
Invoice numbers of the form `KB/2026-27/0NN` appear 15 lines in 5 files: `finance/bookkeeping-assistant/examples.md:9,23`, `finance/collections-coordinator/examples.md:23,36`, `finance/invoicing-specialist/evaluation.md:15,30` and others. `KB` looks like a person's or business's initials [Inference]. `finance/collections-coordinator/examples.md:23` is a first-person dunning message ("Hi Rao garu, invoices KB/... are now 17 days past due ... I can split it ...") written as the freelancer. [Unverified] whether `KB` matches a real owner; nothing in the sampled files confirms it. Recommend a neutral prefix such as `INV/2026-27/0NN`.

### F5. Business names without a "fictional" label that read as a real client portfolio. Severity: Major (cannot confirm they are real)
Small Indian business names used as if real clients, with status, money and delivery details, unlabelled:
- `leadership/delivery-lead/examples.md:9,11`: "Kanha Dental site: on schedule, but milestone 2 invoice is 18 days overdue: Commercial Red" and "Mehndi House site: G2 design gate failed twice". Reads like a real project status board.
- "Kavitha Sarees" 13 hits in 7 files, no fictional label (`analytics/web-analytics-specialist/examples.md:29`). "Lumen Salon" 14 hits, 7 files, none labelled. "Royal Silks Hyderabad" `data-ai/model-operations-specialist/examples.md:34`. "Ayush Clinic" `client-onboarding/client-communication-specialist/AGENT.md:121` (a ready-to-send client email subject). "Lens Craft Studio" `partnerships/partnership-manager/examples.md:18` ("the owner worked with them once"). "Keshava Fintech" `analytics/product-analyst/examples.md:4`.
- Contrast: Sri Vidya, Sunrise Dental, Smile Point, Care Plus Clinic, Little Banyan are mostly labelled "(fictional)". The unlabelled ones are the inconsistency.
- [Unverified] whether any is a real business. Several are plausible real local names. Also the places Hanamkonda and Warangal and the locality "Vinayak Nagar" (`sales/prospect-researcher/examples.md:16`) tie examples to one individual's local market.

### F6. Awkward anonymization residue (find-and-replace artifacts). Severity: Minor
- "Lumen Salon Salons" 10 lines in 7 files (e.g. `analytics/marketing-analyst/examples.md:28`, `customer-success/implementation-specialist/examples.md:28,38`).
- "Glow Studio Unisex" (`sales/account-executive/examples.md:43`), "Glow Hair Studio". Result: duplicated nouns that reveal a substitution happened.
- The sanitiser also left "ai-team" as a product name in generated copy ("Use the ai-team handoff format", e.g. `integrations/claude-code/agents/project-delivery/client-training-specialist.md:150`); 521 lines mention `ai-team` in total, many are legitimate folder names but the role-facing text should say agentForge.

### F7. Committed LICENSE appendix names a third party as copyright holder. Severity: Major (identity attribution, not a privacy leak)
`LICENSE` at HEAD, appendix line: `Copyright 2026 An******* ...` (a company that is not the project owner; 1 occurrence). `NOTICE` says "agentForge contributors". The working tree has an uncommitted change reverting this to the Apache placeholder; that fix is not in the reviewed commit. Needs a committed decision on the correct holder.

### F8. Upstream repository owner handle in project metadata. Severity: Minor (accepted, documented)
`agentforge.lock:4`, `docs/INSTALL.md:3`, `runtime/discover.py:24`, `tests/test_discover.py:28,41` contain `Ba***` handle (5 lines) that is the author's personal GitHub account as canonical repo path. Allowlisted in `config/privacy-allowlist.yaml` with justification. Acceptable only if the public repo really lives under that account; otherwise one rename would change 5 places.

### F9. Git author metadata is a personal name and personal email. Severity: Major (already known, maintainer decision)
All sampled commits (`git log -3`) show author `KI***` with a `gmail.com` address. Already recorded in `docs/release-readiness/privacy-audit.md:34` and `independent-review.md:46`. Public push would expose it permanently. Not a file finding, listed for completeness.

### F10. Realistic-range phone numbers used as examples. Severity: Minor
`98480 12345` / `9848012345` / `919848012345` (`content/proofreader/AGENT.md:77,112`, `content/proofreader/examples.md:20`, `qa/manual-tester/examples.md:9,18`, generated copies): 9 lines. The `98480` prefix is a valid-looking Indian mobile range; the `12345` tail suggests dummy, and the allowlist pattern `12345` suppresses it. Already noted in `independent-review.md:56`. Prefer `90000 00000` or `+91 99999 00000` style. `+919876543210` in `dev/api-specialist/AGENT.md` is a well-known dummy. The `7354476588` match in `.github/workflows/ci.yml:19,44` is a commit SHA substring, a false positive.

### F11. Residual first-person, single-person voice in `examples/` (awkward anonymization). Severity: Minor
The fictional framing is strong and honest (every Brightwell piece says "not a real clinic"; brand README says "does not describe a real person, studio or client"), and there is no real name, number, email or path anywhere in `examples/` or `brands/`. Remaining voice issues:
- First person freelancer voice: "I built", "message me about a website", "Message me about the website" (`examples/projects/brightwell-dental/instagram-carousel/index.html` slides 1 and 7; `.../reel/script.md` Voiceover last line; `.../reel/captions.md` caption 10; `examples/campaigns/example-brand/instagram-carousel/caption.md` Caption: "I check four things ... message me").
- A gendered single owner: "Tell him who the first screen should name" (`examples/projects/brightwell-dental/linkedin.md`, Post section) and "The body is in the owner's voice, for him to post later" (Assumptions). Reads as one individual.
- Single-person service pitch is the whole premise of `brands/example-brand/brand.yaml` (focus: "Modern websites for small businesses", cta: "Message the owner about a website project"). It is labelled fictional, so acceptable, but it is the same storyline as the role files in F1, so it reinforces the impression of one person's studio rather than a neutral sample. Consider a more generic brand focus.
- `examples/projects/brightwell-dental/index.html` has mojibake ("child" followed by a corrupted apostrophe, 2 places) from an encoding fault. Not privacy, worth fixing.
- Execution report `examples/projects/brightwell-dental/execution-report.md` lists "Host: cursor", durations and tool names. No identity, fine.

### F12. Third-party individuals' names and handles in attribution files. Severity: Minor (expected, license-driven)
`SOURCE-MANIFEST.md` and `design-intelligence/skill-registry/REGISTRY.md` list upstream GitHub handles (e.g. 15 mentions of one handle in `SOURCE-MANIFEST.md`), and `social-media/whatsapp-business-specialist/AGENT.md:168` names an upstream contributor handle (`@In*******`) credited by that source. Appropriate for MIT/Apache attribution; not a leak of this repo's author. Names such as Corey Haines, Seth Hobson, Alireza Rezvani, Pawel Huryn, Smit Patel, Jesse Vincent, James Bach, Michael Nygard, Andrew Stellman are authors of cited public works.

## Unguided scan result (proper nouns, emails, domains)
- Emails: only `*@example.com`, `example.invalid`, a synthetic mailbox.test address, `noreply@anthropic.com` (allowlisted). No real-looking address.
- Domains: only `.example`, `example.com` style plus well-known tools and government sites. No private business domain found in the sample or the scan.
- Windows or Unix home paths: one synthetic string in `tests/test_public_ready.py` (`C:\\Users\\someone\\project`), a detector fixture. None elsewhere.
- Cloud ids: AWS documentation account `123456789012` only; allowlisted.
- Social handles: `@example_brand` (131 uses in 90 files), `@exampleclient`; the rest are code tokens (`@media`, `@angular`). No real personal handle found.
- Names in the top 700 frequent capitalised phrases: tools and standards (Google, Core Web Vitals, WCAG bodies), upstream authors (F12), fictional businesses (F5), role titles. No individual customer name stood out except `Rao garu` (1 hit, `finance/collections-coordinator/examples.md:23`) and `Lakshmi P.` (`qa/manual-tester/examples.md:18`), both generic given names.

## RECOMMENDATIONS
1. Decide F1 as a release gate: rewrite role-body references ("the owner's clients in Telangana", "solo studio", "sole proprietor ... he", "deep Angular experience") into neutral conditionals ("when the profile says the organization is a sole proprietor ...", "region from the profile"). Move Telangana/Telugu specifics to `regional-packs/india/`. Use gender-neutral "they". Re-run the generator for `integrations/`.
2. Remove or relocate every `company-profile.md` reference (F2) to "the organization profile (`docs/configuration.md`)" and inline the Next.js default stack as a stated example, not "from company-profile".
3. Rename the Terraform bucket and table to `example-org-tf-state-...` and `example-org-tf-locks` (F3).
4. Replace the `KB/2026-27/` prefix with a neutral `INV/` prefix (F4) and make collections examples third-person templates, not a freelancer's first-person letter.
5. Label every example business "(fictional)" or rename the unlabelled ones with obviously invented names (F5). Fix "Lumen Salon Salons" and "Glow Studio Unisex" (F6). Replace `ai-team` with agentForge in generated text.
6. Commit the LICENSE decision (F7) and confirm the repo URL and author metadata plan (F8, F9) before the first public push.
7. Replace `98480 12345` with a clearly dummy range and tighten the allowlist pattern so `12345` alone does not suppress detection (F10).
8. In `examples/`, switch to the brand's neutral third-person ("the owner", "the studio") or use "they"; drop `#webdesignindia`; fix mojibake (F11).
9. Strengthen `tools/privacy_scan.py`: it cannot see F1 to F5 because they are context, not tokens. Add checks for the phrases "the owner's clients", "solo studio", "sole proprietor", "he says otherwise", and a "fictional label required" rule for business names in `examples.md`. Add a test for first-name-like tokens in cloud resource names.
10. Add a maintainer sign-off step for F9 (author rewrite or a fresh public history).

## UNVERIFIED / NOT CHECKED
- Whether any F5 business name, "Tallyfield" or "DataFlow" is a real business or trademark. I did not search the web. [Unverified]
- Whether `KB` in F4 or the `ar` token in F3 equals the author's initials or name. I did not compare them to the private terms in the report (by instruction), and the private-pattern scan returned no hit for either, so the link is [Inference] only.
- Role, examples and generated files were not each read line by line (about 40 percent were cue-line reviewed, the rest were covered by grep and the unguided scan). `TEAM-INDEX.md`, `registry/agents.json`, `sources/*.json|yaml` and `CAPABILITY-MATRIX.md` were skimmed through cue matches only.
- Binary files other than 3 PNGs, git history content beyond the last 3 commits' author metadata, `.github/`, `runtime/`, `tools/`, `tests/` beyond hits, and files untracked or in `.agentforge/` (the private directory itself was only used for pattern matching) were not reviewed.
- HTML inline CSS in the example pages was not read.
- The `AGENTS.md` text supplied to my session as context contains personal and business details not present in the committed `AGENTS.md`; I reviewed the committed file only. The session copy appears to be an older or unsanitised local version. [Inference]
