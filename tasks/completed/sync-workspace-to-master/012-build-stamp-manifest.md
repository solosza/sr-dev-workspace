# Task 012: Build — Generate and Stamp kernel-manifest.json

## Objective
Generate kernel-manifest.json with actual SHA256 hashes of all kernel artifacts in the master repo.

## Instructions

1. After all prior sync tasks complete, generate hashes for every kernel artifact in master
2. Use Python to compute SHA256 of each file listed in the manifest schema (from 058 research at `projects/kernel-architecture/kernel-manifest-schema.json`)
3. Write `D:/my_ai_projects/isagawa-kernel/kernel-manifest.json` with:
   - `kernel_version`: "1.0.0" (first versioned release)
   - `kernel_version_timestamp`: current ISO timestamp
   - Per-artifact entries with computed hashes
   - `domain` section empty (master has no domain)
4. Validate the JSON is parseable

## Acceptance Criteria
- kernel-manifest.json exists in master root
- Contains kernel_version "1.0.0"
- All hash fields populated (not null)
- Valid JSON

## Gate
BUILD-12
