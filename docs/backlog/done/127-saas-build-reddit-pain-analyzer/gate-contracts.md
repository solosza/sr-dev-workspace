# Gate Contracts — Data Validation Between Phases

Gate contracts are JSON schemas that validate data at every phase boundary. They ensure correctness between outer and inner skills.

## Contract Pattern

```json
{
  "phase": "skill-name/step-N",
  "input_gate": {
    "required_fields": ["field1", "field2"],
    "validations": [
      "field1 is string",
      "field1 length > 0"
    ]
  },
  "output_gate": {
    "required_fields": ["output_field"],
    "validations": [
      "output_field is array",
      "output_field.length > 0"
    ]
  },
  "failure_action": {
    "retry": true,
    "retry_count": 3,
    "backoff": "exponential"
  }
}
```

## Core Contracts

### Contract 1: reddit-data-pipeline → ai-analysis-engine

**Phase:** Data pipeline completes → AI analysis begins

**Input gate (AI analysis receives):**
```json
{
  "required_fields": ["text_content", "posts_count", "tokens"],
  "validations": [
    "text_content is string, length > 500",
    "posts_count >= 30",
    "tokens in [500, 5000]"
  ]
}
```

**Output gate (AI analysis produces):**
```json
{
  "required_fields": ["pain_points", "startup_ideas", "scored_ideas"],
  "validations": [
    "pain_points is array of strings, length >= 5",
    "startup_ideas is array of objects, length >= 5",
    "scored_ideas is array of objects, length >= 5",
    "all scored_ideas have score numeric [1, 10]",
    "all descriptions non-empty"
  ]
}
```

**Failure recovery:**
- LLM timeout → Retry 3x with exponential backoff
- Invalid JSON response → Retry with refined prompt
- Low quality (< 5 ideas) → Retry entire step
- After 3 retries → Mark phase failed, stop

### Contract 2: ai-analysis-engine → results-processor

**Phase:** AI analysis completes → Results processing begins

**Input gate (Results processor receives):**
```json
{
  "required_fields": ["pain_points", "startup_ideas", "scored_ideas"],
  "validations": [
    "All three arrays populated and non-empty",
    "pain_points.length >= 5",
    "startup_ideas.length >= 5",
    "scored_ideas.length >= 5",
    "All scores numeric [1, 10]",
    "No null/undefined fields"
  ]
}
```

**Output gate (Results processor produces):**
```json
{
  "required_fields": ["results_json", "results_markdown", "job_id", "timestamp"],
  "validations": [
    "results_json valid JSON parseable",
    "results_markdown valid Markdown",
    "Both contain pain_points and startup_ideas",
    "Both rendered consistently from same state",
    "job_id is UUID format",
    "timestamp is ISO 8601"
  ]
}
```

### Contract 3: Outer loop → User

**Phase:** Harness completes → User receives deliverables

**Output gate (Harness produces):**
```json
{
  "required_fields": ["results_json", "results_markdown", "job_id", "timestamp"],
  "validations": [
    "Both files exist and are readable",
    "results_json has valid JSON syntax",
    "results_markdown renders without errors",
    "job_id is UUID format",
    "timestamp is ISO 8601 format",
    "file sizes reasonable (10-20KB json, 8-15KB md)"
  ]
}
```

## Cost Tracking Contract

**Goal:** Ensure cost never exceeds budget

```json
{
  "phase": "cost-tracking",
  "input_gate": {
    "required_fields": ["estimated_cost"],
    "validations": [
      "estimated_cost < 0.50"
    ]
  },
  "output_gate": {
    "required_fields": ["actual_cost"],
    "validations": [
      "actual_cost <= estimated_cost * 1.2",
      "actual_cost < 0.50"
    ]
  },
  "failure_action": {
    "retry": false,
    "on_failure": "hard block, alert admin"
  }
}
```

**Enforcement:** If actual_cost > €0.50, execution stops immediately.

## State Validation Contract

**Every state file transition is validated:**

```
Before step: Input gate validates preconditions
  ↓
Step executes (agent follows skill instructions)
  ↓
After step: Output gate validates results
  ↓
If both pass: State updated, next step starts
If either fails: Retry or fail gracefully
```

## Error Codes

| Code | Phase | Recovery |
|------|-------|----------|
| GATE-INPUT-001 | Missing required field | Fail immediately |
| GATE-INPUT-002 | Type mismatch | Fail immediately |
| GATE-OUTPUT-001 | Output incomplete | Retry 3x |
| GATE-OUTPUT-002 | Output invalid format | Retry 3x |
| GATE-COST-001 | Cost exceeds limit | Hard block |

## Testing Gate Contracts

Each contract includes test fixtures:

```json
{
  "test_input_valid": {
    "text_content": "How to validate startup ideas Finding qualified contractors...",
    "posts_count": 75,
    "tokens": 4200
  },
  "test_input_invalid": {
    "text_content": "",
    "posts_count": 10,
    "tokens": 100
  },
  "test_output_valid": {
    "pain_points": ["Hard to find contractors", "Expensive platforms", "Time-consuming", "Quality issues", "Hidden fees"],
    "startup_ideas": [
      {"title": "Vetted Marketplace", "description": "..."},
      {"title": "Executive Network", "description": "..."},
      {"title": "Skill Verification", "description": "..."},
      {"title": "Escrow Service", "description": "..."},
      {"title": "Training Platform", "description": "..."}
    ],
    "scored_ideas": [
      {"title": "Vetted Marketplace", "score": 8.5, "reasoning": "..."},
      {"title": "Executive Network", "score": 7.2, "reasoning": "..."},
      {"title": "Skill Verification", "score": 7.8, "reasoning": "..."},
      {"title": "Escrow Service", "score": 6.9, "reasoning": "..."},
      {"title": "Training Platform", "score": 7.1, "reasoning": "..."}
    ]
  },
  "test_output_invalid": {
    "pain_points": [],
    "startup_ideas": null,
    "scored_ideas": [{"title": "Idea", "score": 15}]
  }
}
```

## Enforcement Mechanism

**Soft enforcement (specification):** Agent reads gate contracts and validates data as instructed in skill markdown.

**Hard enforcement:** Hooks monitor execution and block if gates fail.

Agent algorithm:
```
1. Before executing step: Load input gate from contract
2. Validate current state matches input gate requirements
3. If invalid: Fail immediately with gate error code
4. If valid: Execute step (agent follows skill instructions)
5. After step: Load output gate from contract
6. Validate step output matches output gate requirements
7. If invalid: Retry (if failure_action.retry=true) or fail
8. If valid: Pass to next step
```

## Contract Lifecycle

1. **Define** — Write contract JSON for each phase boundary
2. **Test** — Validate against test fixtures
3. **Deploy** — Load into skill specifications
4. **Monitor** — Track gate failures, alert on violations
5. **Improve** — Refine contracts based on failure patterns

---

Gate contracts are the **safety net** that catches data errors at boundaries, not downstream.
