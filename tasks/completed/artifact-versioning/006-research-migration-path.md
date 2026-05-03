# Task 006: Research — Design Migration Path (Zero to Versioned)

## Objective
Design the step-by-step migration from current state (zero versioning) to full artifact versioning.

## Instructions

1. Read the existing report sections from tasks 001-005
2. Design a phased migration:
   - **Step 1:** Add version to master kernel (create `kernel-manifest.json` in this workspace)
   - **Step 2:** Stamp each synced repo during backlog 057 execution
   - **Step 3:** Add drift detection to session-start or anchor
   - **Step 4:** Add automated sync command
   - **Step 5:** (Optional) Add changelog generation
3. For each step, specify:
   - What changes (files created/modified)
   - Dependencies (which steps must come first)
   - Effort estimate (small/medium/large)
   - Whether it can be a backlog item or needs to be part of 057
4. Address the bootstrap problem:
   - Repos synced before versioning exists — how do they get their first manifest?
   - The master kernel needs a manifest before any repo can compare against it
5. Write findings as `## 6. Migration Path` in the report
   - Include numbered steps with dependencies
   - Include a timeline/sequencing diagram

## Acceptance Criteria
- Migration has numbered steps with clear dependencies
- Bootstrap problem addressed
- Each step has effort estimate

## Gate
RESEARCH-06
