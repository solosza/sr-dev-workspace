---
name: source
description: Front-of-pipeline DISPATCHER. Give it a seed (theme/space); it runs 6 idea-hunters, cross-references for the strongest ideas, and auto-feeds the top into /assay. Lean output, saved. Runs on demand or weekly.
---

# Source Dispatcher (idea-provision pipeline)

**Purpose:** *"You give a seed; the loop takes it from there."* From one seed theme/space, produce a ranked queue of business ideas and start assaying the best — the proactive front-end that feeds the whole pipeline.
**Dispatches:** the 6 hunters — `/trends` · `/pain` · `/arbitrage` · `/assets` · `/gaps` · `/bookmarks`.
**Feeds:** `/assay` (auto-runs the top idea(s)).

## Cross-cutting rules
- **LEAN OUTPUT** ([[loop-output-lean]]). A ranked queue, never a long doc.
- **Standalone & modular.** Runs alone, OR called by another loop that needs fresh candidates.
- **Dedup against history** — drop ideas already in the assay ledger (match on meaning).
- **Every run saved** (see Persist).

## Input modes
- **Seeded (primary):** `/source <seed>` — a theme/space (e.g. "AI for local services", "boring businesses", "healthcare admin"). The hunters explore *from* the seed.
- **Ambient (the weekly drop):** `/source` with no seed — a broad scan across the operator's standing interests for anything new.

## Steps
| # | Step | Do |
|---|------|-----|
| 1 | Dispatch | Run the 6 hunters on the seed (each returns candidate ideas its own way). Run the fitting ones; a narrow seed may skip some. |
| 2 | Cross-reference | THE quality step: find ideas that hit **multiple** signals — **pain × why-now × fit-to-you**. An idea surfaced by 2-3 hunters (real demand + a catalyst + your moat) beats one from a single hunter. |
| 3 | Dedup | Drop anything already in the assay ledger (by meaning). |
| 4 | Rank | By how many signals it hits × strength. Top of the queue = multi-signal ideas. |
| 5 | Hand off / auto-run | Present the ranked queue AND auto-run the **top 1-3** through `/assay` (the loop takes it from there). Assay's own kill-by-default + HITL apply downstream. |

## Output (lean)
1. **The idea drop** — a short ranked table (idea · which hunters flagged it · why-now).
2. **Auto-assayed** — the top 1-3, each with `/assay`'s one-line verdict.
3. **Dropped as already-explored** (one line).
4. **One line:** take which deeper (`/competition` → `/deep-dive`)?

Tables over prose. No essay.

## Persist (compact, mandatory)
- **Report** -> `projects/assay/source/runs/<YYYY-MM-DD>-<seed-or-ambient>.md` — the idea drop + verdicts.
- **Ledger** -> `.claude/skills/source/state/ledger.jsonl` — one line (ts, seed, hunters_run, candidates, multi_signal[], auto_assayed[], report path).
UTF-8, no BOM.

## Cadence
Runs **on demand** (any seed, anytime — the main mode early on) AND on a **weekly schedule** (ambient drop). `/sharpen`'s learnings feed the hunters (what wins → hunt more of it; anti-library → "everyone dies on X" becomes a hunt target).

## Chain
**`/source` (idea drop)** -> `/assay` (which is worth it) -> `/competition` -> `/deep-dive` -> [GO] -> `/offer`... The front of the whole engine.
