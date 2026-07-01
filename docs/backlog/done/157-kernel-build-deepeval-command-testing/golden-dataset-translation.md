# Golden Dataset Translation: Reference Pattern for the Agent

## Status
NEW — reference file, not a pipeline step

## Purpose

This is a **reference pattern** that the eval agent consults when it decides golden datasets are the right approach for what it's testing. It is NOT a hardcoded step — the agent dynamically determines what to build based on the artifact being tested.

## When This Reference Applies

The agent consults this pattern when:
- The target artifact has contract JSONs with `soft_validation_rules`, `success_criteria`, or `expected_artifacts`
- The agent determines that golden dataset-based testing is appropriate for the artifact type

The agent may NOT use this pattern when:
- The artifact has no contracts (test generation uses other signals)
- The artifact type is better served by structural or behavioral metrics only
- The agent creates a different testing approach based on what it finds in `_reference/`

## The Pattern: Contract JSON → Golden Dataset

### Contract Fields That Map to Goldens

| Contract Field | Golden Field | How |
|---------------|-------------|-----|
| Step file instruction | `input` | What the LLM is asked to do |
| `success_criteria` | `expected_output` | What correct behavior looks like |
| Step references | `context` | Reference material the LLM should consult |
| `soft_validation_rules` | GEval criteria | Each rule becomes a scoring criterion |
| `expected_artifacts` | ToolCorrectness assertions | Did the LLM produce expected files |

### DeepEval Golden Schema

```python
LLMTestCase(
    input="...",           # From step file instruction
    expected_output="...", # From success_criteria
    context=["..."],       # From references
    retrieval_context=["..."]  # Optional: what was actually retrieved
)
```

### Severity → Threshold Mapping

| Contract Severity | Suggested Threshold |
|-------------------|-------------------|
| high | 0.80 |
| medium | 0.70 |
| low | 0.60 |

These are defaults. The agent may adjust based on artifact context.

## Example

**Contract:** `step-03-contract.json` with rule SV-301

```json
{
  "soft_validation_rules": [
    { "id": "SV-301", "description": "All date ranges must be contiguous", "severity": "high" }
  ],
  "success_criteria": ["Data validation report produced", "All high-severity rules pass"]
}
```

**Agent might produce:**
```python
LLMTestCase(
    input="Validate all date ranges in the dataset for contiguity",
    expected_output="All date ranges are contiguous with no gaps.",
    context=["reference/date-range-spec.md"]
)

GEvalMetric(
    name="GEval_SV_301",
    criteria="All date ranges must be contiguous with no gaps",
    threshold=0.80
)
```

## Key Principle

This file lives in the eval command's `references/` as a pattern the agent reads. The agent decides whether and how to use it based on what it's testing. The agent is dynamic — it adapts to the artifact, not the other way around.

## Where This Lives in the Eval Command

```
.claude/skills/eval/references/step-05/golden-translation-patterns.md
```

Consulted during Step 5 (Generate Tests) when the agent determines golden datasets are appropriate.
