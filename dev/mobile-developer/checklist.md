# Mobile Developer: Checklist

## Before starting
- [ ] Target platforms confirmed (Android, iOS, PWA) and who owns the developer accounts
- [ ] Delivery form decision written (PWA, Expo, Flutter, native) with a revisit trigger
- [ ] Offline jobs listed: what must work with no network
- [ ] API contract and shared web code located; existing API client reused
- [ ] Every requested permission has a feature reason
- [ ] Mid-range Android test device identified (model, Android version, RAM)

## While working
- [ ] Data classified as cached reference vs queued writes
- [ ] Queued writes carry a client UUID idempotency key
- [ ] Conflict rule defined for money, stock and attendance fields
- [ ] Sessions stored in secure storage, not AsyncStorage or plain prefs
- [ ] Push permission requested after a value moment, not on first launch
- [ ] Android notification channels created per purpose
- [ ] Push payloads carry ids and routes, no personal data
- [ ] Lists virtualised with stable keys; images resized and cached
- [ ] Touch targets 48 dp or 44 pt; icon buttons labelled; font scaling to 200% works
- [ ] Strings externalised for later Telugu or Hindi
- [ ] Keystores and credentials only in EAS or CI secrets

## Before handoff
- [ ] Release build measured on the real device: cold start and size within budget or waived
- [ ] Airplane-mode test: 10 or more queued writes synced with zero duplicates
- [ ] Push delivery checked on at least one aggressive-battery OEM device
- [ ] Tests, type check and lint run; results recorded
- [ ] OTA-safe vs store-build changes stated
- [ ] Permission and SDK data list sent to `privacy-specialist`
- [ ] Platforms not built or not tested listed as such
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A store submission, production OTA or real-user push is requested without recorded approval
- [ ] A developer account must be created or paid for
- [ ] The feature needs background location, SMS, contacts or call log access
- [ ] Someone asks to embed a service-role key or private API key in the app
