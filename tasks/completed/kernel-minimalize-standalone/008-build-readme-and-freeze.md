# Update README and Write Feature Freeze Policy

## Type
BUILD

## Phase Gate
Task 007 must be complete.

## Deliverable
Minimal README.md + `docs/kernel-feature-freeze-policy.md`.

## Instructions
Working in `D:\my_ai_projects\project_test_repos\kernel-minimal`:

1. **Update README.md** to describe the minimal kernel:
   - What it is: agent runtime and governance system
   - What it contains: the loop (7 commands), enforcement (4 hooks), domain-setup (2 skills)
   - What it does NOT contain: no task-builder, no execute-pipeline, no attestation, no extensions
   - How to use: clone into any repo, run domain-setup, the agent self-builds its governance

2. **Create `docs/kernel-feature-freeze-policy.md`:**
   - Policy: no new commands, hooks, or skills in the kernel
   - Core list: the 7 commands, 4 hooks, 2 skills
   - Extensions go in workspace-level `.claude/` additions, not in the kernel repo
   - Rationale: minimal governance layer, not an application framework

## Verification
- `docs/kernel-feature-freeze-policy.md` exists
- README.md does not mention extension commands
