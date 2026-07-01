# Isolation Strategy Evaluation

## Context

15 of 27 fields in sr_dev_workflow.json are per-agent. The file is majority per-agent state treated as global. Five strategies evaluated below.

## Strategy A: Per-Agent Workflow Files

**Pattern:** When `agent_id` is set, `/kernel/complete` and other commands write to `agent-{id}-workflow.json` instead of `sr_dev_workflow.json`. Same routing pattern as actions-log-appender.

**Pros:**
- Proven pattern (already works for actions log)
- Zero contention between agents
- Each agent has full cycling state independence
- Sequential (single-agent) execution unchanged — no agent_id means use shared file

**Cons:**
- Every command that writes per-agent fields needs a routing guard
- Parent must merge N workflow files after parallel completion
- 7 write consumers need modification (complete, anchor, session-start, autonomous-cycle, learn, domain-setup, hook)
- run-task.sh reads workflow state for pre-checks — needs to read agent-specific file

**Files to modify:** 7 (universal-gate-enforcer.py, complete.md, anchor.md, session-start.md, autonomous-cycle.md, run-task.sh, lib/common.sh)

**Risk:** Medium. Pattern is proven but touches many files.

## Strategy B: File Locking

**Pattern:** Advisory file lock (fcntl/msvcrt) before every read-modify-write cycle on sr_dev_workflow.json.

**Pros:**
- No file proliferation
- Single source of truth maintained

**Cons:**
- Windows compatibility (msvcrt vs fcntl) — fragile
- Deadlock risk if agent crashes while holding lock
- Adds latency to every action (hooks run on every tool call)
- Does not solve the semantic problem — agents still overwrite each other's `task_folder` and `completed_tasks`
- Lock timeout recovery is complex

**Files to modify:** Every writer (7 consumers)

**Risk:** High. Cross-platform locking is fragile, doesn't solve semantic contention, and adds latency.

**Verdict: Rejected.** Locking serializes access but agents still write conflicting values to the same fields.

## Strategy C: Carry-and-Merge

**Pattern:** Each agent carries workflow state in its prompt context (via session_state.json context field). No writes to workflow.json during execution. On completion, agent writes its final state. Parent merges.

**Pros:**
- Zero file I/O contention during execution
- Clean separation of execution and persistence

**Cons:**
- Context window cost — carrying full workflow state in prompt
- If agent crashes mid-flight, no persistent state recovery
- run-task.sh pre-checks can't read current progress (no file to read)
- Fundamentally incompatible with run-task.sh which spawns fresh `claude -p` per task — each invocation starts with no context from prior invocations

**Files to modify:** run-task.sh (major redesign), complete.md, session-start.md

**Risk:** High. Incompatible with run-task.sh's one-shot-per-task model.

**Verdict: Rejected.** run-task.sh spawns a new claude -p per task with no memory of prior tasks. State must persist on disk between invocations.

## Strategy D: Split File by Scope

**Pattern:** Keep global fields in `sr_dev_workflow.json`. Move per-agent fields to a new `cycling-state.json` (or `agent-{id}-cycling.json` when agent_id is set).

**Pros:**
- Clean conceptual separation (session config vs runtime cycling)
- Global file rarely written (only domain-setup, learn)
- Per-agent file written frequently but isolated per agent
- Migration path: add new file, update consumers, remove fields from old file

**Cons:**
- Two files to maintain instead of one (or N+1 for parallel)
- All 7 write consumers need to know which file to write
- Read consumers need to know which file to read
- More complex than Strategy A (which just routes the whole file)

**Files to modify:** Same 7 as Strategy A, plus new file creation logic

**Risk:** Medium-High. More complex than A with similar benefits.

## Strategy E: Scoped Write Guard in Commands

**Pattern:** Extend the actions-log-appender guard pattern to `/kernel/complete` and other commands. When `agent_id` is set in session_state.json, commands write per-agent fields to `agent-{id}-workflow.json` and global fields to `sr_dev_workflow.json`.

**Pros:**
- Surgical — only modifies the write path, not read path
- Global fields stay in shared file (domain-setup, learn work unchanged)
- Per-agent fields route to isolated file
- run-task.sh pre-checks read agent-specific file when agent_id is set

**Cons:**
- Each command must classify which fields are global vs per-agent (but we now have the classification table)
- Slightly more complex than Strategy A (field-level routing vs file-level routing)

**Files to modify:** 4 primary (complete.md, anchor.md, universal-gate-enforcer.py, run-task.sh/lib/common.sh)

**Risk:** Low-Medium. Surgical changes, proven pattern, classification is done.

## Comparison Matrix

| Strategy | Contention Fix | Files Changed | Sequential Compatible | Complexity | Risk |
|----------|---------------|---------------|----------------------|------------|------|
| A: Per-Agent Files | Full | 7 | Yes (no agent_id = shared) | Medium | Medium |
| B: File Locking | Partial (semantic conflict remains) | 7 | Yes | High | High |
| C: Carry-Merge | Full | Major redesign | No (incompatible with run-task.sh) | Very High | Very High |
| D: Split File | Full | 7+ | Yes | Medium-High | Medium-High |
| **E: Scoped Write Guard** | **Full** | **4** | **Yes** | **Medium** | **Low-Medium** |

## Top Candidates

**Winner: Strategy E (Scoped Write Guard)** — fewest files to change (4 vs 7), builds on proven actions-log-appender pattern, field classification already complete. Global fields (domain config, lessons) stay in shared file unchanged. Per-agent fields (cycling, tasks, anchor) route to `agent-{id}-workflow.json`.

**Runner-up: Strategy A (Per-Agent Files)** — simpler concept (whole file routing) but touches more files and requires merge logic for global fields that Strategy E avoids.

## Sequential Execution Compatibility

All strategies except C maintain backward compatibility:
- When `agent_id` is null (interactive session, single pipeline), everything writes to `sr_dev_workflow.json` as today
- When `agent_id` is set (run-task.sh one-shot agent), per-agent fields route to isolated file
- No behavior change for single-agent execution
