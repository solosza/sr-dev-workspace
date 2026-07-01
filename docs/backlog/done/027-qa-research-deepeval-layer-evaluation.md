# DeepEval Platform — 5-Layer Architecture Evaluation

## Status
Open

## Priority
Medium — architectural debt check before building more eval features

## Summary
Evaluate whether the DeepEval platform (test-platform-deepeval) actually needs the full 5-layer architecture or if it is over-abstracted. The SSH compliance work revealed that the Task layer (L3) can be a pass-through in some domains. DeepEval may have the same issue — does EvalTask carry real weight between EvalRole and Metric Object, or is it just forwarding calls? Research industry eval patterns and compare against the current implementation.

## Requirements
- Read the actual EvalTask implementations — do they compose multiple Metric Object calls, or just forward one?
- Compare against how DeepEval SDK is used natively (no framework)
- Check if EvalRole directly calling Metric Objects would simplify without losing capability
- If 4 layers is sufficient, document what collapses and what stays
- If 5 layers is justified, document WHY the Task layer earns its existence

## References
- DeepEval platform: isagawa-qa/test-platform-deepeval
- SSH compliance layer analysis (validators are L2, Task was questioned)
- Industry comparison: InSpec 4-layer, Testinfra 3-layer

## Task Builder Input
- **Deliverable:** Architecture evaluation document with recommendation (keep 5 / collapse to 4) + evidence
- **Scope:** RESEARCH
- **Constraints:** Read-only analysis. No code changes until recommendation approved.
