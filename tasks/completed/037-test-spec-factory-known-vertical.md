# Test Spec Factory on Known Vertical

## Context
Test the meta-spec / spec factory by giving it a vertical we already know well (QA testing). The factory should research the domain, score it, and produce a spec that resembles our existing QA specs. This validates the factory produces reasonable output.

**HUMAN REQUIRED:** Needs Claude Code restart after domain-setup in test repo.

## Dependencies
- **032** — meta-spec files built
- **036** — end-to-end flow works (proves the install pipeline works)

## Phase Gate
- [ ] Meta-spec pushed to `isagawa-co/meta-spec`
- [ ] End-to-end flow validated (task 036)

## Requirements

### Create clean test repo for factory
- Location: `D:\my_ai_projects\project_test_repos\test-spec-factory`
- `git init`
- Install kernel spec → domain-setup → restart
- Install meta-spec → domain-setup → restart

### Run spec factory on "QA Testing"
- Invoke the spec factory command (e.g., `/spec-factory-run`)
- Input: industry = "QA Testing"
- Expected: factory should identify sub-domains like:
  - Web application testing (Selenium/Playwright)
  - API testing
  - Mobile testing
  - Performance testing
  - Accessibility testing

### Evaluate output
Compare factory-produced spec against our hand-built selenium-spec:
1. Does it have the right file structure? (skills, commands, lessons, framework)
2. Does the workflow make sense for the domain?
3. Are the seeded lessons relevant?
4. Would domain-setup produce something usable?

### Document findings
Create `research/037-factory-known-vertical.md` with:
- What the factory produced
- Comparison to hand-built spec
- Quality assessment (1-5 scale on each dimension)
- What needs improvement in the factory

### Failure protocol
- Try up to 3 times
- On failure: document what the factory got wrong
- After 3 failures: document in research file, move on

## Output
- Factory-produced spec for QA Testing vertical
- Quality assessment at `research/037-factory-known-vertical.md`

## Validation
- [ ] Factory ran on QA Testing vertical
- [ ] Output spec has correct file structure
- [ ] Quality assessment documented
- [ ] Comparison to hand-built spec documented
- [ ] Improvement areas identified

## Completion Signal
When ALL validation checks pass (or 3 failures documented), invoke `/kernel/complete`.
