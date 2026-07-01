# Harness Design Pattern Optimization Research

## Status
Open

## Priority
High — Harness design (context management strategy) drives performance more than model capability. 4.2-point performance gap between Cursor (10.4/10) and Claude Code (6.2/10) on same Opus model justifies deep optimization research.

## Summary

Research the design patterns, context management strategies, and architectural decisions that drive Claude Code harness performance. Benchmark data shows Cursor's harness outperforms Claude Code's by 4.2 points despite running the same underlying model (Opus 4.7). This indicates context management strategy is the primary performance driver, not model capability. The goal is to identify specific optimization opportunities and create a roadmap for harness evolution.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[133-kernel-research-harness-design-pattern-optimization/benchmarking-methodology]] | How Cursor and Claude Code harnesses are benchmarked; methodology comparison and metrics |
| [[133-kernel-research-harness-design-pattern-optimization/context-management-analysis]] | Deep dive into context window utilization, token distribution, and conversation state strategies |
| [[133-kernel-research-harness-design-pattern-optimization/performance-gap-root-cause]] | Root cause analysis of the 4.2-point performance delta between harnesses |
| [[133-kernel-research-harness-design-pattern-optimization/optimization-opportunities]] | Identified gaps, quick wins, and strategic improvements for Claude Code harness |
| [[133-kernel-research-harness-design-pattern-optimization/implementation-roadmap]] | Phased roadmap for harness improvements with timeline and resource estimates |

## Architecture

```
Benchmarking Methodology
  ↓
Performance Comparison (Cursor vs Claude Code)
  ↓
Context Management Analysis
  ├─ Token Distribution
  ├─ Conversation State Management
  ├─ Recall Strategy
  └─ Decision Tree Optimization
  ↓
Root Cause Analysis (4.2-point gap)
  ↓
Optimization Opportunities
  ├─ Quick Wins (implement in 1-2 weeks)
  ├─ Medium-term (1-3 months)
  └─ Strategic (3-6+ months)
  ↓
Implementation Roadmap
```

## Key Questions

- What specific context management techniques does Cursor use that Claude Code doesn't?
- How does token budget allocation differ between the two harnesses?
- What's the methodology for benchmarking agent performance?
- Are there quick wins (low-effort, high-impact optimizations)?
- What's the phase-sequencing strategy (concurrent vs sequential improvements)?

## References

- Existing harness analysis: `docs/harness-design-pattern/`
- Performance benchmark data: Cursor 10.4/10, Claude Code 6.2/10 (Opus 4.7 model)
- Related backlogs: None yet (foundational research)

## Task Builder Input

- **Deliverable:** Research summary document with 5 design sub-documents (methodology, context analysis, root cause, opportunities, roadmap)
- **Location:** `workspace:docs/harness-design-pattern`
- **Scope:** RESEARCH
- **Constraints:**
  - Research must be grounded in publicly available information + internal benchmark data
  - Each sub-document should be granular enough for follow-on implementation tasks
  - Focus on actionable insights, not just descriptive analysis
  - Identify decision points where user input may be needed (e.g., which opportunities to prioritize)
