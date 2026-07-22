# Hybrid Policy Comparison — PreCompact Re-Anchor Research

## Anchor Cost Baseline

Each full `/kernel/anchor` ceremony reads and processes:

| Component | Size | Estimated Tokens |
|-----------|------|-----------------|
| Protocol (`sr_dev-protocol.md`) | ~200 words, 2.4 KB | ~300 |
| Lessons (`lessons.md`) | ~5,000 words, 37 KB | ~7,000 |
| `session_state.json` | ~1 KB | ~200 |
| `actions.jsonl` (variable) | 0–5 KB | 0–1,000 |
| Anchor output (confirmation block) | ~200 words | ~300 |
| State writes (2 JSON files) | ~1 KB | ~200 |

**Total per anchor: ~8,000–9,000 tokens** (input + output combined).

The lessons file dominates — as the kernel matures and lessons accumulate, anchor cost grows. At 46 lessons, the lessons file is already 75% of the anchor cost.

## Three-Policy Comparison

### Policy A: Pure N-Action Timer (Current)

**Mechanism:** Hook increments counter on every Write/Edit/Bash. At N=30, blocks until full `/kernel/anchor` runs. Counter resets to 0.

**Token cost model (representative 500-action pipeline run):**
- Anchors triggered: ⌈500/30⌉ = 17
- Token cost: 17 × 8,500 = **~144,500 tokens**
- Anchor overhead as % of session: ~5–8% (assuming 2–3M total session tokens)

**Failure modes:**
1. **Post-compaction blind spot.** Compaction fires at action 10. Agent has 20 more actions on degraded context before the next anchor. During those 20 actions, the agent operates on a compressed summary of the protocol and lessons — exactly the state that causes drift violations.
2. **Uniform cost regardless of need.** In stable, repetitive phases (e.g., writing 10 similar task files), the anchor fires every 30 actions even though context quality is still high. The re-centering is correct but inefficient — the agent re-reads the same protocol it already knows well.
3. **Scales linearly.** A 1,000-action pipeline run triggers 34 anchors = ~289K tokens. Cost is proportional to session length, not to context degradation events.

### Policy B: Pure Event-Driven (PreCompact Only)

**Mechanism:** PreCompact hook sets `anchored: false` in workflow state. The next tool call hits Gate 3 in universal-gate-enforcer.py, blocking until `/kernel/anchor` runs. No action counter — anchoring only occurs when compaction fires.

**Token cost model (representative 500-action pipeline run):**
- Auto-compaction events in a typical long session: 3–5 (fires when context approaches the ~200K token window limit)
- Anchors triggered: 3–5
- Token cost: 4 × 8,500 = **~34,000 tokens**
- Anchor overhead: ~1–2% of session

**Failure modes:**
1. **No re-centering in short sessions.** Sessions under ~100K tokens (most one-shot agents, quick fixes, simple tasks) never trigger compaction. The agent gets ZERO anchoring — no protocol re-read, no lesson refresh, no work review. The entire enforcement mechanism is inert.
2. **Gradual drift unchecked.** Between compaction events (which can be 100+ actions apart), the agent accumulates drift without any re-centering checkpoint. The N-action timer exists precisely because drift is gradual, not event-driven.
3. **Compaction frequency varies.** Sessions that read many large files compact more often; sessions with terse exchanges compact rarely. Anchor frequency becomes tied to I/O patterns rather than context quality.
4. **One-shot agents unprotected.** `run-task.sh` agents typically execute 5–15 actions and never hit compaction. Under this policy, they would never anchor at all (currently, one-shot agents skip Gate 3 by design, but if that guard were removed, they'd still rarely trigger compaction).

### Policy C: Hybrid (Event-Driven + Raised Timer)

**Mechanism:** Two triggers, either of which forces a full `/kernel/anchor`:
1. **PreCompact hook** — sets `anchored: false` when compaction fires (immediate re-anchor on context loss)
2. **Raised N-action timer** — counter at N=50 instead of N=30 (periodic re-anchor for gradual drift)

The timer is raised from 30 to 50 because the compaction trigger now covers the catastrophic context-loss scenario that the lower N was partially defending against. The timer only needs to catch gradual drift, which accumulates more slowly.

**Token cost model (representative 500-action pipeline run):**
- Timer anchors: ⌈500/50⌉ = 10
- Compaction anchors: 3–5 (some may coincide with timer anchors; dedup by checking `actions_since_anchor > 0` before forcing re-anchor)
- Effective anchors: ~12 (after dedup)
- Token cost: 12 × 8,500 = **~102,000 tokens**
- Anchor overhead: ~3–5% of session

**Failure modes:**
1. **Double-anchor near compaction.** If compaction fires at action 48 of a 50-action window, the agent anchors for compaction, then 2 actions later the timer fires again. Mitigation: the timer anchor checks `actions_since_anchor`; if it's <10, skip the timer anchor (the recent compaction anchor is sufficient).
2. **Lessons file growth.** As lessons accumulate beyond 46, anchor cost per ceremony grows. At 100 lessons (~15K tokens), each anchor costs ~16K tokens and the hybrid's 12 anchors cost ~192K tokens. This is a shared concern across all three policies, not specific to hybrid.
3. **PreCompact hook failure.** If the hook script errors (file permission, corrupted JSON), compaction proceeds but `anchored` stays `true`. The timer catches this within 50 actions. Under pure event-driven (Policy B), this failure would mean no re-anchor at all.

## Comparison Summary

| Dimension | Policy A (N=30) | Policy B (PreCompact) | Policy C (Hybrid) |
|-----------|----------------|----------------------|-------------------|
| **Token cost (500 actions)** | ~144K | ~34K | ~102K |
| **Token cost (1000 actions)** | ~289K | ~51K | ~187K |
| **Short session coverage** | Yes (every 30 actions) | **No** — never fires | Yes (every 50 actions) |
| **Post-compaction gap** | Up to 30 actions blind | **0** — immediate | **0** — immediate |
| **One-shot agent coverage** | Yes (but skipped by design) | No | Yes (but skipped by design) |
| **Gradual drift protection** | Strong (30-action window) | **None** | Good (50-action window) |
| **Implementation complexity** | Existing | New hook only | New hook + timer adjustment |
| **Hook failure resilience** | Timer always fires | **No fallback** | Timer catches hook failures |

## Recommendation: Policy C (Hybrid)

**Rationale:** The hybrid policy is the only option that closes the post-compaction blind spot (Policy A's weakness) while maintaining periodic re-centering for gradual drift (Policy B's weakness). It achieves both at a ~30% token cost reduction compared to the current N=30 timer.

The key insight from the research: **compaction and drift are two distinct failure modes that require two distinct triggers.**

- **Compaction** is a catastrophic, discrete event — the agent suddenly loses deep context. An event-driven trigger (PreCompact hook) is the natural response: anchor immediately after context loss, don't wait for a timer.
- **Drift** is gradual and continuous — the agent slowly forgets rules over many actions. A timer-based trigger is the natural response: re-center periodically regardless of compaction events.

Neither trigger alone covers both failure modes. Policy B (event-driven only) leaves sessions that never compact completely unprotected — and most kernel one-shot agents fall in this category. Policy A (timer only) wastes up to 30 actions after compaction on degraded context. The hybrid combines both at modest additional complexity (one new hook script, one config change to `actions_limit`).

**Raising N from 30 to 50** is justified because the compaction trigger now handles the worst-case context loss. The 30-action window was conservative partly because compaction could fire at any point within it; with compaction now triggering an immediate anchor, the timer only needs to catch the slower accumulation of gradual drift, which a 50-action window handles well.

**Implementation cost:** One Python script (~30 lines, already designed in 02-compaction-survival-and-design.md), one settings.local.json entry, and changing `actions_limit` from 30 to 50 in workflow state. All infrastructure (Gate 3, anchor ceremony, state files) already exists.
