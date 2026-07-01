# Golden Dataset Translation Patterns

Reference pattern for Step 5 (Generate Tests). The eval agent consults this when it determines golden datasets are the right approach for the artifact under test. This is NOT a hardcoded pipeline — the agent dynamically decides whether and how to use this based on the artifact.

## When This Reference Applies

Consult this pattern when:
- Target artifact has contract JSONs with `soft_validation_rules`, `success_criteria`, or `expected_artifacts`
- Golden dataset-based testing is appropriate for the artifact type

## When NOT to Use

- No contracts exist (test generation uses other signals)
- Artifact is better served by structural or behavioral metrics only
- Agent creates a different testing approach based on what it finds in `_reference/`

## Contract-to-Golden Mapping Table

| Contract Field | Golden Field | How |
|---------------|-------------|-----|
| Step file instruction | `input` | What the LLM is asked to do |
| `success_criteria` | `expected_output` | What correct behavior looks like |
| Step references | `context` | Reference material the LLM should consult |
| `soft_validation_rules` | GEval criteria | Each rule becomes a scoring criterion |
| `expected_artifacts` | ToolCorrectness assertions | Expected files the LLM must produce |

## DeepEval Golden Schema

```python
LLMTestCase(
    input="...",                    # From step file instruction
    expected_output="...",          # From success_criteria
    context=["..."],                # From references
    retrieval_context=["..."]       # Optional: what was actually retrieved
)
```

- `input`: The task or instruction the LLM receives
- `expected_output`: The correct or ideal response
- `context`: Ground-truth reference material
- `retrieval_context`: What the system actually retrieved (for RAG metrics)

## Severity-to-Threshold Mapping

| Contract Severity | Suggested Threshold |
|-------------------|-------------------|
| high | 0.80 |
| medium | 0.70 |
| low | 0.60 |

These are defaults. The agent may adjust based on artifact context.

## Example: Contract SV-301 Translation

**Source contract:** `step-03-contract.json`

```json
{
  "soft_validation_rules": [
    {
      "id": "SV-301",
      "description": "All date ranges must be contiguous",
      "severity": "high"
    }
  ],
  "success_criteria": [
    "Data validation report produced",
    "All high-severity rules pass"
  ]
}
```

**Translated to LLMTestCase + GEvalMetric:**

```python
# Golden test case from contract
test_case = LLMTestCase(
    input="Validate all date ranges in the dataset for contiguity",
    expected_output="All date ranges are contiguous with no gaps.",
    context=["reference/date-range-spec.md"]
)

# GEval metric from soft_validation_rules
metric = GEvalMetric(
    name="GEval_SV_301",
    criteria="All date ranges must be contiguous with no gaps",
    threshold=0.80  # high severity -> 0.80
)
```

**Translation steps:**
1. `success_criteria` -> `expected_output` (what correct behavior looks like)
2. Step instruction -> `input` (what the LLM is asked)
3. `soft_validation_rules[].description` -> `GEvalMetric.criteria`
4. `soft_validation_rules[].severity` -> threshold via mapping table
5. `expected_artifacts` -> ToolCorrectness assertions (file existence checks)

## Key Principle

This file is a pattern the agent reads — not a rigid pipeline. The agent decides whether and how to apply it based on the artifact under test. The agent is dynamic: it adapts to the artifact, not the other way around.
