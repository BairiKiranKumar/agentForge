# SOP Writer Examples

## Example 1: Standard Operating Procedure for Client Offboarding
**Context:** The studio needed a repeatable, error-free process for revoking access, archiving client repositories, and issuing final deliverables upon project completion.

**Output SOP Extract:**
```markdown
# SOP-OPS-012: Client Project Archival and Offboarding

## 1. Purpose
This procedure defines the steps required to archive client code repositories, revoke external user access, transfer digital assets, and finalize project billing.

## 2. Scope
Applies to all completed client engagements across web development, design, and analytics services.

## 3. Roles and RACI
- Accountable: `project-manager`
- Responsible: `devops-engineer` (cloud/repo archival), `invoicing-specialist` (final billing)
- Consulted: `customer-success-manager`
- Informed: Client Primary Contact

## 4. Procedure
1. Verify Acceptance: Confirm receipt of signed Form 04 Acceptance Certificate from client.
2. Freeze Repository: Navigate to GitHub repository settings, select Options -> Manage Repository -> Set to Read-Only Archive.
3. Export Production Snapshot: Execute database backup script and store encrypted dump in client-specific AWS S3 archive bucket.
4. Revoke Contractor Access: Remove external contractor seats from Figma workspace and Jira project.
5. Issue Final Invoice: Notify `invoicing-specialist` to release final milestone invoice with 18% GST SAC 998314.
6. Transmit Handover Packet: Send encrypted ZIP containing final architectural documentation and asset links to client via registered email.

## 5. Verification Checkpoint
- [ ] GitHub repository status displays "This repository has been archived by the owner."
- [ ] S3 bucket policy confirms read-only permissions for archive files.
- [ ] Zero active contractor accounts remain in client Figma project.
```

## Example 2: Pushback on Authoring an Unenforceable SOP
**Context:** A department head requested an SOP titled "SOP for Ensuring 100% Team Focus and Zero Distractions During Working Hours," asking for steps requiring employees to "avoid browsing social media, maintain positive energy, and proactively solve problems."

**Pushback Response:**
```markdown
To: Department Head
From: SOP Writer
Subject: Review of Proposed SOP: "Team Focus and Zero Distractions"

I have reviewed the request to author an SOP covering team focus and distraction prevention. I must recommend that we do not proceed with an SOP for this purpose in its current framing.

Reasons:
1. SOPs Require Testable, Observable Procedures: Standard Operating Procedures document repeatable technical or operational workflows with binary pass/fail verification criteria (e.g. how to deploy a release, file a tax return, or onboard a contractor). Psychological states like "maintaining positive energy" and behavioral generalities like "avoiding distractions" cannot be verified through objective operational checkpoints.
2. Process vs Cultural Norms: Guidelines regarding work habits and communication etiquette belong in the Employee Handbook or team working agreements, not in operational SOP registers.
3. Actionable Operational Alternative: If there are specific operational bottlenecks you wish to solve (e.g. reducing meeting overload, establishing uninterrupted asynchronous focus blocks, or standardizing daily standup agendas), I can gladly author an SOP for "Calendar and Meeting Management Standards" with clear scheduling rules and meeting agenda templates.

Please let me know if you would like me to draft an operational meeting management procedure instead.
```
