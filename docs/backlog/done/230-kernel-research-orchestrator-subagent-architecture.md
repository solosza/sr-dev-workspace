# Orchestrator + Single-Task Subagent Architecture — Is It Right for This Platform?

## Status
Open

## Priority
Medium — architecture strategy; informs command evolution but blocks nothing in the running vertical build

## Summary
Research whether some workspace commands should become orchestrators that delegate to subagents, where each subagent has exactly one specific task. Evaluate whether that architecture fits this platform (kernel commands + the HMSA QA Platform build system). Note the workspace already runs TWO tiers of this pattern — the pipeline level (orchestrator session + one-shot run-task.sh agents, one task each) and prod-test — while a standing user policy (lesson, 2026-04-04) forbids agent spawning elsewhere. This research decides whether that policy should evolve, command by command.

## Requirements
- Map the current architecture honestly first: which commands are already orchestrator-shaped (execute-pipeline, prod-test, spawn-agent-swarm, run-task.sh one-shot agents = single-task subagents), which run inline (gap-check, walkthrough, backlog, anchor, eval), and why the 2026-04-04 no-spawn lesson exists (latency, context loss, user preference for direct work)
- Industry survey (sourced): orchestrator-worker patterns (Claude Code subagents + Agent tool semantics, Anthropic multi-agent guidance, LangGraph supervisor pattern, swarm frameworks) — when single-responsibility subagents win vs when inline wins
- Cost/benefit per candidate command: context isolation (subagent tool output stays out of parent context), parallelism, state isolation (per-agent lessons 2026-06-14), specialization vs latency, loss of conversation context, orchestration overhead, review/gate complexity
- Evaluate specifically for: gap-check (per-check subagents?), eval platform (per-metric?), audit-workflow (per-scan?), task-builder plan review (already spec'd as an automated agent check), the vertical build chain's validate-merge-launch loop, and the /kernel/project-run outer-loop candidate noted in the platform README
- Deliverable: recommendation matrix — per command: stay-inline / orchestrator+subagents / hybrid, with the decision criterion stated generically so future commands self-classify; explicit recommendation on whether to amend the 2026-04-04 lesson
- Honest constraints section: kernel governance implications (hooks/state per subagent — per-agent isolation pattern already exists), sequential-target-repo constraint from the vertical build

## References
- projects/hmsa-qa-platform/README.md (platform context, /kernel/project-run outer-loop note in Process section)
- .claude/lessons/lessons.md — 2026-04-04 no-spawn lesson; 2026-06-14 multi-agent orchestration + state isolation lessons
- .claude/skills/spawn-agent-swarm/, .claude/skills/spawn-subagent/, .claude/skills/prod-test/ (existing orchestrator implementations)
- docs/walkthroughs/ ledgers (walkthrough composability contract — designed for later orchestration)
- projects/multi-persona-architecture/ and projects/loop-composability-research/ (prior related research, check for overlap)

## Task Builder Input
- **Deliverable:** Research report with current-state map, industry survey (sourced), per-command recommendation matrix, generic decision criterion, and an explicit recommendation on amending the 2026-04-04 no-spawn lesson
- **Location:** subproject:orchestrator-subagent-research
- **Scope:** RESEARCH
- **Constraints:** Web research required for the industry survey (claims sourced). Must engage the existing lessons rather than ignore them — the report's recommendation stands or falls on how it handles the recorded failure history (state contention, visibility loss, latency complaints). Read prior research projects first to avoid duplicating existing findings. No code changes; recommendations only. Runs AFTER the current V1 chain link completes if executed via the loop (sequential pipeline rule).
