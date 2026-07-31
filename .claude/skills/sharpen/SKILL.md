---
name: sharpen
description: Meta/learn loop. Read outcomes across the loops, find the misses, propose concrete engine upgrades (new lens/gate/threshold). Automates the manual tuning. Lean output, every run saved.
---

# Sharpen / Learn Loop

**Purpose:** Answer *"where were the loops wrong, how do we make them better, and what loops are we missing?"* — the meta-loop that turns outcomes into engine upgrades AND promotes recurring captured gaps into brand-new loops (the family self-extends).
**Reads** every loop's ledger + the venture records; **improves** the loops themselves.
**Philosophy:** evidence-driven self-improvement. Compare what the loops PREDICTED to what actually HAPPENED; every miss is a lesson the engine should encode. This automates the manual v2 tuning (adding the payer-swap lens, the reachability gate) that was done by hand.

## Cross-cutting rules
- **LEAN OUTPUT.** The misses + the proposed upgrades, never a long doc. See [[loop-output-lean]].
- **Standalone & modular.** Runs alone (scan all loops), OR scoped to one loop when called as a sub-step. Returns its proposed upgrades cleanly so a caller can consume them.
- **Never acts on its own.** Proposes engine changes; a human approves before any skill file is edited (loops are protected system state).
- **Evidence over opinion.** An upgrade needs a real miss behind it, not a hunch.
- **Every run saved** (see Persist).

## Steps

| # | Step | Do |
|---|------|-----|
| 1 | Gather | Read the ledgers (every loop's `state/ledger.jsonl`) + venture records + their outcomes + the **loop-candidates register** `projects/assay/loop-candidates.jsonl` (angles/loops the loops flagged as missing). |
| 2 | Compare | Predicted vs actual: killed ideas that would've worked, GOs that flopped, "moats" that turned out copyable, thresholds that were wrong. |
| 3 | Pattern | Extract the recurring failure/blind-spot behind the misses. |
| 4 | Propose | Two kinds: (a) an **engine upgrade** per pattern — a new lens, gate, threshold, quota, wording fix (name the exact file + change); (b) a **NEW LOOP** — when the loop-candidates register shows the same missing angle/loop flagged **>=2 times** (recurrence = it's real, not a one-off), propose scaffolding it from the loop template (a new `/<name>` command + compact skill). This is how the family self-extends. |
| 5 | Apply-or-queue | On human approval, apply the upgrade / scaffold the new loop; else queue it. Log it (and clear promoted candidates from the register). |

## HITL (the one stop)
After Step 4, present the misses + proposed upgrades. User: `apply <upgrade>` / `queue` / `skip`. Skill files change only on approval.

## Output (lean)
1. **The misses** — a short list (what the loop said vs what happened).
2. **Proposed upgrades** — each: the pattern -> the exact change (file + rule).
3. **One line:** apply / queue / skip.

Table over prose. No essay.

## Persist (compact, mandatory)
- **Report** -> `projects/assay/sharpen/runs/<YYYY-MM-DD>.md` — the misses + upgrades.
- **Ledger** -> `.claude/skills/sharpen/state/ledger.jsonl` — one JSON line (ts, misses[], upgrades[], applied[], report path).
UTF-8, no BOM.

## Chain
Reads all loops -> **`/sharpen` (find misses, upgrade engines)** -> the loops get better each cycle. The compounding meta-loop.
