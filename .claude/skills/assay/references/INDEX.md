# References Index

Routing table only — content lives in the design doc references (one source of truth). No duplication.

## Design Doc References

- -> `.claude/docs/design/assay/index.md` — the design doc (identity, philosophy, workflow summary, file structure)
- -> `.claude/docs/design/assay/references/workflow.md` — per-step Purpose + Procedure (Loops 1-3 + Decide)
- -> `.claude/docs/design/assay/references/lenses.md` — the 6 divergence lenses
- -> `.claude/docs/design/assay/references/gates.md` — the adversarial gate battery
- -> `.claude/docs/design/assay/references/io-contracts.md` — typed objects (Idea / Wedge / BuildVerdict / ValidationResult / Decision)
- -> `.claude/docs/design/assay/references/state-schema.md` — ledger (v1) + v2 stores (anti-library, world-model, registry)
- -> `.claude/docs/design/assay/references/contracts.md` — per-step contract definitions (soft + mechanical rules)

## By Step

### Step 1: Opportunity
- -> design doc: [[io-contracts]] (Idea, Wedge), [[lenses]] (6 lenses), [[gates]] (gate battery)
- contract: `contracts/step-01-contract.json`

### Step 2: Buildability
- -> design doc: [[io-contracts]] (Wedge in, BuildVerdict out)
- contract: `contracts/step-02-contract.json`

### Step 3: Validate
- -> design doc: [[io-contracts]] (ValidationResult)
- contract: `contracts/step-03-contract.json`

### Step 4: Decide
- -> design doc: [[io-contracts]] (Decision), [[state-schema]] (ledger)
- contract: `contracts/step-04-contract.json`

## By Artifact Type

### Typed verdicts (JSON)
- -> design doc: [[io-contracts]] — Idea / Wedge / BuildVerdict / ValidationResult / Decision shapes

### Divergence + gating
- -> design doc: [[lenses]] — how candidate wedges are generated
- -> design doc: [[gates]] — how candidates are killed by default

### Persistence
- -> design doc: [[state-schema]] — the append-only ledger (`state/ledger.jsonl`) + v2 roadmap stores
