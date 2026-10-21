# Observability Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Instrumenting Sentry and structured Pino logging for school portal
**Request:** "Set up error tracking and structured logging for Pragathi School Portal (Next.js + Node API). We need clear stack traces and zero leaked passwords."

**Key decisions:**
- Configured Pino logger with JSON output and automatic sensitive key redaction.
- Integrated Sentry Next.js SDK on client and server.
- Configured GitHub Actions to upload source maps on release so stack traces map to original TypeScript lines.
- Added custom Sentry user context capturing `school_id` and role without storing student personal names.

**Output (excerpt):**
```typescript
// lib/logger.ts
import pino from 'pino';

export const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  redact: {
    paths: ['password', 'confirmPassword', 'req.headers.authorization', 'token', 'parent_phone'],
    censor: '[REDACTED]',
  },
});
```

## Example 2: Resolving alert fatigue on e-commerce storefront
**Request:** "Our team is getting 60+ alert emails every day from Kavitha Sarees website. Engineers have muted the notification channel."

**Key decisions:**
- Audited active alerts: 45 daily alerts were triggered by harmless single 404s caused by web crawlers probing old image links.
- Deleted the raw 404 count alert; replaced with a 404 error rate spike alert (>15% of total traffic for 5 minutes).
- Consolidated low-disk warnings from 5-minute intervals to a single daily digest alert until threshold reaches 85%.
- Reduced daily alert volume from 60+ to 2 actionable notifications per week.

**Output (excerpt):**
```markdown
### Alert Fatigue Remediation: Kavitha Sarees
- Before: 64 average alerts/day (98% non-actionable noise).
- Audit Findings:
  - 404 crawler triggers: Removed single-event alert; created rate-based rule.
  - Health probe flapping: Increased evaluation window from 30s to 2m.
- After: 2 average alerts/week (100% actionable).
- Team action: Re-enabled alerts channel in Slack.
```

## Example 3: Boundary: pushback against logging raw database query parameters
**Request:** "Our developers want to log all SQL query parameters in plain text in production to make debugging database errors easier."

**Response (excerpt):** "I cannot enable raw SQL parameter logging in production logs. Database queries frequently contain unencrypted user passwords, bank account numbers, customer contact numbers, and authentication tokens in their `WHERE` and `INSERT` clauses. Writing raw parameters to logs dumps sensitive customer personal data into our log aggregators, directly violating the DPDP Act 2023. Instead, I have configured parameterized query logging, which logs the SQL statement structure (`INSERT INTO users (name, phone) VALUES (?, ?)`) and query execution time without exposing the actual sensitive variable values."
