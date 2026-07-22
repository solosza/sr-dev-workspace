# Step 2: Detect & Model

## Purpose

Determine what kind of content the target contains and build an internal reference model for gap checking.

## Input

- File inventory from Step 1
- Corpus detection rules: -> design doc: [[gap-check/references/corpus-detection.md]]

## Output

- Corpus type (one or more of: skill, design-doc, test-cases, onboard-run, stories, stored-procedures, contract, generic)
- Internal reference model appropriate to the detected type(s)

## Acceptance Criteria

- [ ] All file content read (or headers for large files)
- [ ] Corpus detection rules applied per corpus-detection.md
- [ ] At least 1 corpus type detected
- [ ] Appropriate model built for each detected type

## References

- -> design doc: [[gap-check/references/corpus-detection.md]] — corpus type signals and priority rules
- -> design doc: [[gap-check/references/workflow.md]] — Step 2 procedure (model building per type)

## Procedure

1. Read file content (or headers for large files)
2. Apply corpus detection rules from corpus-detection.md
3. Based on detected type(s), build the appropriate model:

**Skill corpus model:**
- All wikilinks and file path references -> expected targets
- Step counts from indexes/SKILL.md -> expected file counts
- Vocabulary terms from SKILL.md -> term registry
- Schema definitions (JSON structures described in markdown) -> schema registry

**Test case corpus model:**
- AC identifiers from stories/user stories -> AC registry
- TC identifiers from test-cases.md -> TC registry
- TC-AC mappings from traceability matrix -> coverage map
- Query identifiers from tc-queries.sql -> query registry
- TC-query mappings -> query coverage map

**Design doc corpus model:**
- Required sections from completeness checklist -> section registry
- Wikilinks to payload files -> expected payloads
- Design Documents table entries -> expected references

**Mixed corpus:** Build multiple models. Apply all relevant check sets.

## Verification

- Corpus type is one of the defined types (not "unknown")
- Model contains at least 1 entry
- Detection reasoning is logged (which signals matched)

## Failure Recovery

| Condition | Action |
|-----------|--------|
| No corpus type detected | Fall back to **generic** (reference checking only) |
| Mixed signals conflict | Apply priority rules from corpus-detection.md |
