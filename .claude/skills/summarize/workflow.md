# Workflow — /summarize

## Input Modes

| Input | Mode | Behavior |
|-------|------|----------|
| `[number]` | Backlog | Resolve to backlog file, find deliverables, produce full summary with requirement diff |
| `[path]` | Path | Glob-expand path, inventory files, produce summary without requirement diff |
| (none) | Batch | Find unreviewed completions, summarize next one |

## Integration Modes

| Mode | Trigger | Output Target |
|------|---------|--------------|
| Standalone | User invokes `/kernel/summarize` | Display in conversation |
| Integrated | `/kernel/complete` calls after one-shot agent finishes | Write to review-status.json |

## Phase Flow

```
resolve-target → gather-sources → diff-requirements → classify → format → write+report
     ↓                ↓                  ↓                 ↓          ↓         ↓
  paths obj      structured data    diff table       categories   summary   persisted
```

## Step Details

→ `steps/step-01-resolve-target.md` — Parse input, find source files
→ `steps/step-02-gather-sources.md` — Read backlog, tasks, deliverables, agent state
→ `steps/step-03-diff-requirements.md` — Per-requirement status check
→ `steps/step-04-classify-findings.md` — Decisions vs informational vs problems
→ `steps/step-05-format-summary.md` — Assemble dynamic summary
→ `steps/step-06-write-report.md` — Write to review-status.json or display

## /kernel/complete Integration

When `/kernel/complete` runs in one-shot mode:
1. After marking task complete and before final report
2. If backlog number is available (from pipeline_state or task folder name)
3. Invoke summarize with the backlog number
4. Summary is written to review-status.json under the backlog's entry

## /kernel/review-queue Integration

When review-queue presents a review card:
1. Check if the entry in review-status.json has a `summary` key
2. If yes: display the summary as part of the review card
3. If no: present raw file paths as before (backward compatible)
