# I/O Contracts — Typed objects (loops are pure functions: in -> out)

- **Idea** (Step 1 in): `{ source, raw, normalized: { value, who_pays, mechanism } }`
- **Wedge** (Step 1 out): `{ id, idea_ref, abstraction_rung, lens_origin, description, opening, status: survived|killed, kill_reason?, gate_scores{}, rank }`
  - Step 1 emits the **FULL candidate set** — every idea generated, survivors AND killed — not just survivors. Killed wedges carry `status:"killed"` + a plain-language `kill_reason`. Downstream steps only *process* survivors, but the complete list is preserved for the report + ledger (content fodder; nothing generated is ever discarded).
- **BuildVerdict** (Step 2 out): `{ wedge_ref, buildable, automatable_pct, hitl_line, moat_applies, compounds, build_cost, strategic_dividend, decision: build|pass, picks_and_shovels_variant? }`
- **ValidationResult** (Step 3 out): `{ wedge_ref, test, threshold, signal, pass: bool }`
- **Decision** (Step 4 out): `{ idea_ref, shortlist: [ { wedge_ref, market, build, demand, score, precondition } ], committed_wedge? }`

Each loop consumes the prior contract and emits the next — so `/build-command` can decompose and test each step independently. The full set is appended to the ledger per run ([[state-schema]]).
