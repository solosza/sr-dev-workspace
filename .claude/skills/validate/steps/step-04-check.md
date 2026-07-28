# Step 04 — Check reality

Reach the authority and see what it actually says. Never assume. If you did not check it, it is
`unresolved` — confidence is not a verdict.

## Read first
- the unit + its authority (from step 03)
- the scope contract's `rules` (which are `hard` vs `soft`)

## Method per authority
| Authority | Tool + method |
|---|---|
| a paper / URL / DOI | WebFetch the page. Confirm it exists AND read enough to see if it supports the *specific* claim. |
| an arXiv id | Fetch `arxiv.org/abs/<id>`. Confirm the id resolves and the title/abstract matches what is cited. |
| an in-repo path | Resolve it (Read / Glob). Exists = ok, missing = finding. |
| a `[[wikilink]]` | Resolve against the repo. If it exists only in the memory namespace, it is EXTERNAL (note it), not resolved-in-repo. |
| a live fact | WebFetch / search the authoritative source; capture the value or statement found. |
| `none` (internal) | No fetch. Check the unit against the rest of the corpus for contradiction. |

## Spend proportionally
- `load-bearing` + external → full fetch-and-read.
- `incidental` or internal → light check.
Do not web-search an internal `decided` claim; do not cheap-check a load-bearing citation.

## Capture (for every unit)
- `authority` — exactly what you checked (the resolved link / source / `internal`)
- `evidence` — what it said: a short quote, the value, the resolved status, or the contradiction found

Unreachable → carry `unresolved`. Reachable but does not support the claim → carry `unsupported`.
