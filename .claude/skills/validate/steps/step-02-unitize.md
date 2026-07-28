# Step 02 — Unitize

Decompose the artifact into UNITS, as the scope contract defines them. For the `doc` scope a unit is a
CLAIM; other scopes define their own (a pattern-requirement, a test, a rule).

## Read first
- the scope contract's `unit` block (`name`, `tag_vocabulary`)
- the artifact itself

## Procedure
1. Walk the artifact top to bottom. Each distinct assertion the contract's `unit` describes becomes one unit.
2. For the `doc` scope: a claim = a top-level tagged bullet or a standalone declarative statement.
   **Sub-bullets inherit the parent claim's tag** — do not raise them as separate untagged units.
3. For each unit capture:
   - `id` — stable and locatable (e.g. `s4-claim-3`, or a section + short slug)
   - `text` — the assertion itself (trim decoration; keep the truth condition)
   - `tag` — the discipline tag if present (`decided` / `open` / `hypothesis` / `citation` / ...)
   - `weight` — `load-bearing` (the doc leans on it), `supporting`, or `incidental` (judge it)

## Granularity
- One assertion = one unit. Do not fragment a single claim into clauses.
- Do not merge two distinct claims to save units. Distinct truth conditions = distinct units.
- A heading, a table caption, pure formatting = not a unit.

## Output
An ordered list of unit stubs `{id, text, tag, weight}`, ready for authority + check. Nothing is judged yet.
