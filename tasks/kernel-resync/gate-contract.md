# Gate Contract — Kernel Resync

## Verification Methods
→ [[.claude/skills/task-builder/references/verification-methods.md]]

## Merge Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| MERGE-01 | learn-indexed-protocol merged | run_code | git log shows commits | Resolve conflicts |
| MERGE-02 | domain-setup-rerunability merged | run_code | git log shows commit | Resolve conflicts |
| MERGE-03 | hook-fixes merged | run_code | git log shows commit | Resolve conflicts |
| MERGE-04 | task-builder-audit merged | run_code | git log shows commit | Resolve conflicts |
| PUSH-01 | Main pushed | run_code | git push exits 0 | Fix remote |

## Build Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | v2 branch created | run_code | git branch shows it | Create |
| BUILD-02 | 8-step task-builder | file_exists | step-03-resolve-template.md | Copy |
| BUILD-03 | 8-step audit-workflow | file_exists | step-07-scan-atomicity.md | Copy |
| BUILD-04 | backlog.md | file_exists | File exists | Copy |
| BUILD-05 | task-builder.md updated | grep | Has 'Structural audit' | Copy |
| BUILD-06 | audit-workflow.md updated | file_exists | File exists | Copy |
| BUILD-07 | anchor.md updated | grep | Has 'concrete verb' | Copy |
| BUILD-08 | complete.md updated | file_exists | File exists | Copy |
| BUILD-09 | session-start.md updated | file_exists | File exists | Copy |
| BUILD-10 | gate-enforcer updated | grep | Has check_and_increment | Copy |
| BUILD-11 | test-failure updated | file_exists | File exists | Copy |
| BUILD-12 | auto-approve updated | file_exists | File exists | Copy |
| BUILD-13 | actions-log copied | file_exists | File exists | Copy |
| BUILD-14 | settings.local.json | grep | Has PermissionRequest | Update |
| BUILD-15 | lessons copied | file_exists | lessons.md exists | Copy |
| BUILD-16 | CLAUDE.md updated | grep | Has task-builder + audit-workflow + backlog | Edit |
| BUILD-17 | v2 committed | run_code | git log shows commit | Commit |
| BUILD-18 | PR created | run_code | gh pr list shows PR | Create |
| BUILD-19 | PR merged | run_code | Main includes v2 | Merge |

## Functional Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| FUNC-01 | Kernel hooks pass | run_code | All exit 0 | Fix |
| FUNC-02 | Factory hooks pass | run_code | All exit 0 | Fix |

## Production Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| PROD-01 | Kernel session works | run_code | session_started + anchored = true | Fix |

## Sync Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| SYNC-01 | Factory task-builder resynced | file_exists | step-03-resolve-template.md in factory | Copy |
| SYNC-02 | Factory lessons resynced | file_exists | task-atomicity.md in factory | Copy |

## Cleanup Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| CLEAN-01 | Old branches deleted | run_code | No feature branches remain | Delete |

## Requirements Coverage
Each gate maps to a task acceptance criterion.

## Summary
- Merge: 5, Build: 19, Functional: 2, Production: 1, Sync: 2, Cleanup: 1
- **Total: 30 gates**
