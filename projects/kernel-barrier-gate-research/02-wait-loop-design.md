# Wait/Poll Loop Design + Monitor Visibility

## Research Question

How should run-task.sh implement the wait/poll loop for prerequisite barriers? What poll interval, timeout, and timeout behavior should it use? How does a WAITING agent expose its state to the swarm monitor without being mistaken for a stalled/failed agent? What is the cost of polling vs wave-based non-spawning (backlog 241)?

## Wait/Poll Loop Design

### Location in run-task.sh

The wait loop MUST execute BEFORE `run_claude` is called — between the pre-iteration state setup and the `claude -p` spawn. This preserves the one-shot agent contract: the agent itself never knows about prerequisites or waiting. It receives a task, executes it, and reports completion. The barrier is an infrastructure concern, not an agent concern.

```bash
# Insertion point in main loop (after pre_init_state, before run_claude):

# Check prerequisites from gate-contract.md
check_prerequisites "$TASK_DIR"
# ^ This function blocks until all PRE-* entries are satisfied or timeout
```

### Poll Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Poll interval | 15 seconds | Balances responsiveness with I/O overhead. File existence checks are near-zero cost on local filesystem. Shorter intervals (5s) waste CPU in tight loops; longer (60s) add unnecessary latency when an upstream agent finishes mid-interval. |
| Timeout | 600 seconds (10 min) | Matches `TASK_TIMEOUT` in run-task.sh (currently 600s for claude -p invocations). A prerequisite that hasn't appeared in 10 minutes is likely from a failed or stalled upstream agent, not one still running. |
| Max polls | 40 (600/15) | Derived from timeout/interval. |

### Timeout Behavior

Three options analyzed:

**Option A: Skip per cycling contract (3-attempt rule)**

When the prerequisite times out, treat it like a task failure: increment the failure counter, skip to the next task. If the prerequisite is pipeline-scoped (all tasks need it), every task would fail and the pipeline aborts after `MAX_CONSECUTIVE_FAILS` (currently 4).

- Pro: Consistent with existing failure handling — no new behavior
- Con: Wasteful — 4 task attempts, each waiting 10 minutes, before the pipeline gives up (40 minutes of pure waiting)

**Option B: Abort run immediately**

If any prerequisite times out, exit the entire run-task.sh with a clear error message. The upstream pipeline needs to finish first.

- Pro: Fast failure — no wasted time polling
- Con: Too aggressive — a transient upstream delay (agent retrying, slow model) would kill the downstream pipeline

**Option C: Mark BLOCKED and skip remaining (recommended)**

On prerequisite timeout, mark the pipeline as BLOCKED in the per-agent workflow state, log the specific prerequisite that failed, and exit with a distinct exit code (exit 2, distinct from success=0 and failure=1). The swarm monitor reads BLOCKED state and can re-dispatch the pipeline later.

```bash
if ! check_prerequisites "$TASK_DIR"; then
  echo "[BLOCKED] Prerequisites not met after ${PREREQ_TIMEOUT}s"
  echo "[BLOCKED] Missing: $MISSING_PREREQS"
  update_agent_state "status=BLOCKED" "blocked_by=$MISSING_PREREQS"
  exit 2
fi
```

- Pro: Clear failure mode — the monitor distinguishes BLOCKED (waiting for upstream) from FAILED (code/logic error) from COMPLETE
- Pro: No wasted iterations — one timeout, one exit, one re-dispatch when upstream finishes
- Pro: Composable with 241's wave engine — if the wave engine exists, prerequisites are defense-in-depth; if not, BLOCKED + re-dispatch is a lightweight ordering mechanism

**Recommendation: Option C (BLOCKED + re-dispatch).** The swarm monitor already polls per-agent state files; adding a BLOCKED status is a one-field change. Re-dispatch can be manual (user runs the pipeline again) or automatic (monitor detects upstream COMPLETE → re-fires downstream BLOCKED pipeline).

### Implementation Shape

```bash
check_prerequisites() {
  local task_dir="$1"
  local gate_contract="${task_dir}/gate-contract.md"
  
  if [ ! -f "$gate_contract" ]; then
    return 0  # No gate contract = no prerequisites
  fi
  
  # Extract PRE-* entries
  local prereqs
  prereqs=$(grep -E '^\| PRE-' "$gate_contract" 2>/dev/null || true)
  
  if [ -z "$prereqs" ]; then
    return 0  # No prerequisites declared
  fi
  
  local elapsed=0
  local poll_interval=15
  local timeout=600
  
  while [ "$elapsed" -lt "$timeout" ]; do
    local all_met=true
    MISSING_PREREQS=""
    
    while IFS='|' read -r _ id type target desc _; do
      id=$(echo "$id" | xargs)
      type=$(echo "$type" | xargs)
      target=$(echo "$target" | xargs)
      
      case "$type" in
        file_exists)
          if [ ! -f "$target" ]; then
            all_met=false
            MISSING_PREREQS="${MISSING_PREREQS}${id}:${target} "
          fi
          ;;
        grep)
          # target format: "path | pattern"
          local file pattern
          file=$(echo "$target" | cut -d'|' -f1 | xargs)
          pattern=$(echo "$desc" | xargs)
          if [ ! -f "$file" ] || ! grep -q "$pattern" "$file" 2>/dev/null; then
            all_met=false
            MISSING_PREREQS="${MISSING_PREREQS}${id}:${file} "
          fi
          ;;
        word_count)
          local file min_words
          file=$(echo "$target" | xargs)
          min_words=$(echo "$desc" | grep -oE '[0-9]+' | head -1)
          if [ ! -f "$file" ]; then
            all_met=false
            MISSING_PREREQS="${MISSING_PREREQS}${id}:${file} "
          else
            local wc
            wc=$(wc -w < "$file" 2>/dev/null || echo 0)
            if [ "$wc" -lt "${min_words:-0}" ]; then
              all_met=false
              MISSING_PREREQS="${MISSING_PREREQS}${id}:${file}(${wc}w<${min_words}) "
            fi
          fi
          ;;
      esac
    done <<< "$prereqs"
    
    if [ "$all_met" = true ]; then
      echo "[PREREQS] All prerequisites met."
      return 0
    fi
    
    echo "[WAITING] Prerequisites not yet met (${elapsed}s/${timeout}s): $MISSING_PREREQS"
    sleep "$poll_interval"
    elapsed=$((elapsed + poll_interval))
  done
  
  return 1  # Timeout — prerequisites not met
}
```

## WAITING State Exposure for Monitor Visibility

### The Problem

The swarm monitor polls per-agent state files (`agent-{id}-workflow.json`) to detect agent status. Currently it distinguishes:
- RUNNING: agent spawned, no completion signal yet
- COMPLETE: `complete: true` in workflow state
- FAILED/SKIPPED: task in `skipped_tasks`, or `cycling_complete: true` with incomplete tasks

A WAITING agent (blocked on prerequisites) looks identical to a RUNNING agent — the monitor cannot tell the difference, and may false-positive a waiting agent as stalled after its usual polling window.

### Solution: Status Field in Per-Agent Workflow State

Add a `status` field to `agent-{id}-workflow.json`:

```json
{
  "status": "WAITING",
  "waiting_on": ["PRE-01:projects/kernel-dag-wave-research/research-report.md"],
  "waiting_since": "2026-07-21T23:10:00Z"
}
```

Status values:
- `null` or `"IDLE"` — not yet started
- `"RUNNING"` — agent spawned, working
- `"WAITING"` — prerequisites not met, polling
- `"BLOCKED"` — prerequisites timed out, pipeline exited
- `"COMPLETE"` — all tasks done

The monitor rule change: when `status == "WAITING"`, do NOT count the elapsed time toward the stall detection threshold. Instead, log "Agent {id} WAITING on {prereqs}" and check whether the upstream agent (whose output is being waited on) is still RUNNING. If the upstream is COMPLETE but the file still doesn't exist, THAT is the real error — the upstream completed without producing the expected output.

### Monitor Detection Rules

```
Agent status = WAITING:
  ├─ Upstream agent RUNNING → normal, keep waiting
  ├─ Upstream agent COMPLETE → ERROR (output not produced)
  ├─ Upstream agent BLOCKED → DEADLOCK candidate (see task 004)
  └─ Upstream agent FAILED → ERROR (dependency failed)
```

## Cost Comparison: Polling vs Wave-Based Non-Spawning (Backlog 241)

### Polling Cost (This Proposal)

- **Process cost:** One run-task.sh bash process per waiting pipeline, sleeping in a loop. On Windows (Git Bash), each process holds ~10MB of memory. For a 5-pipeline swarm with 2 blocked pipelines: ~20MB overhead.
- **I/O cost:** One `test -f` syscall per prerequisite per poll interval (15s). Negligible — file existence checks are cached by the OS.
- **Time cost:** Up to 600s (10 min) of wall-clock time per blocked pipeline. If the upstream finishes in 2 minutes, the downstream waits at most 2 min + 15s (next poll).
- **Total cost for the swarm:** Sum of all WAITING times across pipelines. In the worst case (all pipelines chained sequentially), this equals the sequential execution time — no worse than today's STRICTLY_SEQUENTIAL rule.

### Wave-Based Non-Spawning Cost (Backlog 241)

- **Process cost:** Zero — downstream agents are never spawned until their wave is dispatched. No idle processes.
- **I/O cost:** The monitor polls per-agent state files to detect wave completion (already does this). No additional cost.
- **Time cost:** Zero idle time — downstream agents start immediately when the wave barrier lifts. Latency = monitor poll interval (currently ~30s in spawn-agent-swarm).
- **Total cost for the swarm:** Only the monitor process runs between waves.

### Comparison

| Dimension | Polling (242) | Waves (241) |
|-----------|--------------|-------------|
| Idle processes | 1 per blocked pipeline | 0 |
| Memory overhead | ~10MB per blocked process | 0 |
| Latency to start | Up to poll_interval (15s) | Up to monitor_interval (~30s) |
| Failure granularity | Per-prerequisite | Per-wave |
| Implementation complexity | ~50 lines of bash (check_prerequisites) | Topological sort + wave dispatch + barrier monitor |
| Defense-in-depth | Yes (catches intra-wave ordering) | No (assumes wave boundaries are sufficient) |

**Verdict on cost:** Wave-based non-spawning (241) is cheaper by every measure EXCEPT implementation complexity and defense-in-depth. Polling is wasteful but not prohibitively so — 10MB per process and 15s latency are acceptable for swarms of <10 pipelines (current scale). At scale (50+ pipelines), idle polling processes become a concern and wave-based dispatch is clearly superior.

## Conclusion

The wait/poll loop should use 15s intervals, 600s timeout, and BLOCKED exit code (2) on timeout. Per-agent workflow state gains a `status` field (WAITING/BLOCKED/RUNNING/COMPLETE) for monitor visibility. The cost is acceptable at current scale (<10 pipelines) but wave-based dispatch (241) is more efficient and should be the primary ordering mechanism if adopted. Barrier gates are best positioned as defense-in-depth under the wave engine — catching intra-wave ordering violations that the wave DAG doesn't model.
