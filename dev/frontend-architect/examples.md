# Frontend Architect: Examples

Business names below are fictional unless stated.

## Example 1: Restaurant site plus QR ordering in one Next.js app
**Request:** "Spice Route Kitchen (fictional) wants a marketing site and table QR ordering in the same app. Define the frontend architecture."

**Key decisions:**
- Marketing pages SSG; menu ISR revalidated by tag when the owner edits an item; table ordering dynamic with the cart in a small client store.
- Order status uses server data with polling every 10 s on the status page only (no websocket for this volume).
- Feature folders: `features/menu`, `features/cart`, `features/orders`; `ui/` holds primitives only.

**Output (excerpt):**
| Route group | Mode | Freshness | Personalized | Revalidation trigger |
|---|---|---|---|---|
| `/`, `/about`, `/contact` | SSG | days | no | deploy |
| `/menu` | ISR by tag `menu` | minutes | no | owner saves menu item |
| `/t/[table]/order` | dynamic | per request | session | none |

| Feature | State | Category | Home | Reason |
|---|---|---|---|---|
| cart | items, notes | shared client | Zustand store, persisted per table session | many components update it |
| menu | items, prices | server | server component fetch with tag | owner edits |
| filters | veg only, category | URL | search params | shareable, back button |

## Example 2: Angular admin with tangled modules
**Request:** "Our Angular school admin has circular imports and every feature imports everything. Propose a structure."

**Key decisions:**
- Ran `npx madge --circular src/`: 14 cycles, 9 through a shared `utils` barrel. Evidence attached.
- Target: standalone components, feature folders with a public `index.ts`, `shared/ui` with no services that fetch data.
- Migration in six PRs, starting with splitting the barrel; framework mechanics (standalone migration schematic) handed to `angular-specialist`.

**Output (excerpt):**
```
Migration steps
1. Split shared/utils barrel into date, currency, validation modules (fixes 9 cycles). Check: madge cycles <= 5, tests pass.
2. Add eslint no-restricted-imports: features/* may not import features/*/internal. Check: lint green.
3-6. Move one feature per PR to standalone + public API (attendance, fees, students, staff).
```

## Example 3: Boundary: "add Redux, the team knows it"
**Request:** "Add Redux Toolkit for the salon booking site so we have proper state management."

**Response (excerpt):** "I looked at the state in the booking flow: the selected service and slot (form state), available slots (server data) and the step number (URL). None of it is shared across distant components. Redux would add a store, providers and boilerplate with no consumer that needs it. I recommend React Hook Form for the form, server fetch for slots, and the step in the URL. If a later feature (for example a multi-branch cart) needs shared client state, we can add a small store then. Switching the primary state library is a `technical-lead` decision if you still want it."
