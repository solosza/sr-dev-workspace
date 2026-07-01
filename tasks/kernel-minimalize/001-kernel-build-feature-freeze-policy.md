# Write Feature Freeze Policy

## Context
The kernel has accumulated features that belong in extensions, not governance core. Establish a formal policy: no new commands, hooks, or skills in the kernel. Extensions exist for power users.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Create `docs/kernel-feature-freeze-policy.md`
- Define what constitutes "kernel" (governance loop + enforcement)
- List the 7 core commands: session-start, anchor, learn, complete, fix, domain-setup, reset
- List the 4 core hooks: universal-gate-enforcer, actions-log-appender, test-failure-detector, auto-approve-claude-writes
- List the 2 core skills: kernel-domain-setup, autonomous-cycling
- State the freeze rule: no new commands/hooks/skills in the kernel
- State the extension path: all new features go to workspace extensions
- Reference backlogs 147, 150

## Acceptance Criteria
- [ ] File exists: `docs/kernel-feature-freeze-policy.md`
- [ ] Lists all core governance components
- [ ] States freeze rule clearly

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
