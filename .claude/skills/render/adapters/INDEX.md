# Render Adapters — Index

Parent: [[../SKILL.md]]. Adapters convert a venture loop's decide/output into a template's data model, so a loop never hand-translates its result into a board.

## loop_to_leaderboard.py

Converts a loop output into the `leaderboard` template's items.json.

`to_items(loop_output, title, lead) -> dict`

- **Input** `loop_output`: `{"items": [ {name, desc|description, rec|recommendation, fit, merit?} ]}` (a bare list is also accepted). `merit` (or score/rank_signal/strength) drives order; missing merit falls back to input order.
- **Output**: `{title, lead, recLegend, legend, items:[{id, rank, name, desc, rec:{label,tone}, tag:{label,tone}}]}` — exactly what [[../templates/leaderboard/generate.py]] consumes. See [[../templates/leaderboard/template.md]].

### Three rules baked in (callers never re-apply them)
1. **Plain vocabulary** — internal jargon (wedge, assay, GO-IF, kill, hunter, payer-swap, transpose, merit, fit-to-me) is translated to plain English in every shown string.
2. **Rank on merit only** — order comes from the merit signal. Fit is a displayed tag and NEVER changes the order.
3. **No em dashes** — em/en dashes are removed from every produced string.

### Mapping
- rec: Build→(Build, c), Test first / GO-IF→(Test first, b), Don't build / kill / skip→(Don't build, e).
- fit: high→(Your strength, c), partly/cond/medium→(Partly yours, b), low/new/none→(New for you, a).

Used by the shared render step: [[../steps/step-serve-and-watch]].
