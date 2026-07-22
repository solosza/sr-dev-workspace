---
name: walkthrough
type: design-document
version: 1.0
date_created: 2026-07-13
status: draft
purpose: Generic teaching/design loop — decompose any artifact into sections, explain each in a grounded plain-English format, one section per turn, recording settled decisions into a durable ledger
---

# /walkthrough — Design Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->

## Position in System

```
user: /walkthrough [artifact-or-topic]
        ↓
resolve input → ground (read real sources) → decompose → section map approved
        ↓
   ┌─ explain section (format contract) ─┐
   │            ↓                        │   user-paced loop —
   │  discuss → user settles decision    │   blocks on user EVERY
   │            ↓                        │   iteration by design
   └─ record to ledger, advance cursor ──┘
        ↓ (sections exhausted)
durable ledger file → optional handoff to /design or a design doc
```

The anti-cycling loop: where `/kernel/execute-pipeline` must never stop, `/walkthrough` must never proceed without the user. Its exit artifact (the decisions ledger) is raw material for `/design` and design docs.

## Skill Identity

You are a walkthrough guide. You take any artifact or concept, decompose it into sections, explain each one in a fixed plain-English format grounded in the user's actual repositories and documents, one section per turn, and record each settled decision into a ledger that outlives the conversation.

## Philosophy

1. **Teach to decide** — every explanation drives toward a settled decision; understanding is the means, the ledger entry is the end.
2. **Grounded, never generic** — read the real sources (the artifact, the user's repos, contracts, lessons) before explaining. Recommendations are for THIS user's case, never textbook-neutral.
3. **User-paced by contract** — blocking on the user each iteration is the design, not a failure. The never-stop-cycling rule does not apply here.
4. **One section per turn** — never batch sections, never run ahead. The user sets the tempo and the depth.
5. **The format is the product** — plain-English purpose → visual flow → why each piece → grounding → recommendation → mental model → confirm. Protect it.
6. **Decisions are the artifact** — the durable ledger is what remains; it feeds /design without re-litigating anything.

## Vocabulary

| Term | Meaning |
|------|---------|
| **walkthrough** | One loop instance over one artifact — decompose, explain, settle, record |
| **section** | One unit of explanation — a code region, doc heading, concept subtopic, or plan phase |
| **section map** | The ordered section list produced by decomposition, approved by the user before the loop starts |
| **cursor** | Index into the section map — which section is current; survives compaction and session breaks |
| **ledger** | Ordered list of settled decisions, one entry per section; written to a durable file at exit |
| **settled decision** | The user-confirmed outcome of one section — a design choice, or explicitly "understood, no decision needed" |
| **grounding** | Reading the actual sources (repos, contracts, lessons) before explaining — RULE ZERO applied to teaching |
| **depth mode** | `plain` (full teaching format, default) or `terse` (analysis + recommendation only); dialable mid-loop |
| **one-shot** | Single explanation outside the loop — no state, no ledger |

## Input

```
/walkthrough [file-or-topic]              → loop mode, plain depth
/walkthrough [file-or-topic] --terse      → loop mode, terse depth
/walkthrough [narrow question]            → one-shot (inferred from phrasing)
/walkthrough [topic] --once               → one-shot (forced)
continue                                  → resume loop from cursor
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `file-or-topic` | Artifact to walk through: file path, design doc, command, concept, plan, error | `conftest design`, `.claude/commands/kernel/anchor.md`, `"fixture scoping"` |
| `--terse` | Start in terse depth mode | `/walkthrough api-objects.md --terse` |
| `--once` | Force one-shot even for broad topics | `/walkthrough "the intent chain" --once` |

Mid-loop verbal dials (no flags): "terse from here", "slow down on this one", "skip this section", "add a section on X".

## Critical Rules

1. **One section per turn.** Never explain two sections in one message. Never advance without the user's response. (This failure occurred twice during the design of this command — it is the primary drift risk.)
2. **Never explain ungrounded.** Step 2 must Read the actual sources before any explanation; every section's grounding part cites what the user's real repos/docs do. No explanation from memory alone.
3. **Format contract is mandatory.** Plain mode renders all seven parts; terse mode keeps grounding + recommendation + settle, drops the teaching parts. See [[references/format-contract.md]].
4. **Ledger-append before cursor-advance.** Record the settled decision, save state, THEN move — a crash between the two loses position, never a decision.
5. **Core stays artifact-agnostic.** No input-type-specific logic in SKILL.md or step files; decomposition strategies per type live only in [[references/decomposition-strategies.md]].
6. **One-shot writes no state.** It is the explain primitive alone — no section map, no cursor, no ledger.
7. **Never runs autonomously.** Not invocable from run-task.sh, cycling, or any autonomous pipeline. A walkthrough without a user is a contradiction.

## Workflow Summary

| Step | Responsibility | Output | HITL |
|------|---------------|--------|------|
| 1. Resolve Input | Detect mode (loop/one-shot), input type, depth | Resolved artifact + mode + depth | Only if ambiguous |
| 2. Ground | Read the artifact + related real sources (repos, contracts, lessons) | `sources_read` list | No |
| 3. Decompose | Produce section map per input-type strategy; init state | Section map + state file | **Yes — user approves map** |
| 4. Explain | Render current section per format contract at current depth | One explanation message | No (output only) |
| 5. Settle | Discuss until the user settles the section's decision | Settled decision | **Yes — every iteration** |
| 6. Record | Append ledger entry, advance cursor, save state; loop to 4 | Updated state | No |
| 7. Exit | Write durable ledger file, summarize, offer /design handoff | Ledger .md file + summary | Yes — handoff choice |

One-shot mode runs steps 1 → 2 → 4 only.

Step details: [[references/workflow.md]]

## State Persistence Schema

**Location:** `.claude/state/walkthrough-state.json`

```json
{
  "artifact": "conftest design",
  "input_type": "concept",
  "mode": "loop",
  "depth": "plain",
  "sections": ["bootstrap", "cli-options", "config", "..."],
  "cursor": 3,
  "ledger": [
    {"section": "bootstrap", "settled": "3-line bootstrap: path-insert + load_dotenv", "notes": "", "timestamp": "..."}
  ],
  "sources_read": ["platform-selenium/tests/conftest.py", "v2/tests/conftest.py"],
  "ledger_file": null,
  "status": "active",
  "last_updated": "..."
}
```

**Resume:** "continue" (or re-invoking `/walkthrough` with the same artifact) reads state, re-reads the current section's sources if needed, and picks up at `sections[cursor]`. Ledger and depth survive intact. Details: [[references/ledger-spec.md]]

## Complete File Structure

```
.claude/commands/kernel/walkthrough.md      ← command entry point
.claude/skills/walkthrough/
├── SKILL.md                                ← identity, philosophy, step table
├── workflow.md                             ← loop behavior, state, resume
├── gate-contract.md                        ← per-step gates
├── steps/
│   ├── step-01-resolve-input.md
│   ├── step-02-ground.md
│   ├── step-03-decompose.md
│   ├── step-04-explain.md
│   ├── step-05-settle.md
│   ├── step-06-record.md
│   └── step-07-exit.md
├── references/
│   └── INDEX.md                            ← routing table → design doc payloads (link, don't copy)
└── contracts/
    ├── step-03-contract.json               ← section map + state init validation
    ├── step-06-contract.json               ← iteration record validation
    └── step-07-contract.json               ← exit / durable ledger validation
```

## Design Documents

| Payload | Content |
|---------|---------|
| [[references/workflow.md]] | Step specs (purpose + procedure per step), loop mechanics, resume, one-shot path |
| [[references/format-contract.md]] | The seven-part explanation format with per-part rules and examples |
| [[references/decomposition-strategies.md]] | Section derivation per input type (file, doc, command, concept, plan, error) |
| [[references/depth-modes.md]] | Plain vs terse rendering, mid-loop dial phrases, per-section overrides |
| [[references/ledger-spec.md]] | Ledger entry schema, durable file format/location, /design handoff contract |
| [[references/contracts.md]] | Contract definitions — soft validation rules + mechanical validations |
