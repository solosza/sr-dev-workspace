# Gate Contract

## Phase Gates

| Gate | Trigger | Check | On Fail |
|------|---------|-------|---------|
| Phase 1 -> 2 | After Step 1 | `Wedge[]` emitted (empty allowed). Every survivor cleared the gate battery kill-by-default; uncertain gates killed or flagged, never silent-passed. | Re-run Step 1; if diverge skipped or a gate silent-passed, redo |
| Phase 2 -> 3 | After Step 2 | One `BuildVerdict` per input wedge; each `decision` in {build, pass}; buildable scored reuse-first; picks-and-shovels flagged for 1-hop re-entry | Re-run Step 2 for the missing/malformed verdicts |
| Phase 3 -> 4 | After Step 3 | One `ValidationResult` per build-viable wedge; threshold set BEFORE the signal; test is cheapest + boxed | Re-run Step 3; reject any post-hoc goalpost |
| Phase 4 done | After Step 4 | Green light only when market AND build AND demand pass (two-of-three = park); shortlist ranked; full run appended to ledger; HITL commit presented | Re-run Step 4; block if ledger append missing |

## Step Gates

| Step | Output | Validation |
|------|--------|-----------|
| 1 | `Wedge[]` | Shape matches io-contracts (id, idea_ref, abstraction_rung, lens_origin, description, opening, gate_scores, rank). Empty array is valid + explicit. All 6 lenses applied before gating. |
| 2 | `BuildVerdict[]` | One per input Wedge. Shape matches io-contracts. `decision` in {build, pass}. HITL line stated per verdict. moat_applies honest (false when governance adds nothing). |
| 3 | `ValidationResult[]` | One per build-viable wedge. Shape matches io-contracts (wedge_ref, test, threshold, signal, pass). Threshold pre-set; test cheapest + time/cost-boxed. |
| 4 | `Decision` + ledger append | Shape matches io-contracts (idea_ref, shortlist[], committed_wedge?). Three-of-three rule enforced. Ranked by speed x defensibility x reuse. Each shortlisted wedge names one precondition. Full run appended to `state/ledger.jsonl`. No action taken. |
