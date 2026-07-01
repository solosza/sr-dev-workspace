# Performance Gap Root Cause Analysis

## Status
NEW — Research phase, connecting context strategies to performance delta

## Location
`workspace:docs/harness-design-pattern` (research documentation)

## Purpose

Identify the specific design decisions and architectural patterns in Cursor's harness that drive the 4.2-point performance advantage over Claude Code. Root cause analysis bridges context management techniques with measurable performance outcomes.

## Key Questions

- Which context management strategies have the biggest performance impact?
- Is the gap driven by a single dimension (e.g., token allocation) or multiple factors?
- Are there quick wins (easy-to-implement improvements) vs. architectural overhauls?
- What's the performance impact of each identified difference?
- Are there trade-offs (e.g., context size vs. cost) that explain the gap?

## Research Areas

### 1. Performance Delta Attribution

Analyze the 4.2-point gap (10.4 vs 6.2):
- How much is explained by context window management?
- How much by conversation state architecture?
- How much by token allocation?
- How much by recall/retrieval strategy?
- Are there unexplained factors?

### 2. Cursor's High-Performing Patterns

Identify specific design decisions in Cursor that correlate with high performance:
- System prompt engineering (does Cursor use specialized prompts per task type?)
- Token budget management (how does Cursor allocate?)
- Conversation structure (stateful patterns, explicit decision trees?)
- Recovery mechanisms (how does Cursor handle errors/contradictions?)

### 3. Claude Code's Underperforming Patterns

Identify specific gaps in Claude Code harness:
- Is system prompt too generic or task-agnostic?
- Is token budget wasted on verbose output?
- Are there missing recall mechanisms?
- Is conversation state insufficiently tracked?

### 4. Hypothesis Generation

Develop ranked hypotheses:
1. [High confidence] Context management difference → estimated 2-point impact
2. [Medium confidence] System prompt optimization → estimated 1-point impact
3. [Low confidence] Token allocation → estimated 0.5-point impact
...

### 5. Validation Strategy

Plan how to validate hypotheses:
- Can we measure each dimension independently?
- Are there A/B tests possible (swap one component at a time)?
- What would constitute proof of root cause?

## Input Schema

Depends on outputs from:
- [[133-kernel-research-harness-design-pattern-optimization/benchmarking-methodology]]
- [[133-kernel-research-harness-design-pattern-optimization/context-management-analysis]]

Needs:
- Performance metrics per dimension
- Architecture details of both harnesses
- Benchmark results (breakdown by task type if available)

## Output

- Root cause attribution table (factor → estimated performance impact)
- Ranked hypotheses (confidence, estimated impact, validation method)
- Quick wins summary (high-impact, low-effort improvements)
- Decision tree for optimization prioritization

## Dependencies

Depends on: Benchmarking methodology, context management analysis
