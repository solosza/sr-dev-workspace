# Step 01 — Discover (invokes the discover primitive)

Do not re-implement discovery here. **Invoke the shared `discover` primitive**
(`.claude/skills/discover/`), then proceed from what it returns.

## Invoke
```
/discover <artifact> --goal "scope + contract + authorities for this artifact"
```

## What you pass
- the artifact (a first pass is enough to characterize it)
- goal: determine the **scope** (doc / code / command / ...), the **contract** (`contracts/<scope>.json`),
  and where the **authorities** for its claims live.

## What you get back
A discovery: `{ kind, target: { scope, contract, authority-map }, ambiguities[] }`. The primitive handles
ambiguity-triggered HITL (e.g. "is this a doc or a spec?").

## Then
- Load `contracts/<scope>.json` from the discovery and continue to unitize (step 02).
- If the discovery says **no contract fits** the kind, that is a finding — report it; do not force a
  wrong scope.
