# Step 5: Generate Tests

Dynamically build a pytest-based deepeval test suite based on the artifact analysis from Step 4. Consult `_reference/` patterns for golden datasets, metrics, and test structure — adapt to the artifact, not the other way around.

## Input

| Field | Source | Example |
|-------|--------|---------|
| `mode` | Output of Step 0 | `artifact` or `harness` |
| `target` | Output of Step 0 | `check-data` (artifact mode) or `null` (harness mode) |
| `test-repo` | Output of Step 1 | `D:\...\evals\eval-check-data` |
| Component decision log | Output of Step 4 | REUSED/CREATED/SKIPPED components |
| Pipeline type | Step 4 checkpoint | Agent / RAG / Hybrid / Harness |
| Contract rules | Step 4 directed reading | List of `soft_validation_rules` (artifact mode only) |

## Pre-Generation Checkpoint

Before writing any test files, read the golden translation reference:
→ `references/step-05/golden-translation-patterns.md`

This reference defines how contract fields map to golden dataset entries. Only apply this pattern when contracts exist with `soft_validation_rules`, `success_criteria`, or `expected_artifacts`.

## Mode-Specific Behavior

### Harness Mode — Test Generation Strategy

In harness mode, the "artifact" is the entire repo. Tests evaluate the harness as a system using GEval with custom criteria. The agent reads each component from `harness-under-test/` and generates test cases.

**Harness eval dimensions (each becomes one or more GEval test cases):**

| Dimension | What's Tested | GEval Criteria | Input | Actual Output |
|-----------|--------------|---------------|-------|---------------|
| **Command quality** | Each command .md | "Are instructions unambiguous, complete, and sequentially executable by an LLM agent?" | Command filename + purpose | Full command text |
| **Skill completeness** | Each skill directory | "Does this skill have clear identity, complete step table, and no missing file references?" | Skill name | SKILL.md text |
| **CLAUDE.md coherence** | CLAUDE.md | "Does this accurately describe the system's loop, commands, and enforcement? Are there contradictions?" | "Describe this harness" | CLAUDE.md text |
| **Loop integrity** | Cross-command references | "Do these commands form a complete, unbroken loop? Is every transition accounted for?" | Loop description from CLAUDE.md | Concatenated command summaries |
| **Hook coverage** | Hooks vs CLAUDE.md enforcement claims | "Does every enforcement claim in CLAUDE.md have a corresponding hook implementation?" | Enforcement claims | Hook file names + descriptions |

**Structural checks (non-GEval, L1/L2):**

| Check | Method | Pass |
|-------|--------|------|
| Manifest integrity | Every file in `kernel-manifest.json` exists | All present |
| Settings wiring | Every hook .py in `.claude/hooks/` is registered in `settings.local.json` | All wired |
| Skill structure | Every skill dir has `SKILL.md` | All present |
| Reference resolution | Every `->` wikilink in all .md files resolves | All resolve |

Both GEval tests and structural checks go into the test suite.

### Artifact Mode — Test Generation Strategy (unchanged)

Follows the existing contract-based golden translation approach.

## What to Produce

### 1. conftest.py

Create `<test-repo>/tests/conftest.py` with:

```python
import pytest
import json
from pathlib import Path

@pytest.fixture
def golden_dataset():
    """Load golden dataset from fixtures if available."""
    fixture_path = Path(__file__).parent.parent / "framework" / "fixtures"
    datasets = {}
    if fixture_path.exists():
        for f in fixture_path.glob("*.json"):
            datasets[f.stem] = json.loads(f.read_text())
    return datasets

@pytest.fixture
def eval_config():
    """Load eval configuration (thresholds, model, etc.)."""
    return {
        "model": "gpt-4o-mini",
        "threshold_high": 0.80,
        "threshold_medium": 0.70,
        "threshold_low": 0.60
    }
```

Adapt fixtures to what Step 4 discovered — add component-specific fixtures as needed.

### 2. Test File(s)

Create `<test-repo>/tests/test_eval_<target>.py` with parametrized test cases:

- One test function per metric type discovered in Step 4
- Use `@pytest.mark.parametrize` for multiple test cases per metric
- Import metric classes from `framework/metrics/`
- Import task runners from `framework/tasks/` if needed

### 3. Golden Dataset Fixtures (When Contracts Exist)

For each contract with `soft_validation_rules` or `success_criteria`:

1. Translate contract fields to `LLMTestCase` instances:
   - `input` ← step file instruction (what the LLM is asked to do)
   - `expected_output` ← `success_criteria` (what correct behavior looks like)
   - `context` ← step references (reference material the LLM should consult)

2. Write fixture JSON to `<test-repo>/framework/fixtures/<target>_golden.json`

3. Load via conftest.py `golden_dataset` fixture

### 4. Metric Instances with Thresholds

Select metrics based on pipeline type and artifact analysis:

| Pipeline Type | Primary Metrics | When to Use |
|--------------|----------------|-------------|
| Agent | ToolCorrectness, TaskCompletion | Agent produces tools/actions |
| RAG | Faithfulness, ContextualRelevancy | Retrieval-based pipeline |
| Hybrid | GEval (custom criteria) | Mixed or custom contract rules |
| Harness | GEval (per dimension) + structural checks | Whole-repo harness eval |

#### Threshold Mapping

| Contract Severity | Threshold | Applies To |
|-------------------|-----------|------------|
| high | 0.80 | Critical validation rules |
| medium | 0.70 | Standard validation rules |
| low | 0.60 | Advisory rules |

These are defaults — adjust based on artifact context and what Step 4 discovered.

## No-Contract Fallback

When the artifact has NO contracts (no `soft_validation_rules`, no `success_criteria`):

1. Skip golden dataset generation entirely
2. Use structural and behavioral metrics instead:
   - **Structural**: does the output have expected format/fields?
   - **Behavioral**: does invoking the artifact produce consistent results?
3. Generate test cases from Step 4's directed reading summary (pipeline type, step count, output type)

## Verification

| ID | Check | Method | Pass |
|----|-------|--------|------|
| G5.1 | conftest.py exists | `test -f <test-repo>/tests/conftest.py` | File present |
| G5.2 | Fixtures load | `python -c "import conftest"` in test dir | No import error |
| G5.3 | At least one test case | `grep -r "def test_" <test-repo>/tests/` | At least 1 match |
| G5.4 | Metrics have thresholds | Test file contains threshold values | Present |
| G5.5 | Golden fixtures valid (if applicable) | JSON parses without error | Valid JSON |

All checks must pass before transitioning to Step 6.

## Error Handling

| Failure | Action |
|---------|--------|
| No metrics match pipeline type | Default to GEval with generic criteria |
| Golden dataset translation fails | Fall back to no-contract approach |
| conftest.py import fails | Check paths, fix relative imports. Retry once. |
| No test cases generated | Abort — Step 4 analysis may be incomplete |
| Still failing after retry | Set `failed` state with `resume_step: 5`. Invoke `/kernel/learn`. |

## Output

- `<test-repo>/tests/conftest.py` — fixture loading and eval config
- `<test-repo>/tests/test_eval_<target>.py` — parametrized deepeval test cases
- `<test-repo>/framework/fixtures/<target>_golden.json` (if contracts exist)
- State transition: `checking_components` → `generating_tests` → ready for Step 6
- Contract: → `contracts/step-05-contract.json`
