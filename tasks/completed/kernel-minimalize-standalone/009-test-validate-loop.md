# Validate Minimal Kernel Loop

## Type
TEST

## Phase Gate
Tasks 007 and 008 must be complete.

## Deliverable
Proof that the minimal kernel can domain-setup a fresh workspace and the full loop works.

## Instructions

1. Verify the minimal kernel repo at `D:\my_ai_projects\project_test_repos\kernel-minimal` has:
   - CLAUDE.md with 7 core commands only
   - `.claude/commands/kernel/` with exactly 7 files
   - `.claude/skills/` with exactly 2 directories
   - `.claude/hooks/` with 4 hook files
   - `.claude/lessons/lessons.md` with RULE ZERO only
   - `run-task.sh` and `lib/common.sh` present
   - `docs/kernel-feature-freeze-policy.md` present
   - No `delegation/`, `scanner/`, `backlog/`, `tests/` directories
   - No `lib/attestation/`, `lib/validators/`

2. Verify `.claude/settings.local.json` references only the 4 core hooks

3. Report pass/fail for each check

## Verification
- All structural checks pass
- No extension artifacts remain
