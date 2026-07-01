# DeepEval Platform — 5-Layer Architecture Evaluation

**Backlog:** 027-qa-research-deepeval-layer-evaluation
**Date:** 2026-06-22
**Verdict:** Keep 5 layers. Task layer earns its existence.

## Question

Does the DeepEval platform need the full 5-layer architecture, or is the Task layer (L3) over-abstracted?

## Evidence

### Layer 3 Implementations Examined

| Task File | Metrics Composed | Additional Logic |
|-----------|-----------------|-----------------|
| `run_rag_eval.py` | FaithfulnessMetrics + RetrievalMetrics + RelevancyMetrics | Stores results on test_case as `_eval_results` dict |
| `run_agent_eval.py` | AgentMetrics | Stores results on test_case |
| `run_read_compliance_eval.py` | ReadComplianceMetric + ReadTraceParser | Two variants: explicit lists vs trace parsing. Prints formatted results. |

### Does L3 Carry Real Weight?

**Yes.** The Task layer provides three functions that don't belong at L2 (Metric Object) or L4 (Role):

1. **Multi-metric composition** — `run_rag_eval` orchestrates 3 separate Metric Objects in one call. Without L3, the Role would contain this composition logic, mixing orchestration (iterate over dataset) with evaluation (run metrics). L3 keeps these concerns separate.

2. **Result storage pattern** — Tasks attach results to the test_case object (`test_case._eval_results`), creating a standard accessor pattern. This is a coordination concern, not a metric concern.

3. **Variant dispatch** — `run_read_compliance_eval.py` exposes two entry points for the same evaluation: `run_read_compliance_eval()` (from explicit lists) and `run_read_compliance_from_trace()` (from agent trace files). This variant logic doesn't belong in the metric (L2) or the orchestrator (L4).

### Comparison: What If L3 Collapsed?

If Tasks collapsed into Roles:

```python
# RAGEvaluator.evaluate_pipeline would become:
for golden in dataset:
    test_case = ...
    # All this composition logic moves into the Role:
    faithfulness = FaithfulnessMetrics(thresholds).evaluate(test_case)
    retrieval = RetrievalMetrics(thresholds).evaluate(test_case)
    relevancy = RelevancyMetrics(thresholds).evaluate(test_case)
    test_case._eval_results = { ... }
```

This works but:
- Role now knows which metrics to run (coupling)
- Agent pipeline would duplicate the composition pattern
- Adding a new pipeline type requires editing a Role, not just writing a new Task

### Industry Comparison

| Framework | Layers | Task Equivalent? |
|-----------|--------|-----------------|
| InSpec | 4 (Profile → Control → Resource → Matcher) | Yes — Control groups Resources |
| Testinfra | 3 (Test → Module → Backend) | No — Module does double duty |
| DeepEval SDK (native) | 2 (Metric → assert_test) | No — composition is user's problem |
| Isagawa DeepEval | 5 (Interface → Metric → Task → Role → Test) | Yes — Task composes Metrics |

Frameworks with a composition layer (InSpec's Control, our Task) are easier to extend. Testinfra's lack of one is a known pain point for complex assertions.

## Recommendation

**Keep 5 layers.** The Task layer:
- Prevents Role bloat when multiple metrics are needed
- Enables variant dispatch (trace vs explicit)
- Maintains the single-responsibility pattern (Metric = score, Task = compose, Role = orchestrate)
- Matches InSpec's proven 4-layer pattern (our Interface layer is the additional one, justified by SDK wrapping)

The `run_agent_eval` task is the weakest case (only one metric), but even there, the pattern consistency across pipeline types justifies keeping it — adding new agent metrics later won't require restructuring.

## No Action Required

Architecture is sound. No changes recommended.
