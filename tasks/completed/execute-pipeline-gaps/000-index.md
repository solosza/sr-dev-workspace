# Execute Pipeline Gaps — Task Index

## Source
docs/backlog/051-kernel-fix-execute-pipeline-gaps.md

## Tasks

### Phase 1: Skill File Updates (Gaps 1, 3, 4, 5, 6, 7)

| # | Task | Type | Gap |
|---|------|------|-----|
| 001 | [[001-build-edit-step03-plan-review]] | BUILD | Gap 1: re-enable plan review |
| 002 | [[002-build-edit-run-task-timeout-feedback]] | BUILD | Gap 3: per-task timeout logging |
| 003 | [[003-build-edit-step09-mode-docs]] | BUILD | Gap 4: document execution mode divergence |
| 004 | [[004-build-edit-complete-gate-verify]] | BUILD | Gap 5: gate contract verification |
| 005 | [[005-build-edit-run-task-move-to-done]] | BUILD | Gap 6: move-to-done in run-task.sh |
| 006 | [[006-build-edit-step04-backlog-path]] | BUILD | Gap 6: pass BACKLOG_PATH to run-task.sh |
| 007 | [[007-build-rewrite-step04-dispatch]] | BUILD | Gap 7: classify-then-route dispatch |

### Phase 2: Granularity Reference

| # | Task | Type |
|---|------|------|
| 008 | [[008-build-write-granularity-reference]] | BUILD |
| 009 | [[009-build-edit-step05-decompose-wikilink]] | BUILD |
| 010 | [[010-build-edit-step06-atomize-wikilink]] | BUILD |

### Phase 3: Testing

| # | Task | Type |
|---|------|------|
| 011 | [[011-test-l1-verify-all-files]] | TEST |
| 012 | [[012-test-l2-bash-syntax]] | TEST |
| 013 | [[013-test-l3-dispatch-coherence]] | TEST |

## Notes
- Gap 2 (attestation) already shipped in step-05-validate-report.md — skipped
- 13 tasks total (10 BUILD, 3 TEST)
