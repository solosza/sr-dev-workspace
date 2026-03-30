# Gate Contract — Cross-Repo Agent Delegation

## Verification Methods
→ [[.claude/skills/task-builder/references/verification-methods.md]]

## Build Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | step-06 has factory mode | grep | `grep -q 'factory' step-06-write-tasks.md` | Edit |
| BUILD-02 | step-07 has factory logic | grep | `grep -q 'Factory Task' step-07-execute.md` | Edit |
| BUILD-03 | workflow has factory handling | grep | `grep -q 'factory' workflow.md` | Edit |
| BUILD-04 | delegation reference exists | file_exists | `test -f cross-repo-delegation.md` | Write |
| BUILD-05 | SKILL.md has reference | grep | `grep -q 'cross-repo' SKILL.md` | Edit |
| BUILD-06 | Old SSH output cleaned | run_code | `test ! -d output/ssh-image-testing` | Clean |

## Functional Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| FUNC-01 | Agent reads factory | run_code | Agent reports CLAUDE.md content | Fix access |
| FUNC-02 | Agent reads platform-docker | run_code | Agent reports FRAMEWORK.md content | Fix access |

## Production Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| PROD-01 | Agent runs factory step | file_exists | Decomposition doc produced | Fix prompt |
| PROD-02 | Full factory run produces spec | file_exists | SKILL.md in output | Fix factory |
| PROD-03 | Output follows template architecture | run_code | No paramiko refs, has Docker/ImageInterface | Fix spec |

## Sync Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| SYNC-01 | Kernel repo has delegation ref | file_exists | cross-repo-delegation.md in kernel | Copy |
| SYNC-02 | Kernel PR merged | run_code | git log shows commit | Merge |

## Summary
- Build: 6, Functional: 2, Production: 3, Sync: 2
- **Total: 13 gates**
