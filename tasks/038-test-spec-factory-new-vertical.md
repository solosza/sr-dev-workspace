# Test Spec Factory on New Vertical

## Context
Test the spec factory on a vertical we have NOT built before. This is the real test — can the factory research an unknown domain, score it, and produce a usable spec? The user will provide the industry when they're ready.

**HUMAN REQUIRED:** Needs Claude Code restart + user provides the industry input.

## Dependencies
- **037** — factory tested on known vertical (proves factory runs, output is reasonable)

## Phase Gate
- [ ] Task 037 complete (factory works on known vertical)

## Requirements

### Use the test repo from 037
Continue in: `D:\my_ai_projects\project_test_repos\test-spec-factory`
(Already has kernel + meta-spec installed)

### Get industry from user
Ask the user: "What industry should I build a spec for?"
Wait for response. Do NOT pick an industry autonomously — the user wants to choose.

### Run spec factory
- Invoke the spec factory command
- Input: industry provided by user
- Let the factory run: research → score sub-domains → build specs for passing domains

### Evaluate output
For each spec produced:
1. Does the file structure match the template?
2. Are the domain-specific details accurate? (not generic placeholders)
3. Would a user find this useful without heavy modification?
4. Could it pass domain-setup and basic cycling?

### Document findings
Create `research/038-factory-new-vertical.md` with:
- Industry chosen
- Sub-domains identified and scores
- Specs produced
- Quality assessment
- Factory improvements needed

### Failure protocol
- Try up to 3 times
- On failure: document what the factory got wrong
- After 3 failures: document in research file, move on

## Output
- Factory-produced spec(s) for user-chosen industry
- Quality assessment at `research/038-factory-new-vertical.md`

## Validation
- [ ] User provided industry input
- [ ] Factory researched and scored sub-domains
- [ ] At least one spec produced
- [ ] Quality assessment documented
- [ ] Comparison to expected output documented

## Completion Signal
When ALL validation checks pass (or 3 failures documented), invoke `/kernel/complete`.
