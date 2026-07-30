# Contract Definitions

Design-level contract specs, one per step. `/build-command` Step 6 materializes these into `.claude/skills/assay/contracts/step-0N-contract.json`. Each has soft_validation_rules (judgment, logged with rationale) + mechanical_validations (checkable) + a canonical_reference.

## step-01 — Opportunity -> Wedge[]
```json
{
  "contract_id": "assay:step-01:output",
  "artifact_type": "json",
  "canonical_reference": { "path": ".claude/docs/design/assay/references/io-contracts.md" },
  "soft_validation_rules": [
    { "id": "diverge-coverage", "rule": "candidates were generated from all 6 lenses across the abstraction rungs BEFORE any gating" },
    { "id": "gate-legal", "rule": "each surviving wedge cleared the legal/reg gate (no missing license, not ToS-violating)" },
    { "id": "gate-saturation", "rule": "each survivor names a seam vs incumbents + generic tools" },
    { "id": "gate-whynow", "rule": "each survivor cites a timing catalyst" },
    { "id": "gate-moat", "rule": "each survivor has a defensible edge, not pure commodity" },
    { "id": "gate-fit", "rule": "each survivor maps to an asset/skill/channel the operator has" },
    { "id": "kill-by-default", "rule": "uncertain gates killed or flagged for escalation, never silent-passed" }
  ],
  "mechanical_validations": [
    { "id": "shape", "rule": "output is a Wedge[] matching io-contracts (id, idea_ref, abstraction_rung, lens_origin, description, opening, gate_scores, rank)" },
    { "id": "empty-ok", "rule": "an empty array is VALID and means no opening found (must be explicit, not an error)" }
  ]
}
```

## step-02 — Buildability -> BuildVerdict[]
```json
{
  "contract_id": "assay:step-02:output",
  "artifact_type": "json",
  "canonical_reference": { "path": ".claude/docs/design/assay/references/io-contracts.md" },
  "soft_validation_rules": [
    { "id": "reuse-first", "rule": "buildable scored against reusing the existing stack before proposing new build" },
    { "id": "hitl-line", "rule": "the automate/HITL boundary is stated per verdict" },
    { "id": "moat-honesty", "rule": "moat_applies is false when governance adds no real defensibility" },
    { "id": "pns-reentry", "rule": "a picks-and-shovels variant, if emitted, is flagged for 1-hop re-entry into Step 1" }
  ],
  "mechanical_validations": [
    { "id": "shape", "rule": "output is a BuildVerdict[] matching io-contracts, one per input Wedge, decision in {build, pass}" }
  ]
}
```

## step-03 — Validate -> ValidationResult[]
```json
{
  "contract_id": "assay:step-03:output",
  "artifact_type": "json",
  "canonical_reference": { "path": ".claude/docs/design/assay/references/io-contracts.md" },
  "soft_validation_rules": [
    { "id": "threshold-first", "rule": "the pass threshold is defined BEFORE the signal is recorded (no post-hoc goalposts)" },
    { "id": "cheapest", "rule": "the chosen test is the cheapest signal that would actually change the decision" },
    { "id": "boxed", "rule": "the test is time- and cost-boxed" }
  ],
  "mechanical_validations": [
    { "id": "shape", "rule": "output is a ValidationResult[] matching io-contracts (wedge_ref, test, threshold, signal, pass)" }
  ]
}
```

## step-04 — Decide -> Decision
```json
{
  "contract_id": "assay:step-04:output",
  "artifact_type": "json",
  "canonical_reference": { "path": ".claude/docs/design/assay/references/io-contracts.md" },
  "soft_validation_rules": [
    { "id": "three-of-three", "rule": "green light ONLY when market AND build AND demand all pass; two-of-three = park" },
    { "id": "ranked", "rule": "shortlist ranked by speed-to-first-dollar x defensibility x reuse" },
    { "id": "precondition", "rule": "each shortlisted wedge names one precondition to clear first" },
    { "id": "no-act", "rule": "no action taken; the commit is left to the human (HITL)" }
  ],
  "mechanical_validations": [
    { "id": "shape", "rule": "output is a Decision matching io-contracts (idea_ref, shortlist[], committed_wedge?)" },
    { "id": "ledger", "rule": "the full run is appended to state/ledger.jsonl" }
  ]
}
```
