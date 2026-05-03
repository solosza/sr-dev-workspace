# 007 — Rewrite step-04: Classify-Then-Route Dispatch (Gap 7)

## Type
BUILD

## Requirements
- Edit `.claude/skills/execute-pipeline/references/step-04-execute-tasks.md`
- Add a classification step BEFORE the dispatch step (between "Read pipeline state" and "Spawn background Agent")
- Classification logic:
  1. Read each task file from the task folder
  2. Classify as simple or complex based on:
     - Count acceptance criteria (<=3 = simple candidate)
     - Check for complexity keywords: "docker", "install", "multiple files", "infrastructure", "external", "API", "spawn", "run-task.sh"
     - Default: complex (safe fallback)
  3. Route:
     - Simple tasks → autonomous-cycle (inline, same session)
     - Complex tasks → run-task.sh (isolated, fresh claude -p)
- Add a new "Dispatch Logic" section explaining the two paths
- Keep the existing run-task.sh spawning logic for complex tasks
- Add autonomous-cycle invocation logic for simple tasks
- Add a classification summary to the output section

## Acceptance Criteria
- [ ] `step-04-execute-tasks.md` contains "classif" (classification logic)
- [ ] File mentions "autonomous-cycle" as the inline path
- [ ] File mentions "simple" and "complex" task routing
- [ ] File still contains run-task.sh for complex tasks
