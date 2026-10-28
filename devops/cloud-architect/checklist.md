# Cloud Architect: Checklist

## Before starting
- [ ] Application workload specifications and concurrency estimates reviewed
- [ ] Monthly hosting budget ceiling in INR/USD confirmed with the owner or client
- [ ] Target user geographical distribution identified
- [ ] Regulatory and data residency requirements (DPDP Act, RBI payment rules) checked
- [ ] Preferred or existing cloud provider commitments identified

## While working
- [ ] Indian regional cloud centers (`ap-south-1` / `ap-south-2`) prioritized for low latency
- [ ] Data residency verified for all databases holding personal or financial records
- [ ] Egress bandwidth costs modeled and mitigated via CDN caching (Cloudflare)
- [ ] High Availability (HA) topology designed with multi-AZ failover for critical paths
- [ ] Recovery Time Objective (RTO) and Recovery Point Objective (RPO) defined
- [ ] Serverless PaaS compared objectively against containerized managed hosting
- [ ] Component-by-component monthly cost model calculated in INR and USD
- [ ] Budget alerts and spending guardrails incorporated into design
- [ ] Cloud architecture diagram created using clear Mermaid or structural format
- [ ] Over-engineering avoided: Kubernetes rejected if managed containers suffice
- [ ] Non-production environments budgeted with automated shutdown schedules

## Before handoff
- [ ] Cloud Architecture Specification completed with cost breakdown and topology
- [ ] Disaster recovery and backup frequencies documented
- [ ] Shared with `infrastructure-engineer` for IaC translation
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Architecture estimate exceeds the client's confirmed monthly budget by >20%
- [ ] Storing regulated Indian citizen payment or health data in foreign cloud regions
- [ ] Client demands high-cost enterprise cloud services for low-traffic static sites
- [ ] Cloud provider lacks data center presence or adequate SLA in the required region
