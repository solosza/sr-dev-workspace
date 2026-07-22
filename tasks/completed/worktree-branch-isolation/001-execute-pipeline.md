# Execute Pipeline: Backlog 183

## Task
Run `/kernel/execute-pipeline 183` to completion.

This will:
1. Read backlog 183 (Build Worktree Branch Isolation)
2. Read prior incomplete research at `projects/worktree-research/` and `tasks/completed/worktree-research/`
3. Run task-builder to decompose into atomic tasks
4. Execute all tasks

## References
- Prior research (incomplete): `projects/worktree-research/README.md`
- Prior task folder: `tasks/completed/worktree-research/`
- Original backlog: `docs/backlog/done/123-kernel-research-worktree-pipeline-isolation.md`
- State isolation research: `docs/backlog/done/146-kernel-research-state-isolation-and-ci-solutions.md`

## Deliverable
- EnterWorktree behavior research
- State isolation confirmation
- Worktree lifecycle integration into execute-pipeline
- Merge gate design
- Output in `projects/worktree-research/` (extend existing)

## Acceptance Criteria
- [ ] EnterWorktree behavior documented
- [ ] State isolation confirmed or workaround designed
- [ ] Execute-pipeline updated with worktree mode
- [ ] run-task.sh updated for worktree support
- [ ] Merge gate integrated into review-queue accept flow
