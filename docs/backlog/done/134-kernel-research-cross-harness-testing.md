# Cross-Harness Testing Framework Research

## Status
Open

## Priority
Medium-High — Understanding how to test harnesses is critical for harness optimization (backlog 133). Testing framework unlocks continuous improvement and competitive benchmarking.

## Summary

Research whether and how we can build a testing framework that evaluates other AI harnesses (e.g., Cursor, competitor tools) and generates comparative performance reports. The goal is to understand the testing methodology, metrics, and architecture needed to systematically compare harnesses and identify what drives the 4.2-point performance gap documented in backlog 133. Use existing QA platform architecture (Python, Selenium, SSH-based testing) as reference patterns.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[134-kernel-research-cross-harness-testing/qa-platform-analysis]] | Analyze existing isagawa-qa platforms (Selenium, SSH) for testable patterns and architecture |
| [[134-kernel-research-cross-harness-testing/harness-testing-patterns]] | Research methodology for testing AI harnesses: metrics, test cases, automation patterns |
| [[134-kernel-research-cross-harness-testing/cross-harness-design-architecture]] | Proposed architecture for a harness testing framework that evaluates multiple harnesses |
| [[134-kernel-research-cross-harness-testing/implementation-strategy]] | Phased strategy to build cross-harness testing capability |

## Architecture

```
QA Platform Patterns Analysis
  ├─ Selenium-based testing architecture
  ├─ SSH integration patterns
  ├─ Python automation patterns
  └─ Comparative metrics & reporting
         ↓
Harness Testing Methodology
  ├─ What metrics measure harness performance?
  ├─ What test cases compare harnesses?
  ├─ What automation patterns apply?
  └─ How do we isolate harness from model?
         ↓
Cross-Harness Testing Architecture
  ├─ Testbed design (multiple harnesses in parallel)
  ├─ Metric collection & comparison
  ├─ Report generation (gaps, deltas, patterns)
  └─ Continuous integration pipeline
         ↓
Implementation Roadmap
  ├─ Phase 1: Test harness locally (Claude Code vs reference)
  ├─ Phase 2: Build comparative benchmarking tool
  ├─ Phase 3: Integrate with CI/CD
  └─ Phase 4: Scale to multiple harnesses
```

## Key Questions

- What distinguishes a "harness" from a "model" in testing context?
- Can we isolate harness behavior independent of model capability?
- What QA patterns from Selenium/SSH can apply to harness testing?
- How do we measure context management performance?
- Is it feasible to test closed-source harnesses (Cursor, etc.)?
- What metrics predict real-world performance deltas?
- Can we build a harness testing standard (like SPEC for benchmarking)?

## References

- **Backlog 133:** Harness Design Pattern Optimization (performance gap research)
- **QA Platforms:** isagawa-qa/platform-selenium, SSH testing infrastructure
- **Performance Data:** Cursor 10.4/10, Claude Code 6.2/10 (Opus 4.7)
- **Related Projects:** projects/ai-harness-job-search/ (harness comparison context)

## Task Builder Input

- **Deliverable:** 4 research design documents + synthesis on feasibility, architecture, and phased implementation strategy
- **Location:** `workspace:docs/harness-design-pattern`
- **Scope:** RESEARCH
- **Constraints:**
  - Must reference existing QA platform patterns (Python, Selenium, SSH)
  - Focus on testable dimensions (context management, decision-making, error recovery)
  - Identify gaps between testing capability and performance measurement
  - Propose actionable framework that could be built in phases
  - Highlight blockers (closed-source harnesses, model isolation, etc.)
