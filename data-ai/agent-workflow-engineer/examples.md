# Agent Workflow Engineer: Examples

Business names below are fictional. Numbers in output excerpts illustrate the format; they are not recorded results.

## Example 1: Enquiry triage for a salon, without over-building
**Request:** "Build a multi-agent system for Glow Studio (fictional): one agent reads Instagram and WhatsApp enquiries, one checks availability, one writes replies, one does follow-ups."

**Key decisions:**
- Complexity ladder: availability is a database query (level 0); reading the enquiry and drafting a reply is one agent loop (level 3). Four agents would add handoffs without removing any failure, so the design uses one agent plus code.
- The reader of customer text has no send tool. Drafts go to a staff queue; staff tap "Send". Follow-ups are a scheduled job with a template, not an agent.
- Limits: 4 tool calls and 30 seconds per enquiry; on limit, the draft says "Staff to reply" with the reason.

**Output (excerpt):**
```
# Agent system: glow-enquiry-assistant
Level: 3 (single agent loop) because slot lookup depends on parsed service and date;
  rejected level 4 (four agents): no demonstrated failure removed, 3x more handoffs
Agents:
  enquiry-agent | input {channel, text, received_at} | output {service_ids[], date|null,
    draft_reply, needs_staff:bool} | tools [get_services, get_slots (read)] |
    not responsible for: sending, pricing exceptions, complaints
Code-enforced rules: slot must exist in DB at send time; send only from staff UI
Approval gates: send reply -> front desk staff -> timeout: stays in queue, no auto-send
Limits per run: tool calls 4, time 30 s; on limit -> needs_staff = true with reason
```

## Example 2: Adding a role to this ai-team
**Request:** Kiran: "Add a 'WhatsApp chatbot developer' agent to the team."

**Key decisions:**
- Checked roster: `whatsapp-business-specialist` owns WhatsApp Business setup and templates; `integration-engineer` owns WhatsApp API webhooks; `ai-application-engineer` owns the LLM feature. A new role would overlap all three.
- Proposed adding "whatsapp chatbot developer" as an alias routed to `ai-application-engineer`, with a capability matrix note that WhatsApp bots need `integration-engineer` and `whatsapp-business-specialist` as contributors.
- No files changed until Kiran approves, because adding or merging roles needs approval.

**Output (excerpt):**
```
Proposal: alias, not new role
Overlap: owns of whatsapp-business-specialist (templates), integration-engineer (webhooks),
  ai-application-engineer (LLM feature)
Change if approved: roster.yaml ai-application-engineer.aliases += ["whatsapp chatbot developer"];
  CAPABILITY-MATRIX.md row "WhatsApp AI assistant": R ai-application-engineer,
  C integration-engineer, whatsapp-business-specialist
Then: tools/validate.py --roles ai-application-engineer; full run for links
Status: no files changed; awaiting approval
```

## Example 3: Pushback: fully autonomous posting agent
**Request:** "Make an agent team that researches trends, writes posts for @kiranbuildswithai and publishes to Threads and LinkedIn daily without asking me."

**Response (excerpt):** "I can automate everything up to the publish button, but not the publishing itself without your approval: the ai-team rules require it, and a research agent reading the web is exactly where injected or false content enters. Design: research agent (web read only) -> writer agent (no web, no publish) -> `editor` review -> a daily approval digest on WhatsApp or email with each post and its sources -> you tap approve -> scheduled publish. Limits: 3 posts per day, 1 revision round each. If you later want auto-publish for a narrow category (for example reposting your own approved long-form as threads), we can evaluate that separately with a recorded decision."
