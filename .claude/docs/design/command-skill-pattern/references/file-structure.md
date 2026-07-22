# File Structure

<!-- Payload of: command-skill-pattern/index.md -->

## Canonical Tree

```
.claude/
|-- commands/kernel/
|   +-- [command-name].md
|-- skills/[command-name]/
|   |-- SKILL.md (orchestrator, vocabulary, rules)
|   |-- workflow.md (phase definitions, state schema)
|   |-- gate-contract.md (phase gates, verification)
|   |-- steps/
|   |   |-- step-01-[name].md
|   |   |-- step-02-[name].md
|   |   +-- step-N-[name].md
|   |-- references/
|   |   |-- INDEX.md (tiered indexing with wikilinks)
|   |   |-- step-01/
|   |   |   |-- canonical-example-1.md
|   |   |   +-- pattern-guide.md
|   |   |-- step-02/
|   |   |   +-- canonical-example.md
|   |   +-- step-N/
|   |       +-- [references]
|   +-- contracts/
|       |-- step-01-contract.json
|       |-- step-02-contract.json
|       +-- step-N-contract.json
|-- hooks/
|   +-- [hook-name].py (reads contracts, validates mechanical_validations)
+-- docs/design/
    |-- command-skill-pattern/
    |   +-- index.md (this pattern)
    +-- [command-name]/
        +-- index.md (specific command design)
```

---

## State Persistence

**Location:** `.claude/state/[command-name]-state.json` or `[project-folder]/.qa-state.json`

**Schema:**
```json
{
  "command_name": "[command-name]",
  "current_phase": "phase-name",
  "current_step": null,
  "steps_complete": [],
  "steps_failed": [],
  "artifacts_produced": [],
  "last_updated": null,
  "context_notes": ""
}
```

---

## Expandability

This pattern scales:
- **Horizontal:** Add more steps (N can be 3, 7, 18, or any number)
- **Vertical:** Nest commands (skill can call other skills as sub-orchestrators)
- **Cross-cutting:** Share references/contracts across commands
- **Domain-specific:** Extend vocabulary, add domain rules

---

## Example Instantiations

| Command | Design Doc | Steps | HITL |
|---------|-----------|-------|------|
| create-test-artifacts | `.claude/docs/design/create-test-artifacts/` | 8 | 4 |
| create-sit-xlsx | `.claude/docs/design/create-sit-xlsx/` | 5 | 2 |
| verify-sit-xlsx | `.claude/docs/design/verify-sit-xlsx/` | 4 loops | on discrepancies |
| check-data | `.claude/docs/design/check-data/` | 10 | 2 (Step 2, Step 8) |

---

## Using This Template

To design a NEW command:

1. **Create design doc** at `.claude/docs/design/[command-name]/index.md`
2. **Follow tiered-index** -- index.md is pure index, payloads in references/
3. **Complete checklist** -- all 7 required sections (see `completeness-checklist.md`)
4. **Run `/build-command`** -- scaffolds skill package from design doc
5. **Verify** -- build-command Step 8 checks all 3 tiered-index layers
