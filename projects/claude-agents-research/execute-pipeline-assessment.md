# Execute-Pipeline Integration Assessment — Named Agent Dispatch

**Date:** 2026-06-01
**Dependencies:** agents-spec-summary.md, kernel-integration-assessment.md

---

## Current State: Two-Route Design

Step-04-execute-tasks.md classifies tasks into two routes:

| Route | Target | Overhead | Governance |
|-------|--------|----------|------------|
| **Simple** (inline) | Autonomous-cycle in outer agent | ~0s | Full kernel (session-start, anchor, complete) |
| **Complex** (run-task.sh) | Spawned `claude -p` per task | ~30s per task | Full kernel (one-shot agents do session-start, anchor, complete) |

Both routes produce kernel-governed output: anchored, tracked in actions.jsonl, gate-contract verified, completed_tasks updated.

---

## The Third Route Concept: Named Agent Dispatch

A third route would dispatch certain tasks to named agents (e.g., `@reviewer`, `@security`) instead of running them inline or via run-task.sh. The task file would signal this with syntax like:

```markdown
## Execution
agent: @reviewer
```

The execute-pipeline classifier would recognize this and invoke the named agent instead of inline execution or run-task.sh.

---

## Gains vs Losses: Named Agent Dispatch vs run-task.sh

### What named agent dispatch gains

| Gain | Detail |
|------|--------|
| **Tool restriction** | Named agents can be locked to Read/Glob/Grep only — impossible to accidentally Write or Edit. run-task.sh agents have full tool access. |
| **Model routing (static)** | Agent YAML specifies model (haiku for summarization, sonnet for review). No need for model-router.sh keyword heuristics. |
| **Lower overhead** | No `claude -p` subprocess spawn (~30s saved per task). Named agent invocation is near-instant. |
| **Specialized system prompt** | Agent carries its own domain expertise (review rules, security patterns) in its body. run-task.sh agents rely on CLAUDE.md + task file only. |
| **Background execution** | `background: true` agents run concurrently. run-task.sh is strictly sequential. |

### What named agent dispatch loses

| Loss | Detail | Severity |
|------|--------|----------|
| **Kernel governance** | Named agents do NOT inherit parent hooks. No universal-gate-enforcer, no actions-log-appender, no test-failure-detector. | **Critical** |
| **Gate contract verification** | run-task.sh agents verify acceptance criteria via `/kernel/complete`. Named agents have no built-in gate mechanism. | **Critical** |
| **Attestation trail** | run-task.sh agents update `completed_tasks` in workflow state. Named agents don't know about this state file. | **High** |
| **Retry/upgrade logic** | run-task.sh retries failed tasks with model upgrade (haiku → sonnet → opus). Named agents have no retry mechanism. | **Medium** |
| **State tracking** | run-task.sh agents append to actions.jsonl. Named agent actions are invisible to the kernel unless hooks are manually wired. | **High** |
| **No nesting** | Named agents cannot spawn sub-agents. A @reviewer can't delegate to @security. Limits composability. | **Low** |

### Trade-off summary

The gains are real but narrow: tool restriction and model routing are genuinely useful for lightweight, read-only verification tasks. The losses are structural: named agents operate outside the kernel's enforcement loop. Wiring hooks into agent YAML partially mitigates this, but creates state contention (documented in kernel-integration-assessment.md and state-contention.md lesson).

---

## Proposed Routing Table (If Third Route Added)

| Task Type | Route | Rationale |
|-----------|-------|-----------|
| BUILD | run-task.sh | Writes files. Needs full kernel governance, gate contracts, attestation. |
| RESEARCH | run-task.sh | Produces deliverable docs. Needs completed_tasks tracking and acceptance criteria verification. |
| TEST (structural — does it exist?) | **named agent** | Read-only verification. @reviewer with Read/Glob/Grep can check file existence, naming, structure. No writes needed. |
| TEST (functional — does it run?) | run-task.sh | Runs code, needs Bash, needs test-failure-detector hook, needs isolation. |
| VERIFY (quick — grep acceptance criteria) | **named agent** | Read-only, fast. Named agent checks grep patterns against deliverables. |
| VERIFY (complex — run and validate output) | run-task.sh | Needs Bash execution, isolation, retry logic. |

### What this means in practice

In a typical 6-task pipeline (like this claude-agents-research batch):
- Tasks 001-004: RESEARCH/BUILD → run-task.sh (4 tasks)
- Task 005: BUILD → run-task.sh (1 task)
- Task 006: BUILD → run-task.sh (1 task)

**Zero tasks would route to named agents.** The third route only activates for structural TEST and quick VERIFY tasks — which are uncommon in current task decomposition patterns. Most verification happens inside `/kernel/complete`, not as separate tasks.

---

## Hybrid Model Assessment

A hybrid model where named agents handle lightweight classify-and-review while run-task.sh handles all production work:

**How it would work:**
1. After run-task.sh completes a batch, @reviewer scans all deliverables for quality
2. @security scans all code for vulnerabilities
3. Results feed back to the outer agent for /kernel/complete

**This is already possible without a third route.** The outer agent can invoke @reviewer or @security at any time — it doesn't need to be wired into the execute-pipeline classifier. Named agents are complementary tools, not a replacement route.

**Key insight:** Named agents are best used as **post-execution validators**, not as **task executors**. They validate what run-task.sh produced, rather than replacing run-task.sh for certain task types.

---

## Go/No-Go Recommendation

**Recommendation: NO-GO on adding a third route to step-04.**

### Rationale

1. **The losses outweigh the gains for task execution.** Kernel governance (hooks, gate contracts, attestation, retry) is non-negotiable for task completion. Named agents lack all of these by default, and retrofitting them creates state contention.

2. **The efficiency gain is marginal.** The ~30s overhead per run-task.sh task is acceptable. In a 6-task pipeline, that's 3 minutes total. Named agent dispatch saves this but loses attestation — bad trade-off.

3. **The target task types barely exist.** Structural TEST and quick VERIFY tasks are uncommon in current decomposition patterns. Most verification is embedded in `/kernel/complete`, not separate task files.

4. **Named agents add value elsewhere.** @reviewer, @security, and @pr-writer are genuinely useful — but as on-demand tools invoked by the outer agent or by run-task.sh one-shot agents, not as a third execution route in the pipeline classifier.

### What to do instead

- **Deploy @reviewer and @security as project-level agents** (`.claude/agents/`)
- **Use them from the outer agent** for post-batch review (after run-task.sh completes)
- **Use them from one-shot agents** when a task's acceptance criteria include "review" or "security scan"
- **Keep the two-route design** (simple inline, complex run-task.sh) — it's working and kernel-governed

The third route solves a problem that doesn't exist in practice. Named agents are powerful tools — just not as pipeline execution routes.
