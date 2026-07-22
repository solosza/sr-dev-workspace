---
name: summarize
type: design-document
version: 1.0
date_created: 2026-07-07
status: draft
purpose: Dynamic summarization of completed agent output with requirement diffing and decision flags
---

# /summarize — Design Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->

## Position in System

```
/kernel/execute-pipeline → completes → agent output produced
                                              ↓
/kernel/complete → auto-fires /kernel/summarize (one-shot agents)
                                              ↓
/kernel/summarize → reads backlog + tasks + deliverables + agent state
                                              ↓
                        produces dynamic summary with requirement diff + decision flags
                                              ↓
                        summary written to review-status.json entry
                                              ↓
/kernel/review-queue → shows summary instead of raw output
```

`/summarize` is the visibility bridge between agent completion and human review.

## Skill Identity

You are a summarizer. You read completed agent output (backlog requirements, task plans, deliverable files, agent state), diff deliverables against backlog requirements, and produce a dynamic summary. Summaries scale with output complexity — no artificial compression. You surface decisions needing human input separately from informational completions.

## Philosophy

1. **Dynamic sizing** — summary scales with output complexity. 10 findings = 10 findings shown. No hardcoded line limits.
2. **Requirement diffing** — every backlog requirement is checked against deliverables. Per-requirement status: met, partial, not addressed.
3. **Decision-first** — separate "decisions needed" (recommendations requiring human choice) from "informational" (facts, completions).
4. **Deliverable inventory** — list all files created/changed with paths and brief descriptions.
5. **Problem surfacing** — failures, skips, blockers, anything needing attention gets its own section.

## Vocabulary

| Term | Meaning |
|------|---------|
| **summary** | The output — a structured report of what an agent produced vs what was asked |
| **requirement diff** | Per-requirement status check: backlog requirement → deliverable evidence |
| **decision flag** | An item requiring human choice, separated from informational items |
| **deliverable inventory** | List of all files created/changed by the agent |
| **summary target** | What is being summarized: a backlog number, project folder, or unreviewed set |
| **integrated mode** | Auto-fired by `/kernel/complete` for one-shot agents |
| **standalone mode** | User invokes directly with a target |

## Input

```
/kernel/summarize 188
/kernel/summarize projects/ssh-*
/kernel/summarize
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `[number]` | Summarize specific backlog's output | `/kernel/summarize 188` |
| `[path]` | Summarize a project folder | `/kernel/summarize projects/ssh-*` |
| (none) | Summarize all unreviewed completions | `/kernel/summarize` |

## Output

Dynamic summary report with sections: requirement diff, decision flags, deliverable inventory, problems.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[summarize/references/workflow]] | Steps 1-6: resolve target, gather sources, diff, format, write, report |
| [[summarize/references/source-resolution]] | How to find backlog, tasks, deliverables, agent state for a target |
| [[summarize/references/summary-format]] | Output template with all sections and dynamic sizing rules |

## Workflow Summary

| Step | Responsibility | Output | HITL |
|------|---------------|--------|------|
| 1. Resolve Target | Parse input, find backlog + related files | Source file paths | — |
| 2. Gather Sources | Read backlog requirements, task index, deliverables, agent state | Structured input data | — |
| 3. Diff Requirements | Check each backlog requirement against deliverables | Requirement diff table | — |
| 4. Classify Findings | Separate decisions from informational items | Classified findings | — |
| 5. Format Summary | Produce dynamic summary report | Summary text | — |
| 6. Write + Report | Write summary to review-status.json and/or display | Persisted summary | — |

## Critical Rules

1. **Never compress findings.** If the agent produced 15 files, list 15 files. Dynamic sizing means showing everything relevant.
2. **Always diff against backlog requirements.** Every requirement from the backlog must appear in the diff with a status.
3. **Separate decisions from information.** Recommendations requiring human choice go in "Decisions Needed." Everything else is "Informational."
4. **Handle both research and build deliverables.** Research produces reports in `projects/`. Build produces code in `.claude/skills/`, `.claude/commands/`, or repo directories.
5. **Integrated mode writes to review-status.json.** When called by `/kernel/complete`, the summary is stored in the review entry for the backlog.
6. **Standalone mode displays directly.** When invoked by user, show the summary in conversation output.

## Integration Points

### /kernel/complete Integration

In one-shot mode, after marking the task complete, `/kernel/complete` calls `/kernel/summarize [backlog-number]` to generate and store the summary. The summary is written to the backlog's entry in `review-status.json` under a `summary` key.

### /kernel/review-queue Integration

When presenting a review card, `/kernel/review-queue` checks for a `summary` key in the review-status.json entry. If present, it shows the summary instead of requiring the user to read raw output files.

### Discussion Mode

After displaying a summary, the user may respond with direction or questions. If the user wants follow-up work, use `/kernel/backlog` to create a follow-up backlog with parent linking.

## State Persistence

**None.** Stateless — summaries are stored in review-status.json entries, not in a separate state file.

## Complete File Structure

**Skill package:**

```
.claude/commands/kernel/summarize.md                ← Layer 1
.claude/skills/summarize/
├── SKILL.md                                        ← Layer 2
├── workflow.md, gate-contract.md                   ← Layer 2
├── steps/step-{01..06}-*.md                        ← Layer 3 (6 steps)
└── references/
    └── INDEX.md                                    ← Layer 4
```

**Design doc:**

```
.claude/docs/design/summarize/
├── index.md                                        ← this file
└── references/
    ├── workflow.md                                 ← step details
    ├── source-resolution.md                        ← how to find input files
    └── summary-format.md                           ← output template + dynamic sizing
```

---

**Version:** 1.0
**Last Updated:** 2026-07-07
