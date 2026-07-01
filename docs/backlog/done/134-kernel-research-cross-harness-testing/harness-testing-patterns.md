# Harness Testing Patterns & Methodology

## Status
NEW — Research phase, exploring how to systematically test harness behavior

## Location
`workspace:docs/harness-design-pattern` (research documentation)

## Purpose

Define what it means to "test a harness" and what methodology would measure harness-specific performance dimensions. Identify testable dimensions of harness behavior: context management, decision-making quality, error recovery, conversation state handling, and goal pursuit strategies.

## Key Questions

- What is a "testable dimension" of harness behavior?
- How do we isolate harness performance from model performance?
- What test cases would reveal harness quality differences?
- How do we measure context management effectiveness?
- What metrics correlate with the 4.2-point performance gap?
- Can we use adversarial testing (intentional failures, edge cases)?

## Research Areas

### 1. Harness vs. Model Distinction

**Status:** NEW — critical distinction needs clarification
- What aspects of performance are harness-driven vs. model-driven?
- Can we swap models and measure harness contribution?
- What is "harness-neutral" baseline testing?

**Testability questions:**
- Is context management measurable independent of model quality?
- Is decision-making quality testable without model variation?
- Can we use same model with different harnesses?

### 2. Testable Harness Dimensions

**Status:** NEW — needs identification

Potential dimensions to test:
1. **Context Window Management**
   - Token allocation efficiency (how well is budget spent?)
   - Recall accuracy (can harness retrieve relevant context?)
   - Compression strategy (how are old contexts summarized?)

2. **Decision-Making Quality**
   - Task decomposition (does harness break goals into logical steps?)
   - State tracking (does harness maintain conversation state correctly?)
   - Error detection (does harness recognize mistakes, contradictions?)
   - Recovery (can harness self-correct and retry?)

3. **Conversation Architecture**
   - Turn structure (how are exchanges organized?)
   - State transitions (clear state machine vs. ad-hoc?)
   - Goal tracking (explicit goal stack vs. implicit?)

4. **Scalability & Robustness**
   - Multi-turn reliability (does performance degrade over long conversations?)
   - Context saturation (what happens at token limit?)
   - Error cascades (single mistake → multiple failures?)

### 3. Test Case Design

**Status:** NEW — needs methodology

Test case categories:
1. **Unit tests** (isolated harness components)
   - Token counting accuracy
   - Context pruning strategies
   - Decision tree evaluation

2. **Integration tests** (harness + model interaction)
   - Can harness + model solve multi-step problems?
   - Does conversation state persist correctly?
   - Are failures recovered from?

3. **Scenario tests** (realistic workflows)
   - Complex task (10+ step goal)
   - Adversarial input (contradictions, impossible requests)
   - Context saturation (approaching token limit)
   - Long conversation (50+ turns)

4. **Comparative tests** (harness A vs. harness B)
   - Same problem, different harnesses
   - Measure decision quality, context usage, error recovery
   - Quantify delta

### 4. Metrics Definition

**Status:** NEW — needs specification

Candidate metrics:
- **Efficiency:** Context tokens used / total available (waste ratio)
- **Recall:** Correct context retrieved / total relevant context (precision, recall)
- **Accuracy:** Correct decisions / total decisions (decision error rate)
- **Robustness:** Successful recovery / total errors (error recovery rate)
- **Convergence:** Steps to goal completion / optimal steps (solution efficiency)
- **Consistency:** Performance variance across repeated runs (stability)

**Measurement approach:**
- Instrument harness to log: context operations, decisions, state transitions
- Collect per-turn metrics (token count, decision quality, state consistency)
- Aggregate to per-test and per-harness scores
- Compare across harnesses

### 5. Isolation Testing (Harness-Specific)

**Status:** NEW — needs strategy

How to isolate harness effects:
1. **Control group approach:** Same task, same model, different harnesses
2. **Synthetic tasks:** Problems designed to expose harness differences (not model differences)
3. **Instrumentation:** Log harness-level operations independent of model
4. **Baseline normalization:** Account for model variance in comparison

**Blockers:**
- Closed-source harnesses (Cursor, etc.) may not be instrumentable
- Need access to multiple harnesses for comparison
- Model variance may obscure harness effects

## Output

- **Harness testing framework:** Dimensions, test case categories, metrics
- **Test case library:** 20+ test cases that reveal harness quality differences
- **Metrics specification:** Precise definitions, measurement methods, aggregation
- **Isolation strategy:** How to measure harness independent of model
- **Feasibility assessment:** What's testable, what's blocked, what requires tooling
- **Tooling gaps:** What would need to be built to enable harness testing

## Dependencies

Depends on: [[134-kernel-research-cross-harness-testing/qa-platform-analysis]] (patterns to reuse)

## Notes

This research should answer: "If we built a harness testing framework, what would it actually test?"
