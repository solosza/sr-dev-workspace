# Execute-Pipeline Integration — Named Agents in Classify-Then-Route Dispatch

## Status
NEW — step-04-execute-tasks.md currently routes to Agent tool or run-task.sh only

## Context
The current classify-then-route step in step-04-execute-tasks.md classifies tasks as simple (inline) or complex (run-task.sh). Named agents introduce a third possible route: dispatch to a named `.claude/agents/` agent instead of spawning a generic `claude -p` via run-task.sh.

## Research Questions

### Can task files specify a named agent?
Could a task file include a frontmatter field or section that tells step-04 to dispatch to a specific agent?

Example:
```markdown
## Execution
agent: @reviewer
```

Would step-04 detect this and dispatch `@reviewer` instead of run-task.sh?

### What would this buy us?
- Named agents have pre-configured tool restrictions and model routing
- They don't need run-task.sh overhead (bash subprocess, env -u CLAUDECODE, etc.)
- They can be leaner for focused tasks

### What would we lose?
- Named agents likely don't follow kernel governance (session-start, anchor, complete, learn)
- No gate contract enforcement
- No `completed_tasks` state tracking
- No retry logic from run-task.sh
- No attestation

### The real question: is there a hybrid model?
Could step-04 use named agents for lightweight classify-and-review tasks while keeping run-task.sh for all BUILD and RESEARCH tasks that need kernel governance?

Example routing table:
| Task type | Route |
|-----------|-------|
| BUILD | run-task.sh (kernel-governed) |
| RESEARCH | run-task.sh (kernel-governed) |
| TEST (structural) | @security or @reviewer (lightweight) |
| TEST (functional) | run-task.sh (needs isolation + gate contract) |
| VERIFY (quick) | named agent (no kernel overhead needed) |

## What to Produce
- Decision: should step-04-execute-tasks.md be updated to support a third route (named agent)?
- If yes: what task file syntax signals named agent dispatch?
- If yes: which task types are appropriate for named agent dispatch vs run-task.sh?
- Updated routing table for step-04 (or note that current routing is sufficient)

## Dependencies
- agents-spec-research.md (isolation model determines governance compatibility)
- kernel-integration.md (which agents exist to route to)
