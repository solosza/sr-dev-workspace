# Task 008: Build — Write Manifest Schema

## Objective
Write the proposed `kernel-manifest.json` schema based on the research recommendation.

## Instructions

1. Read the recommendation from the report (task 007)
2. Write `projects/kernel-architecture/kernel-manifest-schema.json` with:
   - A JSON schema or example manifest showing the proposed structure
   - Fields for kernel version (semver)
   - Per-artifact entries with: path, content hash, category (kernel/domain), last-modified
   - Sections for: commands, skills, hooks, protocols, infrastructure, CLAUDE.md
   - A domain section (empty in master, populated in synced repos)
3. Include comments (via `"_comment"` fields) explaining each section
4. The schema should be valid JSON that could be used as-is or as a template

## Acceptance Criteria
- File exists: `projects/kernel-architecture/kernel-manifest-schema.json`
- Schema includes kernel version field
- Schema includes per-artifact entries with path and hash
- Schema distinguishes kernel vs domain artifacts

## Gate
BUILD-08
