---
name: operate
description: Post-GO loop, the kernel's home turf. Run the live business, HITL-governed (every step proposes, a human approves). Govern-by-default, not kill-by-default. Lean output, every cycle saved.
---

# Operate / Run Loop

**Purpose:** For a live business, answer *"how do I run this repeatably, with a human in control of every real decision?"*
**Runs after** `/launch` (it's live); loops continuously.
**Philosophy:** govern-by-default — the kernel's core. Every automated step PROPOSES; a human APPROVES. No auto-act on a real (money/clinical/customer) decision, ever. The user decides; the loop runs the machine + surfaces decisions.

## Cross-cutting rules
- **LEAN OUTPUT.** A run-state view, never a long doc. See [[loop-output-lean]].
- **Standalone & modular.** Runs alone on any live business, OR as a sub-step called by another loop. If an input an upstream loop would normally supply is missing, gather it or ask — never require the upstream loop to have run first. Returns its run-state cleanly so a caller can consume it.
- **HITL is MANDATORY wherever a human decision applies.** Auto-*prepare* is fine; auto-*act on a decision* is banned. Gated outputs + human-review checkpoints + an audit ledger — this is what the kernel is for.
- **Govern-by-default** (not kill): the business is running; the loop's job is control + visibility, not a go/no-go.
- **Every cycle logged** to the audit ledger (append-only) — the decision trail.

## Steps

| # | Step | Do |
|---|------|-----|
| 0 | State | Read the operate ledger; show current run-state (what's pending, what's live, last cycle). |
| 1 | The operation | Define/confirm the repeating loop (e.g. fulfill -> deliver -> bill; or produce -> publish -> monetize). |
| 2 | HITL checkpoints | Per step: what the machine PROPOSES + what the human APPROVES. The approval gates. |
| 3 | Metrics | The few numbers to watch (revenue, throughput, quality, churn) + thresholds that trigger attention. |
| 4 | Exceptions | Failure/exception handling: what pauses, what escalates to the human. |
| 5 | Cadence | How often the loop runs + when the human is asked to approve. |
| 6 | Improve | One continuous-improvement hook: what to feed back (to `/sharpen` or the offer/GTM loops). |

## HITL (continuous, not one-shot)
This loop's whole point is the approval gates. Present each proposed action + wait for `approve` / `edit` / `hold` before anything real happens. Nothing acts without a human yes.

## Output (lean)
1. **Run-state** — one line (what's live, what's pending your approval).
2. **Pending decisions** — a short list, each: proposed action + the approve/edit/hold ask.
3. **Metrics** — the 3-5 numbers + any threshold tripped.
4. **One line:** what needs your call now.

Tables/bullets over prose. No essay.

## Persist (compact, mandatory)
- **Run-state report** -> `projects/assay/operate/runs/<slug>.md` (the LIVE state — this one updates in place per cycle; keep it short).
- **Audit ledger** -> `.claude/skills/operate/state/ledger.jsonl` — append one line per cycle/decision (ts, proposed, approved_by_human, outcome). The decision trail — append-only, never mutate.
- **Venture record** -> `projects/assay/ventures/<slug>.md` — set Stage = Operating + refresh Next-action + ventures INDEX.
UTF-8, no BOM.

## Chain
`/launch` (shipped) -> **`/operate` (run it, governed)** -> feeds `/sharpen` (outcomes) + back to `/offer`//`/gtm` when the business shifts.
