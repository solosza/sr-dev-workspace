# Execute Pipeline: Backlog 180

## Task
Run `/kernel/execute-pipeline 180` to completion.

This will:
1. Read backlog 180 (Build Generalized Loop Integration for D&D Game Engine)
2. Read the 4 sub-documents in `docs/backlog/180-domain-build-dnd-game-loop-integration/`
3. Run task-builder to decompose into atomic tasks
4. Execute all tasks against the dnd-game-engine-test repo

## Design References
- Loop architecture: `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/loop-architecture/`
- Command-skill pattern: `.claude/docs/design/command-skill-pattern/index.md`
- Tiered index: `.claude/docs/design/tiered-index-architecture/index.md`

## Deliverable
- Generalized loop template (reusable across repos)
- All 11 game loops with complete contracts, DDD structure, gates, and integration
- No Python code — agent-orchestrated only

## Acceptance Criteria
- [ ] Generalized loop template exists and is repo-agnostic
- [ ] All 11 loops have SKILL.md with DDD structure
- [ ] All loops have input, output, rules, and integration contracts
- [ ] All loops have gate contracts
- [ ] All loops have test fixtures
- [ ] Outer/inner composition works via integration contracts
- [ ] No legacy Python files remain
