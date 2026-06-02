# Research: Claude Code Named Agents — Kernel Integration

## Status
Open

## Priority
Medium — kernel is fully functional without this; named agents add interactive convenience and potential pipeline optimization. Not blocking any current work.

## Summary
Claude Code has a `.claude/agents/` spec for named sub-agents with YAML frontmatter, @-mention invocation, auto-delegation, and per-agent tool/model restrictions. The kernel currently uses the Agent tool programmatically via run-task.sh (batch, autonomous). Research must determine whether named agents complement the existing pattern, replace any part of it, and how they would integrate into the execute-pipeline classify-then-route dispatch.

The two use cases are distinct: named agents are on-demand interactive delegates (`@reviewer check last commit`); run-task.sh agents are kernel-governed batch executors. Research determines if/how to support both.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[115-kernel-research-claude-agents-integration/agents-spec-research]] | The `.claude/agents/` YAML spec: frontmatter fields, tool restriction, model routing, @-mention, auto-delegation, /agents command |
| [[115-kernel-research-claude-agents-integration/kernel-integration]] | Named agents for on-demand interactive use alongside pipelines — reviewer, pr-writer, security scanner |
| [[115-kernel-research-claude-agents-integration/execute-pipeline-integration]] | Whether the classify-then-route step in step-04-execute-tasks.md can use named agents instead of generic Agent tool calls |
| [[115-kernel-research-claude-agents-integration/design-decisions]] | When named agents vs run-task.sh, naming conventions, governance tradeoffs, open questions |

## Architecture

```
Current pattern:
  User → /kernel/execute-pipeline → task-builder → run-task.sh → one-shot claude -p per task

Proposed addition:
  User → @reviewer / @pr-writer / @security (on-demand, interactive)
       ↕
  Named agent in .claude/agents/ (YAML frontmatter, tool restriction, model routing)

Question: can execute-pipeline's step-04 dispatch to named agents instead of (or in addition to) generic Agent tool?
```

## Requirements
- Understand the full `.claude/agents/` YAML spec — all supported fields, behavior differences from Agent tool
- Map current kernel capabilities against what named agents add (avoid redundancy)
- Determine whether task classification in step-04-execute-tasks.md can route to named agents
- Identify which named agents would be immediately useful to create (reviewer, pr-writer, security)
- Determine governance implications: do named agents follow kernel hooks (session-start, anchor, learn)?
- Assess whether global agents (`~/.claude/agents/`) vs project agents (`.claude/agents/`) should be used

## References
- Claude Code agents spec: `~/.claude/agents/` and `.claude/agents/`
- Current execute-pipeline step-04: `.claude/skills/execute-pipeline/references/step-04-execute-tasks.md`
- Current Agent tool usage: `.claude/skills/execute-pipeline/SKILL.md`, run-task.sh
- Context: the post describing 5 ready-to-use agent templates (reviewer, test-writer, doc-writer, security, pr-writer)

## Task Builder Input
- **Deliverable:** Research report with integration recommendation — which named agents to create, how they fit the kernel, whether step-04 routing should be updated
- **Location:** `subproject:claude-agents-integration`
- **Scope:** RESEARCH
- **Constraints:** Must not break existing execute-pipeline pattern. Named agents are additive, not a replacement for run-task.sh unless research proves otherwise. Kernel governance (hooks, anchor, lessons) compatibility must be assessed.
