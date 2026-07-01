# Context Management Analysis

## Status
NEW — Research phase, analyzing context strategies

## Location
`workspace:docs/harness-design-pattern` (research documentation)

## Purpose

Deep dive into how Cursor and Claude Code manage context windows, allocate tokens, maintain conversation state, and optimize for recall. Context management is the hypothesized root cause of the performance gap, so this analysis is critical.

## Key Questions

- How does each harness allocate tokens between system prompt, conversation history, and function calls?
- What's the strategy for handling long conversations (truncation, summarization, selective recall)?
- How are previous decisions/context tracked and recalled during new interactions?
- What role does conversation metadata (timestamps, success/failure flags) play?
- How do the harnesses handle context switches between tasks?

## Research Areas

### 1. Token Allocation Strategy
- System prompt size (Cursor vs Claude Code)
- Conversation history retention (full vs sliding window vs hierarchical?)
- Reasoning/thinking token budget (CoT vs inline vs explicit planning?)
- Function call overhead and token cost

### 2. Conversation State Management
- How is state persisted between interactions?
- What context is surfaced to the model on each turn?
- Are there explicit state objects or implicit in the conversation?
- How are decisions and rationales tracked?

### 3. Recall and Context Injection
- How does each harness retrieve relevant prior context?
- Is there semantic search (embedding-based)?
- Are there explicit "memory" structures or just conversation history?
- How are function results cached or summarized?

### 4. Conversation Architecture
- Is the harness stateful or stateless?
- How are multi-turn interactions structured?
- Are there explicit turn-taking rules or negotiation protocols?
- How does the harness handle contradictions or retractions?

### 5. Optimization Techniques
- Context pruning/compression (removing redundant context)?
- Hierarchical summarization of past conversations?
- Selective token allocation per task type?
- Explicit decision trees to avoid re-reasoning?

## Input Schema

- Cursor harness documentation or code samples
- Claude Code harness specification (.claude/protocols, skills, commands)
- Any public writing on context management (Anthropic blog, papers)
- Comparative analysis framework (dimensions, scoring)

## Output

- Context management strategy matrix (Cursor vs Claude Code)
- Token allocation breakdown per harness
- State management architecture diagram
- Identified differences and hypothesized impact on performance

## Dependencies

Depends on: [[133-kernel-research-harness-design-pattern-optimization/benchmarking-methodology]]
(Need to understand what's being measured before optimizing context)
