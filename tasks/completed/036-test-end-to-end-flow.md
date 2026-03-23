# Test End-to-End Flow

## Context
Full end-to-end test: clean repo → install kernel spec → domain-setup → restart → install domain spec → domain-setup → restart → give tasks → cycling works. This is the "clone and go" experience from a user's perspective.

**HUMAN REQUIRED:** Multiple Claude Code restarts needed.

## Dependencies
- **035** — layered domain-setup tested

## Phase Gate
- [ ] Task 035 complete (layered install works)

## Requirements

### Create a NEW clean test repo
- Location: `D:\my_ai_projects\project_test_repos\test-e2e-flow`
- `git init`
- Create minimal `CLAUDE.md`: "Test repo for end-to-end flow."
- Do NOT reuse test-kernel-bootstrap — fresh start

### Phase 1: Install kernel
1. Copy kernel spec into `.claude/skills/` and `.claude/commands/`
2. Run `/kernel/domain-setup`
3. **RESTART**
4. Verify kernel works (hooks block, anchor works)

### Phase 2: Install domain spec
1. Copy selenium-spec (or docker-spec) skills, commands, framework into repo
2. Run `/kernel/domain-setup` again
3. **RESTART**
4. Verify both kernel and domain work

### Phase 3: Give tasks and cycle
1. Create 3 simple test tasks in `tasks/`:
   - `001-verify-framework-structure.md` — check that framework dirs exist
   - `002-create-sample-test.md` — create a basic test file
   - `003-run-sample-test.md` — execute the test
2. Set `cycling: true` in workflow state
3. Tell agent to cycle
4. Verify it picks tasks, implements, verifies, completes, advances

### Failure protocol
- Try up to 3 times per phase
- On failure: document which phase failed, what broke
- After 3 failures on any phase: create `research/036-e2e-failures.md`, move on

## Output
- Successful end-to-end flow in clean test repo
- OR failure documentation at `research/036-e2e-failures.md`

## Validation
- [ ] Clean repo created
- [ ] Kernel installed and verified
- [ ] Domain spec layered and verified
- [ ] Tasks created and cycling works
- [ ] Full flow: install → setup → restart → setup → restart → cycle

## Completion Signal
When ALL validation checks pass (or 3 failures documented), invoke `/kernel/complete`.
