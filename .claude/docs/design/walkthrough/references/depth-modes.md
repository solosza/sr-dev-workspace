# Depth Modes — Plain vs Terse

Parent: [[../index.md]]

Same loop, same grounding, same ledger — the dial changes only how much teaching the explanation carries. Familiarity varies by topic, not by session, so the dial must move mid-loop.

## The Two Modes

| Aspect | `plain` (default) | `terse` |
|--------|-------------------|---------|
| Format parts rendered | All seven | 4 (grounding) → 5 (recommendation) → 7 (settle) |
| Assumes | No domain familiarity | User knows the mechanics; wants analysis + judgment |
| Teaching (purpose, flow, why, metaphor) | Full | Dropped |
| Grounding + recommendation + settle prompt | Full | Full — never compressed away |
| Typical length | Screens | A paragraph or two |

**Invariant:** grounding, recommendation, and the settle prompt survive every depth. Depth only ever removes teaching, never analysis — a terse section still cites the user's real files and still ends with a decision.

## Setting and Moving the Dial

| Trigger | Effect |
|---------|--------|
| (default) | `plain` |
| `--terse` at invocation | Loop starts terse |
| "terse from here" mid-loop | `depth: terse` for remaining sections |
| "slow down" / "explain this one properly" | This section re-rendered plain; dial position for the NEXT section unchanged unless the user says so |
| "plain from here" | Back to plain for remaining sections |

Depth lives in the state file next to the cursor, so it survives resume. Per-section overrides are transient (not persisted) — only "from here" statements move the stored dial.

## One-Shot Depth

One-shot mode defaults to `plain` (its typical use is "explain this to me"). `--terse --once` is valid for a quick grounded recommendation on a single point.
