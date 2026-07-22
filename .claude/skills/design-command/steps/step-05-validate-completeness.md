# Step 5: Validate Completeness

## Purpose

Check the draft design doc against build-command's input-contract AND tiered-index architecture before writing to disk. This ensures the output is consumable by `/build-command` Step 1, which validates both content sections and tiered-index compliance.

## Input

- Draft content from Step 4
- Input contract: `.claude/docs/design/build-command/references/input-contract.md`
- Tiered-index architecture: `.claude/docs/design/tiered-index-architecture/index.md`

## Output

- Completeness report (pass/fail per section + tiered-index compliance)

## Acceptance Criteria

- [ ] All 7 required sections checked against minimum depth
- [ ] All 5 optional sections noted (present or absent)
- [ ] Tiered-index Layer 1 compliance checked
- [ ] Tiered-index Layer 2 compliance checked
- [ ] Tiered-index Layer 3 compliance checked
- [ ] Report generated in standard format
- [ ] If PASS: proceed to Step 6
- [ ] If FAIL: loop back to Step 3/4 to fix

## References

- Design doc: `.claude/docs/design/design-command/references/output-contract.md`
- Build command input contract: `.claude/docs/design/build-command/references/input-contract.md`
- Tiered-index architecture: `.claude/docs/design/tiered-index-architecture/index.md`

## Procedure

1. Read `.claude/docs/design/build-command/references/input-contract.md`
2. For each of the 7 required sections, verify:
   - Present in draft (index or payload)
   - Meets minimum depth:
     - Identity: 1+ sentence
     - Philosophy: 3+ principles
     - Vocabulary: 3+ terms
     - Critical rules: 2+ rules
     - Workflow: 2+ steps with all 4 columns
     - Step specs: purpose + procedure each
     - File structure: shows skills/ tree
3. For each of the 5 optional sections, note presence/absence
4. **Tiered-index Layer 1 checks:**
   - index.md is pure index (no identity/philosophy/vocabulary/rules inline)
   - All payloads in references/ (not alongside index.md)
   - Every file under 200 lines
   - No file is both index and payload
5. **Tiered-index Layer 2 checks:**
   - Workflow steps that produce output have pre-generation checkpoint blocks
   - Checkpoints list specific file paths (not generic "read references")
6. **Tiered-index Layer 3 checks:**
   - Contract definitions exist (in a payload file) with full JSON
   - Each contract has soft_validation_rules array
   - Each contract has mechanical_validations array (may be empty with justification)
7. Generate combined report

## Verification

Report format:
```
COMPLETENESS CHECK: /[command-name]

Required (N/7):
  [PASS/FAIL] Section -- location (depth)

Optional (N/5):
  [PASS/WARN] Section -- location or "not specified"

Tiered-Index Compliance:
  Layer 1 (Organization):  PASS / FAIL -- [details]
  Layer 2 (Checkpoints):   PASS / FAIL -- [details]
  Layer 3 (Contracts):     PASS / FAIL -- [details]

RESULT: PASS | FAIL
```

## Failure Recovery

| Result | Action |
|--------|--------|
| PASS (7/7 + tiered-index) | Proceed to Step 6 |
| FAIL (missing sections) | Identify gaps, loop to Step 3 to fill them |
| FAIL (insufficient depth) | Expand the thin section, re-validate |
| FAIL (Layer 1 violation) | Restructure: split index from payloads, loop to Step 4 |
| FAIL (Layer 2 violation) | Add checkpoints to workflow steps, loop to Step 4 |
| FAIL (Layer 3 violation) | Add contract definitions, loop to Step 4 |
