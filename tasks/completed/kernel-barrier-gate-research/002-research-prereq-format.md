# Task 002 — Prerequisite Declaration Format

## Type
RESEARCH

## Description
Design the prerequisite declaration: extend gate-contract.md with a Prerequisites section vs. a per-task Prerequisites block — pick one and define bash-parseable parse rules for run-task.sh (grep/sed-level parsing, no new tooling). Read run-task.sh and the task-builder verification-methods reference first (RULE ZERO). Decide whether prerequisites may assert content (reuse existing grep/word_count gate types) or only existence, given file_exists proves presence not correctness.

## Acceptance Criteria
- [ ] File `projects/kernel-barrier-gate-research/01-prereq-format.md` exists
- [ ] Covers: chosen declaration format with parse rules run-task.sh can implement in bash
- [ ] Covers: existence-only vs content-assertion decision with rationale
- [ ] Covers: worked example referencing a real prior pipeline dependency
- [ ] Minimum 300 words

## Gate
DOC-01, DOC-02

## Dependencies
001
