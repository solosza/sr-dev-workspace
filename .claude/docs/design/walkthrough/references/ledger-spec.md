# Ledger Spec — Schema, Durable File, Handoff

Parent: [[../index.md]]

The ledger is the walkthrough's real output: the ordered record of what was settled. The state-file copy is the working copy; the durable file is the deliverable.

## Entry Schema (state file, during the loop)

```json
{
  "section": "bootstrap",
  "settled": "3-line bootstrap: __file__-anchored path insert + load_dotenv. No editable install (survives prod-test repo copies). No vendored site-packages.",
  "notes": "Revisit installable-package if the platform ever ships as a pip dependency.",
  "timestamp": "2026-07-13T06:40:00Z"
}
```

| Field | Rule |
|-------|------|
| `section` | Name from the section map, verbatim |
| `settled` | The decision in full sentences, self-contained — readable without the conversation. "Understood, no decision needed" is a valid outcome for teaching-only sections |
| `notes` | Optional: deferred questions, conditions, dissent |
| `timestamp` | ISO, at append time |

Deferred sections get `settled: "DEFERRED"` + notes, and the loop revisits them before exit.

## Durable File (written at Step 7)

**Default path:** `docs/walkthroughs/YYYY-MM-DD-[artifact-slug].md`
**Override:** user may redirect at exit (e.g., into `projects/hmsa-qa-platform/02-reference-patterns/` next to the design doc the walkthrough served).

```markdown
# Walkthrough Ledger — [artifact]

**Date:** YYYY-MM-DD
**Mode/Depth:** loop / plain
**Sources read:** [list from sources_read]
**Sections:** N settled, M deferred

| # | Section | Settled |
|---|---------|---------|
| 1 | bootstrap | 3-line bootstrap: path insert + load_dotenv... |
| ... | | |

## Notes & Deferred
- [section]: [note]
```

## Handoff Contract

At exit, offer exactly these options (HITL):

| Option | What happens |
|--------|-------------|
| **Feed /design** | Invoke `/design [name] [description]` with the ledger presented as pre-settled requirements — the interview confirms instead of re-asking |
| **Fold into a design doc** | Ledger content merged into a named existing design doc (e.g., decisions become the doc's Decision sections) |
| **Stop** | Durable file only; nothing else invoked |

**Rule:** the ledger is input material for downstream commands — downstream never re-litigates a settled entry; it may surface NEW gaps the walkthrough didn't cover.

## One-Shot

No ledger. If the one-shot answer settles something worth keeping, the user says so and the agent appends it to the most recent relevant durable ledger (or starts one) — explicit, never automatic.
