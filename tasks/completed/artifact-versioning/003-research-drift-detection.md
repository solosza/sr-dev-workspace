# Task 003: Research — Design Drift Detection Mechanism

## Objective
Design how repos detect that their kernel artifacts are outdated compared to the master.

## Instructions

1. Read the versioning scheme recommendation from task 002 in the report
2. Design drift detection approaches:
   - **Manifest comparison** — repo's `kernel-manifest.json` vs master's. Diff shows which files changed.
   - **Content hash comparison** — hash each local file, compare to master hashes in manifest
   - **Version field in frontmatter** — each `.md` file has `version: X` in YAML frontmatter
   - **`kernel-version` field in state** — `session_state.json` or CLAUDE.md stores the expected version
3. For each approach, assess:
   - Where does the check run? (session-start? anchor? manual command?)
   - What triggers it? (every session? on demand? on sync?)
   - What's the output? (warning? block? report?)
   - How does it handle domain-specific additions? (domain files shouldn't trigger drift warnings)
4. Write findings as `## 3. Drift Detection` in the report
   - Include the recommended detection mechanism
   - Include example output of a drift report

## Acceptance Criteria
- At least 2 detection approaches compared
- Recommended mechanism described with trigger point and output format
- Domain-specific artifact exclusion addressed

## Gate
RESEARCH-03
