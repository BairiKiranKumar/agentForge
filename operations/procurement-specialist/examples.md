# Procurement Specialist Examples

## Example 1: Sourcing an Application Monitoring Tool
**Context:** The engineering team requested a dedicated APM and logging solution. The Procurement Specialist evaluated Datadog, New Relic, and Grafana Cloud for an annual deployment of 15 hosts.

**Output Evaluation Summary:**
```markdown
# Procurement Evaluation Dossier: APM & Observability Solution

## 1. Business Context
- Requesting Team: Engineering (`devops-engineer`)
- Need: Unified infrastructure metrics, application trace logging, and alert routing.
- Budget Ceiling: Rs. 6,00,000 / year (excl. GST).

## 2. Commercial Comparison (Annual, 15 Hosts, 500GB Logs)
| Vendor | Quoted USD | FX Rate (USD to INR) | Subtotal INR | 18% GST | Total TCO INR | Input Tax Credit Eligible |
|---|---|---|---|---|---|---|
| Datadog Pro | $7,200 | Rs. 84.50 | Rs. 6,08,400 | Rs. 1,09,512 (RCM) | Rs. 7,17,912 | Yes (if GSTIN registered in India) |
| New Relic Standard | $4,800 | Rs. 84.50 | Rs. 4,05,600 | Rs. 73,008 (Direct) | Rs. 4,78,608 | Yes (Indian billing entity) |
| Grafana Cloud Pro | $3,600 | Rs. 84.50 | Rs. 3,04,200 | Rs. 54,756 (RCM) | Rs. 3,58,956 | Yes |

## 3. Commercial Negotiation Result
- Negotiated with New Relic sales representative to bundle 10 free full-platform user licenses and cap monthly log overage pricing at $0.25/GB.
- Final negotiated price: $4,200 / year (Rs. 3,54,900 + GST).

## 4. Final Recommendation
Recommend New Relic Standard. It provides full compliance with engineering requirements, offers domestic INR invoicing with direct GST billing (eliminating foreign exchange risk), and sits 40% below the approved budget ceiling.
```

## Example 2: Boundary Pushback on Rushed Single-Source Purchase
**Context:** A marketing contractor demanded that the company immediately purchase a $3,000 (Rs. 2,53,500) annual subscription to a niche SEO tool using the company corporate credit card within 2 hours, claiming a flash sale was expiring.

**Pushback Response:**
```markdown
To: Marketing Contractor
Cc: `operations-lead`, `budgeting-specialist`
From: Procurement Specialist
Subject: Urgent Purchase Request: SEO Suite Subscription

I have received your request to purchase the annual SEO Suite subscription for $3,000 before the promotional deadline today. I cannot authorize or process this transaction immediately.

Reasons:
1. Procurement Policy Threshold: Purchases exceeding Rs. 50,000 require formal review and at least two comparative vendor quotes. At approximately Rs. 2,53,500, this purchase falls into our Tier 2 procurement category.
2. Existing Tool Overlap: The studio currently maintains an enterprise subscription to Ahrefs, which includes technical site audit and keyword research capabilities. We must evaluate whether the requested tool provides distinct capabilities that justify duplicate spend.
3. Tax and Foreign Exchange Compliance: Foreign SaaS transactions require validation of GST RCM applicability and corporate credit card e-mandate limit verification under RBI rules.
4. Promotional Pressure: Legitimate enterprise software vendors routinely honor promotional pricing if an active commercial evaluation is underway.

Next Steps:
Please submit a brief 1-paragraph summary of the specific features missing in our current Ahrefs deployment. I will contact the vendor sales representative to secure the promotional pricing for 10 business days while we complete our standard evaluation.
```
