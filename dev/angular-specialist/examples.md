# Angular Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Duplicate fee API calls in a school admin
**Request:** "The fees page in the Green Valley School (fictional) Angular admin fires the fee API three times when the class filter changes, and sometimes shows the wrong class."

**Key decisions:**
- Versions from lockfile: @angular/core 19.x, rxjs 7.8. Verified `toSignal` and `takeUntilDestroyed` exist in that version.
- Cause: three template `async` pipes on the same cold HTTP observable, and `mergeMap` on filter changes so slow responses arrive out of order.
- Fix: one stream with `switchMap`, exposed with `toSignal`; template reads the signal.

**Output (excerpt):**
```ts
private readonly classId = toObservable(this.selectedClass); // signal from filter
readonly fees = toSignal(
  this.classId.pipe(switchMap(id => this.feesApi.forClass(id))),
  { initialValue: [] as Fee[] }
);
```
```
Root cause: 3 subscriptions to a cold observable + mergeMap (no cancellation)
Verification: ng test -> 112 passed; network tab shows 1 request per filter change
Convention: one subscription per data stream; switchMap for parameter-driven loads
```

## Example 2: Upgrade from Angular 16 to the current major
**Request:** "Upgrade the clinic portal from Angular 16 to the latest version."

**Key decisions:**
- One major per step (16 to 17 to 18 and onward), each a separate commit with tests green.
- Checked peer dependencies before each step: the date-picker library has no release for the target at step 3, so the upgrade pauses there and the options go to `technical-lead`.
- Control flow and standalone migrations are deferred to separate PRs after the version upgrade.

**Output (excerpt):**
| Step | Command | Migrations applied | Manual changes | Tests |
|---|---|---|---|---|
| 16 -> 17 | `ng update @angular/core@17 @angular/cli@17` | automatic | none | 88 passed |
| 17 -> 18 | `ng update @angular/core@18 @angular/cli@18 @angular/material@18` | automatic | theme import path | 88 passed |
| 18 -> 19 | blocked | n/a | date-picker peer dep supports up to 18 | not run |

## Example 3: Boundary: "just add detectChanges everywhere"
**Request:** "The attendance list doesn't refresh after marking. Add `cdr.detectChanges()` after every update so it works."

**Response (excerpt):** "That would hide the cause and add change detection cost on every update. The list component is OnPush, and `markPresent()` mutates the student object in place, so Angular sees the same array reference. I've changed the store to a signal and updated it immutably (`students.update(list => list.map(...))`). The view now refreshes without manual calls. Test added: 'marking a student updates the row status'. If there are other places with the same pattern, I've listed the three files I found for `frontend-developer`."
