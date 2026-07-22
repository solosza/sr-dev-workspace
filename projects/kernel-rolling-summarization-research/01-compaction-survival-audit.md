# Compaction Survival Audit

## Purpose

Audit what state survives context-window compaction in a live kernel session, across the three persistence layers: (1) `session_state.json` context key, (2) workflow JSON files, (3) harness-generated compaction summary. Identify what signal is lost and whether existing mechanisms adequately recover it.

## The Three State Layers

### Layer 1: session_state.json `context` key

The anchor ceremony (Step 10) writes a structured JSON object:

```json
{
  "context": {
    "current_task": "002-research-compaction-survival-audit.md",
    "task_folder": "tasks/kernel-rolling-summarization-research/",
    "progress": "1/5 tasks complete",
    "last_completed": "001-build-create-project-dir.md",
    "next_step": "Write compaction survival audit",
    "notes": "Research backlog 240. Concurrent agents for 237-239."
  }
}
```

**Survives compaction:** Yes — fully. This is a file on disk, not in the conversation context window. The anchor ceremony reads it back on every anchor (Step 5: "Restore conversation context"). After compaction, the next anchor re-reads this file and the agent recovers: what task it was on, what it last did, and what to do next.

**Limitations:** The `notes` field is free-text and limited by what the agent chose to write at the last anchor. If the agent recorded "fix in progress" but not the specific approach being attempted, that decision rationale is lost. The structured fields (`current_task`, `progress`) are deterministic — they always accurately reflect task state.

### Layer 2: Workflow JSON (domain and per-agent)

`sr_dev_workflow.json` and `agent-{id}-workflow.json` persist:
- `completed_tasks` array — which tasks are done
- `skipped_tasks` array — which were skipped (with attempt counts)
- `current_task` — what's in progress
- `actions_since_anchor` — counter state
- `anchored` — whether the agent is anchored
- Cycling state (`cycling`, `task_folder`, `total_tasks`)

**Survives compaction:** Yes — fully. These are disk files. The anchor reads them (Step 14 writes, but also Step 6's routing reads them for gate checks). After compaction, the workflow JSON tells the agent exactly where it is in the task sequence.

**Limitations:** Workflow JSON tracks completion state, not execution history. It knows task 003 is done but not that it took 3 attempts, or that the first attempt failed because of a missing dependency. The `attempts_on_current` field tracks retry count for the *current* task only and resets on completion.

### Layer 3: Harness-Generated Compaction Summary

When the Claude Code harness approaches context limits, it compresses prior messages into a summary. This summary is injected into the next context window as a system message. The harness documentation states: "some or all of the current context is summarized; the summary, along with any remaining unsummarized context, is provided in the next context window."

**Survives compaction:** Partially. The harness summary preserves the *gist* of what happened — "the agent was working on task 003, it read these files, it wrote this output." But it is a lossy compression:
- Terminal output (test results, error messages) is summarized or dropped
- Multi-step reasoning chains are condensed
- Failed attempts that led to dead ends may be omitted entirely
- The specific wording of decisions ("I chose approach A over B because X") is often lost

**Limitations:** The harness summary is not under kernel control. Its quality depends on the harness's own summarization algorithm, which the kernel cannot configure or influence. The kernel cannot guarantee that any specific piece of information survives the harness summary.

## Survival Matrix

| Signal Type | Layer 1 (context key) | Layer 2 (workflow JSON) | Layer 3 (harness summary) | Net Survival |
|---|---|---|---|---|
| Current task identity | Full | Full | Likely present | **Deterministic** |
| Task completion state | Full | Full | Likely present | **Deterministic** |
| Next action intent | Full | Not tracked | May be present | **Deterministic** (Layer 1) |
| Decision rationale | Partial (notes) | Not tracked | Lossy | **At risk** |
| Failed attempt history | Not tracked | Not tracked | Lossy / omitted | **Lost** |
| Terminal output details | Not tracked | Not tracked | Lossy | **Lost** |
| Error messages / stack traces | Not tracked | Not tracked | Lossy | **Lost** |
| Intermediate reasoning | Not tracked | Not tracked | Condensed | **Lost** |
| Protocol/lesson state | Hash only | Not tracked | Not tracked | **Recovered** (re-read from disk) |

## Concrete Examples of Lost Signal

### Example 1: DEF-014 Import Root Fix (2026-07-21)

The anchor log from `01-41-00Z.json` shows 28 actions including: grepping for import patterns across `_reference/`, checking multiple files, creating a fix branch, editing `orders_page.py`. After compaction, what survives is "DEF-014 resolved: import roots unified" in the workflow's `last_lesson` field. What's lost: the specific grep commands that identified dual-root imports, the reasoning for choosing `from _reference.components` over adding a second PYTHONPATH entry, the intermediate test runs. The lesson in `lessons.md` captures the rule ("single import root") but not the investigation process.

### Example 2: Concurrent Agent State Contention (This Session, 2026-07-21)

During this research session, `session_state.json` was overwritten multiple times by concurrent agents (precompact-reanchor, ephemeral-subagents, jit-rule-injection). Each overwrote `agent_id`, `one_shot`, and `context` — erasing this agent's state. At one point, the parent session reformatted the file via PowerShell (UTF-16 encoding), causing the Python hook to fail to parse it, blocking all writes with "Session not started." If compaction happened during any of these overwrites, Layer 1 would contain another agent's context, not this one's. The per-agent workflow file (`agent-{id}-workflow.json`) survived because it's agent-scoped, but the shared session state is a single point of contention — a live demonstration of the lesson in `multi-agent-orchestration.md`.

### Example 3: Pipeline 205 Environment Investigation (2026-07-15)

From the lessons file: investigating Chrome input loss required bare-selenium reproduction, GPU flag testing, CDP raw dispatch, headed/headless comparison across multiple browser versions. This multi-step investigation chain produced the lesson "machine-wide Chrome input loss after first navigation" but the 20+ intermediate commands that proved it was environmental (not code) are only in anchor logs — not recoverable after compaction. The lesson captures the conclusion; the investigative path is forensic-only.

## How DEFECT_LOG Covers Failed-Attempt History

The `DEFECT_LOG.md` pattern partially addresses the "lost failed-attempt history" gap. Each defect entry records:
- What happened (the failure)
- Expected vs actual behavior
- Root cause analysis
- Proposed fix options (some entries list 2-3 alternatives considered)
- Resolution with specific files modified

This captures the *outcome* of a failure investigation and sometimes the *alternatives considered* (DEF-001 lists 3 options: stronger CLAUDE.md language, hook enforcement, command chaining). But it doesn't capture the intermediate *process* — the commands run, the hypotheses tested and rejected, the order in which evidence was gathered.

For preventing retry of dead ends, DEFECT_LOG is effective: if the same symptom recurs, the agent can read the entry and skip directly to the known fix. For understanding *why* certain approaches were rejected, it depends on how detailed the "Proposed Fix Options" section is.

The lessons cheat sheet (`lessons.md`) serves a similar role at a higher level — recording anti-patterns and quality gates derived from failures. Together, DEFECT_LOG + lessons capture an estimated 70% of the "don't retry dead ends" signal. The remaining 30% — intermediate reasoning, abandoned approaches that weren't wrong enough to become lessons, and environmental investigation chains — is genuinely lost after compaction.

## Conclusions

1. **Deterministic state is well-covered.** Task identity, completion state, and next-action intent survive compaction reliably through Layers 1 and 2. The kernel's disk-based state persistence is the primary survival mechanism, not the harness summary.

2. **Decision rationale is at risk.** It depends on the agent writing good `notes` during the anchor, which is voluntary and variable in quality. A structured schema for decisions (what, why, alternatives considered) would improve this but adds per-anchor cost.

3. **Failed-attempt history is the biggest gap.** Neither the context key nor the workflow JSON tracks what was tried and failed. DEFECT_LOG and lessons partially cover this for significant failures, but routine dead ends are lost.

4. **Anchor logs are the closest to a rolling ledger.** The archived anchor logs in `.claude/state/anchor-logs/` contain the raw action sequence between anchors. They survive compaction (they're on disk) but are never re-read during normal operation — they're forensic, not operational. Converting them to an operational read-back during anchor Step 5 would be the cheapest path to recovering lost signal.

5. **Shared state contention undermines Layer 1 for concurrent agents.** The per-agent workflow file pattern solves Layer 2 contention, but Layer 1 (`session_state.json` context key) remains a shared mutable file. A per-agent context file (paralleling the per-agent workflow pattern) would close this gap.
