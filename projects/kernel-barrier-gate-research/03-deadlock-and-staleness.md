# Deadlock + Staleness Analysis for Barrier Gates

## Research Question

What failure modes arise from deliverable-based barrier gates? How do we detect or prevent deadlocks (two agents waiting on each other)? How do we handle stale prerequisites from prior runs, partial upstream outputs from skipped tasks, and other edge cases? Should barrier gates be adopted standalone or as defense-in-depth under the wave engine (backlog 241)?

## Deadlock Analysis

### Scenario: Mutual Wait

Agent A has `PRE-01: file_exists projects/B-output/report.md` and Agent B has `PRE-01: file_exists projects/A-output/report.md`. Both enter the wait/poll loop, both wait forever (until timeout).

### Detection vs Prevention

**Prevention (static, at dispatch time):**

The prerequisite declarations in gate-contract.md form a directed graph. Before spawning any agent, build the graph and check for cycles:

```
Agent A → depends on → Agent B's output
Agent B → depends on → Agent A's output
→ CYCLE DETECTED → abort swarm with error
```

This is the same topological sort that backlog 241's wave engine performs. The key insight: **if the wave engine exists, deadlock is impossible by construction** — Wave N+1 only dispatches after Wave N completes, and cycles are rejected at sort time. Barrier gates under the wave engine inherit this guarantee.

**Detection (runtime, during polling):**

If no wave engine exists (standalone barrier gates), runtime detection is needed. The monitor checks: if Agent A is WAITING on Agent B's output AND Agent B is WAITING on Agent A's output, both are deadlocked.

Implementation: when `check_prerequisites` enters the WAITING state, it writes `waiting_on: [list of prerequisite targets]` to the per-agent workflow state. The monitor reads all agent states and builds the wait-for graph. If it finds a cycle, it can:

1. **Timeout (passive):** Both agents eventually hit the 600s timeout and exit with BLOCKED status. The monitor reports the deadlock post-hoc.
2. **Active detection:** Monitor scans for cycles every poll interval. If found, it kills one of the waiting processes and marks it DEADLOCK_VICTIM, allowing the other to eventually complete and unblock a re-dispatch.

**Comparison with 241's cycle detection at sort time:**

| Approach | When | Cost | Coverage |
|----------|------|------|----------|
| 241 sort-time | Before dispatch | O(V+E) topological sort | Catches all static cycles |
| 242 runtime timeout | During execution | 600s of wasted wait time | Catches dynamic cycles only |
| 242 monitor active detection | During execution | Per-poll-interval graph scan | Catches dynamic cycles faster |

**Recommendation: Prevention via static check.** Add a cycle detection step to run-task.sh (or the spawning orchestrator) that reads all prerequisite declarations across the swarm's pipelines and rejects cycles before any agent spawns. This mirrors 241's approach at a different layer. Runtime timeout serves as a backstop for cases the static check can't see (e.g., prerequisites referencing files produced by agents in OTHER swarms).

### Static Cycle Detection (Bash-Parseable)

```bash
# Build dependency graph from all gate-contracts in the swarm
detect_cycles() {
  local task_dirs=("$@")
  local deps=""
  
  for dir in "${task_dirs[@]}"; do
    local contract="${dir}/gate-contract.md"
    if [ ! -f "$contract" ]; then continue; fi
    
    local agent_id
    agent_id=$(basename "$dir")
    
    # Extract PRE-* targets and identify which agent produces them
    grep -E '^\| PRE-' "$contract" 2>/dev/null | while IFS='|' read -r _ id type target _; do
      target=$(echo "$target" | xargs)
      # Map target path to producing agent (convention: projects/{agent-name}/...)
      local producer
      producer=$(echo "$target" | sed -E 's|^projects/([^/]+)/.*|\1|')
      if [ -n "$producer" ] && [ "$producer" != "$agent_id" ]; then
        echo "${agent_id} -> ${producer}"
      fi
    done
  done
  
  # Feed to tsort (standard Unix utility) — exits non-zero on cycles
  echo "$deps" | tsort 2>&1
  return $?
}
```

## Staleness Analysis

### Scenario: Stale Files from Prior Runs

Pipeline 242 ran yesterday, produced `projects/kernel-barrier-gate-research/research-report.md`. Today, pipeline 242 is re-run with updated tasks. Pipeline 243 has a prerequisite on that file. The STALE file from yesterday satisfies the prerequisite, but the CURRENT run hasn't produced a new version yet.

### Mitigation Options

**Option 1: Timestamp comparison**

Compare the prerequisite file's modification time against the current swarm's start time. If the file predates the swarm, it's stale. But this requires a swarm start timestamp to be written somewhere accessible, and `stat -c %Y` behavior varies across platforms.

**Option 2: Manifest-based freshness (ties into backlog 243)**

Instead of checking raw files, check a manifest that includes a run ID or timestamp. Prerequisites reference `projects/{name}/exports/manifest.json` and verify it contains the current swarm's run ID. This cleanly separates "file exists from a prior run" from "file exists from the current run."

- Pro: Definitive freshness — no timestamp ambiguity
- Con: Requires the artifact bus (backlog 243) to be adopted. Creates a hard dependency between proposals.

**Option 3: Clean workspace before dispatch**

Delete or move prior run outputs before spawning agents. If `projects/kernel-barrier-gate-research/` is emptied at swarm start, only fresh outputs will exist.

- Pro: Simple, no metadata needed
- Con: Destructive — loses prior outputs if the re-run fails partway through. Conflicts with the workspace's role as persistent storage.

**Option 4: Content-based freshness (recommended)**

Use `grep` or `word_count` prerequisites that check for content only the CURRENT run would produce. For example:

```markdown
| PRE-01 | grep | projects/kernel-dag-wave-research/research-report.md | Verdict |
```

A stale report from a prior run that reached the verdict stage would still satisfy this — but that's acceptable because the content is still CORRECT even if not fresh. The real danger is a stub file (headers only, no verdict) from a PARTIAL prior run.

**Recommendation: Combine content assertion + documentation.** Use `grep`/`word_count` prerequisites to verify the upstream output is COMPLETE (not just present), and document in the gate-contract.md that prerequisites reference outputs from specific backlogs. Staleness from successful prior runs is acceptable — the content is valid. Staleness from partial prior runs is caught by content assertions.

### Scenario: Partial Upstream Outputs (Skipped Tasks)

Pipeline 241 runs 5 tasks. Tasks 001-003 complete, task 004 fails 3 times and is SKIPPED, task 005 (which writes the final report) depends on 004 and either runs with incomplete input or is also skipped.

If pipeline 242 has a prerequisite on 241's final report:
- If task 005 was skipped: the report doesn't exist → prerequisite fails → 242 enters WAITING → eventually times out → BLOCKED. Correct behavior.
- If task 005 ran with incomplete input: the report exists but may be incorrect → prerequisite passes (file exists) → 242 runs on bad data. Incorrect behavior.

**Mitigation: Upstream completion status check.**

Before evaluating prerequisites, check whether the upstream pipeline completed successfully. The per-agent workflow state has `complete: true` and `skipped_tasks: []`. If the upstream has skipped tasks, treat its outputs as unreliable.

```bash
# Check if upstream agent completed successfully (no skipped tasks)
check_upstream_health() {
  local upstream_agent_id="$1"
  local upstream_state="${STATE_DIR}/agent-${upstream_agent_id}-workflow.json"
  
  if [ ! -f "$upstream_state" ]; then
    return 1  # Upstream state not found — cannot verify
  fi
  
  local skipped
  skipped=$(python -c "
import json
w = json.loads(open('${upstream_state}').read())
skipped = w.get('skipped_tasks', [])
print(len(skipped))
" 2>/dev/null || echo "-1")
  
  if [ "$skipped" != "0" ]; then
    echo "[WARN] Upstream agent ${upstream_agent_id} has ${skipped} skipped tasks"
    return 1
  fi
  return 0
}
```

This adds a soft check — the prerequisite file exists AND the upstream completed cleanly. If the upstream has skips, the downstream can still proceed (the prerequisite file exists) but with a warning logged for the monitor to surface.

## Standalone vs Defense-in-Depth Recommendation

### Standalone Barrier Gates (242 only)

Barrier gates without the wave engine (241) CAN work:
- Prerequisites declare inter-pipeline dependencies
- run-task.sh polls before spawning
- Timeout + BLOCKED status handles failures
- Static cycle detection prevents deadlocks

But standalone barrier gates have weaknesses:
1. **Cost:** Idle processes polling in wait loops (10MB each, 15s intervals)
2. **No global ordering:** Each pipeline only sees its own prerequisites, not the swarm's dependency DAG. The orchestrator has no global view of which pipelines should run first.
3. **Deadlock detection is reactive:** Cycles in the prerequisite graph might not be caught until runtime if the static check doesn't cover cross-swarm dependencies.
4. **Re-dispatch is manual:** When a BLOCKED pipeline's upstream finishes, someone (user or monitor) must re-dispatch it.

### Defense-in-Depth Under the Wave Engine (241 + 242)

The wave engine provides the PRIMARY ordering:
- Topological sort eliminates deadlocks by construction
- Wave barriers eliminate idle polling — downstream agents aren't spawned until upstream waves complete
- The monitor already handles wave dispatch — no new re-dispatch mechanism needed

Barrier gates provide SECONDARY defense:
- Catch intra-wave ordering violations (two agents in the same wave where one actually depends on the other's output)
- Catch cross-swarm dependencies that the wave DAG doesn't model
- Provide per-prerequisite granularity (wave barriers are all-or-nothing; prerequisites can be per-file)
- Serve as a runtime validation that the wave engine's ordering was correct

### Recommendation: Defense-in-depth, not standalone

Barrier gates are most valuable as a safety net under the wave engine. Standalone, they work but are costly and lack global ordering intelligence. Under the wave engine, they add per-file granularity and catch edge cases the DAG doesn't model.

**If 241 is adopted:** Implement barrier gates as a lightweight `check_prerequisites` function in run-task.sh. Prerequisites are checked once at pipeline start (not per-task). Timeout is short (120s instead of 600s) because the wave engine should have already ensured upstream completion — a missing prerequisite at this point indicates a bug, not a timing issue.

**If 241 is NOT adopted:** Barrier gates CAN serve as a standalone ordering mechanism, but the orchestrator should add the static cycle detection step and the monitor should add BLOCKED → re-dispatch logic. The 600s timeout and full wait/poll loop are needed in this case.

## Conclusion

Deadlocks are best prevented statically (cycle detection at dispatch time), matching 241's approach. Staleness is mitigated by content-based prerequisites (grep/word_count) rather than timestamp comparison. Partial upstream outputs require checking the upstream agent's completion status alongside the prerequisite file. Barrier gates are recommended as defense-in-depth under the wave engine (241), not as a standalone ordering mechanism — the wave engine handles global ordering; barrier gates handle per-file validation.
