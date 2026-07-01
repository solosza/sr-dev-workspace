# Optimization Opportunities

## Status
NEW — Research phase, identifying actionable improvements

## Location
`workspace:docs/harness-design-pattern` (research documentation)

## Purpose

Translate root cause analysis into concrete, actionable optimization opportunities for Claude Code harness. Categorize by effort/impact and provide detailed specs for each opportunity so downstream tasks can implement without re-researching.

## Key Questions

- What specific changes to Claude Code harness would close the 4.2-point performance gap?
- Which improvements are quick wins (1-2 weeks) vs. medium-term (1-3 months) vs. strategic (3-6+ months)?
- What are the trade-offs (performance vs. cost, simplicity vs. completeness)?
- Are there blockers or dependencies between improvements?
- Which improvements would require user input or approval?

## Opportunity Categories

### Quick Wins (Effort: Low, Impact: 1-2 points estimated)

#### 1. System Prompt Optimization
- **Current state:** Generic system prompt
- **Opportunity:** Task-specific prompts with explicit instructions for reasoning, context recall, error recovery
- **Implementation:** Create prompt variants per task type (agent tasks, reasoning tasks, content generation)
- **Estimated impact:** 0.5-1 point
- **Effort:** 1-2 weeks

#### 2. Token Allocation Rebalancing
- **Current state:** Unclear/generic token budget
- **Opportunity:** Explicit token allocation strategy (50% system, 30% history, 20% reasoning)
- **Implementation:** Modify harness to enforce token limits per component
- **Estimated impact:** 0.5-1 point
- **Effort:** 1 week

#### 3. Conversation State Tracking
- **Current state:** Implicit state in conversation history
- **Opportunity:** Explicit state object (decisions, goals, constraints, last error)
- **Implementation:** Add state serialization/deserialization to harness
- **Estimated impact:** 0.5 points
- **Effort:** 1-2 weeks

### Medium-Term Improvements (Effort: Medium, Impact: 1-2 points estimated)

#### 4. Selective Context Recall
- **Current state:** Full conversation history (expensive, can lose focus)
- **Opportunity:** Smart retrieval (semantic similarity + recency weighting)
- **Implementation:** Embedding-based search for relevant past context
- **Estimated impact:** 1 point
- **Effort:** 2-4 weeks (depends on embedding infrastructure)

#### 5. Error Recovery Mechanisms
- **Current state:** No explicit error handling in harness
- **Opportunity:** Automatic retry with context injection, backtracking on failures
- **Implementation:** Add recovery patterns to harness loop
- **Estimated impact:** 0.5-1 point
- **Effort:** 2-3 weeks

#### 6. Multi-Model Routing
- **Current state:** Single model (Opus)
- **Opportunity:** Intelligent model selection (Opus for reasoning, Sonnet for fast decisions)
- **Implementation:** Add routing logic to harness
- **Estimated impact:** 0.5 points (cost savings, potentially performance)
- **Effort:** 2-3 weeks

### Strategic Improvements (Effort: High, Impact: 1-2+ points estimated, uncertain)

#### 7. Hierarchical Context Compression
- **Current state:** No compression
- **Opportunity:** Multi-level summarization (per-interaction summaries, historical rollups)
- **Implementation:** Conversation hierarchy with incremental summarization
- **Estimated impact:** 1-1.5 points (speculative)
- **Effort:** 4-8 weeks

#### 8. Explicit Decision Tree Layer
- **Current state:** Decisions implicit in model reasoning
- **Opportunity:** Structured decision tracking with explicit branch exploration
- **Implementation:** Decision tree state machine + validation layer
- **Estimated impact:** 0.5-1 point (speculative)
- **Effort:** 4-6 weeks

#### 9. Adaptive Context Window Management
- **Current state:** Fixed token allocation
- **Opportunity:** Dynamic allocation based on task complexity/type
- **Implementation:** Complexity classifier + adaptive budget allocation
- **Estimated impact:** 0.5-1 point (speculative)
- **Effort:** 4-8 weeks

## Opportunity Matrix

| Opportunity | Effort | Est. Impact | Confidence | Blockers |
|------------|--------|------------|-----------|----------|
| System Prompt Optimization | Low | 0.5-1 | High | None |
| Token Allocation Rebalancing | Low | 0.5-1 | High | None |
| Conversation State Tracking | Low | 0.5 | High | None |
| Selective Context Recall | Medium | 1 | Medium | Embedding infrastructure |
| Error Recovery | Medium | 0.5-1 | High | None |
| Multi-Model Routing | Medium | 0.5 | Medium | User decision on model strategy |
| Hierarchical Compression | High | 1-1.5 | Low | Major refactor needed |
| Decision Tree Layer | High | 0.5-1 | Low | Validation complexity |
| Adaptive Context Management | High | 0.5-1 | Low | Classifier training data |

## Input Schema

Depends on: [[133-kernel-research-harness-design-pattern-optimization/performance-gap-root-cause]]

Needs:
- Root cause attribution (which factors drive performance)
- Confidence levels for hypotheses
- Trade-off analysis (performance vs. cost/complexity)

## Output

- Prioritized opportunity list (ranked by effort/impact ratio)
- Detailed spec for each opportunity (current state, target state, implementation approach, risks)
- Effort estimates and resource needs
- Decision tree for user input (which opportunities to pursue?)

## Dependencies

Depends on: Root cause analysis, benchmarking methodology
