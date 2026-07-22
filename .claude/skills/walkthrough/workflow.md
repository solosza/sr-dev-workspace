# Walkthrough — Workflow

## Phases

### Phase 1: Setup (Steps 1–3)
- Steps: Resolve Input, Ground, Decompose
- Gate: state file initialized with user-approved section map + non-empty sources_read
- HITL: Step 1 only if input is ambiguous; **Step 3 — user approves section map**
- One-shot path: Step 1 → Step 2 → Step 4, then stop. No state, no ledger.

### Phase 2: Loop (Steps 4–6, repeated)
- Steps: Explain, Settle, Record — once per section
- Gate: per iteration — exactly one section rendered, decision recorded before cursor advance
- HITL: **every iteration** — Step 5 blocks on the user by contract

### Phase 3: Exit (Step 7)
- Steps: Exit
- Gate: durable ledger file written, state marked complete
- HITL: user chooses handoff (feed /design, fold into doc, stop)

## Loop Shape

```
1 Resolve → 2 Ground → 3 Decompose (map approved)
                            ↓
                 ┌── 4 Explain ──┐
                 │       ↓       │   repeat until cursor
                 │   5 Settle    │   == len(sections),
                 │       ↓       │   deferred revisited
                 └── 6 Record ───┘
                            ↓
                        7 Exit
```

## State Persistence

**Location:** `.claude/state/walkthrough-state.json`

```json
{
  "artifact": "conftest design",
  "input_type": "concept",
  "mode": "loop",
  "depth": "plain",
  "sections": ["bootstrap", "cli-options", "..."],
  "cursor": 3,
  "ledger": [
    {"section": "bootstrap", "settled": "...", "notes": "", "timestamp": "..."}
  ],
  "sources_read": ["platform-selenium/tests/conftest.py"],
  "ledger_file": null,
  "status": "active",
  "last_updated": "..."
}
```

**Resume:** "continue" (or `/walkthrough` on the same artifact) with `status: active` → read state → announce position ("section 4 of 9: credentials") → Step 4 at `sections[cursor]`. Depth and ledger survive. New artifact while one is active → ask before overwriting state.

**Cleanup:** `status: complete` + `ledger_file` set at exit. State is overwritten by the next walkthrough only after explicit confirmation if still active.

## HITL Stops

| Step | Why | User Options |
|------|-----|-------------|
| 1 | Only if artifact ambiguous | clarify |
| 3 | Section map approval before loop starts | approve / reorder / add / remove |
| 5 | Every iteration — the loop IS the conversation | settle / discuss / dial depth / defer / park |
| 7 | Ledger handoff | feed /design / fold into doc / stop |

## Step Checkpoints

### Step 1: Resolve Input
Reads only (no artifact output). Dependencies: `.claude/state/walkthrough-state.json` (resume check FIRST), the argument string.

### Step 2: Ground

**Pre-generation checkpoint:**
- Read the artifact itself (if file/doc/command)
- Read related workspace sources: sibling implementations, governing contract, relevant lessons — enumerate exact paths before reading
- Record every path into `sources_read`

**How agent uses the reference:** sources are the ONLY basis for grounding claims in Step 4 part 4 — no claims from memory.

### Step 3: Decompose

**Pre-generation checkpoint:**
- Read canonical reference: `.claude/docs/design/walkthrough/references/decomposition-strategies.md` (strategy for the input type)
- Read contract: `contracts/step-03-contract.json`
- Read input from prior step: `sources_read` list (must be non-empty or marked external-only)

**How agent uses the reference:** strategy table → section map → present → user approves → write state file.

### Step 4: Explain

**Pre-generation checkpoint:**
- Read state: `.claude/state/walkthrough-state.json` (cursor, depth) — this turn, not from memory
- Read canonical reference: `.claude/docs/design/walkthrough/references/format-contract.md` (the seven parts)
- Read depth rules: `.claude/docs/design/walkthrough/references/depth-modes.md`
- Re-read the sources backing `sections[cursor]` if context was compacted

**How agent uses the reference:** renders exactly `sections[cursor]` in the format at current depth, ends with settle prompt, stops.

### Step 5: Settle
Reads only. Dependencies: user responses; `.claude/docs/design/walkthrough/references/depth-modes.md` for mid-loop dial phrases.

### Step 6: Record

**Pre-generation checkpoint:**
- Read canonical reference: `.claude/docs/design/walkthrough/references/ledger-spec.md` (entry schema)
- Read state file (current ledger + cursor)

**How agent uses the reference:** append entry → save → increment cursor → save. Append-before-advance is the invariant.

### Step 7: Exit

**Pre-generation checkpoint:**
- Read canonical reference: `.claude/docs/design/walkthrough/references/ledger-spec.md` (durable file format + handoff contract)
- Read state file (full ledger, deferred sections)

**How agent uses the reference:** revisit deferred → write `docs/walkthroughs/YYYY-MM-DD-[slug].md` (or user-directed path) → mark state complete → offer handoff.

## Composability Contract (spec only — not wired in v1)

- Iteration input: `{section, sources, depth}` → output: `{explanation, settled_decision}`
- Loop input: `{artifact, sections?, depth}` (outer loop may supply the map, skipping Step 3) → output: ledger + durable file path

V1 runs standalone only. Integration with /design is a doc change, not a redesign.
