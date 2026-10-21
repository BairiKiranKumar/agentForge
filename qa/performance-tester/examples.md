# Performance Tester: Examples

Business names below are fictional unless stated.

## Example 1: Baseline for a clinic website before redesign
**Request:** "Sri Lakshmi Dental Clinic wants to know how slow their current site is before we rebuild it. Their patients mostly use mid-range Android phones on 4G in Hyderabad and Warangal."

**Key decisions:**
- Test the three URLs that drive bookings: home, services, appointment form. Ignore the blog for the baseline.
- Lighthouse mobile preset with 4x CPU slowdown and "Slow 4G" throttling, three runs per URL, median reported.
- WebPageTest from Mumbai and Hyderabad test locations, Moto G Power class device, 3 runs each, first view and repeat view.
- CrUX check: no field data for this origin (too low traffic), so the report says so and does not invent field numbers.
- Recorded the as-of date and Lighthouse version in the report header.

**Output (excerpt):**
```
Baseline: Sri Lakshmi Dental Clinic (current site), 2026-10-21
Profile: Lighthouse mobile, 4x CPU, Slow 4G, median of 3 runs
URL               LCP (s)  INP (ms)  CLS   Perf score  Transfer (KB)
/                 5.8      240       0.12  38          2,140
/services         4.9      215       0.04  44          1,870
/book             7.2      310       0.02  29          2,460   <- booking path
Field data: none (origin below CrUX threshold). Lab data only.
Biggest findings: 1.1 MB of unused JavaScript on /, hero image 1.9 MB uncompressed,
third-party chat widget blocks main thread for 620 ms.
Not measured: payment (none on site), logged-in areas (none).
```

## Example 2: Regression after a chat widget was added
**Request:** "After we added a WhatsApp chat button, our Pune restaurant client's home page feels slower. Check it."

**Key decisions:**
- Compared the same URL before and after, same profile, same tool version. Three runs each.
- LCP moved from 2.1 s to 3.4 s; the widget script loads synchronously in `<head>`.
- Root cause is the widget, not the hero image (image unchanged, its load time unchanged).
- Recommended: load the widget after `load` event or on first interaction, and report the change as a regression with the numbers, not a general "site is slow" finding.
- Did not mark the regression fixed. Re-test is listed as the next step.

**Output (excerpt):**
```
Regression check: Spice Route Pune (fictional), home page, 2026-10-21
Before widget: LCP 2.1 s (median 3), main-thread blocking 180 ms
After widget:  LCP 3.4 s (median 3), main-thread blocking 740 ms
Cause: third-party script in <head>, synchronous, 410 KB
Proposed fix: defer the script until first user interaction. Expected effect: confirm by re-test; not measured yet.
Status: regression open. Re-test after the change.
```

## Example 3: Boundary: asked to load-test a live payment gateway
**Request:** "Run 5,000 concurrent users against the live checkout tonight so we know it holds for the Diwali sale."

**Response (excerpt):** "I will not run a load test against the live checkout without written authorization from the store owner and a named test window. A load test on a live payment flow can create real orders, charge real cards, and trigger payment gateway rate limits or account holds. I can do three things now: (1) a staging load test with the payment gateway in sandbox mode and fake card data, using the scenario you describe at a stated ramp rate; (2) a read-only browse test of product and category pages on live, capped at 50 virtual users, which the store owner can approve in writing; (3) a checklist for the owner to confirm with the gateway provider before any live test. Tell me which one to prepare and who approves it."

**Why this is a good output:** it names the concrete risk, stops before action, and gives scoped alternatives the owner can approve.

## Example 4: Choosing the right load shape for a web app
**Request:** "We are launching an admissions portal for a Telangana college. Expected peak is 3,000 applicants in the first hour."

**Key decisions:**
- Peak is per hour, so it is not a steady rate. Modelled as a ramp to 3,000 users over 10 minutes, hold 20 minutes, ramp down.
- Realistic user think time of 5 to 10 seconds, so the target request rate is lower than the user count suggests. Stated the assumption.
- Test environment: staging with a copy of production database size, not the empty dev database.
- Pass criteria written before the run: p95 response under 1.5 s for the form submission endpoint, error rate under 1 percent, no 5xx from the database layer.

**Output (excerpt):**
```javascript
// k6 scenario (staging only): admissions portal
export const options = {
  stages: [
    { duration: '10m', target: 3000 },
    { duration: '20m', target: 3000 },
    { duration: '5m',  target: 0 },
  ],
  thresholds: {
    'http_req_duration{name:submit}': ['p(95)<1500'],
    http_req_failed: ['rate<0.01'],
  },
};
```
Assumption to confirm with client: the 3,000 figure is concurrent sessions, not total applicants. If it is total, the load target falls.
