# Pull Model: Step Topic Declarations

## Status
NEW

## Purpose

Define how command steps declare their topic interests so the scanner can match payloads to steps. The "pull" model means steps pull what they need — the index doesn't need to know about commands.

## How Steps Declare Interests

Each step file includes a `topics` field in its frontmatter or a dedicated section:

### Option A: Frontmatter (preferred)

```yaml
---
topics: [rules, drg-mapping, date-assignment, dos-overlap]
---
```

### Option B: Section

```markdown
## Topics
- rules
- drg-mapping
- date-assignment
```

### Option C: References section (current pattern)

Steps already have a References section listing what they need. The scanner can parse these to infer topics. No new syntax needed — just smarter parsing of what's already there.

## Matching Algorithm

1. Scanner produces `payload_catalog` with topics per payload
2. Each step has a list of topic interests
3. Match: if ANY topic in the step's interests matches ANY topic in a payload's topics → map that payload to that step
4. Special topic `all` → mapped to every step (e.g., rules that always apply)

## Topic Taxonomy

Topics should be broad enough to be reusable across projects but specific enough to filter:

| Topic | Matches Payloads About |
|-------|----------------------|
| `rules` | Test data creation rules, constraints, validations |
| `drg-mapping` | DRG-to-MDC lookup tables |
| `drg-exclusion` | DRG exclusion file reference |
| `dates` | Date assignment, DOS overlap, effective dates |
| `qrs-columns` | QRS column format, Col Q/R/S rules |
| `xlsx-format` | Excel formatting, column headers, auto-sizing |
| `tools` | 837BT, QNXT, DynamicClaims, Mass Processing |
| `sp-logic` | Stored procedure filter logic, pairing conditions |
| `claim-lifecycle` | Claim states, transitions, verification |

Projects can extend with domain-specific topics. The taxonomy is not fixed.

## Why Pull Over Push

- **No index modifications needed.** Reference docs stay clean. New payloads are automatically discoverable.
- **Steps own their dependencies.** Each step knows what it needs. Adding a step doesn't require updating every index.
- **Decoupled evolution.** Reference docs and commands evolve independently. New rules in reference docs are picked up automatically on next scan.
- **Simpler maintenance.** Only one place to update when a step's needs change (the step file itself).

## Dependencies

- Scanner loop must produce topic-annotated payload catalog
- /build-command must generate topic declarations in step templates
