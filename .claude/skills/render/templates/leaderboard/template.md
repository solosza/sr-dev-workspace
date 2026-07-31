# Leaderboard Template

Parent: [[../../SKILL.md]]. A generic, topic-agnostic **ranked list** in plain English. Each item shows: rank, name, a clear **Build / Test-first / Don't-build** recommendation, one plain sentence, a small "how close to your world" tag, and its **own question box** (ask about that idea; the answer appears right there). Readable-first, no jargon, no em dashes. The default format for any ranked idea list; the kanban `venture-board` is for tracking items across stages.

## Data Source

Any ranked list, shaped into one items JSON. Topic-agnostic (business ideas, tools, candidates, anything ranked):

```json
{ "title": "Best business ideas right now",
  "lead": "Ranked by how good the opportunity is.",
  "recLegend": [ {"label":"Build","tone":"c"}, {"label":"Test first","tone":"b"}, {"label":"Don't build","tone":"e"} ],
  "legend": { "label": "How close to your world:",
              "tags": [ {"label":"New for you","tone":"a"}, {"label":"Partly yours","tone":"b"}, {"label":"Your strength","tone":"c"} ] },
  "items": [ { "id":"cre", "rank":"1", "name":"Buy discounted real-estate loans",
               "rec": {"label":"Test first","tone":"b"},
               "desc":"one plain sentence",
               "tag": {"label":"New for you","tone":"a"} } ] }
```

### Per-item fields
| Field | Meaning |
|-------|---------|
| `id` | stable slug (the target routed on annotate) |
| `rank` | display rank ("1"); top 3 get the accent color |
| `name` | the idea in plain words |
| `rec` | the recommendation: `{label,tone}` — e.g. Build (c/green), Test first (b/amber), Don't build (e/red) |
| `desc` | one plain sentence |
| `tag` | how close to the operator's world: `{label,tone}` (a small chip, does not change the order) |

`tone` -> color: **a**=blue **b**=amber **c**=green **d**=grey **e**=red. `legend`/`recLegend` optional.

Each item also renders its **own question box** (input + Ask). The answer arrives on the status reply's `answers` array as `{ref, answer}` and fills in inline.

## Writing rules (operator)
- **Plain English, no jargon** in everything shown (not "fit / GO-IF / assay"). Translate idea names too. See memory `plain-vocabulary`.
- **No em dashes.** Periods, commas, colons, parentheses.
- **Give a clear recommendation** on each: Build / Test first / Don't build. The rank is the opportunity strength; the tag is fit; the rec is the call.

## Action Map
| action | routes to |
|--------|-----------|
| ask | the session answers the question (raw_words = the question); answer returns on the reply's `answers[]` keyed by `ref` |

## Page Requirements
1. Self-contained (inline CSS/JS, no external hosts), dark/light aware, no em dashes.
2. One item per row: big rank, name + a recommendation badge, one-line desc, a small fit tag, and a per-item question box.
3. `GET /status` polling: fill each pending answer by its `ref`.
4. Frozen POST to `/annotate`: `{ "target":"<id>", "action":"ask", "raw_words":"<question>", "ref":"<qid>", "at":"<ISO>" }`.
