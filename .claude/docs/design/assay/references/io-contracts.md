# I/O Contracts — Typed objects (loops are pure functions: in -> out)

- **Idea** (Step 1 in): `{ source, raw, normalized: { value, who_pays, mechanism } }`
- **Wedge** (Step 1 out): `{ id, idea_ref, abstraction_rung, lens_origin, description, opening, gate_scores{}, rank }`
- **BuildVerdict** (Step 2 out): `{ wedge_ref, buildable, automatable_pct, hitl_line, moat_applies, compounds, build_cost, strategic_dividend, decision: build|pass, picks_and_shovels_variant? }`
- **ValidationResult** (Step 3 out): `{ wedge_ref, test, threshold, signal, pass: bool }`
- **Decision** (Step 4 out): `{ idea_ref, shortlist: [ { wedge_ref, market, build, demand, score, precondition } ], committed_wedge? }`

Each loop consumes the prior contract and emits the next — so `/build-command` can decompose and test each step independently. The full set is appended to the ledger per run ([[state-schema]]).
