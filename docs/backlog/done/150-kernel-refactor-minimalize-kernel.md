# Minimalize the Kernel — Feature Freeze and Strip Down

## Status
Open

## Priority
High — the kernel is a governance layer, not an application framework. Every feature added dilutes the core purpose and makes the three-way sync problem (backlog 147) worse.

## Summary
The kernel has accumulated features that belong in extensions or workspaces, not in the governance core. A kernel for governance should be minimal: the loop (session-start, anchor, work, learn, complete), enforcement hooks, and domain-setup. Everything else is extension. This backlog establishes a feature freeze on the kernel and plans a strip-down pass to remove anything that isn't core governance. No more features. Keep it minimal. It's a kernel.

## Principles
- The kernel governs. It does not build, test, deploy, or orchestrate.
- If it's not part of the loop or enforcement, it's not kernel.
- Fewer files = easier sync, easier adoption, easier reasoning.
- Extensions exist for power users. The kernel exists for everyone.

## What Stays (Core Governance)
- Commands: session-start, anchor, learn, complete, fix, domain-setup, reset
- Hooks: universal-gate-enforcer.py, actions-log-appender.py, test-failure-detector.py, auto-approve-claude-writes.py
- Scripts: CLAUDE.md, run-task.sh, common.sh
- Skills: kernel-domain-setup/, autonomous-cycling/
- Lessons: lessons.md (template with RULE ZERO only)

## What Gets Removed or Moved to Extensions
- execute-pipeline, task-builder, prod-test, spawn-agent-swarm, audit-workflow
- backlog, attest, scan-bookmarks
- elegant, grill, clone, spawn-subagent
- Any future feature proposals go to extensions, not kernel

## Requirements
- Establish feature freeze policy: no new commands, hooks, or skills in the kernel
- Document what's kernel vs extension (aligns with backlog 147 kernel-manifest)
- Strip non-governance items from isagawa-kernel repo
- Update CLAUDE.md to reflect minimal kernel only
- Update domain-setup to only install minimal kernel files
- Extensions that are currently in the kernel namespace get moved out

## Relationship to Other Backlogs
- **147** — Define kernel boundary (detailed technical plan for the separation)
- **148** — Site pivot research (messaging should reflect minimal governance framing)
- **149** — Resume rewrite (should describe the kernel as minimal governance, not a feature-rich platform)

## References
- Backlog 147: `docs/backlog/147-kernel-refactor-define-kernel-boundary.md` (detailed separation plan)
- isagawa-kernel repo: the target of this minimalization
- Current CLAUDE.md in this workspace (shows bloat — lists 12+ commands for a "minimal" kernel)

## Task Builder Input
- **Deliverable:** Minimalized kernel repo with feature freeze policy, stripped of non-governance items
- **Location:** workspace
- **Scope:** REFACTOR
- **Constraints:** Must not break existing workspaces that use extensions (they keep their copies). Backlog 147 is the technical implementation plan. This backlog is the strategic decision and policy.
