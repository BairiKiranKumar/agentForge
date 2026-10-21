# CMS Specialist: Checklist

## Before starting
- [ ] Approved content model received from `information-architect`
- [ ] Editors, devices, edit frequency and languages known
- [ ] CMS decision record written with plan limits and an as-of date
- [ ] CMS account owner is the client, or a dated transfer is recorded
- [ ] Locked vs editable parts agreed with `ui-designer`
- [ ] Owning seam identified for the task (schema, editor UI, media, preview, webhook, template)

## While working
- [ ] All types and fields defined in version-controlled code
- [ ] Design-critical values (prices, timings, phone) are structured fields with validation
- [ ] Every image field has a required alt text field with help text
- [ ] Slugs unique; redirect created when a published slug changes
- [ ] SEO fields have fallbacks to title and hero image
- [ ] Site-wide settings in a singleton (address, WhatsApp number, timings)
- [ ] Locale strategy (field-level or document-level) applied; English fallback works
- [ ] Telugu or Hindi font loaded and tested with real text when in scope
- [ ] Upload size limit, resizing and EXIF stripping in place
- [ ] Preview uses draft mode with a token and `noindex`
- [ ] Revalidation endpoint checks a shared secret server-side
- [ ] Each new plugin vetted: update date, installs, advisories, license
- [ ] No write-capable CMS token in client-side code

## Before handoff
- [ ] Top 5 editor tasks timed at 375 px width, each under 2 minutes
- [ ] Publish-to-live time measured on a preview deployment
- [ ] Type check, lint and tests run; results recorded
- [ ] Editor task list and screenshots sent to `client-training-specialist`
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A paid plan, trial or new account is needed
- [ ] Content import into the client's production dataset is requested without approval
- [ ] Content includes identifiable people with no consent record
- [ ] The client wants free layout editing on a locked premium design
