# Three-Way Drift Resolution

## Status
NEW

## What
Resolve divergence between the three repos that have kernel copies. Pick a winner per file, sync all three.

## Current Drift

### sr_dev_workspace (SOURCE OF TRUTH for kernel evolution)
- Latest versions of all core commands (anchor, learn, complete, etc.)
- Task-builder has 10 steps (added convention-check at 3, plan-review at 7)
- universal-gate-enforcer.py has Gate 6 removed (RAFT consensus lesson)
- lessons.md has full RULE ZERO with all recurrence notes
- execute-pipeline has classify-then-route dispatch (simple inline, complex run-task.sh)

### isagawa-kernel (BEHIND)
- Task-builder still has 8 steps with old numbering
- universal-gate-enforcer.py still has Gate 6 (protocol hash check during execution)
- lessons.md is stale
- Missing: execute-pipeline, prod-test, spawn-agent-swarm skills

### hmsa-healthcare-qa (INDEPENDENTLY EVOLVED)
- Has execute-pipeline and spawn-agent-swarm but different versions
- Has domain-specific skills: healthcare-qa, create-sit-xlsx, test-pipeline, validate-tc
- Has validate-artifact-contracts.py hook (domain-specific)
- Has build-command, design-command, gap-check skills (domain-specific)

## Resolution Plan

1. **Core kernel files**: sr_dev_workspace wins (latest). Sync to isagawa-kernel.
2. **Extensions in hmsa**: leave as-is — they're workspace-local tools, not kernel.
3. **Domain-specific files**: leave in each repo — domain-setup generated them.
4. **hmsa kernel core**: sync from isagawa-kernel AFTER step 1 completes. Only core files.
5. **Verify**: after sync, `diff -rq` between all three repos should show ONLY domain/extension differences, zero core kernel differences.

## Risk
- hmsa may have made changes to core kernel files (e.g., universal-gate-enforcer.py) that workspace doesn't have
- Need to diff each core file between all three repos before overwriting
- Some hmsa changes may need to be cherry-picked back into the kernel

## Dependencies
- kernel-manifest.md (defines what's core)
- sync-mechanism.md (how to push changes)
