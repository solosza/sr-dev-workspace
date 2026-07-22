# PreCompact Re-Anchor Hook — Research Report

## Verdict: YAH

Integrate PreCompact event-driven re-anchoring into the kernel as a **hybrid policy** (Policy C): the existing N-action timer raised from 30 to 50, plus a new PreCompact hook that forces immediate re-anchor on compaction events. This closes the post-compaction blind spot while preserving gradual-drift protection, at a ~30% token cost reduction.

---

## Research Summary

### Hook Capability (Task 002)

Claude Code 2.1.207 supports `PreCompact` and `PostCompact` hooks. PreCompact fires before compaction and can write state files as side effects — it cannot inject content into the compacted summary, but it can set `anchored: false` in the workflow state file. This is sufficient: the existing Gate 3 in `universal-gate-enforcer.py` already blocks tool calls when `anchored: false`, forcing the agent to run a full `/kernel/anchor` before proceeding.

The `SessionStart` hook with `compact` matcher was the intended content-injection path but is bugged (GitHub #15174) — stdout output is silently discarded. CLAUDE.md is the only reliable post-compaction content source. The PreCompact-to-Gate-3 path sidesteps this bug entirely by not relying on content injection.

### Compaction Survival Audit (Task 003)

On-disk state (`session_state.json`, workflow state, protocol, lessons, `actions.jsonl`) survives compaction intact. What degrades is the agent's in-context understanding: nuanced decisions, specific rule applications, direction changes, and verification results are compressed or lost. The `context` key in `session_state.json` provides structured recovery (current task, progress, notes) when the next anchor reads it, but today no anchor fires on compaction — the agent can operate for up to 30 actions on degraded context before the N-action timer intervenes.

The proposed PreCompact hook is ~30 lines of Python, writes to existing state fields, and requires no changes to `universal-gate-enforcer.py`. Agent-aware routing (`agent_id` → per-agent workflow file) prevents cross-agent interference in concurrent execution.

### Policy Comparison (Task 004)

Three policies evaluated over a representative 500-action pipeline run:

| Dimension | A: N=30 (current) | B: PreCompact only | C: Hybrid (N=50 + PreCompact) |
|-----------|-------------------|--------------------|-----------------------------|
| Token cost | ~144K | ~34K | ~102K |
| Post-compaction gap | Up to 30 actions | 0 (immediate) | 0 (immediate) |
| Short-session coverage | Yes | **No** | Yes |
| Gradual drift protection | Strong | **None** | Good |
| Hook failure resilience | Timer always fires | **No fallback** | Timer catches failures |

Policy B is disqualified: sessions that never compact (most one-shot agents, short interactive sessions) get zero re-centering. Policy A leaves a real gap after compaction. Policy C is the only option that covers both failure modes.

---

## Comparison Against Current N-Action Re-Anchor Loop

The current loop (Policy A, N=30) was designed conservatively because compaction could fire at any point within the 30-action window. Without a compaction trigger, the timer had to be tight enough that the worst case (compaction at action 1, then 29 actions on degraded context) was tolerable. This produced a reliable but expensive mechanism: 17 anchors per 500-action run, each costing ~8,500 tokens.

The hybrid policy (Policy C) splits the two concerns:
1. **Compaction** (catastrophic, discrete) — handled by the PreCompact hook, which triggers immediate re-anchor with zero post-compaction gap.
2. **Drift** (gradual, continuous) — handled by the N-action timer, which can now be raised to N=50 because compaction is separately covered.

This reduces anchors from ~17 to ~12 per 500-action run (~30% token savings) while eliminating the post-compaction blind spot entirely. The timer at N=50 still catches gradual drift at reasonable intervals, and serves as a fallback if the PreCompact hook fails (file permission error, corrupted JSON, etc.).

---

## Integration Design

### Components

**1. New hook script: `.claude/hooks/precompact-reanchor.py`**

The script (designed in Task 003) reads `session_state.json` to resolve the domain and agent routing, then sets `anchored: false` in the appropriate workflow state file. It also records the compaction source and timestamp in `session_state.json` for anchor ceremony diagnostics. Exits 0 to allow compaction to proceed.

**2. Hook registration: `settings.local.json`**

Add a PreCompact hook entry:
```json
{
  "hooks": {
    "PreCompact": [
      {
        "matcher": "auto|manual",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/precompact-reanchor.py"
          }
        ]
      }
    ]
  }
}
```

**3. Timer adjustment: `sr_dev_workflow.json`**

Change `actions_limit` from 30 to 50. This affects the hook's counter threshold in `universal-gate-enforcer.py` (which reads `actions_limit` from the workflow state).

**4. Anchor ceremony update: `/kernel/anchor`**

Minor: after anchor completes, clear `compaction_anchor_reason` in `session_state.json` (set to `null`). This distinguishes compaction-triggered anchors from timer-triggered anchors in diagnostics.

### New state fields

| File | Field | Purpose |
|------|-------|---------|
| `session_state.json` | `compaction_anchor_reason` | Why anchor was forced (`"auto_compaction"`, `"manual_compaction"`, or `null`) |
| `session_state.json` | `compaction_timestamp` | When compaction fired (ISO timestamp) |

### Dedup logic

If compaction fires near the timer threshold (e.g., at action 48 of a 50-action window), the compaction-triggered anchor resets `actions_since_anchor` to 0. The timer won't fire again until 50 more actions accumulate. No double-anchor occurs because the counter reset is part of every anchor ceremony.

For the edge case where `actions_since_anchor < 10` when a timer fires (meaning a compaction anchor just ran), the timer anchor can be skipped — the recent re-centering is sufficient. This is optional; the double-anchor cost (~8.5K tokens) is low enough that the complexity of the skip logic may not be worth it.

### Rollback path

If the hybrid policy proves problematic:
1. Remove the PreCompact hook entry from `settings.local.json`
2. Restore `actions_limit` to 30 in `sr_dev_workflow.json`
3. Delete `precompact-reanchor.py`
4. No other changes needed — the gate enforcer, anchor ceremony, and state files are unchanged

---

## Risks and Mitigations

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| PreCompact hook script error | Low | Timer at N=50 catches failures; logs show hook exit code |
| State file contention (concurrent agents) | Medium | Agent-aware routing already implemented; PreCompact uses the same routing |
| N=50 too high for gradual drift | Low | Monitor for drift violations in lessons; lower to 40 if needed |
| Lessons file growth increases anchor cost | Inevitable | Shared across all policies; periodic lessons consolidation is the fix |
| Hook not firing in `claude -p` | Low | One-shot agents skip Gate 3 by design; they rarely compact anyway |

---

## Implementation Effort

- **1 new file:** `precompact-reanchor.py` (~30 lines, already designed)
- **1 config change:** `settings.local.json` PreCompact hook entry
- **1 value change:** `actions_limit: 30 → 50`
- **1 minor update:** Anchor ceremony clears `compaction_anchor_reason`
- **0 changes to existing hooks or gate enforcer**

Estimated build: 1 pipeline run (4–6 tasks). No breaking changes. Fully backward-compatible — sessions without the hook work identically to today.
