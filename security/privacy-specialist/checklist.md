# Privacy Specialist: Checklist

## Before starting
- [ ] Feature description and user groups known (adults, parents, children, patients, staff)
- [ ] Schema, forms and tracking plan available (fields, not summaries)
- [ ] Third parties listed with regions where known (hosting, database, payments, WhatsApp, email, analytics, AI APIs)
- [ ] Studio role identified: processor for the client, or fiduciary for Kiran's own product
- [ ] EU or UK users checked; GDPR marked applicable or not applicable with reason
- [ ] Prior PIA or inventory for this product located

## While working
- [ ] PIA needed or not decided, reason recorded
- [ ] Every field mapped: purpose, ground, storage, access roles, processors, retention, deletion method
- [ ] Generated data included (logs, analytics IDs, AI prompts and outputs, backups)
- [ ] One ground per purpose; legitimate-use claims tagged for lawyer confirmation
- [ ] Marketing and new-purpose uses default to consent
- [ ] Consent: separate, unticked, purpose-specific, withdrawal equally easy, stored with notice version
- [ ] Under-18 users: parental consent step present; no tracking or targeted ads aimed at children
- [ ] Minimisation tests applied (less sensitive alternative; Aadhaar flagged)
- [ ] Notice compared with each new flow (data, purpose, processor, retention)
- [ ] Regional language need for the notice assessed
- [ ] Every time-sensitive legal statement checked against a current source, tagged and dated
- [ ] Risks are specific to flows, actors and harm

## Before handoff
- [ ] Launch conditions testable and owned
- [ ] Questions for a lawyer listed
- [ ] "Not legal advice" line present
- [ ] Retention schedule proposals marked as proposals for client decision
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff in `orchestration/handoff-format.md` format with `authorization: none`

## Stop and escalate if
- [ ] A personal data breach may have happened (to `incident-coordinator` and Kiran immediately)
- [ ] Someone shares real personal records with you to "check"
- [ ] A client asks for a compliance verdict or a regulator-facing document
- [ ] Children's or health data will go to an AI API or abroad and no one has checked terms
