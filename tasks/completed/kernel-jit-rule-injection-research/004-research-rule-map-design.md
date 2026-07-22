# Task 004 — Rule-Map Design + Coverage Limits

## Type
RESEARCH

## Description
Design the rule-routing layer: file-path/layer glob pattern to rule snippet lookup (JSON map derived from lessons.md quality gates and the 5-layer contract), payload discipline (max snippet size, consecutive-write dedup), and counter interaction. Then quantify what JIT CANNOT cover — task-direction drift, cross-file architecture — i.e. what the anchor must still do.

## Acceptance Criteria
- [ ] File `projects/kernel-jit-rule-injection-research/03-rule-map-design.md` exists
- [ ] Covers: rule-map JSON schema with worked examples
- [ ] Covers: payload discipline rules (size, dedup)
- [ ] Covers: explicit list of anchor duties JIT cannot replace
- [ ] Minimum 300 words

## Gate
DOC-05, DOC-06

## Dependencies
001
