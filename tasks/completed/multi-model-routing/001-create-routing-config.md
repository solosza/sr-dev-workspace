# Task 001: Create model-routing-config.json

**Type:** BUILD
**Action:** Create routing configuration file

## What

Create `lib/model-routing-config.json` with model tier definitions and routing rules.

```json
{
  "default_model": "claude-opus-4-6",
  "tiers": {
    "opus": {
      "model_id": "claude-opus-4-6",
      "description": "Architecture, complex code, production precision, multi-file coordination",
      "task_types": [],
      "keywords": ["architecture", "refactor", "security", "migration", "multi-file", "production", "critical"]
    },
    "sonnet": {
      "model_id": "claude-sonnet-4-6",
      "description": "Standard builds, test writing, research synthesis, moderate complexity",
      "task_types": ["BUILD", "TEST", "RESEARCH"],
      "keywords": ["implement", "write", "create", "update", "test", "research"]
    },
    "haiku": {
      "model_id": "claude-haiku-4-5-20251001",
      "description": "File scaffolding, data formatting, simple edits, copy tasks",
      "task_types": [],
      "keywords": ["copy", "scaffold", "format", "rename", "move", "simple", "trivial"]
    }
  },
  "routing_rules": {
    "criteria_threshold": 3,
    "opus_if_criteria_above": 5,
    "haiku_if_criteria_below": 2
  },
  "retry_upgrade_order": ["haiku", "sonnet", "opus"]
}
```

## Acceptance Criteria

- [ ] File exists at `lib/model-routing-config.json`
- [ ] File is valid JSON: `python -c "import json; json.load(open('lib/model-routing-config.json'))"` exits 0
