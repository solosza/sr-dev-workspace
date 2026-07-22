# Portfolio Ranking — Four Context-Decay Strategies

## Purpose

Rank the four context-decay strategies researched under backlogs 237–240 as a portfolio for the Isagawa Kernel. Identify redundancies, the recommended combination, and sequencing for implementation.

## The Four Strategies

| # | Backlog | Strategy | Core Mechanism |
|---|---------|----------|---------------|
| 237 | Ephemeral Sub-Agents | Reduce long-lived session exposure by delegating work to short-lived one-shot agents | Per-agent state isolation, semantic handoff schema |
| 238 | PreCompact Re-Anchoring | Force a full `/kernel/anchor` after context compaction | PreCompact hook sets `anchored: false`; existing Gate 3 blocks until re-anchor |
| 239 | JIT Rule Injection | Inject relevant lesson rules at the PreToolUse boundary via `additionalContext` | Non-blocking advisory context, rule-map JSON, dedup window |
| 240 | Rolling Summarization | Persist structured decision/failure ledger entries during anchor Step 10 | Schema-enforced ledger array in `context` key, rolling window |

## Ranking Table

| Dimension | 238 PreCompact | 239 JIT | 240 Rolling Ledger | 237 Ephemeral |
|-----------|---------------|---------|-------------------|---------------|
| **Implementation cost** | Very Low (1 hook, 0 gate changes) | Low–Medium (1 hook + rule-map, phased) | Low (2 tasks: modify anchor Step 10 + test) | High (env-var routing, handoff schema, run-task.sh changes) |
| **Token efficiency** | Zero per-action cost; re-anchor ~200 tokens when triggered | ~100 tokens per injection (5 rules x 20 tokens); advisory, non-blocking | 30–50 tokens per anchor cycle (ledger entry) | ~7,000 tokens per 10-task pipeline (handoff reads/writes) |
| **Determinism** | High — reuses Gate 3, existing anchor ceremony | Medium — pattern matching can false-positive; advisory only | High — schema-enforced structured fields | Medium — handoff quality depends on agent writing good entries |
| **Coverage** | Compaction-triggered decay only | Per-action soft-rule violations between anchors | Decision rationale + failed-attempt history (the two identified gaps) | State contention in concurrent agents; orchestrator context decay |
| **Architectural risk** | Very Low — zero changes to existing gates | Low — advisory injection is non-blocking; worst case ignored | Very Low — additive change to existing Step 10 | Medium — requires changes to session-start, hooks, run-task.sh |
| **Proven mechanism?** | Yes — Gate 3 already exists; PreCompact hook is standard | Yes — `additionalContext` live-tested and confirmed working | No — schema proposed but not yet tested | Partial — per-agent workflow routing exists; handoff and env-var routing are new |

## Redundancy Analysis

### Does 238 make 240 redundant?

**No.** They address different gaps. 238 (PreCompact re-anchoring) solves *when* the agent re-reads protocol after compaction — it ensures the anchor fires. But it doesn't change *what* the anchor saves. The anchor's Step 10 still writes the same free-text `notes` field. 240 (Rolling Ledger) improves *what* the anchor captures — structured decisions and failures instead of terse notes. They are complementary: 238 ensures re-anchoring happens after compaction; 240 ensures the anchor captures better data when it runs.

### Does 239 make 240 redundant?

**No.** 239 (JIT) operates at the per-action level — it reminds the agent of relevant rules before each tool call. 240 operates at the per-anchor-cycle level — it records what happened (decisions, failures) for future recovery. JIT prevents violations; the ledger prevents retry of dead ends. Different time scales, different failure modes.

### Does 237 make all others redundant?

**No.** Ephemeral agents reduce context-decay *exposure* (shorter sessions = less decay) but don't eliminate it. The orchestrator is still long-lived. And within each ephemeral agent's lifecycle, the same gaps exist: no JIT rule injection, no compaction re-anchor (though short sessions rarely compact), no structured decision capture. 237 is orthogonal to 238–240.

### Actual redundancy found

**238 + 240 partially overlap on anchor-cycle context recovery.** Both modify the anchor ceremony. 238 triggers the anchor after compaction; 240 enriches what the anchor writes. If both ship, the anchor ceremony is modified twice — once for the trigger mechanism (238) and once for the ledger schema (240). These can be combined into a single anchor modification.

**239 Phase 4 (auto-derivation from lessons) and the `/kernel/learn` integration overlap with 240's "prevent retry" goal.** If JIT injection includes a "failed approaches" trigger type, it could surface failed-attempt history at the tool boundary, reducing the need for a persisted ledger. However, JIT operates on *rules* derived from failures, not on *specific instance* failures. The ledger captures "I tried grep X at 14:05 and got no results" — JIT captures "always verify before write." Both are valuable.

## Recommended Combination

**Ship all four, but not equally.**

### Tier 1 — Ship immediately (high value, low cost)

1. **238 PreCompact Re-Anchoring** — One hook file, zero gate changes, fully compatible. Closes the compaction blindspot that every kernel session faces. This is the highest ROI item in the portfolio.

2. **240 Rolling Structured Ledger (Candidate A only)** — Two tasks: modify anchor Step 10 schema, test with a real session. Closes the decision-rationale and failed-attempt gaps. Can be combined with 238's anchor ceremony changes.

### Tier 2 — Ship in phases (medium value, medium cost)

3. **239 JIT Rule Injection** — Phase 1 (2 high-priority rules) ships first as a proof-of-concept. Phases 2–4 follow based on measured violation-rate reduction. The research already provides the full architecture; implementation is phased by design.

### Tier 3 — Ship when blockers resolve (high value, high cost)

4. **237 Ephemeral Sub-Agents expansion** — Requires resolving session_state.json contention (env-var agent_id routing), building the semantic handoff schema, and modifying run-task.sh. These are real engineering tasks, not research. Ship after the Tier 1 items stabilize the anchor loop, since ephemeral agents inherit the anchor's behavior.

## Recommended Build Order

| Phase | Backlog(s) | Work | Depends On |
|-------|-----------|------|-----------|
| **Phase 1** | 238 + 240 | PreCompact hook + rolling ledger schema in anchor Step 10 | Nothing — can start immediately |
| **Phase 2** | 239 (Phase 1) | JIT hook + rule-map with S1 (verify before write) and S12 (no unnecessary agents) | Phase 1 stable (anchor changes settled) |
| **Phase 3** | 239 (Phases 2–3) | Medium-priority rules + session-state tracking + dedup | Phase 2 validated |
| **Phase 4** | 237 | Env-var agent_id routing + semantic handoff schema + run-task.sh integration | Phase 1 stable + state contention resolved |
| **Phase 5** | 239 (Phase 4) | Auto-derivation from lessons.md + `/kernel/learn` integration | Phase 3 stable + 237 shipping (learn cycle sees more one-shot agents) |

## Sequencing Rationale

238 ships first because it's zero-risk and closes the most dangerous gap (post-compaction context loss with no recovery trigger). 240 ships alongside it because they both modify the anchor ceremony and the combined change is still small. 239 follows because it requires a stable anchor loop (JIT's value depends on the anchor catching what JIT misses — if the anchor is changing, JIT's complementary role is harder to evaluate). 237 ships last because its blockers (state contention, handoff schema) are the most complex and because Tier 1–2 improvements to the anchor make each ephemeral agent's lifecycle more resilient.

## Key Insight

The four strategies form a defense-in-depth stack, not competing alternatives:

```
Action level:    239 JIT        -> reminds rules before each action
Anchor level:    240 Ledger     -> captures decisions/failures at each anchor
Compaction level: 238 PreCompact -> forces re-anchor after compaction
Session level:   237 Ephemeral  -> reduces exposure by shortening sessions
```

Each layer catches what the layer above it misses. No single strategy is sufficient; the combination provides coverage across all four time scales of context decay.
