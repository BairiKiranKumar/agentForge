# Cloud Architect: Examples

Business names below are fictional unless stated.

## Example 1: Cost-optimized architecture for Hyderabad school portal
**Request:** "Design the cloud hosting architecture for Greenfield Vidyalaya school portal (1,500 students, 4,000 parents). Budget is strict: under Rs. 10,000 per month."

**Key decisions:**
- Evaluated AWS Fargate vs Vercel + Supabase PaaS.
- Selected Vercel Pro for Next.js frontend/SSR (served via Mumbai edge route) combined with Supabase Pro on AWS Mumbai (`ap-south-1`).
- Placed Cloudflare in front of public school gallery assets to eliminate S3 egress fees.
- Configured automated database point-in-time recovery with 7-day retention.
- Modeled monthly cost: ₹6,500/month, well within the ₹10,000 budget ceiling.

**Output (excerpt):**
```markdown
### Cloud Hosting Recommendation: Greenfield Vidyalaya
- Architecture: Edge Next.js Frontend + Managed Serverless Postgres
- Primary Region: AWS Mumbai (`ap-south-1`)
- Monthly Cost: ₹6,500 ($78 USD)
- Component Breakdown:
  - Vercel Pro: ₹1,700/seat/month (1 seat)
  - Supabase Pro: ₹2,100/month (8GB RAM, 100GB storage)
  - Cloudflare Pro: ₹1,700/month (WAF, image optimization, edge cache)
  - AWS S3 (Backup & Archives): ₹1,000/month
- Latency Benchmark: < 45 ms roundtrip for Hyderabad broadband and 4G users.
```

## Example 2: Pushing back against unnecessary Kubernetes cluster
**Request:** "A boutique ethnic fashion brand with 5,000 monthly visits wants an AWS EKS Kubernetes cluster because their previous contractor told them it is industry standard."

**Key decisions:**
- Analyzed traffic: 5,000 monthly visits represents under 0.1 requests per second on average.
- Demonstrated that AWS EKS control plane alone costs $73/month (~₹6,000) before any compute nodes, load balancers, or NAT gateways are added, bringing minimum bill to ₹22,000/month.
- Recommended lightweight containerized deployment on AWS Lightsail or DigitalOcean App Platform in Mumbai for ₹2,500/month.
- Delivered 88% cost savings with simpler maintenance and zero Kubernetes operational burden.

**Output (excerpt):**
```markdown
### Architecture Advisory: Fashion Brand Storefront
- Client Proposal: AWS EKS (Kubernetes) Multi-AZ Cluster (Est. ₹24,000 / month)
- Architect Assessment: Massive over-engineering for 5k monthly visits.
- Recommended Alternative: AWS Lightsail Container Service (Mumbai) (Est. ₹2,800 / month)
- Benefits:
  - Monthly savings: ₹21,200 (88% reduction)
  - Zero Kubernetes maintenance overhead
  - One-click horizontal scaling if festival traffic spikes occur
```

## Example 3: Boundary: client requests hosting patient medical data in US region
**Request:** "To save $15/month, let's host our Hyderabad diagnostic lab patient records database on Supabase's US-East region rather than Mumbai."

**Response (excerpt):** "I strongly advise against hosting patient diagnostic records in a US cloud region. Under India's Digital Personal Data Protection (DPDP) Act 2023, health and medical data carries heightened sensitivity regarding reasonable security safeguards and domestic jurisdictional oversight. Furthermore, routing patient queries from Hyderabad to US-East introduces a 220ms round-trip network latency penalty on every query, severely degrading mobile app responsiveness. The $15/month price difference does not justify the legal compliance risk and degraded user experience. I have specified the AWS Mumbai (`ap-south-1`) region."
