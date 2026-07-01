# Build Pull Model

## Type
BUILD

## Phase Gate
Task 001 must be complete.

## Deliverable
Updated `.claude/skills/reference-scanner/scanner.py` with topic matching.

## Instructions
1. Read the pull-model design doc: `docs/backlog/153-kernel-build-reference-scanner/pull-model.md`
2. Add to `scanner.py`:
   - `parse_step_topics(step_file_path)` — reads a step file and extracts topic interests from:
     - YAML frontmatter (`topics: [rules, drg-mapping]`)
     - `## Topics` section with bullet list
     - References section (infer topics from listed references)
   - `match_payloads_to_steps(payload_catalog, step_files)` — matches payloads to steps by topic intersection
   - Special topic `all` maps to every step
3. Topic matching: if ANY topic in step's interests matches ANY topic in payload's topics, map that payload to that step

## Verification
- `scanner.py` contains `parse_step_topics` and `match_payloads_to_steps` functions
- `grep -l "topic_tags\|interests" .claude/skills/reference-scanner/scanner.py` returns a match
