# Fix Execute-Pipeline Gaps + Granular Decomposition Reference

## Status
Open

## Priority
High — execute-pipeline is the primary autonomous path and currently skips plan review, has no attestation, no gate verification, and divergent execution modes. The granularity reference is needed because task-builder repeatedly produces fat tasks despite RULE ZERO corrections.

## Summary
Seven gaps identified in the execute-pipeline → task-builder → run-task.sh chain. Each gap causes silent failures, wasted work, or broken provenance. Additionally, task-builder needs an unambiguous granularity reference with concrete examples so the agent never produces fat tasks.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[051-kernel-fix-execute-pipeline-gaps/gap-1-plan-review]] | Re-enable plan review in autonomous pipeline |
| [[051-kernel-fix-execute-pipeline-gaps/gap-2-attestation-step]] | Add attestation + signing to pipeline step 5 |
| [[051-kernel-fix-execute-pipeline-gaps/gap-3-timeout-feedback]] | Add per-task identification to timeout logs |
| [[051-kernel-fix-execute-pipeline-gaps/gap-4-execution-mode-divergence]] | Reconcile step 9 inline vs run-task.sh paths |
| [[051-kernel-fix-execute-pipeline-gaps/gap-5-gate-verification]] | Add gate contract verification to /kernel/complete |
| [[051-kernel-fix-execute-pipeline-gaps/granularity-reference]] | Definitive decomposition reference with examples — the most important deliverable |
| [[051-kernel-fix-execute-pipeline-gaps/gap-6-move-to-done]] | Enforce move-to-done for completed backlogs and task folders |
| [[051-kernel-fix-execute-pipeline-gaps/gap-7-execution-dispatch]] | Add classify-then-route dispatch: simple tasks → autonomous-cycle, complex → run-task.sh |
| [[051-kernel-fix-execute-pipeline-gaps/extraction-evidence]] | Real-world evidence from 044 extraction proving why granularity + specific acceptance criteria matter |

## Architecture

```
execute-pipeline
  step 3 ──→ task-builder (gap 1: plan review skipped)
  step 4 ──→ run-task.sh  (gap 3: no task ID in timeout)
                │
                └── claude -p ──→ /kernel/complete (gap 5: no gate verification)
  step 4 ──→ dispatch     (gap 7: no classify-then-route, all tasks go to run-task.sh)
                │
                ├── simple tasks ──→ autonomous-cycle (inline)
                └── complex tasks ──→ run-task.sh (isolated)
  step 5 ──→ validate     (gap 2: no attestation)
         ──→ move-to-done (gap 6: never enforced, backlogs/tasks stay in place)

task-builder
  step 9 ──→ execute      (gap 4: divergent modes)
  step 5 ──→ decompose    (needs granularity-reference.md)
  step 6 ──→ atomize      (needs granularity-reference.md)
```

## Requirements
- Fix all 7 gaps in the pipeline chain
- Create a granularity reference document that the agent reads during decomposition and atomization
- Granularity reference must include concrete before/after examples, not just rules
- All changes must preserve backward compatibility (run-task.sh on Linux, task-builder standalone)

## References
- Execute pipeline skill: `.claude/skills/execute-pipeline/`
- Task builder skill: `.claude/skills/task-builder/`
- run-task.sh: `run-task.sh` + `lib/common.sh`
- Attestation: `lib/attestation/`
- Complete command: `.claude/commands/kernel/complete.md`
- Lessons (task atomicity): `.claude/lessons/task-atomicity.md`
- Backlog 050: run-task.sh zombie fix (just shipped)

## Task Builder Input
- **Deliverable:** Updated execute-pipeline skill (steps 3, 4, 5), updated task-builder skill (steps 5, 6, 9), updated run-task.sh (timeout feedback + move-to-done), updated /kernel/complete (gate verification), new granularity-reference.md, execution dispatch logic in step 4 (classify-then-route: simple → autonomous-cycle, complex → run-task.sh)
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Must not break existing pipelines. Granularity reference must be referenced by step-05-decompose.md and step-06-atomize.md via wikilink. Attestation step must use existing lib/attestation/ infrastructure.
