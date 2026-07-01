# Build Detection Engine

## Context
Create the Python detection script that scans text for AI writing patterns. This is the core of `/kernel/human-check`.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Create `.claude/skills/human-check/detect.py`
- Detection categories (all regex-based where possible):
  - Em dashes (unicode \u2014) — flag every occurrence
  - AI hedge words: "arguably", "notably", "it's worth noting", "it's important to", "in conclusion", "overall", "essentially", "fundamentally", "leveraging", "utilizing", "facilitate", "comprehensive", "robust", "cutting-edge", "innovative", "game-changing", "transformative", "seamless", "streamlined", "holistic"
  - Formulaic starters: "In today's...", "When it comes to...", "It goes without saying...", "At the end of the day..."
  - Passive voice detection (flag if >20% of sentences)
  - Triple adjective stacking ("comprehensive, robust, and scalable")
  - Colon-list patterns ("There are three key benefits: first... second... third...")
  - Exclamation marks in professional prose
  - AI verbs: "delve", "dive into", "deep dive", "unpack", "unlock"
  - Emoji in professional documents
  - Overly parallel structure
- Output: JSON report with line numbers, flagged text, category, suggested fix
- Exit code: 0 if clean, 1 if AI tells found
- Script must work standalone: `python detect.py [file-path]`

## Acceptance Criteria
- [ ] File exists: `.claude/skills/human-check/detect.py`
- [ ] Detects em dashes correctly
- [ ] Detects at least 10 AI hedge words
- [ ] Returns non-zero exit code when tells found
- [ ] JSON output includes line_number, text, category, suggestion

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
