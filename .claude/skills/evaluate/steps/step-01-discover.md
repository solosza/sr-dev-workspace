# Step 01 — Discover (invokes the discover primitive)

Do not re-implement discovery here. **Invoke the shared `discover` primitive**
(`.claude/skills/discover/`), then proceed from what it returns.

## Invoke
```
/discover <need> --goal "where capabilities for this need live"
```

## What you pass
- the raw need (the caller's request)
- goal: characterize the need (kind, scope, inputs/outputs) and locate the **search-locations** where
  candidate capabilities for a need of this kind would live — the kernel skills, a client repo, a domain
  repo, a registry, etc. Do NOT assume the kernel skills.

## What you get back
A discovery: `{ kind, scope, target: [search-locations], ambiguities[] }`. The primitive handles
ambiguity-triggered HITL (e.g. "is this a command capability or a domain capability?").

## Then
- Hand the `search-locations` to the survey (step 02); it enumerates exactly those.
