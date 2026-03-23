# Test Kernel Spec Bootstrap

## Context
Test that the kernel spec (built in tasks 020-024) actually works. Create a completely clean repo, install the kernel spec, run domain-setup, and verify the kernel gets built correctly.

**HUMAN REQUIRED:** This task requires Claude Code restarts (domain-setup creates hooks that only load on restart).

## Dependencies
- **024** — kernel spec complete and pushed
- **026** — domain-setup rerunability implemented (feature branch)

## Phase Gate
- [ ] Kernel spec pushed to `isagawa-co/kernel-spec`
- [ ] Feature branch `feature/domain-setup-rerunability` pushed to `isagawa-co/isagawa-kernel`

## Requirements

### Create clean test repo
- Location: `D:\my_ai_projects\project_test_repos\test-kernel-bootstrap`
- `git init`
- Create a minimal `CLAUDE.md` with just: "This is a test repo for kernel bootstrap."
- This simulates a user's empty project

### Install kernel spec
Copy the kernel spec files into the test repo:
```
From: D:\my_ai_projects\project_test_repos\specs\kernel-spec\.claude\
To:   D:\my_ai_projects\project_test_repos\test-kernel-bootstrap\.claude\
```
Copy: skills/, commands/ (only kernel spec files, not domain-setup outputs)

### Run domain-setup
- Invoke `/kernel/domain-setup`
- Domain-setup should read the kernel spec and build:
  - Protocol at `.claude/protocols/[domain]-protocol.md`
  - Hooks (gate enforcer)
  - Commands wrapped for kernel loop
  - State files
  - Lessons folder
- **RESTART REQUIRED** after domain-setup completes

### Verify after restart
After Claude Code restart, verify:
1. Hooks are active (try writing without anchor — should block)
2. `/kernel/anchor` works
3. `/kernel/learn` works
4. `/kernel/complete` works
5. State files exist and are correct

### Failure protocol
- Try up to 3 times
- On each failure: document what failed, why, what was tried
- After 3 failures: create `research/034-bootstrap-failures.md` with findings, move on

## Output
- Working kernel built from kernel spec in clean test repo
- OR failure documentation at `research/034-bootstrap-failures.md`

## Validation
- [ ] Clean repo created
- [ ] Kernel spec installed
- [ ] Domain-setup ran successfully
- [ ] Restart completed
- [ ] Hooks active and blocking correctly
- [ ] All kernel commands functional

## Completion Signal
When ALL validation checks pass (or 3 failures documented), invoke `/kernel/complete`.
