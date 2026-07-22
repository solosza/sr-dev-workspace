# Gap Analysis + Design Candidate

## Purpose

Compare the kernel's current context-persistence behavior against the rolling-summarization pattern's promise. Design two candidate implementations: (A) extending anchor Step 10 into a rolling structured ledger, and (B) a new periodic summarizer. Evaluate cost and complexity of each.

## Current Behavior — What the Anchor Saves

The anchor ceremony (Step 10) writes a structured `context` object into `session_state.json`:

```json
{
  "current_task": "003-research-gap-analysis.md",
  "task_folder": "tasks/kernel-rolling-summarization-research/",
  "progress": "2/5 tasks complete",
  "last_completed": "002-research-compaction-survival-audit.md",
  "next_step": "Write gap analysis document",
  "notes": "free-text field for key decisions and constraints"
}
```

Step 11 archives the actions log (`actions.jsonl`) into `anchor-logs/YYYY-MM-DD/HH-MM-SSZ.json` and truncates the live log. This archive contains every Edit, Write, Bash, and Read action with timestamps, but is never re-read during normal operation.

The workflow JSON (`sr_dev_workflow.json` or `agent-{id}-workflow.json`) independently tracks `completed_tasks`, `skipped_tasks`, `current_task`, and `attempts_on_current`.

## The Rolling-Summarization Pattern Promise

The pattern claims to preserve signal that conversational filler would otherwise bury:

1. **Structural state** — what files exist, what changed, what the codebase looks like now
2. **Decision log** — choices made and alternatives rejected, with rationale
3. **Failed-attempt registry** — what was tried and didn't work, preventing retries
4. **System rules pinned** — protocol constraints remain at top priority regardless of context depth

The kernel already achieves #1 (via the context key's structured fields) and #4 (via the anchor re-reading protocol + lessons every N actions). The gaps are in #2 (decision log) and #3 (failed-attempt registry).

## Gap List — Signal We Drop That the Pattern Would Keep

### Gap 1: Decision Rationale (Partial Coverage)

**Current state:** The `notes` field in the context key can contain decision rationale, but it's free-text and the agent often writes terse notes ("fix in progress") rather than structured decisions. No schema enforces recording alternatives considered.

**What rolling summarization would preserve:** A structured entry per decision: what was decided, what alternatives were considered, why the chosen path won. This would survive compaction as a disk-persisted ledger entry.

**Severity:** Medium. Most decisions in kernel work are task-driven (the task file says what to do), so autonomous decision points are infrequent. When they occur (e.g., "should I use importlib direct-load or package import?" in DEF-014), the rationale is genuinely valuable for preventing recurrence.

### Gap 2: Failed-Attempt Registry (Minimal Coverage)

**Current state:** Failed attempts are captured only if they escalate to a defect (DEFECT_LOG entry) or a lesson (lessons.md). Routine failures — "tried grep X, no results" or "approach A timed out, switched to B" — are lost after compaction. The actions log archives capture the *commands* but not the *outcomes* or *reasoning*.

**What rolling summarization would preserve:** A structured failure entry: what was attempted, what the error was, what was learned, what was done instead. This prevents the agent from retrying the exact same approach after compaction.

**Severity:** High for long sessions with multiple anchor cycles. In a 28-action anchor window (as seen in `01-41-00Z.json`), several failed approaches may have been tried. After compaction, the agent has no way to know what didn't work unless it was significant enough for a lesson.

### Gap 3: Cross-Anchor Continuity for Investigations

**Current state:** Each anchor resets the actions log. An investigation that spans 2-3 anchor cycles has its evidence fragmented across separate archive files. The context key's `notes` field bridges anchors, but only if the agent writes the investigation thread into it.

**What rolling summarization would preserve:** A running investigation thread that accumulates evidence across anchor boundaries, so the full chain of "tried X → learned Y → tried Z → concluded W" is available in one place.

**Severity:** Low-Medium. Most kernel tasks complete within one anchor cycle. Investigations that span multiple cycles (like the Chrome input loss in pipeline 205) are rare but produce the most valuable lessons.

## Design Candidate A: Rolling Structured Ledger (Anchor Step 10 Extension)

### Schema

Extend the `context` object in `session_state.json` to include a rolling `ledger` array:

```json
{
  "context": {
    "current_task": "...",
    "progress": "...",
    "next_step": "...",
    "notes": "...",
    "ledger": [
      {
        "anchor_cycle": 5,
        "timestamp": "2026-07-21T20:05:00Z",
        "completed": ["001-build-create-project-dir.md"],
        "failed": [],
        "decisions": [
          {
            "what": "Created project dir at projects/kernel-rolling-summarization-research/",
            "alternatives": "Could have used existing projects/kernel-* dir",
            "why": "Task file specifies dedicated directory"
          }
        ]
      }
    ]
  }
}
```

### Trigger Point

During anchor Step 10, after writing the standard context fields, the agent appends a new ledger entry for the just-completed anchor cycle. The ledger accumulates across anchors. A rolling window (e.g., last 5 entries) prevents unbounded growth.

### Cost

- **Per-anchor overhead:** ~30-50 additional tokens to write the ledger entry. The agent must reflect on what was completed, what failed, and what decisions were made. This is modest — the anchor already requires reviewing inter-anchor work (Part B), so the information is available.
- **State file growth:** Each ledger entry is ~150-300 bytes. With a rolling window of 5, the ledger adds at most ~1.5KB to session_state.json. Negligible.
- **Cognitive load:** The agent must write structured decision entries, which requires more discipline than free-text notes. Risk of the agent writing perfunctory entries ("task completed per spec") that add no value.

### Complexity

- **Changes required:** Modify anchor.md Step 10 to include ledger schema. Add ledger read-back in Step 5 (restore context). Add rolling window truncation logic.
- **Estimated work:** 1 task (modify anchor command), 1 task (test with a real session).
- **Risk:** Low. The change is additive — existing context fields are unchanged. The ledger is optional recovery data.

## Design Candidate B: Periodic Summarizer (New Hook)

### Architecture

A new PostToolUse hook that triggers every N actions (configurable, e.g., every 5). The hook reads the last N actions from `actions.jsonl`, summarizes them into a structured format, and appends to a rolling summary file (`rolling-summary.jsonl`). The anchor reads this file during Step 5 to recover cross-anchor context.

### Schema

```json
{
  "timestamp": "2026-07-21T20:05:00Z",
  "actions_range": [15, 20],
  "summary": "Investigated import paths in _reference package. Grepped for dual-root imports (from components vs from _reference.components). Found 3 files with bare imports. Decided to unify to _reference-prefixed imports rather than dual PYTHONPATH.",
  "decisions": ["Unified to _reference-prefixed imports"],
  "failures": ["pytest collection failed with single PYTHONPATH — needs both roots"],
  "state_changes": ["orders_page.py: import path changed"]
}
```

### Trigger Point

PostToolUse hook, every N actions. Runs independently of the anchor cycle, so it captures signal between anchors.

### Cost

- **Per-trigger overhead:** The hook would need to read the last N actions, understand their context, and generate a structured summary. This requires LLM inference within the hook — which hooks cannot currently do (hooks are Python scripts, not LLM calls). Alternative: the hook writes raw data, and the anchor Step 5 uses the LLM to summarize when reading back. This shifts the cost to anchor time.
- **If hook-side summarization:** Would require spawning a sub-process or API call from within the hook. Adds latency (~2-5s) to every Nth action. Hooks are designed to be fast gatekeepers, not inference engines.
- **If anchor-side summarization:** The anchor reads `actions.jsonl` entries and generates the summary. This adds ~50-100 tokens to anchor processing. More aligned with the existing architecture.

### Complexity

- **Changes required:** New hook file, settings registration, new summary file format, anchor Step 5 modification to read summaries, truncation/rotation logic for the summary file.
- **Estimated work:** 3-4 tasks (hook, settings, anchor modification, testing).
- **Risk:** Medium. Adding a new hook introduces a new failure mode. Hook-side LLM inference is architecturally novel and may conflict with the "hooks are fast gatekeepers" principle. The anchor-side variant is safer but provides less value (same data, just formatted differently).

## Cost/Complexity Comparison

| Dimension | Candidate A (Ledger) | Candidate B (Summarizer) |
|---|---|---|
| Implementation effort | Low (2 tasks) | Medium-High (3-4 tasks) |
| Per-action overhead | Zero | 2-5s every N actions (hook-side) or zero (anchor-side) |
| Per-anchor overhead | 30-50 tokens | 50-100 tokens (if anchor-side) |
| Architectural fit | Natural extension of existing Step 10 | New hook type, new file format |
| Signal preserved | Decisions + failures per anchor cycle | Continuous action summaries |
| Granularity | Per-anchor-cycle | Per-N-actions (finer) |
| Risk | Low (additive change) | Medium (new hook architecture) |
| Value-add over current | Structured decisions + failure registry | Same + finer granularity |

## Recommendation

**Candidate A (Rolling Structured Ledger)** is the clear winner for the kernel. It has lower implementation cost, lower runtime overhead, fits naturally into the existing anchor architecture, and covers the two identified gaps (decision rationale and failed-attempt registry). The finer granularity of Candidate B doesn't justify the architectural complexity — the anchor cycle (every 10-30 actions) is already a reasonable summarization interval.

The key design constraint for Candidate A: the ledger entries must be *structured* (schema-enforced), not free-text. Free-text notes are what we already have and they degrade to terse summaries. The schema forces the agent to record decisions and failures explicitly, which is the entire value proposition.
