# API Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Orders API for restaurant QR ordering with a future mobile app
**Request:** "Spice Route Kitchen (fictional) will add an Android app later. Define the orders API now."

**Key decisions:**
- REST with OpenAPI 3.1 because a second client (the app) is planned; web keeps using it through generated types.
- `POST /v1/orders` requires `Idempotency-Key`: table customers on weak Wi-Fi tap "Place order" twice.
- Prices are never accepted from the client; the server computes totals from menu item ids.
- Order list for the kitchen uses cursor pagination by `created_at, id`.

**Output (excerpt):**
```yaml
/v1/orders:
  post:
    summary: Place an order for a table
    security: [{ tableSession: [] }]
    parameters:
      - in: header
        name: Idempotency-Key
        required: true
        schema: { type: string, format: uuid }
    requestBody:
      content:
        application/json:
          schema: { $ref: '#/components/schemas/OrderCreate' }
          example: { table_id: "t-07", items: [{ menu_item_id: "m-112", qty: 2, note: "less spicy" }] }
    responses:
      '201': { $ref: '#/components/responses/OrderCreated' }
      '409': { $ref: '#/components/responses/Problem' }   # code: ITEM_UNAVAILABLE
      '422': { $ref: '#/components/responses/ValidationProblem' }
components:
  schemas:
    Money:
      type: object
      required: [amount_paise, currency]
      properties:
        amount_paise: { type: integer, minimum: 0, example: 34000 }
        currency: { type: string, const: INR }
```
```
Lint: redocly lint -> 0 errors, 2 warnings (missing operation descriptions on GET /v1/menu, fixed)
```

## Example 2: Classifying a requested change
**Request:** "Rename `student_name` to `name` and make `section` required in the students API. The parent app v1.3 is live."

**Key decisions:**
- Both are breaking: rename removes a field; making a field required breaks old writes.
- Proposed: add `name` alongside `student_name` (additive, v1.4 contract), mark `student_name` deprecated; keep `section` optional in v1, required in v2.
- The owner approval needed because a released app consumes v1.

**Output (excerpt):**
| Change | Additive/Breaking | Migration for consumers |
|---|---|---|
| Add `name` (same value as `student_name`) | Additive | New app versions read `name` |
| Deprecate `student_name` | Additive (deprecation) | Removed in v2 after sunset date agreed by the owner |
| `section` required on create | Breaking | Only in v2; v1 defaults to class's first section |

## Example 3: Boundary: "design the Razorpay webhook API too"
**Request:** "While you're at it, design how Razorpay calls us and how we call Razorpay."

**Response (excerpt):** "Razorpay's API and webhook payloads are defined by Razorpay, and the integration (signature verification, retries, idempotent processing) belongs to `integration-engineer`. What I can define is our own side that our apps consume: for example `GET /v1/orders/{id}` returning `payment_status` from our database, with the values `pending`, `paid`, `failed`, `refunded` and the rule that status changes only from verified webhooks. I've added that to the spec and sent the integration questions to `integration-engineer`."
