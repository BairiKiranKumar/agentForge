# Vendor Manager Checklist

## Before starting
- [ ] Inspect Master Vendor Register to verify complete metadata for all active subscriptions
- [ ] Check upcoming contract renewal dates scheduled within the next 90 days
- [ ] Verify that every tool has an assigned internal business owner and technical lead
- [ ] Review recent support ticket escalations and outage logs for key vendors
- [ ] Check vendor GST filing status in GSTR-2B for domestic vendors

## While working
- [ ] Export user activity and login audit logs from vendor admin consoles
- [ ] Identify inactive accounts (no login >30 days) and flag for deprovisioning
- [ ] Calculate effective cost per active user for each core subscription
- [ ] Audit vendor uptime records against contracted SLA percentage (e.g. 99.9%)
- [ ] Issue 90-day and 60-day renewal review notifications to internal tool owners
- [ ] Benchmark current pricing against current market rates and alternative tools
- [ ] Negotiate renewal terms, seeking multi-year price caps or seat flexibility
- [ ] Track SLA credit claims for documented service disruptions

## Before handoff
- [ ] Update Master Vendor Register with new contract dates, pricing, and seat counts
- [ ] Transmit renewal cost forecasts to `budgeting-specialist` for annual budgeting
- [ ] Ensure all executed renewal documents are archived in central legal repository
- [ ] Verify that deprovisioned seats are successfully reflected in the next billing invoice
- [ ] Confirm zero em dashes are present in any documentation
- [ ] Format handoff according to `orchestration/handoff-format.md` standards

## Stop and escalate if
- [ ] Mission-critical vendor announces sudden service sunset or major architectural deprecation
- [ ] Vendor incurs catastrophic security breach compromising customer or company data
- [ ] Vendor unilaterally imposes predatory price increase (>20%) with zero negotiation flexibility
- [ ] Strategic vendor experiences repeated SLA failures impacting client deliverables
