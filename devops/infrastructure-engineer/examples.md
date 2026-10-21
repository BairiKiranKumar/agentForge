# Infrastructure Engineer: Examples

Business names below are fictional unless stated.

## Example 1: Secure VPC and S3 bucket provisioning for school portal
**Request:** "Provision the network subnets and private document storage for Pragathi Vidyalaya on AWS Mumbai (`ap-south-1`)."

**Key decisions:**
- Created a custom VPC (`10.0.0.0/16`) across 2 Availability Zones (`ap-south-1a`, `ap-south-1b`).
- Created public subnets for Application Load Balancers and private subnets for application containers and database.
- Provisioned S3 bucket for student records with AES256 encryption, public access block, and `prevent_destroy = true`.
- Configured remote state backend with DynamoDB locking.

**Output (excerpt):**
```hcl
# outputs.tf
output "vpc_id" {
  description = "The ID of the provisioned VPC"
  value       = aws_vpc.main.id
}

output "private_subnet_ids" {
  description = "Subnet IDs for application containers"
  value       = aws_subnet.private[*].id
}

output "documents_bucket_name" {
  description = "S3 bucket for student document archives"
  value       = aws_s3_bucket.school_documents.id
}
```

## Example 2: Catching and preventing accidental database destruction
**Request:** "Update the database instance module to change storage allocation."

**Key decisions:**
- Ran `tofu plan` to evaluate changes.
- Discovered that an updated parameter (`engine_version` upgrade without maintenance window) was triggering resource recreation: `aws_db_instance.postgres must be replaced`.
- Halted apply immediately. Reverted the breaking parameter change and reconfigured in-place storage autoscaling.
- Prevented accidental destruction and data loss of the staging database.

**Output (excerpt):**
```markdown
### Infrastructure Guardrail Alert: Database Recreation Intercepted
- Action: `tofu plan`
- Warning Detected: `aws_db_instance.database must be replaced (forces new resource)`
- Root Cause: Changing `engine_version` directly triggers replacement on this provider version.
- Action Taken: Halted deployment. Added `allow_major_version_upgrade = false` and adjusted parameter to allow in-place storage increase. Re-plan confirmed in-place modification.
```

## Example 3: Boundary: pushback against public database access
**Request:** "Our remote developer in Vijayawada can't connect his desktop DBeaver to the RDS database. Add an ingress rule allowing port 5432 from `0.0.0.0/0` so he can connect directly."

**Response (excerpt):** "I cannot and will not open PostgreSQL port 5432 to `0.0.0.0/0`. Opening database ports to the entire public internet exposes the database to automated brute-force attacks, port scans, and credential stuffing. Instead, I offer two secure solutions: (1) We whitelist the developer's specific static IP address temporarily; or (2) We provision an AWS SSM Session Manager bastion host, allowing the developer to create a secure, encrypted tunnel from his local machine using `aws ssm start-session` without exposing any public database ports. I will set up the SSM bastion tunnel within 30 minutes."
