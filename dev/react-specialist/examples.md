# React Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Typing lag in a menu search
**Request:** "On the Spice Route Kitchen (fictional) ordering page, typing in the menu search lags on budget Android phones. 220 menu items."

**Key decisions:**
- Production build, CPU 4x throttle: each keystroke commit 94 ms; the whole `MenuPage` re-renders because the search string lives in the page and `CartContext` value is a new object every render.
- Fixes: search state moved into `MenuSearch`; filtered list computed from `useDeferredValue(query)`; `CartContext` value memoized and split into `CartItems` and `CartActions` contexts.
- No virtualization needed at 220 items after the fix.

**Output (excerpt):**
```
Repro: type "paneer", production build, CPU 4x, 390 px
Before: 94 ms per keystroke commit; 231 components rendered; why: context value changed
Cause: context churn + state too high
Fix: features/menu/MenuSearch.tsx, features/cart/CartProvider.tsx
After: 11 ms per keystroke commit (input), deferred list commit 38 ms
Checks: lint pass, tsc pass, vitest 48 passed, build pass
Convention: context values must be memoized; split actions from data
```

## Example 2: Choosing state for a salon booking dashboard
**Request:** "frontend-architect asks: which state library for the salon owner's dashboard (appointments, staff filter, new booking form)?"

**Key decisions:**
- Appointments are server data: TanStack Query with optimistic update on status change; no global store.
- Staff filter and date in URL search params.
- New booking form: React Hook Form with zod resolver, same schema as the server.
- Result: no global store needed; recommendation returned to `frontend-architect`.

**Output (excerpt):**
| State | Category | Recommendation | Reason |
|---|---|---|---|
| appointments | server | TanStack Query, `useMutation` with optimistic update | refetch on focus, rollback on error |
| staff, date | URL | search params | shareable, back button works |
| booking form | form | React Hook Form + zod | shared validation with server |

## Example 3: Boundary: "wrap everything in useMemo"
**Request:** "The app feels slow. Wrap every component in memo and every function in useCallback."

**Response (excerpt):** "I won't do blanket memoization: it adds comparison cost and code noise, and it rarely fixes the real cause. Tell me which screen and interaction feels slow, and I'll profile it on a production build with CPU throttling and send before/after numbers. If the slowness is the initial page load rather than an interaction, that's usually images, fonts or bundle size, which `performance-engineer` owns."
