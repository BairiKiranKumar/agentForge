# Incident Coordinator: Checklist

## Before starting
- [ ] Incident notification or alert received and acknowledged
- [ ] Initial severity assessed against P1-P4 matrix
- [ ] Dedicated incident response channel/bridge opened
- [ ] Technical service owner and operations lead identified
- [ ] Incident Commander authority formally announced

## While working
- [ ] First status notification published within 10 minutes of declaration
- [ ] Scribe assigned to record timestamped events and actions
- [ ] External stakeholders shielded from interrupting technical responders
- [ ] "Mitigate first, debug later" principle enforced
- [ ] Rollback ordered if active debugging stalls beyond 15 minutes
- [ ] Status updates published every 20 minutes (P1) or 45 minutes (P2)
- [ ] Mitigation verified through metrics and smoke tests before closing
- [ ] Next update time stated in every communication
- [ ] Telemetry observed for 15 minutes post-fix to confirm stability

## Before handoff
- [ ] Official "Incident Resolved" communication published
- [ ] Final timeline and chat logs preserved for postmortem review
- [ ] Blameless postmortem meeting scheduled within 48 hours
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Customer personal data or credentials appear leaked or exposed
- [ ] Complete database corruption or irreversible data loss occurs
- [ ] Incident remains unmitigated past 60 minutes with no viable rollback target
- [ ] Responders refuse command authority or engage in toxic finger-pointing
