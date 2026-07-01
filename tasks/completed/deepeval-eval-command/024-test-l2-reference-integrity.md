# L2 Test: Reference Integrity and Cross-File Consistency

## Context
Level 2 verification — confirm that all internal references between files are consistent. SKILL.md references all step files, step files reference their dependencies, INDEX.md lists all references, command entry point points to SKILL.md, contract JSONs parse, and no file exceeds 200 lines.

## Type
TEST

## Execution
agent

## Dependencies
- 023-test-l1-file-existence

## Phase Gate
- [ ] L1 test passed (all files exist)

## Requirements
- **SKILL.md references**: grep SKILL.md for all 6 step filenames (step-01 through step-06), workflow.md, gate-contract.md, INDEX.md
- **Step file references**: each step file references its corresponding reference files (step-02 references kernel-file-list.md and deepeval-file-list.md, step-03 references dependency-resolution.md, etc.)
- **INDEX.md references**: grep INDEX.md for all 7 reference file names
- **Command entry point**: grep eval.md for "SKILL.md"
- **Contract JSON validity**: run `python -c "import json; json.load(open(f))"` for each of the 4 contract JSONs
- **200-line threshold**: run `wc -l` on every file, verify none exceed 200 lines
- Report any broken references or oversized files

## Acceptance Criteria
- [ ] SKILL.md references all 6 step files
- [ ] SKILL.md references workflow.md and gate-contract.md
- [ ] INDEX.md references all 7 reference files
- [ ] eval.md references SKILL.md
- [ ] All 4 contract JSONs parse as valid JSON
- [ ] No file exceeds 200 lines

## Gates Satisfied
INT-01 through INT-07, FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
