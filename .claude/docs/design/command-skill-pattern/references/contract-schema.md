# Contract Schema

<!-- Payload of: command-skill-pattern/index.md -->

## JSON Schema

```json
{
  "contract_metadata": {
    "contract_id": "[command-name]:step-N:output",
    "version": "1.0",
    "artifact_type": "markdown|sql|json",
    "artifact_filename": "...",
    "canonical_reference": {
      "path": "skills/[command-name]/references/step-N/canonical-example.md",
      "hash": "sha256_hash",
      "section_examples": {
        "example_name": "lines X-Y"
      }
    },
    "dependencies": [
      {
        "contract_id": "[command-name]:step-M:output",
        "version": "^1.0",
        "required": true
      }
    ],
    "validation_metadata": {
      "validation_count": 0,
      "last_validated_at": null,
      "staleness_threshold_hours": 24
    }
  },
  "validations": [
    {
      "rule_id": "rule_name",
      "description": "...",
      "pattern": "regex or null",
      "violation_message": "...",
      "how_to_fix": "...",
      "canonical_reference_section": "lines X-Y",
      "example": "..."
    }
  ],
  "mechanical_validations": [
    {
      "rule_id": "rule_name",
      "type": "pattern|existence|uniqueness|presence|count",
      "pattern": "regex if type==pattern",
      "check": "...",
      "applies_to": "artifact_filename",
      "severity": "BLOCK|WARN",
      "violation_message": "...",
      "how_to_fix": "...",
      "canonical_reference_section": "lines X-Y",
      "example": "..."
    }
  ],
  "overrides": []
}
```

---

## Contract Dependencies (dbt pattern)

- Each contract declares what upstream contracts it requires
- Downstream contracts declare requirements (not upstream declaring produces_for)
- Forms acyclic dependency chain: Step 1 -> Step 2 -> Step 3 -> ... -> Step N

---

## Dual Validation

### Soft Gate (Agent-Driven)

- Agent reads contract.validations rules
- Agent reads canonical_reference examples
- Agent validates artifact against rules + examples
- Reports violations with how_to_fix + reference section
- Agent records lessons via `/kernel/learn` if pattern discovered

### Hard Gate (Hook-Driven)

- Hook intercepts file write
- Hook reads contract.mechanical_validations
- Hook checks rules deterministically (regex, uniqueness, etc.)
- Blocks write if severity==BLOCK, allows if all pass
- Reports error with how_to_fix + example + canonical reference

### Why Both

| Gate | Catches | Example |
|------|---------|---------|
| Soft | Content is wrong but formatted correctly | Test case has correct headers but tests the wrong thing |
| Hard | Format is wrong regardless of content | Missing headers, no keywords, format violations |

Neither gate alone is sufficient. Together they cover both content quality and structural compliance.
