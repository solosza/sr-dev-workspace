# Gap 7: Execution Dispatch Logic in Execute-Pipeline

## Status
NEW

## Location
- `.claude/skills/execute-pipeline/references/step-04-execute-tasks.md` (dispatch point)
- `.claude/skills/autonomous-cycling/` (inline path)
- `run-task.sh` (isolated path)

## Problem
Execute-pipeline step 4 currently sends ALL tasks to run-task.sh regardless of complexity. This is wasteful for simple tasks (single file write, quick research note, small edit) that don't need process isolation, timeout protection, or fresh `claude -p` context. Meanwhile, task-builder step 9 has its own inline execution via Agent tool, and autonomous-cycle has a third inline path — three execution modes with no unified decision logic.

The four current execution paths:

| Path | Entry Point | How Tasks Execute |
|------|------------|-------------------|
| task-builder standalone | `/kernel/task-builder` | Dual: BUILD inline (Agent), TEST spawned (run-task.sh) |
| execute-pipeline | `/kernel/execute-pipeline` | Everything via run-task.sh |
| autonomous-cycle | `/kernel/autonomous-cycle` | Everything inline (same session) |
| run-task.sh direct | `bash run-task.sh` | One-shot `claude -p` per task |

Problems with this:
1. **No single decision point** — execution mode is implicit based on which command you ran, not task characteristics
2. **autonomous-cycle has no protection** — no timeout, no process isolation, no log capture, context window fills across tasks
3. **Simple tasks pay isolation overhead** — spawning `claude -p` for a 3-line file write wastes ~30s startup per task
4. **Complex tasks get no isolation in autonomous-cycle** — a crash loses all progress

## Fix

Make execute-pipeline the single dispatcher with a classify-then-route pattern:

```
execute-pipeline step 4:
  for each task:
    weight = classify(task)
    if weight == "simple":
      route to autonomous-cycle (inline, same session)
    else:
      route to run-task.sh (isolated, fresh claude -p)
```

### Classification Heuristic

Classification is about **task weight**, not task type. Works equally for build, research, test, and verify tasks.

| Signal | Route |
|--------|-------|
| Few acceptance criteria, single deliverable, no external deps | autonomous-cycle (inline) |
| Many criteria, multi-file, external services, infrastructure, docker, install | run-task.sh (isolated) |
| Uncertain | run-task.sh (safe default) |

The heuristic can start simple:
- Count acceptance criteria (<=3 = simple candidate)
- Check for complexity keywords: "docker", "install", "multiple files", "infrastructure", "external", "API"
- Check for multi-file deliverables (task mentions creating/editing 2+ files)
- Default to run-task.sh when uncertain

### What Changes

- **execute-pipeline step 4** — add classification logic before dispatch. Simple tasks route to autonomous-cycle. Complex tasks route to run-task.sh.
- **task-builder step 9** — no change (standalone mode keeps its own execution, pipeline_mode defers to execute-pipeline)
- **autonomous-cycle** — no change (already has the inline loop: pick task, work, complete, next)
- **run-task.sh** — no change (already has timeout, isolation, logging)

### Key Principle

Task-builder is the **planner** (produces tasks). Execute-pipeline is the **executor** (decides how to run them). Planning and execution stay decoupled.

## Dependencies
- autonomous-cycle skill must be callable programmatically from execute-pipeline (currently user-invoked only — may need a "single task" mode)
- Classification heuristic lives in step 4 reference file
