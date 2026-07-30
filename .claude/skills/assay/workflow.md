# Workflow

Triggered pipeline (v1): `Idea -> Step 1 (normalize -> PRIOR-ART CHECK -> diverge -> gate) -> (per surviving wedge) Step 2 -> (per build-viable) Step 3 -> Step 4 Decide (-> PERSIST the run)`. Sequential and autonomous. Loop 2's picks-and-shovels variant re-enters Step 1's diverge, bounded to **1 hop**. Ambient loops (Source/Scan, Learn/Meta) are v2 roadmap; the prior-art check is the first, cheapest slice of the Learn loop pulled forward — v1 lays the ledger the rest will consume.

## Phases

### Phase 1: Opportunity
- Steps: 1
- Gate: `Wedge[]` emitted (possibly empty = "no opening found", which is valid). Every survivor cleared the adversarial gate battery kill-by-default.

### Phase 2: Buildability
- Steps: 2
- Gate: one `BuildVerdict` per input `Wedge`, each with a `decision` in {build, pass}. Any picks-and-shovels variant is flagged for 1-hop re-entry.

### Phase 3: Validate
- Steps: 3
- Gate: one `ValidationResult` per build-viable wedge, each with a pre-set threshold defined before any signal.

### Phase 4: Decide
- Steps: 4
- Gate: green light only when market AND build AND demand all pass. Ranked shortlist emitted, full run appended to the ledger.
- HITL: **the human picks which wedge (if any) to pursue** — the only real-world commit.

## Step Checkpoints

### Step 1: Opportunity
**Pre-generation checkpoint:**
- Read canonical reference: `.claude/docs/design/assay/references/io-contracts.md` (Idea in, Wedge out)
- Read `.claude/docs/design/assay/references/lenses.md` (the 6 divergence lenses)
- Read `.claude/docs/design/assay/references/gates.md` (the adversarial gate battery)
- Read contract: `contracts/step-01-contract.json`
- Input: the raw `<idea>` argument

**How agent uses the reference:**
1. Reads io-contracts -- sees the exact Idea/Wedge shape
2. Reads lenses + gates -- knows how to diverge then kill
3. Emits `Wedge[]` matching the contract, empty array allowed

### Step 2: Buildability
**Pre-generation checkpoint:**
- Read canonical reference: `.claude/docs/design/assay/references/io-contracts.md` (Wedge in, BuildVerdict out)
- Read contract: `contracts/step-02-contract.json`
- Input: Step 1's `Wedge[]`

**How agent uses the reference:**
1. Reads io-contracts -- sees the BuildVerdict shape
2. Scores each wedge (buildable / automatable_pct / hitl_line / moat_applies / compounds / build_cost / strategic_dividend)
3. Emits one `BuildVerdict` per wedge; picks-and-shovels variants flagged for 1-hop re-entry

### Step 3: Validate
**Pre-generation checkpoint:**
- Read canonical reference: `.claude/docs/design/assay/references/io-contracts.md` (ValidationResult)
- Read contract: `contracts/step-03-contract.json`
- Input: build-viable wedges from Step 2 (`decision == build`)

**How agent uses the reference:**
1. Reads io-contracts -- sees the ValidationResult shape
2. Picks the single cheapest decision-changing test + a pre-set, boxed threshold
3. Emits one `ValidationResult` per build-viable wedge

### Step 4: Decide
**Pre-generation checkpoint:**
- Read canonical reference: `.claude/docs/design/assay/references/io-contracts.md` (Decision)
- Read `.claude/docs/design/assay/references/state-schema.md` (the ledger record shape)
- Read contract: `contracts/step-04-contract.json`
- Input: Step 1 `Wedge[]` + Step 2 `BuildVerdict[]` + Step 3 `ValidationResult[]`

**How agent uses the reference:**
1. Intersects market x build x demand (all three required for green light)
2. Ranks green-lit wedges by speed-to-first-dollar x defensibility x reuse
3. Appends the full run to `state/ledger.jsonl`, then presents the shortlist for the HITL commit

## State Persistence

Every run is saved in **three** places (Step 4 persists all three before presenting):

| Layer | Location | For |
|-------|----------|-----|
| Readable report | `projects/assay/runs/<date>-<slug>.md` (re-runs get `-2`, `-3`) | Humans — the plain-language writeup you re-read later. Git-tracked. |
| Ledger (machine) | `.claude/skills/assay/state/ledger.jsonl` (append-only, one record/run) | The audit trail + the prior-art memory Step 1 reads + the v2 Learn-loop substrate |
| Index | `projects/assay/runs/INDEX.md` (one row/run) | One-glance scan of everything ever assayed |

Working/resume state for the build itself lives at `.claude/state/build-command-state.json` during scaffolding only.

```json
{
  "ts": "...", "idea": {}, "wedges": [], "build_verdicts": [],
  "validations": [], "decision": {}, "committed_wedge": null
}
```

The ledger is the audit trail and the substrate v2's self-sharpening (outcomes, anti-library, world-model, registry) will consume. No run mutates a prior record — append only.

## HITL Stops

| After Step | Why | User Options |
|-----------|-----|-------------|
| 1 (Prior-art hit) | This idea (by meaning) was already assayed. Don't silently re-spend a full run or silently skip. | `(a) show prior result` / `(b) re-run fresh` / `(c) re-run, focus on what changed` |
| 4 (Decide) | Terminal commit — which validated wedge (if any) to actually pursue is a real-world spend decision Assay must not make. Any ambiguous gate from Steps 1-3 also surfaces here. | `commit <wedge>` / `park` / `kill-all` |

## Cross-Cutting Rules

- **Never acts.** Assay produces verdicts only; downstream build/operate carries the kernel's mandatory HITL.
- **Kill-by-default.** Uncertain gates kill or escalate — never silent-pass.
- **1-hop re-entry.** A picks-and-shovels variant re-enters Step 1 once; no infinite loops.
- **Prior-art first.** Before diverging, check the ledger for an equivalent past idea (match on meaning); surface a hit and let the human choose — never silently re-run or skip.
- **Every run persisted, three ways.** No run finishes until it is saved: a plain-language report in `projects/assay/runs/`, an appended ledger line (`state/ledger.jsonl`), and an index row. The report is for humans; the ledger is the machine index + the prior-art memory; re-runs never overwrite prior reports.
