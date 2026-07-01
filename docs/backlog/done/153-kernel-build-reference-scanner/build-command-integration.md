# /build-command Integration

## Status
NEW

## Purpose

When `/build-command` scaffolds a new skill from a design doc, it should auto-generate topic declarations in step files so the reference scanner works out of the box.

## What Changes in /build-command

### Step Generation (Step 4 of build pipeline)

Currently, `/build-command` generates step files with:
- Purpose, Input, Output, Acceptance Criteria, References, Procedure, Verification, Failure Recovery

Add: **Topic declaration** in frontmatter or a Topics section.

### How to Derive Topics

The design doc's step definitions already list what each step reads:

```markdown
### Step 1: Confirm History
Pre-generation checkpoint:
- Read DRG-to-MDC mapping
- Read DRG exclusion list
```

`/build-command` parses these checkpoints and maps them to topics:
- "DRG-to-MDC mapping" → `drg-mapping`
- "DRG exclusion" → `drg-exclusion`
- "validation rules" → `rules`
- "SP" or "stored procedure" → `sp-logic`

### Keyword-to-Topic Map (built into /build-command)

| Keyword in checkpoint | Generated topic |
|----------------------|-----------------|
| mapping, lookup | `drg-mapping` |
| exclusion | `drg-exclusion` |
| rules, validation | `rules` |
| SP, stored procedure | `sp-logic` |
| dates, DOS, registry | `dates` |
| QRS, Col Q, Col R, Col S | `qrs-columns` |
| xlsx, excel, format | `xlsx-format` |
| 837, QNXT, DynamicClaims | `tools` |

### Fallback

If no keywords match, generate `topics: [general]` and flag for manual review.

## What Changes in Step Template

Current step template output:
```markdown
# Step N: [Name]

## Purpose
...
```

New step template output:
```markdown
---
topics: [rules, drg-mapping]
---

# Step N: [Name]

## Purpose
...
```

## Dependencies

- Scanner loop must be implemented first (or in parallel)
- Existing skills (check-data, validate-tc) need topic declarations added retroactively
