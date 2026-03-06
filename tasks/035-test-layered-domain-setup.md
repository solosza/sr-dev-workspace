# Test Layered Domain-Setup

## Context
Test that domain-setup can run TWICE — first for the kernel spec (builds kernel), then for a domain spec (builds domain governance on top). The kernel must survive the second run. This validates the rerunability fix from task 026.

**HUMAN REQUIRED:** Two Claude Code restarts needed (one after each domain-setup).

## Dependencies
- **034** — kernel spec bootstrap tested (proves kernel spec works alone)
- **026** — domain-setup rerunability implemented

## Phase Gate
- [ ] Task 034 complete (kernel bootstrap works)
- [ ] Feature branch `feature/domain-setup-rerunability` exists on `isagawa-co/isagawa-kernel`

## Requirements

### Use the test repo from 034
Continue in: `D:\my_ai_projects\project_test_repos\test-kernel-bootstrap`
(Already has kernel built from task 034)

### Install a domain spec on top
Choose one of the existing domain specs (selenium-spec recommended — most mature):
```
From: D:\my_ai_projects\project_test_repos\specs\selenium-spec\.claude\skills\
To:   D:\my_ai_projects\project_test_repos\test-kernel-bootstrap\.claude\skills\
```
Also copy any framework reference code the spec needs.

### Run domain-setup again
- Invoke `/kernel/domain-setup`
- Domain-setup should:
  - Detect existing kernel protocol and MERGE (not overwrite)
  - Add domain-specific protocol sections
  - Add domain-specific hooks (append, not overwrite)
  - Create domain-specific commands
  - Preserve existing kernel state
- **RESTART REQUIRED** after domain-setup completes

### Verify layered install
After restart, verify:
1. **Kernel still works:** `/kernel/anchor`, `/kernel/learn`, hooks still block
2. **Domain governance added:** domain-specific protocol sections exist
3. **No overwrites:** kernel protocol sections preserved alongside domain sections
4. **State merged:** both kernel and domain state coexist
5. **Commands work:** both kernel commands and domain commands functional

### Failure protocol
- Try up to 3 times
- On each failure: document what broke (especially: did kernel get overwritten?)
- After 3 failures: create `research/035-layered-setup-failures.md` with findings, move on

## Output
- Working layered install (kernel + domain) in test repo
- OR failure documentation at `research/035-layered-setup-failures.md`

## Validation
- [ ] Domain spec installed on top of existing kernel
- [ ] Domain-setup ran without overwriting kernel
- [ ] Restart completed
- [ ] Kernel commands still functional
- [ ] Domain commands functional
- [ ] Protocol has both kernel and domain sections
- [ ] State has both kernel and domain data

## Completion Signal
When ALL validation checks pass (or 3 failures documented), invoke `/kernel/complete`.
