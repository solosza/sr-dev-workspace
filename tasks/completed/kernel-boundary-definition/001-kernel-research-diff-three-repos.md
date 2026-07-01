# Diff All Three Repos — Identify Core vs Extension vs Domain Files

## Context
Before defining the kernel boundary, we need a complete picture of what each repo contains and where they diverge. This produces the authoritative diff report that all subsequent tasks reference.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Diff sr_dev_workspace/.claude/ against isagawa-kernel/.claude/ (core kernel files)
- Diff sr_dev_workspace/.claude/ against hmsa-healthcare-qa/.claude/ (independently evolved)
- For each file that differs: classify as CORE (governance), EXTENSION (workspace tool), or DOMAIN (per-repo generated)
- Use the proposed boundary from docs/backlog/147-kernel-refactor-define-kernel-boundary.md
- Output a structured report with three columns: file path, classification, which repo has latest version

## Acceptance Criteria
- [ ] File exists: `projects/kernel-boundary/three-way-diff.md`
- [ ] Report covers all files in .claude/commands/, .claude/hooks/, .claude/skills/, .claude/state/
- [ ] Each file classified as CORE, EXTENSION, or DOMAIN
- [ ] Winner identified per core file (which repo has latest)

## Gates Satisfied
- RESEARCH-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
