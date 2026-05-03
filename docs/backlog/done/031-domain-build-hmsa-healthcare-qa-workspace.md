# Build HMSA Healthcare QA Workspace

## Status
Open

## Priority
High — active project needs its own workspace with kernel + features installed

## Summary
Create a new workspace for the healthcare-qa spec at `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa`. Copy the kernel and healthcare-qa spec into it, run domain-setup, validate the setup, then install all uncommitted kernel feature branch code (lessons/recurrence, lessons/decay, lessons/extraction, delegation, scanner packages + their tests). The workspace should be ready for immediate development with all kernel features working.

## Requirements
- Create workspace directory at `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa`
- Copy kernel from `D:\my_ai_projects\isagawa-kernel` (`.claude/` directory structure)
- Copy healthcare-qa spec from `D:\my_ai_projects\project_test_repos\specs\health-insurance\healthcare-qa-spec`
- Initialize git repo
- Run `/kernel/domain-setup` using the healthcare-qa spec
- Validate domain-setup output (state files, hooks, protocol, settings.local.json)
- Install uncommitted kernel feature code from 6 branches into workspace:
  - `lessons/` package (schema, recurrence, alerts, tiers, decay, promotion, archival, maturity, draft_generator, approval, promotion_tracker, integrations, __init__)
  - `delegation/` package (schema, engine, collector, factory, __init__)
  - `scanner/` package (config, state, fetcher, analyzer, backlog_gen, notifier, __init__)
  - All corresponding test packages (`tests/test_recurrence/`, `tests/test_decay/`, `tests/test_extraction/`, `tests/test_delegation/`, `tests/test_scanner/`)
- Updated `/kernel/learn` command with recurrence check (Step 5)
- Updated `/kernel/scan-bookmarks` command
- Run all tests to validate features work in new workspace
- Commit everything

## References
- Kernel repo: `D:\my_ai_projects\isagawa-kernel`
- Healthcare-qa spec: `D:\my_ai_projects\project_test_repos\specs\health-insurance\healthcare-qa-spec`
- Feature source: `D:\my_ai_projects\project_test_repos\sr_dev_workspace` (merged feature code lives here)
- Kernel feature branches: 008-recurrence-detection, 006-tiered-memory-decay, 007-skill-extraction, 023-cross-repo-delegation, 001-zep-cloud-research, 019-x-bookmark-scanner

## Task Builder Input
- **Deliverable:** Fully bootstrapped workspace at `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa` with kernel domain-setup complete, all 6 kernel features installed, all tests passing, committed
- **Scope:** BUILD
- **Constraints:** Kernel files copied from isagawa-kernel main branch. Feature code copied from sr_dev_workspace (already merged there). Domain-setup requires restart mid-flow (hooks need reload). Settings.local.json must use string matcher format with nested hooks arrays (not object matchers — causes Settings Error).
