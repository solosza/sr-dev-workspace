# Step 03 — Determine authority

For each unit, decide the AUTHORITATIVE source of truth: the "correct corpus" that would confirm or
refute it. This is judgment, not a fixed list. Choosing wrong invalidates the check.

## Read first
- the scope contract's `authorities` map (starting points per unit type)
- the unit stubs from step 02

## Procedure
Ask, per unit: *what, in the world, would settle this?* Then name that source.

| Unit looks like | Authority |
|---|---|
| a citation (arXiv id, DOI, paper, URL) | the cited work itself — fetch it |
| a live fact (a number, a status, a claim about the world) | the live source of truth (site, registry, standard, dataset) |
| an in-repo path or `[[wikilink]]` | the repository tree (does it resolve); memory namespace = external |
| an internal decision (`decided`/`open`) with no external claim | `none` — a self-contained / consistency unit |

## Rules
- **Do not use your own training as the authority for a live fact.** Go to the live source.
- If you cannot determine an authority, or two plausible authorities conflict: that is a material
  ambiguity — ask (HITL) if the unit is load-bearing, else record it for `unresolved`.
- Self-contained units (an internal decision asserting nothing about the world) get authority `none`
  and are checked for internal consistency, not fetched.

## Output
Per unit: a concrete authority to check, or `none` (internal). Carry `weight` forward so the next step
spends effort in proportion.
