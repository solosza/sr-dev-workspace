# Step 03 — Match candidates

Score how well each surveyed capability serves the need. Match on PURPOSE and shape, not name.

## Read first
- the need + the survey (step 02)

## Fit rubric
| fit | meaning |
|-----|---------|
| `exact` | does the job as-is (at most a different input) |
| `adaptable` | does the job with a declared delta — usually a new/edited contract, or a small change |
| `none` | wrong shape; "adapting" it would be a rewrite |

## Procedure
1. For each candidate, compare its `purpose` + output shape to the need. Assign `exact` / `adaptable` / `none`.
2. For `adaptable`, note the `delta` — what would change. The most common delta is **"add a `<scope>`
   contract"**: the same capability shell serving a new scope is `adaptable`, not a new build.
3. Rank candidates best-fit first.

## Guard against false "none"
Before marking everything `none`, ask: is the need really a new *shell*, or a new *contract* for an
existing shell? A different unit type, output shape, or domain is usually a contract, i.e. `adaptable`.

## Output
Candidates `{capability, fit, note}`, best fit first.
