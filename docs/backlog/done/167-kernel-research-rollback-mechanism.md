# Research: Rollback Mechanism for Lessons and Protocol Changes

## Status
Open

## Priority
Medium — important for self-correction but depends on metrics/evaluation being in place first

## Summary
Research how to add rollback capability to the kernel's learning system. Currently lessons are append-only — there's no mechanism to say "lesson X was wrong, remove it and revert the associated hook/protocol change." When the user corrects a bad memory entry, it's done manually. The system doesn't self-correct. A rollback mechanism would allow: detecting that a change made things worse, reverting the change, and recording why the rollback happened.

## Requirements
- Research how to version protocol and hook changes (git-based? snapshot-based? diff-based?)
- Research how to link lessons to their associated code changes (lesson → hook modification → protocol edit)
- Research rollback triggers: manual (user says "undo"), automatic (metrics show degradation), eval-driven (eval suite regression)
- Research the "lesson was wrong" workflow: what happens to the lesson entry, the hook, the protocol?
- Research how to prevent rollback cascades (rolling back A breaks B which was built on A)
- Research prior art: database migrations (up/down), feature flag rollbacks, model versioning
- Consider: should lessons have a "confidence" or "validated" flag?

## References
- `.claude/lessons/lessons.md` — current append-only lesson log
- `.claude/hooks/` — hook files modified by /kernel/learn
- `.claude/protocols/` — protocol files modified by /kernel/learn
- Backlog 164-166 (metrics, experiments, auto-eval — dependencies for automatic rollback)
- Database migration patterns (Alembic, Flyway)

## Task Builder Input
- **Deliverable:** Research report with rollback architecture design
- **Location:** subproject:kernel-rollback-research
- **Scope:** RESEARCH
- **Constraints:** Manual rollback is achievable independently. Automatic rollback depends on metrics (164), experiment tracking (165), and auto-eval (166).
