# Minimalize Kernel as Standalone Local Repo

## Status
Open

## Priority
High -- this is the safe path to minimalization. Work in a standalone copy, validate it works, then push to the golden master.

## Summary
Take the minimalization plan from backlog 150 and execute it in a new standalone local repo instead of modifying the golden master (isagawa-kernel). Copy the current kernel source into a fresh repo at `D:\my_ai_projects\project_test_repos\kernel-minimal`, strip it down to core governance only, establish the feature freeze policy, and validate the minimal kernel can still domain-setup + run tasks. The golden master stays untouched until this is proven.

## Requirements
- Create new repo at `D:\my_ai_projects\project_test_repos\kernel-minimal`
- Copy current isagawa-kernel source as starting point
- Strip to core only (per backlog 150's "What Stays" list):
  - Commands: session-start, anchor, learn, complete, fix, domain-setup, reset
  - Hooks: universal-gate-enforcer.py, actions-log-appender.py, test-failure-detector.py, auto-approve-claude-writes.py
  - Scripts: CLAUDE.md, run-task.sh, lib/common.sh
  - Skills: kernel-domain-setup/, autonomous-cycling/
  - Lessons: lessons.md (template with RULE ZERO only)
- Remove everything else (execute-pipeline, task-builder, prod-test, spawn-agent-swarm, audit-workflow, backlog, attest, scan-bookmarks, elegant, grill, clone, spawn-subagent)
- Update CLAUDE.md to reflect minimal kernel only
- Validate: run domain-setup in a test workspace, confirm the loop works (session-start, anchor, work, learn, complete)
- Do NOT touch the golden master at github.com/isagawa-co/isagawa-kernel

## References
- Backlog 150: `docs/backlog/150-kernel-refactor-minimalize-kernel.md` (strategic plan)
- isagawa-kernel repo: `D:\my_ai_projects\isagawa-kernel` (golden master, do not modify)
- Feature freeze policy: `docs/kernel-feature-freeze-policy.md`
- Core vs extension classification: `docs/kernel-core-vs-extension.md`

## Task Builder Input
- **Deliverable:** Standalone minimal kernel repo, stripped to core governance, validated with domain-setup + loop test
- **Location:** `new-repo:D:\my_ai_projects\project_test_repos\kernel-minimal`
- **Scope:** REFACTOR
- **Constraints:** Golden master untouched. Must pass domain-setup and full loop validation in a test workspace before considered done.
