# /walkthrough — Workflow (Step Specs)

Parent: [[../index.md]]

## Loop Shape

```
Step 1 (Resolve) → Step 2 (Ground) → Step 3 (Decompose + map approval)
                                          ↓
                              ┌── Step 4 (Explain) ──┐
                              │        ↓             │  repeat until
                              │  Step 5 (Settle)     │  cursor == len(sections)
                              │        ↓             │
                              └── Step 6 (Record) ───┘
                                          ↓
                                   Step 7 (Exit)

One-shot path: Step 1 → Step 2 → Step 4. Stop.
```

## Step 1: Resolve Input

**Purpose:** Determine what is being walked through, in which mode, at which depth.

**Pre-generation checkpoint:** none (entry step). If resuming, read `.claude/state/walkthrough-state.json` FIRST — if `status: active` and the input matches (or input is "continue"), skip to Step 4 at `sections[cursor]`.

**Procedure:**
1. Parse argument: extract flags (`--terse`, `--once`), remainder is the artifact/topic.
2. Detect input type: existing file path → `file`; path into docs/design → `design-doc`; path into commands/skills → `command`; phase/plan reference → `plan`; error text/log → `error`; otherwise → `concept`.
3. Detect mode: `--once` → one-shot. Narrow-question phrasing ("just explain X", "what does Y mean", a single named mechanism) → one-shot. Otherwise → loop.
4. Depth: `--terse` → terse, else plain.
5. If artifact is ambiguous (multiple matching files, vague topic), ask ONE clarifying question — otherwise proceed.

## Step 2: Ground

**Purpose:** RULE ZERO applied to teaching — read the real sources before explaining anything.

**Pre-generation checkpoint:** the resolved artifact from Step 1 must name concrete files or a concept whose sources can be enumerated.

**Procedure:**
1. Read the artifact itself (if it is a file/doc/command).
2. Enumerate related sources: sibling implementations in the user's repos, the governing contract, relevant lessons, prior design docs. For concepts: whatever files embody the concept in THIS workspace.
3. Read them with the Read tool — never rely on memory of what a file contains.
4. Record every path read into `sources_read`.

**Rule:** if no workspace sources exist for the topic (pure external concept), grounding falls back to best-practice knowledge — but the explanation must SAY so instead of implying repo-verification.

## Step 3: Decompose

**Purpose:** Produce the section map and initialize loop state.

**Pre-generation checkpoint:** `sources_read` is non-empty (or explicitly marked external-only).

**Procedure:**
1. Apply the strategy for the input type — see [[decomposition-strategies.md]].
2. Present the section map to the user: numbered sections, one line each on what it covers.
3. User approves / reorders / adds / removes sections (HITL).
4. Write `.claude/state/walkthrough-state.json`: artifact, input_type, mode, depth, sections, cursor 0, ledger [], sources_read, status active.

**Gate:** state file exists with non-empty `sections` and user-approved map before any explanation begins.

## Step 4: Explain

**Purpose:** Render the current section per the format contract.

**Pre-generation checkpoint:** state file read this turn; `sections[cursor]` is the section being explained; the sources backing THIS section are in `sources_read` (re-read if context was compacted).

**Procedure:**
1. Render `sections[cursor]` using [[format-contract.md]] at the current depth ([[depth-modes.md]]).
2. End with the confirm/settle prompt — what decision this section needs from the user (or "nothing to decide — confirm understanding").
3. STOP. Output exactly one section. Wait.

## Step 5: Settle

**Purpose:** Discussion until the user lands the section's decision.

**Procedure:**
1. Answer follow-ups; go deeper or terser on request (mid-loop dials).
2. A section is settled when the user states a choice, accepts a recommendation, or confirms understanding (for no-decision sections).
3. Do not nudge toward speed; the user may park a section ("come back to this") — mark it `deferred`, move on, revisit before exit.

## Step 6: Record

**Purpose:** Persist the outcome, then advance. Order is load-bearing.

**Procedure:**
1. Append ledger entry: `{section, settled, notes, timestamp}`.
2. Save state (ledger updated, cursor still pointing at the recorded section).
3. Increment cursor, save state again.
4. If `cursor < len(sections)`: proceed to Step 4 on the user's next turn (never same-turn).
5. If sections exhausted (including revisiting deferred ones): Step 7.

**Rule:** ledger-append before cursor-advance — a crash between the two loses position, never a decision.

## Step 7: Exit

**Purpose:** Make the ledger durable and hand off.

**Procedure:**
1. Write the durable ledger file per [[ledger-spec.md]] (default `docs/walkthroughs/YYYY-MM-DD-[slug].md`; user may redirect it, e.g. into a project folder).
2. Set state `status: complete`, `ledger_file: <path>`.
3. Summarize: sections covered, decisions settled, anything deferred.
4. Offer handoff (HITL): feed the ledger to `/design`, fold into an existing design doc, or stop here.

## Resume

| Event | Behavior |
|-------|----------|
| "continue" with `status: active` | Read state → announce position ("section 4 of 9: credentials") → Step 4 |
| Context compaction mid-loop | Same — state file is the source of truth, not conversation memory |
| New `/walkthrough X` while another is active | Ask: finish/park the active one first, or abandon it (state overwritten only on explicit confirmation) |

## Composability Contract (spec only — not wired in v1)

Per-iteration contract, so a later outer loop (e.g. `/design`) can drive this skill without redesign:
- **Iteration input:** `{section, sources, depth}`
- **Iteration output:** `{explanation (rendered), settled_decision}`
- **Loop input:** `{artifact, sections?, depth}` — an outer loop may supply its own section map, skipping Step 3 decomposition
- **Loop output:** the ledger (list of settled decisions) + durable file path

V1 runs standalone only. This contract exists so integration is a doc change, not a redesign.
