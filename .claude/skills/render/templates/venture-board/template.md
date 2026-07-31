# Venture Board Template

Parent: [[../../SKILL.md]]. Spec for venture-board page generation. Renders venture-loop ideas as **pipeline stage-columns** (kanban) with a **summary funnel** on top and **verdict cards** — the format for every venture-loop output (source drops, assay verdicts, the venture dashboard).

## Data Source

Any venture-loop artifact, shaped into one items JSON by the caller (the loop or the session):

```json
{ "title": "...", "subtitle": "...",
  "funnel":  [ {"label":"sourced","value":6}, {"label":"surviving","value":4}, {"label":"killed","value":3}, {"label":"ventures","value":2} ],
  "columns": ["Ideas","Assayed","Competition","Deep-Dive","GO","Killed"],
  "cards":   [ {"id":"...", "column":"Assayed", "verdict":"GO-IF", "fit":"high",
               "title":"...", "signals":["trends","assets"], "summary":"...", "take":"/competition"} ] }
```

Sources: a `/source` drop (cards = ideas), a loop's ledger, or the venture records in `projects/assay/ventures/` (cards = ventures, `column` = current Stage).

### Per-card fields
| Field | Meaning |
|-------|---------|
| `id` | stable slug (the target routed on annotate) |
| `column` | pipeline stage bucket (must be one of `columns`) |
| `verdict` | GO / GO-IF / KILL / PARK / - → colored pill |
| `fit` | high / cond / low → colored chip (match to the operator's assets) |
| `signals` | which hunters/lenses/gates flagged it → chips |
| `summary` | one-line what-it-is |
| `take` | the next move (rendered as "Next: …") |

## Action Map
| action | destructive | routes to |
|--------|------------|-----------|
| ok (Take deeper) | no | session runs the card's next loop (`take` — e.g. `/competition`, `/deep-dive`) on that idea |
| hold | no | park it (a note on the venture record; no pipeline advance) |
| redirect | no | `raw_words` steers it — session re-seeds / adjusts (may route to `/assay` with the note, or `/kernel/backlog`) |
| submit (`__session__`) | no | board-wide general-comments `raw_words` → session-wide input |

Routing is session-side (the primitive only transports). `raw_words` reach the routed kernel command verbatim.

## Page Requirements
1. **Self-contained** — inline CSS/JS, zero external hosts.
2. **Funnel on top** — the summary stats are the biggest element (visual hierarchy → overview-to-action).
3. **Stage columns** — a horizontal-scroll `.board` of `.col`s, one per `columns` entry, each with a count; cards grouped by `column`. Wide content scrolls in its own container.
4. **Verdict cards** — pill + fit/signal chips + summary + `Next:` + a per-card note textarea + OK/Hold/Redirect buttons.
5. **Legend (MANDATORY)** — pill meanings + what OK/Hold/Redirect do + the fit definition. (operator convention — every board carries a legend).
6. **General-comments** field above the send bar; on submit it rides the `__session__` annotation's `raw_words`.
7. **Frozen POST schema** — `{ "target": "<id|__session__>", "action": "<ok|hold|redirect|submit>", "raw_words": <note|null>, "at": "<ISO>" }` to `/annotate`; `GET /status` polling for results.

## Annotation Schema
```json
{ "target": "assumable-leaseback", "action": "ok", "raw_words": "focus on assumable supply first", "at": "2026-07-31T04:00:00Z" }
```
→ [[../../../docs/design/render/references/annotation-contract.md]] (law)
