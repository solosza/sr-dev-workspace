# Step 04 — Decide, emit, gate

Pick the decision, emit it, self-gate.

## Read first
- the ranked candidates (step 03)
- `contracts/decision.schema.json`

## Decision rule (strict order)
1. any `exact` candidate → **reuse** (`target` = that capability).
2. else any `adaptable` candidate → **adapt** (`target` = the closest; `delta` = the changes).
3. else → **build** (nothing fits; `rationale` must name the closest `none` and why adapting it is a rewrite).

Reuse > adapt > build. Never choose `build` while an `adaptable` candidate exists.

## Adapt mode (in-place vs by-copy)
When the decision is `adapt`, choose how:
- **by-copy** when the target is LOAD-BEARING (a live dependency; mutating it would break something that
  works) OR belongs to a different repo/boundary than the output. Fork a renamed v2 copy, tailor it,
  leave the original untouched.
- **in-place** only when the target is not depended-on and shares the output's boundary.

Default to `by-copy` when unsure. Record `adapt_mode` in the decision.

## Emit + gate
1. Write the decision conforming to `decision.schema.json`:
   `{need, scope, decision, target?, delta?, rationale, candidates[]}`.
2. `reuse`/`adapt` require `target`; `adapt` requires `delta` (the schema enforces both).
3. Soft-gate: the decision is well-formed; the choice follows reuse>adapt>build; every surveyed
   candidate is listed with its fit (show your work).
4. Report one line: `reuse X` / `adapt X (delta)` / `build` + the rationale.

## Hand-off
- `reuse` → the coordinator points at `target`; no design/build needed.
- `adapt` → design/build runs on `target` with the `delta` (usually just a new contract).
- `build` → design/build runs fresh.
