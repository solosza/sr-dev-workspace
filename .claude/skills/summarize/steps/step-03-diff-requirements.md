# Step 3: Diff Requirements

## Purpose

Check each backlog requirement against deliverables and assign a status.

## Procedure

1. **For each requirement from the backlog:**
   - Search deliverable inventory for evidence the requirement is met
   - Evidence types:
     - File exists at a path mentioned in the requirement
     - File content matches the requirement's description
     - Test or verification passes
   - Assign status:
     - **Met** — deliverable clearly satisfies the requirement. Include file path as evidence.
     - **Partial** — some aspects addressed, others missing. Include notes on what's missing.
     - **Not addressed** — no deliverable maps to this requirement.

2. **Build requirement diff table:**
   ```
   | # | Requirement | Status | Evidence |
   |---|------------|--------|----------|
   ```

3. **Compute summary stats:**
   - N/M met, K partial, J not addressed

## Skip Condition

If mode is `path` (no backlog), skip this step entirely. Path-mode summaries don't have requirements to diff.

## Acceptance Criteria

- [ ] Every backlog requirement has a status
- [ ] Met requirements have file path evidence
- [ ] Partial requirements have notes on what's missing
