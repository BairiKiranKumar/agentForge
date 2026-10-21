# Implementation Specialist: Checklist

## Before starting
- [ ] Production environment URL and super-admin credentials confirmed
- [ ] Signed scope baseline and agreed integration list reviewed
- [ ] Client operational contacts identified for data supply and admin training
- [ ] 15-day Implementation Workplan drafted and shared
- [ ] Standardized CSV/Excel import templates prepared

## While working
- [ ] Core organization settings configured (branding, logo, time zone IST, currency INR)
- [ ] Client legacy data received and backed up in secure archive
- [ ] Automated data sanitization run: duplicate IDs, missing fields, phone regex checked
- [ ] Data Migration Exception Report sent to client for any rejected rows
- [ ] Cleaned data imported into database; record counts reconciled 100%
- [ ] User accounts created with strict role-based access control (RBAC)
- [ ] Third-party integrations tested: WhatsApp alert triggers and payment test webhooks verified
- [ ] Admin user walkthrough conducted covering primary daily operational workflows
- [ ] Short Loom/video tutorial recorded and shared with client staff
- [ ] Live test transaction executed and verified end-to-end

## Before handoff
- [ ] First live operational transaction successfully completed by client staff
- [ ] Formal Go-Live sign-off received from client leadership
- [ ] Account configuration notes compiled for `customer-success-manager`
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Client legacy data is hopelessly corrupt (>40% missing mandatory data)
- [ ] Client refuses to participate in administrative training sessions
- [ ] Payment gateway or SMS provider credentials fail activation
- [ ] Client demands custom engineering changes before agreeing to Go-Live
