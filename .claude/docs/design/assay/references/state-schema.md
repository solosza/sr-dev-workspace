# State & Persistence

## v1 — Ledger (append-only)
`.claude/skills/assay/state/ledger.jsonl` — one record per `/assay` run:

```json
{ "ts": "...", "idea": {...}, "wedges": [...], "build_verdicts": [...],
  "validations": [...], "decision": {...}, "committed_wedge": null }
```

The audit trail, and the substrate v2's self-sharpening consumes. Append-only, git-friendly.

## v2 — Self-sharpening stores (roadmap, not built in v1)
- **outcomes** — ground-truth attached to past decisions later (go -> revenue? kill -> won elsewhere?) for gate calibration.
- **anti-library** — structured kill-reasons: reason -> count -> "everyone dies on X" flag (which surfaces X as an opening).
- **world-model** — saturation / tools / reg snapshots per domain + freshness timestamps (Source/Scan refreshes them).
- **registry** — versioned gates + lenses; Learn/Meta evolves them (missed opening -> add a lens; flopped go -> tighten a gate).

v1 writes only the ledger. Because the ledger already records every verdict + decision, v2 can be added without changing the Loop 1-4 contracts.
