# Build: Root-Cause Report

## Context
Backlog 235 final deliverable.

## Type
BUILD
## Execution
inline
## Dependencies
- 001, 002

## Requirements
- Write `projects/selenium-click-fault/root-cause-report.md` with sections (gate greps): `## Timeline`, `## Pipeline Diff`, `## Root Cause` (or best-evidence candidate + confidence), `## Fix` (concrete; if it needs user/system action, state it as a finding with evidence — do NOT apply), `## Attestation` (no system state modified), `## Probe` (how to run tools/selenium-click-probe.py)
- Synthesize ONLY from notes-timeline.md + notes-pipeline-diff.md + the backlog's evidence block — cite

## Acceptance Criteria
- [ ] Report complete with all sections, every claim traced to notes

## Gates Satisfied
- SCF-01, SCF-02, SCF-04, SCF-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
