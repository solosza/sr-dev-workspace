# Task 001: Write jit-rule-map.json

**Type:** BUILD | **Gates:** JIT-01

## Action

Write `.claude/hooks/jit-rule-map.json` (ONE file).

## Spec

READ `projects/kernel-jit-rule-injection-research/01-rule-inventory.md` (candidate ranking) and `03-rule-map-design.md` (schema, snippet size cap) FIRST. Take the TOP 2 ranked rules — do not pick by memory. Each entry follows the design doc's exact schema: id, match (tool + pattern), snippet. Respect the snippet size cap.

## Acceptance

JSON parses; exactly 2 entries; ids equal the doc's top 2; caps respected.
