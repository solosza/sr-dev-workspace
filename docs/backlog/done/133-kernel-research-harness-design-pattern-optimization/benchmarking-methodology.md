# Benchmarking Methodology

## Status
NEW — Research phase, understanding current benchmarking approaches

## Location
`workspace:docs/harness-design-pattern` (research documentation)

## Purpose

Understand how Claude Code and Cursor harnesses are benchmarked, compare methodologies, and identify gaps or blind spots in performance measurement. This forms the foundation for all other analyses (root cause, optimization opportunities).

## Key Questions

- What metrics do Cursor and Claude Code use to measure harness performance?
- How are benchmark scenarios constructed (scope, complexity, diversity)?
- Are benchmarks standardized or custom per organization?
- What's the sample size and statistical significance of the performance gap?
- Are benchmarks task-specific (agent tasks) or general (token efficiency, recall, reasoning)?

## Research Areas

### 1. Cursor Benchmarking
- Harness performance score: 10.4/10
- What are the scoring dimensions?
- Sample scenarios (what tasks are benchmarked?)
- Measurement methodology (time, cost, success rate, user satisfaction?)

### 2. Claude Code Benchmarking
- Harness performance score: 6.2/10 (Opus 4.7 same as Cursor)
- Scoring methodology alignment with Cursor?
- Any public benchmarks or documentation?
- Internal metrics tracked by Anthropic?

### 3. Methodology Comparison
- Are both harnesses measured on identical scenarios?
- Is the Opus 4.7 model version exactly the same?
- Are there confounding variables (infrastructure, latency, cost)?
- How is "harness performance" defined operationally?

### 4. Gaps in Current Benchmarking
- Are there dimensions missing from current metrics (e.g., creativity, novel problem-solving)?
- Is user experience/satisfaction measured?
- Are there benchmarks for specific domains (coding, reasoning, content generation)?

## Input Schema

This sub-document needs:
- Public benchmark data or references
- Internal Claude Code performance metrics
- Cursor documentation or blog posts on benchmarking methodology
- Any existing benchmark scenarios (GitHub repos, research papers)

## Output

- Methodology comparison table (dimensions, scoring, scenarios)
- Gap analysis (missing benchmarks, methodological differences)
- Recommendations for improving Claude Code benchmarking
