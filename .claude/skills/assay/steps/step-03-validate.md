# Step 3: Validate

## Purpose

Pick the single cheapest real-world signal that would CHANGE the decision for each build-viable wedge, with the pass threshold set up front. Assay proposes the test and threshold; it never runs spend or outreach itself.

## Input

- Build-viable wedges from Step 2 (`decision == build`)
- Canonical reference: `.claude/docs/design/assay/references/io-contracts.md` (ValidationResult)
- Contract: `contracts/step-03-contract.json`

## Output

- `ValidationResult[]` — one per build-viable wedge: `{ wedge_ref, test, threshold, signal, pass }`.

## Acceptance Criteria

- [ ] One `ValidationResult` per build-viable wedge
- [ ] The chosen test is the cheapest signal that would actually change the decision
- [ ] The pass threshold is defined BEFORE any signal is recorded (no post-hoc goalposts)
- [ ] The test is time- and cost-boxed
- [ ] output shape matches io-contracts

## References

- [[../references/INDEX]] -> design doc `references/io-contracts.md`

## Procedure

1. For each build-viable wedge, pick the single cheapest test that would change the decision: landing page + small ad spend (demand) / N cold outreaches (B2B interest) / one manual concierge delivery (will they actually pay).
2. Define the pass threshold up front (X signups / Y replies / 1 paying pilot) and time- + cost-box it.
3. v1: propose the test + threshold; the operator may run it. Record `signal` + `pass` (pass = signal met the pre-set threshold; below -> kill).

## Verification

- Output validates against `contracts/step-03-contract.json` (shape + threshold-first + cheapest + boxed rules)
- Every threshold is present and was set before its signal

## Failure Recovery

- If no signal has been gathered yet (v1 typical), record `signal: null, pass: null` with the proposed test + threshold intact — the operator runs it, then the result is re-recorded.
- If a proposed test can't change the decision, replace it with one that can before recording.
