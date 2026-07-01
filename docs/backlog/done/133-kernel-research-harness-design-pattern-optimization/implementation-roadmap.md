# Implementation Roadmap

## Status
NEW — Research phase, planning execution sequence

## Location
`workspace:docs/harness-design-pattern` (research documentation + project roadmap)

## Purpose

Create a phased roadmap for implementing harness optimizations. Sequencing is critical because some improvements have dependencies (e.g., conversation state must exist before selective recall), and others can run in parallel. The roadmap balances quick wins with strategic improvements.

## Key Questions

- What's the optimal sequencing of improvements (dependencies, parallel work)?
- Should we do one comprehensive redesign or incremental improvements?
- What's the rollout strategy (single PR, feature flags, staged deployment)?
- How do we measure success for each phase?
- What are the success criteria for "done" (close the 4.2-point gap completely, or target a subset)?

## Phased Approach

### Phase 0: Measurement & Validation (Weeks 1-2)

**Goal:** Establish baseline and validate root causes

**Tasks:**
- Set up benchmark harness with detailed metrics collection
- Run baseline Claude Code harness benchmark (establish 6.2/10 as baseline)
- Implement dimension-level metrics (token usage, context recall accuracy, error rate)
- Create A/B test framework for isolated improvements

**Deliverables:**
- Baseline benchmark report
- Metrics instrumentation in harness
- A/B test framework ready

**Effort:** 1-2 engineers, 2 weeks

**Dependencies:** None

### Phase 1: Quick Wins (Weeks 3-6)

**Goal:** Implement high-confidence, low-effort improvements

**Parallel Tracks:**
1. System Prompt Optimization (2 weeks)
   - Design task-specific prompts
   - Implement variant switching logic
   - Measure impact (estimate: +0.5-1 point)

2. Token Allocation Rebalancing (1 week)
   - Define allocation strategy
   - Implement enforce layer
   - Measure impact (estimate: +0.5-1 point)

3. Conversation State Tracking (2 weeks)
   - Design state schema
   - Implement serialization
   - Measure impact (estimate: +0.5 point)

**Deliverables:**
- 3 harness variants with isolated improvements
- Benchmark results per variant
- Cumulative impact analysis (should see +1.5-2.5 points)

**Effort:** 2-3 engineers, 4 weeks

**Dependencies:** Phase 0 (measurement framework)

### Phase 2: Medium-Term Improvements (Weeks 7-12)

**Goal:** Implement selective recall and error recovery

**Sequential Tasks:**
1. Selective Context Recall (3 weeks)
   - Implement embedding-based search
   - Integrate into harness
   - Measure impact (estimate: +1 point)
   - **Blocker:** Need embedding infrastructure (check if available)

2. Error Recovery Mechanisms (2-3 weeks)
   - Design recovery patterns (retry, backtrack, reframe)
   - Implement state save/restore
   - Measure impact (estimate: +0.5-1 point)

**Deliverables:**
- Selective recall implementation + metrics
- Error recovery patterns + test suite
- Cumulative harness impact (should reach +2.5-4 points from baseline)

**Effort:** 2-3 engineers, 6 weeks

**Dependencies:** Phase 1 (baseline improvements must be stable)

### Phase 3: Strategic Improvements (Weeks 13+)

**Goal:** Explore high-risk/high-reward improvements

**Options (choose based on Phase 2 results):**

**Option A: Hierarchical Compression** (4-8 weeks)
- If context recall is still insufficient, implement hierarchical summarization
- Riskier but potentially higher impact

**Option B: Multi-Model Routing** (2-3 weeks)
- If cost is a constraint, implement model selection
- Lower risk, moderate impact

**Option C: Decision Tree Layer** (4-6 weeks)
- If reasoning quality is limiting, add decision tree
- Highest risk/uncertainty

**Deliverables:** Depends on chosen option

**Effort:** 2-3 engineers, 4-8 weeks

**Dependencies:** Phase 2 (understand remaining gaps)

## Decision Points

| Gate | Condition | Action |
|------|-----------|--------|
| After Phase 1 | Cumulative impact < 1.5 points | Re-evaluate quick wins; consider alternative approaches |
| After Phase 1 | Cumulative impact > 2 points | Proceed to Phase 2 with confidence |
| After Phase 2 | Cumulative impact 2.5-3.5 points | Gap reduced but not closed; proceed to Phase 3 |
| After Phase 2 | Cumulative impact > 3.5 points | Gap substantially closed; Phase 3 optional |
| After Phase 3 | Cumulative impact >= 4.2 points | Gap closed; ship consolidated harness |

## Resource Estimates

| Phase | Duration | Team Size | Total Effort |
|-------|----------|-----------|--------------|
| Phase 0 | 2 weeks | 1-2 eng | ~1.5 person-weeks |
| Phase 1 | 4 weeks | 2-3 eng | ~8-10 person-weeks |
| Phase 2 | 6 weeks | 2-3 eng | ~12-15 person-weeks |
| Phase 3 | 4-8 weeks | 2-3 eng | ~8-20 person-weeks |
| **Total** | **16-20 weeks** | **2-3 eng avg** | **~30-45 person-weeks** |

(Note: Assumes parallel work within phases; can compress with more engineers or extend with fewer)

## Success Criteria

### Phase 1 Success
- ✓ All quick wins implemented and tested
- ✓ Cumulative impact ≥ 1.5 points
- ✓ No regressions in existing functionality

### Phase 2 Success
- ✓ Selective recall working reliably
- ✓ Error recovery patterns effective
- ✓ Cumulative impact ≥ 2.5 points

### Final Success
- ✓ Performance gap closed to within 0.5 points (Cursor 10.4 → Claude Code 9.9+)
- ✓ No increase in cost or latency
- ✓ All improvements documented in harness protocol

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Selective recall embedding infra unavailable | Phase 2 blocked | Pre-check availability; fallback to simpler retrieval |
| Quick wins don't compound as expected | Impact < 1.5 points | Build in measurement gates; pivot quickly |
| Hierarchy compression introduces latency | Performance improves but speed worsens | Implement early performance testing; consider caching |
| User impact of harness changes | User confusion or complaints | Comprehensive testing + opt-in feature flags for risky changes |

## Input Schema

Depends on: [[133-kernel-research-harness-design-pattern-optimization/optimization-opportunities]]

Needs:
- Prioritized opportunity list
- Effort/impact estimates
- Decision criteria from stakeholders (what's the success bar?)

## Output

- Detailed phased roadmap (Gantt-style timeline)
- Resource allocation plan
- Milestone definitions and success criteria
- Risk mitigation strategies
- Post-implementation plan (monitoring, tuning, documentation)
