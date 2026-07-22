# Rolling Summarization Research Report

## Verdict: YAH (Conditional)

Integrate rolling summarization into the kernel as a **rolling structured ledger** in anchor Step 10 (Candidate A from the gap analysis). The condition: ship alongside PreCompact re-anchoring (backlog 238) as a combined anchor ceremony update. Do not ship the periodic summarizer hook (Candidate B) — its architectural complexity is not justified by its marginal value over the ledger approach.

---

## Research Summary

### Task 002 — Compaction Survival Audit

Audited the three persistence layers that survive context-window compaction:

1. **Layer 1 (session_state.json context key):** Fully survives. Structured fields (`current_task`, `progress`, `next_step`) provide deterministic resume. The `notes` field is free-text and variable in quality.

2. **Layer 2 (workflow JSON files):** Fully survives. Tracks completion state (`completed_tasks`, `skipped_tasks`, `current_task`) but not execution history or decision rationale.

3. **Layer 3 (harness compaction summary):** Partially survives. Lossy compression — terminal output, failed attempts, multi-step reasoning chains, and decision rationale are condensed or dropped.

**Key finding:** Deterministic state (task identity, completion, next action) is well-covered. Decision rationale and failed-attempt history are the two gaps. The anchor logs archive raw action sequences but are never re-read during normal operation — they are forensic, not operational.

### Task 003 — Gap Analysis + Design

Identified three specific gaps between current behavior and rolling-summarization's promise:

- **Gap 1 (Decision Rationale):** Medium severity. The `notes` field can capture decisions but often degrades to terse summaries. No schema enforces recording alternatives considered.
- **Gap 2 (Failed-Attempt Registry):** High severity for long sessions. Routine failures ("tried grep X, no results") are lost after compaction. Only failures significant enough for DEFECT_LOG or lessons.md entries survive.
- **Gap 3 (Cross-Anchor Continuity):** Low-medium severity. Investigations spanning multiple anchor cycles have evidence fragmented across separate archive files.

Evaluated two design candidates:

- **Candidate A (Rolling Structured Ledger):** Extend the anchor Step 10 `context` object with a schema-enforced `ledger` array. Per-anchor entries capture completed tasks, failed attempts, and decisions with alternatives. Rolling window of 5 entries prevents unbounded growth. Cost: 30-50 additional tokens per anchor, ~1.5KB max state growth. Effort: 2 tasks.

- **Candidate B (Periodic Summarizer Hook):** New PostToolUse hook every N actions, generating summaries into `rolling-summary.jsonl`. Finer granularity but requires hook-side LLM inference (architecturally novel) or anchor-side summarization (marginal value). Cost: 3-4 tasks, medium architectural risk.

**Recommendation:** Candidate A wins on every dimension — lower cost, lower risk, natural fit with existing anchor architecture.

### Task 004 — Portfolio Ranking

Ranked all four context-decay strategies (backlogs 237-240) as a portfolio:

| Rank | Strategy | Value | Cost | Ship When |
|------|----------|-------|------|-----------|
| 1 | 238 PreCompact Re-Anchoring | Highest ROI — closes compaction blindspot | Very low | Immediately |
| 2 | 240 Rolling Structured Ledger | Closes decision + failure gaps | Low | Immediately (combine with 238) |
| 3 | 239 JIT Rule Injection | Prevents per-action violations between anchors | Medium (phased) | After anchor changes stabilize |
| 4 | 237 Ephemeral Sub-Agents | Reduces session-level exposure | High (blockers) | After Tier 1-2 stabilize |

**No redundancy between strategies.** They operate at four different time scales (action, anchor, compaction, session) and form a defense-in-depth stack. Each layer catches what the layer above it misses.

---

## Trade-Off Analysis vs Current N-Action Re-Anchor

### What the Current System Does Well

The N-action anchor (limit: 30) forces a full protocol re-read, lessons internalization, holistic work review, and context recovery at regular intervals. It is battle-tested through 46 lessons. The structured `context` key in session_state.json provides deterministic task resume. The workflow JSON provides deterministic completion tracking. Together, these mechanisms ensure the agent can always find its place after compaction.

### What the Current System Misses

1. **Post-compaction gap:** No mechanism triggers re-anchor after compaction. The agent could have 0 `actions_since_anchor` and proceed for up to 30 actions on degraded context. This is the most dangerous gap — compaction is the single largest context-loss event, and it triggers no recovery.

2. **Decision rationale gap:** The `notes` field is voluntary and unstructured. When the agent writes "fix in progress" instead of "chose approach A over B because X was failing," the decision rationale is lost after the next compaction. Example: DEF-014's reasoning for choosing single import root over dual PYTHONPATH is only recoverable from the lesson entry, not from the anchor context.

3. **Failed-attempt gap:** Routine failures are not persisted. After compaction, the agent may retry an approach that already failed — "tried grep X, no results" is in the anchor log archive but never re-read. This waste is invisible because the agent doesn't know it's repeating work.

### What Rolling Summarization Adds

The rolling structured ledger addresses gaps #2 and #3 without changing the anchor's timing (#1 is addressed by 238 PreCompact):

- **Structured decisions:** Schema forces the agent to record `what`, `alternatives`, `why` for each decision. This survives compaction in Layer 1 (disk file) and is re-read at anchor Step 5.
- **Structured failures:** Schema forces the agent to record `attempted`, `error`, `instead` for each failure. The rolling window (5 entries) provides enough history to prevent retry of recent dead ends.
- **No change to anchor frequency or ceremony structure.** The ledger is an additional write during Step 10, not a new phase or gate.

### What Rolling Summarization Costs

- **30-50 tokens per anchor cycle** for writing the ledger entry. The agent already reviews inter-anchor work in Part B; the ledger entry summarizes that review into a structured format.
- **~1.5KB maximum state file growth** (5 entries x 300 bytes each). Negligible.
- **Discipline risk:** The agent must write meaningful ledger entries, not perfunctory "task completed per spec" stubs. The schema helps (structured fields prompt specific answers), but cannot guarantee quality. Anchor Part B could include a ledger-quality check.

### Net Assessment

The rolling structured ledger is a low-cost, low-risk addition that closes two of the three identified gaps. It does not replace the N-action anchor — it enriches what the anchor captures. The anchor's irreducible duties (protocol refresh, lessons internalization, drift detection, violation review) are unchanged. The ledger adds one new duty: structured state recording.

---

## Integration Design

### Schema (Anchor Step 10 Extension)

Add a `ledger` array to the `context` object in `session_state.json`:

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
        "failed": [
          {
            "attempted": "grep for DEFECT_LOG in isagawa-qa-platform",
            "error": "file not found at expected path",
            "instead": "searched recursively, found at docs/DEFECT_LOG.md"
          }
        ],
        "decisions": [
          {
            "what": "Used single PYTHONPATH root (framework/) instead of dual roots",
            "alternatives": "Could add framework/_reference/ to PYTHONPATH",
            "why": "DEF-014 resolution: unified imports to _reference-prefixed style"
          }
        ]
      }
    ]
  }
}
```

### Rolling Window

Keep the last 5 ledger entries. On each anchor, append a new entry and drop entries beyond 5. This provides ~150 actions of decision/failure history (5 x 30 actions per cycle) while keeping state file size bounded.

### Anchor Command Changes

**Step 10 (Save conversation context):** After writing the standard context fields, append a new ledger entry. The agent reflects on the just-reviewed inter-anchor work (Part B output) and structures it into completed/failed/decisions.

**Step 5 (Restore conversation context):** When reading back the context key, also read the ledger entries. Surface any failed-attempt entries that match the current task's domain (e.g., if working on import paths, flag prior import-path failures).

### Implementation Tasks

| # | Task | Type |
|---|------|------|
| 1 | Modify `anchor.md` Step 10 to include ledger schema; modify Step 5 to read ledger back | BUILD |
| 2 | Run a real session with the modified anchor; verify ledger entries are written and read back correctly after a simulated compaction (clear conversation, re-anchor) | TEST |

### Combined with 238

If shipping alongside PreCompact re-anchoring, the anchor command changes include both the PreCompact trigger mechanism (set `anchored: false` on compaction) and the ledger schema. One anchor.md modification, one test session.

---

## Disqualifying Factors Considered (But Not Disqualifying)

1. **Agent discipline:** The agent might write perfunctory ledger entries. Mitigation: schema structure prompts specific fields; future quality check in Part B.
2. **State file contention:** The ledger is in `session_state.json`, which is shared and contended. Mitigation: per-agent session state (237's blocker) would also fix this; until then, the rolling window keeps entries small.
3. **Token cost at scale:** In a 100-action session (3-4 anchor cycles), the ledger adds 120-200 tokens total. Negligible against the ~200K total session cost.

None of these are disqualifying. The rolling structured ledger is a net positive with bounded downside.
