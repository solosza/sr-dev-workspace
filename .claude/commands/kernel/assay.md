# /assay

Take any idea and surface the revenue streams the operator can *actually capture* — an adversarial, kill-by-default, self-sharpening research engine. Idea = ore; assay it for value + extractability; output = the lode (a ranked, build-verified, demand-tested shortlist) or a fast kill.

## Usage

```
/assay <idea>
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `<idea>` | The raw idea to assay — mine, or pulled from anywhere on the internet | `/assay AI-generated real-estate listing videos` |

## What It Does

Runs the triggered core (v1): one idea in -> **Opportunity** (normalize, climb the abstraction ladder, diverge across 6 lenses, then kill by default through an adversarial gate battery) -> **Buildability** (can WE build + automate + govern it with an edge, reusing the existing stack) -> **Validate** (the single cheapest test that would change the decision, threshold set up front) -> **Decide** (intersect market x build x demand; only all-three green-lights). It hands back a ranked shortlist with per-wedge preconditions and logs the full run to an append-only ledger. Assay never acts — the only HITL is the terminal human commit at Decide.

## Examples

```
/assay surplus-funds recovery service
  -> normalizes -> diverges (adjacent/transpose/recombine/invert/constraint-break/zoom)
  -> gates kill-by-default -> Wedge[] -> BuildVerdict[] -> ValidationResult[]
  -> Decision: ranked shortlist + preconditions (human picks what to pursue)

/assay YouTube nursery-rhyme channels
  -> may return an explicit empty shortlist (a valid "fast kill") with logged kill-reasons
```

## Design Reference

-> `.claude/docs/design/assay/index.md`

## Skill Reference

-> `.claude/skills/assay/`
