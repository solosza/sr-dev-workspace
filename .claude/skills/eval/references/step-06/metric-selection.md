# Metric Selection Guide

Reference for Step 6 (Run and Score). The eval agent consults this when selecting deepeval metrics for the test suite. Selection depends on the pipeline type of the artifact under test and the contracts discovered during component check.

## Pipeline Type to Metric Mapping

| Pipeline Type | Primary Metrics | When to Use |
|--------------|----------------|-------------|
| **Agent pipeline** (kernel commands, tool-calling agents) | ToolCorrectness, TaskCompletion, GEval (per contract rule) | Artifact uses tools, produces files, follows multi-step instructions |
| **RAG pipeline** (retrieval-augmented generation) | Faithfulness, ContextualRelevancy, AnswerRelevancy | Artifact retrieves context and generates answers from it |
| **Hybrid** (agent + RAG) | All of the above | Artifact both retrieves context and calls tools/produces artifacts |
| **Structural** (no contracts, static output) | File existence checks, output format validation | Artifact produces files with known structure but no behavioral contracts |
| **Harness** (whole repo as system) | GEval (per dimension), structural assertions | Harness mode — evaluating commands, skills, hooks, loop integrity as a system |

## Metric Descriptions

### Agent Metrics

- **ToolCorrectness**: Validates that the LLM calls the right tools with correct arguments and produces expected artifacts. Maps from `expected_artifacts` in contracts.
- **TaskCompletion**: Validates that multi-step task instructions are fully executed. Maps from `success_criteria` in contracts.
- **GEval** (per contract): One GEval metric per `soft_validation_rules` entry. The `criteria` field comes directly from the rule's `description`.

### RAG Metrics

- **Faithfulness**: Measures whether the generated output is factually consistent with the retrieved context. Catches hallucination.
- **ContextualRelevancy**: Measures whether the retrieved context is relevant to the input query. Catches retrieval failures.
- **AnswerRelevancy**: Measures whether the generated answer addresses the input query. Catches off-topic responses.

### Structural Checks

- **File existence**: `os.path.exists()` on each `expected_artifacts` path
- **Format validation**: JSON schema checks, line count bounds, required section headers

### Harness Metrics

- **GEval: Command Quality**: Per-command evaluation — "Are instructions unambiguous, complete, and sequentially executable by an LLM agent?" Threshold: 0.70.
- **GEval: Skill Completeness**: Per-skill evaluation — "Does this skill have clear identity, complete step table, and no missing file references?" Threshold: 0.70.
- **GEval: CLAUDE.md Coherence**: System-level — "Does this accurately describe the system's loop, commands, and enforcement? Are there contradictions?" Threshold: 0.80.
- **GEval: Loop Integrity**: Cross-command — "Do these commands form a complete, unbroken loop? Is every transition accounted for?" Threshold: 0.80.
- **GEval: Hook Coverage**: Enforcement — "Does every enforcement claim in CLAUDE.md have a corresponding hook implementation?" Threshold: 0.80.
- **Structural: Manifest Integrity**: Every file in `kernel-manifest.json` exists. Binary pass/fail (1.0).
- **Structural: Settings Wiring**: Every hook .py is registered in `settings.local.json`. Binary pass/fail (1.0).
- **Structural: Reference Resolution**: Every `->` wikilink in all .md files resolves. Binary pass/fail (1.0).

## Metric Sources

| Source | What It Provides |
|--------|-----------------|
| `_reference/` metrics in target repo | Pre-existing deepeval metric definitions the artifact already uses |
| Step 4 component check | Discovered contracts, `soft_validation_rules`, `expected_artifacts` |
| Step 5 generated tests | New GEval metrics created from contract translation |
| This file | Selection logic for which metrics apply to which pipeline type |

The agent checks `_reference/` first. If existing metrics cover the artifact, reuse them. Only create new metrics when contracts require coverage that existing metrics don't provide.

## Threshold Defaults

Thresholds derive from contract severity:

| Contract Severity | Threshold | Meaning |
|-------------------|-----------|---------|
| high | 0.80 | Must score at or above 80% to pass |
| medium | 0.70 | Must score at or above 70% to pass |
| low | 0.60 | Must score at or above 60% to pass |

When no contract severity exists (e.g., structural checks), use 1.0 for binary pass/fail or 0.70 as a safe default for scored metrics.

## Metric Combination Rules

Every test suite MUST include:

1. **At least one pipeline-type metric** from the mapping table above (based on detected pipeline type)
2. **One GEval metric per contract rule** (when `soft_validation_rules` exist in contracts)
3. **ToolCorrectness assertions** (when `expected_artifacts` exist in contracts)

### Minimum viable test suites by pipeline type:

| Pipeline Type | Minimum Metrics |
|--------------|----------------|
| Agent | 1x TaskCompletion + 1x GEval per contract rule |
| RAG | 1x Faithfulness + 1x AnswerRelevancy |
| Hybrid | 1x TaskCompletion + 1x Faithfulness + GEval per contract |
| Structural | File existence for each expected artifact |
| Harness | 1x CLAUDE.md Coherence + 1x Loop Integrity + 1x GEval per command + structural checks |

## Override Guidance

The agent may adjust thresholds based on artifact context, but must document rationale:

```python
# Example: lowering threshold with documented rationale
GEvalMetric(
    name="GEval_SV_301",
    criteria="All date ranges must be contiguous",
    threshold=0.65  # Lowered from 0.80: artifact handles ambiguous date formats
    # Rationale: date parsing edge cases reduce deterministic scoring
)
```

**Override rules:**
- Never lower a high-severity threshold below 0.60
- Never lower a medium-severity threshold below 0.50
- Document the rationale inline (comment or test metadata)
- If more than 50% of thresholds need overrides, reassess whether the pipeline type classification is correct

## Key Principle

This file is a selection guide the agent reads — not a rigid pipeline. The agent decides which metrics to apply based on what it discovers in the artifact's contracts and `_reference/` directory. The agent adapts to the artifact, not the other way around.
