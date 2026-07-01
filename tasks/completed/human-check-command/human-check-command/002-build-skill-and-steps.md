# Build Skill and Steps

## Context
Create the SKILL.md orchestrator and step files for the human-check command following command-skill-pattern.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-build-detection-engine

## Phase Gate
- [ ] `.claude/skills/human-check/detect.py` exists

## Requirements
- Create `.claude/skills/human-check/SKILL.md` with:
  - Identity: "You are a writing quality gate that ensures all text reads as human-authored"
  - Philosophy: factual, technical, declarative; no inflated claims; match isagawa.co tone
  - Vocabulary: AI tells, hedge words, formulaic structure, parallel structure
  - Workflow: 3 steps (parse input, run detection, report results)
  - Critical rules: every em dash is a violation; no tolerance for hedge words in professional prose
  - File index listing all skill files
- Create step files in `.claude/skills/human-check/steps/`:
  - `step-01-parse-input.md` — accept file path or inline text
  - `step-02-run-detection.md` — invoke detect.py, collect results
  - `step-03-report-results.md` — format report, set exit code

## Acceptance Criteria
- [ ] SKILL.md exists with all required sections
- [ ] 3 step files exist in steps/
- [ ] Each step has Purpose, Input, Output, Procedure sections

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
