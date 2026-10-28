# Budgeting Specialist: Checklist

## Before starting
- [ ] Period confirmed (April to March financial year, or project start and end dates)
- [ ] Categorized actuals received from `bookkeeping-assistant`, or bank export marked `[Inference]`
- [ ] GST registration status known (decides gross vs net budgeting)
- [ ] Current subscription list with plans, cycles and currencies collected
- [ ] the owner's goals and planned big purchases recorded

## While working
- [ ] Every line has driver, owner, cycle, currency and renewal date
- [ ] Annual renewals phased into their actual month
- [ ] Unregistered: input GST budgeted as a cost; registered: ex-GST with ITC noted for `gst-specialist`
- [ ] USD tools include card forex markup as a separate line
- [ ] Prices for new tools taken from vendor pages with as-of date, or marked unknown
- [ ] Set-aside amounts copied from `ca-assistant` / `gst-specialist` with as-of dates
- [ ] Variance = actual minus budget, sign convention stated
- [ ] Price and volume effects sum to total variance
- [ ] Materiality uses both percentage and amount thresholds
- [ ] Each material variance classified: price, volume, timing, one-off, new item, or error
- [ ] Timing variances state when they reverse
- [ ] Project spend checked against 80% and 100% alert levels
- [ ] Consecutive unfavourable months counted per category

## Before handoff
- [ ] Budget vs actual total matches the ledger total for the month
- [ ] No circular or "various items" narratives
- [ ] Unbudgeted recurring charges listed
- [ ] Subscription audit (quarterly) includes last-used date and cancel-by date
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A project has reached 100% of its cost budget and more spend is planned
- [ ] Asked to cancel, buy or upgrade a tool directly
- [ ] Personal and business spend cannot be separated without the owner
- [ ] Asked to compute a tax set-aside with no figure from a tax role
