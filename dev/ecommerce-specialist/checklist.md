# E-commerce Specialist (Shopify): Checklist

## Before starting
- [ ] Platform decision written; Shopify plan and pricing marked "verify as of <date>"
- [ ] Store, payment provider and domain accounts are in the client's name
- [ ] Products, SKU count, variant dimensions and shipping area known
- [ ] Tax display and product tax fields specified in writing by `gst-specialist`
- [ ] Invoice app and format agreed with `invoicing-specialist`
- [ ] Payment methods wanted (UPI, cards, netbanking, COD) confirmed
- [ ] Regulated or claim-heavy products flagged

## While working
- [ ] Work on a development store or unpublished theme, tracked in Git
- [ ] Sections expose only safe settings; blocks capped with `max_blocks`
- [ ] `render` used for snippets; no nested product loops
- [ ] Variant vs separate product decided per rule
- [ ] Metafield definitions typed; metaobjects for reusable content
- [ ] Imports use a pinned API version and paginated or bulk operations
- [ ] Images use width-limited `image_url`, lazy loading below the fold, hero preloaded only
- [ ] Every app vetted: purpose, cost, scopes, script weight, recent reviews
- [ ] COD rules decided: value cap, pincode exclusions, confirmation, prepaid incentive
- [ ] Pincode limits and delivery slots set for perishables
- [ ] No theme form or app collects card details
- [ ] Plan-dependent checkout features verified before promising them

## Before handoff
- [ ] `shopify theme check` shows zero errors
- [ ] Test-mode orders pass for every enabled payment method on an Android phone, ids recorded
- [ ] UPI intent flow returns to the store after payment
- [ ] Catalogue counts match the source sheet; 10-product sample checked
- [ ] Lighthouse mobile, LCP and CLS recorded for home, collection and product pages
- [ ] Setup note lists apps, costs to verify and leftover snippet cleanup
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Asked to publish a theme, switch payments live or enable COD without approval
- [ ] Asked to enter the client's bank, PAN or KYC details
- [ ] Asked to decide GST rates or call order emails "tax invoices"
- [ ] A paid app or plan upgrade is needed
