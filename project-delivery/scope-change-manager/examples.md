# Scope Change Manager Examples

## Example 1: Evaluating a Complex Scope Variation Request
**Context:** During the build of a mobile booking app for an Indian boutique hotel chain, the client requested adding real-time WhatsApp booking confirmations and dynamic currency conversion, which were not in the baseline SOW.

**Output Impact Assessment Extract:**
```markdown
# Scope Impact Assessment: CR-012 (WhatsApp Notifications & Multi-Currency)

## 1. Scope Boundary Audit
- SOW Baseline Reference: SOW Section 4.2 specifies email notifications via SendGrid exclusively.
- Exclusions Reference: SOW Section 9.1 explicitly lists "WhatsApp Business API integrations" and "Multi-currency processing" under Excluded Capabilities.
- Determination: Billable Scope Change (Major).

## 2. Technical & Schedule Impact
- Effort Breakdown (from `estimation-specialist` & `technical-lead`):
  - WhatsApp Meta Cloud API integration & webhook handler: 24 hrs
  - Multi-currency rate conversion service & currency switcher UI: 32 hrs
  - Regression testing & localization QA: 16 hrs
  - Total Effort Delta: 72 engineering hours
- Schedule Impact: Milestone 3 (Checkout Flow) extended by 5 business days.

## 3. Commercial Impact
- Rate Basis: Rs. 2,500 / billable hour
- Additional Fee: 72 hrs * Rs. 2,500 = Rs. 1,80,000 + 18% GST (Rs. 32,400) = Rs. 2,12,400 INR
- Invoicing Terms: 50% upon Change Order signature, 50% upon staging UAT sign-off.

## 4. Recommendation
Submit formal Change Order CR-012 to client Managing Director for dual execution before Sprint 5 planning.
```

## Example 2: Boundary Pushback on Disguising Scope as a Defect
**Context:** A client product manager filed a critical "Sev 1 Bug" ticket stating: "The customer dashboard cannot export consolidated tax reports across multiple financial years in Excel format." The original specification called only for monthly CSV export.

**Pushback Response:**
```markdown
To: Client Product Manager
Cc: `delivery-manager`, `project-manager`
From: Scope Change Manager
Subject: Ticket Triage: #402 (Multi-Year Consolidated Tax Excel Export)

I have audited Ticket #402, which was logged as a Severity 1 Defect. I must inform you that this item has been reclassified from a Defect to a Feature Request / Scope Change.

Reasons:
1. Contractual Specification: Statement of Work #2026-04, Section 5.3 (Reporting) explicitly specifies: "User may export active monthly transaction ledger as a standard CSV file."
2. Technical Distinction: Building multi-year cross-table financial aggregation with custom Excel formatting (.xlsx formula injection, cell styling, sheet compilation) represents net-new business logic requiring heavy database querying and a new backend export queue worker. It is not an error in the existing monthly CSV export function, which operates with zero defects.
3. Constructive Path Forward:
   - I have logged this request in our Change Register as CR-015.
   - We have sized this feature at 20 engineering hours (Rs. 50,000 + GST).
   - If approved, we can schedule this for Sprint 5 without delaying your core launch next month.

The existing monthly CSV export remains fully functional and verified on staging.
```
