# WF-01: Lead Research to Client Onboarding

Lead research, qualification, discovery, proposal, then onboarding of a signed client.

## Entry requirements
- A target segment or a named lead (for example "salons in Nizamabad" or one inbound enquiry).
- Current offer and rate card from Kiran (agents never invent prices).
- Authorization for outreach is **none** unless the brief says otherwise. Drafts are prepared; Kiran sends.

## Roles
| Role | Part |
|---|---|
| `icp-researcher` | Defines who to target (skip if ICP already exists) |
| `prospect-researcher` | Lead for stage 2 |
| `lead-qualification-specialist` | Lead for stage 3 |
| `outreach-copywriter` | Drafts messages |
| `business-development-representative` | Outbound plan and cadence (outbound) |
| `sales-development-representative` | Inbound response (inbound) |
| `discovery-specialist` | Lead for stage 5 |
| `proposal-specialist` | Lead for stage 6 |
| `proposal-writer` | Narrative sections |
| `pricing-strategist` | Price check against rate card |
| `sales-lead` | Reviewer and approver of proposal terms |
| `onboarding-manager` | Lead for stage 8 |
| `requirements-specialist`, `kickoff-facilitator` | Onboarding contributors |

## Stages
| # | Stage | Owner | Inputs | Deliverables | Quality gate | Reviewer |
|---|---|---|---|---|---|---|
| 1 | ICP | `icp-researcher` | Past wins, offer | `sales/icp.md` with criteria and disqualifiers | Every criterion observable from public info | `sales-lead` |
| 2 | Prospect list | `prospect-researcher` | ICP | Prospect table: name, location, public channels, presence audit, personalization hook, source link | Every row has a source link; no private personal data | `lead-qualification-specialist` |
| 3 | Qualification | `lead-qualification-specialist` | Prospect table | Scored list with tiers A/B/C and reasons | Scores use the written framework; reasons per lead | `sales-lead` (spot check 5) |
| 4 | Outreach drafts | `outreach-copywriter` with `business-development-representative` | Tier A list | Per-lead first message plus 2 follow-ups, channel chosen | Each message references a real observation; under 80 words; no false claims | `sales-lead` |
| 5 | Discovery | `discovery-specialist` | Reply or inbound enquiry | Discovery guide, call notes, qualification outcome, next step | Pain, impact, decision process, budget range, timeline captured or marked unknown | `account-executive` |
| 6 | Proposal | `proposal-specialist` with `proposal-writer`, `pricing-strategist` | Discovery notes, rate card | Proposal (Markdown draft): scope, exclusions, timeline, milestones, price, terms | Scope matches discovery; prices from rate card; exclusions explicit; third-party costs separate | `sales-lead` |
| 7 | Close | `account-executive` | Proposal feedback | Revised proposal, negotiation prep if needed (`negotiation-prep-specialist`) | Changes logged; any discount approved by `sales-lead` and Kiran | Kiran |
| 8 | Onboarding | `onboarding-manager` with `requirements-specialist`, `kickoff-facilitator` | Signed agreement, advance status | Onboarding checklist, intake questionnaire, access request list, kickoff agenda | Access requested via user invites, never plain passwords; kickoff date set | `delivery-manager` |

## Human authorization points
- Sending any outreach, follow-up, proposal or onboarding message.
- Any discount or change to terms.
- Recording a deal as won.

## Smallest-team rules
- Single inbound enquiry: start at stage 5 with `sales-development-representative` then `discovery-specialist`.
- Existing ICP: skip stage 1.
- Small proposal from rate card: `proposal-specialist` alone, reviewed by `sales-lead`.

## Exit criteria
- Lost or deferred: reason recorded in CRM notes (`crm-operations-specialist`).
- Won: signed agreement recorded, onboarding checklist complete, kickoff held, handoff to `delivery-manager` (WF-02 entry).

## Example invocation
"Run WF-01 stages 1 to 4 for home bakeries in Hyderabad. Prepare outreach drafts only; I will send them."
