# 004 — Edit complete.md: Add Gate Contract Verification (Gap 5)

## Type
BUILD

## Requirements
- Edit `.claude/commands/kernel/complete.md`
- Add a new step between "Verify deliverables" (step 2) and "Determine completion mode" (step 3)
- New step: "Verify gate contract (if exists)"
  - Read `gate-contract.md` from the task folder (if `task_folder` is set in workflow state)
  - Find gates matching the current task (by task number prefix)
  - For each matching gate, run the verification method:
    - `file_exists` → check file exists
    - `grep` → run grep command
    - `run_code` → execute, check exit 0
  - If any gate fails: report which gate failed, do NOT mark complete, set `needs_learn: true`
  - If all gates pass or no gates match: proceed normally
- Renumber subsequent steps (old step 3 becomes step 4, etc.)

## Acceptance Criteria
- [ ] `complete.md` contains text about gate contract verification
- [ ] File mentions reading `gate-contract.md`
- [ ] File mentions `file_exists` and `grep` as verification methods
- [ ] File mentions setting `needs_learn: true` on gate failure
