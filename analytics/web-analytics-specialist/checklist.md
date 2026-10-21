# Web Analytics Specialist: Checklist

## Before starting
- [ ] GTM container and GA4 property access verified with publish permissions
- [ ] Website tech stack and routing architecture (Next.js, SPA, MPA) confirmed
- [ ] Business conversion goals identified (leads, bookings, purchases, clicks)
- [ ] DPDP Act consent requirements and cookie banner integration reviewed
- [ ] Tag Assistant Companion extension installed for debugging

## While working
- [ ] Measurement Plan authored mapping business goals to standard GA4 events
- [ ] Consent Mode v2 defaults configured (`denied` before interaction)
- [ ] Clean dataLayer push specifications provided to frontend developers
- [ ] GA4 Configuration Tag initialized with anonymize IP and clean URL parameters
- [ ] Conversion events (`generate_lead`, `purchase`, `contact`) configured with clean triggers
- [ ] Enhanced E-commerce events configured with items array, currency, and value
- [ ] Single Page App (Next.js) virtual pageviews configured on route change
- [ ] URL parameters audited to prevent PII (email, phone) leaking into GA4
- [ ] GTM Preview Mode executed across mobile and desktop viewports
- [ ] GA4 DebugView verified: events and custom parameters register accurately

## Before handoff
- [ ] GTM container published with descriptive version notes
- [ ] Conversion events marked as conversions in GA4 property settings
- [ ] Measurement Plan shared with `marketing-analyst` and development team
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Tracking tags are discovered harvesting unhashed customer passwords or Aadhaar data
- [ ] Client refuses to implement consent mechanisms under DPDP Act requirements
- [ ] Tracking tags inject heavy third-party scripts that severely degrade mobile page speed
- [ ] Container publish access is blocked or locked by previous agency vendor
