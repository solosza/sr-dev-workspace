# Design Decisions — Named Agents vs run-task.sh

## Status
NEW — to be resolved by research

## Core Decision: When Named Agents, When run-task.sh

### Named agents are the right choice when:
- Task is interactive and on-demand (user-triggered, not pipeline-triggered)
- Task is stateless (no need to write to `completed_tasks`, no gate contract)
- Task is a quality check, not a deliverable producer
- Context isolation is desired but kernel governance overhead is not needed
- Task is sub-10-minute work

### run-task.sh is the right choice when:
- Task is part of a pipeline (tracked in `completed_tasks`, has a gate contract)
- Task produces a file artifact that is attested
- Task needs kernel governance (anchor, learn, lessons)
- Task may fail and needs retry logic
- Task chains into a subsequent task via shared state

### The dividing line:
Named agents = quality assurance layer (review, scan, describe)
run-task.sh = production layer (build, research, test with attestation)

## Open Questions to Resolve

1. **Governance inheritance:** Do named agents inherit PreToolUse/PostToolUse hooks from the parent session? If yes, do they need to do session-start + anchor? If no, they bypass the kernel entirely — is that acceptable?

2. **Auto-delegation risk:** If auto-delegation is enabled and a user says "review this" during an execute-pipeline run, could Claude auto-route to @reviewer mid-pipeline? Would this cause state contention?

3. **Global vs project placement:**
   - `.claude/agents/` — version-controlled with the workspace, shared via git
   - `~/.claude/agents/` — global, available in all repos including isagawa-co.github.io
   - Recommendation likely: @reviewer and @security in `~/.claude/agents/` (useful everywhere), @pr-writer in `~/.claude/agents/` too

4. **Model routing:** Current run-task.sh has model routing (backlog 087). Named agents specify model in YAML. These are independent — named agents bypass run-task.sh routing entirely. Is there a conflict?

5. **Naming convention:** Kernel commands use kebab-case (`kernel:anchor`). Named agents use single words (`reviewer`). No conflict since they're different invocation mechanisms.

## Resolved Decisions (will be filled in after research)
- [ ] Named agents inherit kernel hooks: YES / NO
- [ ] Auto-delegation: ENABLE / DISABLE / SELECTIVE
- [ ] Placement: global vs project
- [ ] step-04 update: YES (add agent route) / NO (keep current two routes)

## What to Produce
- Resolved decision table (all 5 open questions answered)
- Naming conventions for agent files
- Governance model recommendation
