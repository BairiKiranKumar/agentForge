# Infrastructure Engineer: Checklist

## Before starting
- [ ] Cloud architecture specification and target region confirmed from `cloud-architect`
- [ ] Cloud credentials provisioned with scoped IaC permissions
- [ ] Remote state S3 bucket and DynamoDB state lock table created
- [ ] Domain registrar and DNS delegation access verified
- [ ] `.gitignore` verified to include `*.tfstate*`, `.terraform/`, and `*.tfvars`

## While working
- [ ] Remote state backend configured with S3 encryption and DynamoDB locking
- [ ] Strict resource tagging applied (`Environment`, `Project`, `ManagedBy: OpenTofu`)
- [ ] VPC created with multi-AZ public and private subnets
- [ ] Databases and persistent compute placed in private subnets with no direct public IPs
- [ ] Security groups audited: zero open administrative ports (22, 5432) to `0.0.0.0/0`
- [ ] S3 buckets configured with `block_public_access` and server-side encryption
- [ ] `lifecycle { prevent_destroy = true }` attached to all persistent databases and storage
- [ ] Automated snapshot and backup lifecycle rules defined
- [ ] DNS records configured with low TTL (300s) during transition periods
- [ ] `terraform plan` / `tofu plan` executed and audited line-by-line for destructive changes
- [ ] Static IaC security scan run (`checkov` or `tfsec`)

## Before handoff
- [ ] `terraform apply` executed cleanly with zero manual console interventions
- [ ] Network subnet IDs, VPC ID, and S3 bucket names documented
- [ ] Disaster recovery restore runbook updated
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] `terraform plan` indicates destruction of an existing persistent database or storage volume
- [ ] Security scan discovers plain-text cloud secrets or unencrypted remote state
- [ ] Client requests opening database ports (5432) to the entire public internet
- [ ] State lock contention locks deployment pipeline with unresolved state mismatch
