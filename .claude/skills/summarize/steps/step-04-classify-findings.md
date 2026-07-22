# Step 4: Classify Findings

## Purpose

Separate items into three categories: decisions needing human input, problems needing attention, and informational items.

## Procedure

1. **Scan deliverables and agent state for findings:**
   - Recommendations with multiple options → **Decision needed**
   - Open questions or trade-offs documented in output → **Decision needed**
   - Failures (tasks that failed, tests that broke) → **Problem**
   - Skipped tasks with reasons → **Problem**
   - Blockers encountered → **Problem**
   - Completions (tasks done, files created) → **Informational**
   - Research findings and facts → **Informational**
   - Metrics and statistics → **Informational**

2. **Each finding gets exactly one category.** No duplicates across categories.

3. **Output:** Three lists:
   - `decisions`: items requiring human choice
   - `problems`: failures, skips, blockers
   - `informational`: facts, completions, findings

## Acceptance Criteria

- [ ] Every finding assigned to exactly one category
- [ ] Decisions are genuine choice points (not just FYIs)
- [ ] Problems include impact and suggested fix where possible
