# Step 05 — Judge, emit, gate

Assign a verdict to each unit, attach the evidence, apply the contract's rules, emit the register, and
soft-gate it.

## Read first
- units + their `{authority, evidence}` (step 04)
- the scope contract's `rules` (each with `gate: hard|soft`) and its `pass` condition
- `contracts/verdict-register.schema.json`

## Verdict rubric
| Verdict | When | Requires |
|---|---|---|
| `confirmed` | authority checked, supports the claim | `authority` + `evidence` |
| `refuted` | authority checked, contradicts the claim | `authority` + `evidence`, `flagged: true` |
| `unsupported` | authority reachable but does not say what is claimed | `authority` + `evidence`, `flagged: true` |
| `unresolved` | authority unreachable, or unit uncheckable as written | `evidence` (why), `flagged: true` |
| `not-applicable` | self-contained/internal unit, internally consistent; or a rule not triggered | — |

## Apply the contract rules
For each rule, on the units it `applies_to`:
- `hard` rules (structural) — if violated, `flag` the unit (untagged claim; hypothesis with no
  falsification criterion; dangling in-repo reference). The generic gate hook enforces these too.
- `soft` rules (judgment) — you enforce them here (a citation must be `confirmed` against its authority,
  never assumed).

## Emit + soft gate
1. Write the `verdict-register` conforming to the schema: `{artifact, scope, contract, units[], gate}`.
2. Every unit MUST carry a `verdict`; every checked verdict MUST carry `authority` + `evidence`
   (no evidence = the unit fails, regardless of confidence).
3. Soft-gate: `gate.findings` = count of `flagged` units; `gate.verdict` = `pass` iff `findings == 0`.
4. Report the one-line verdict and list the findings.
