# Build Meta-Spec Files

## Context
Build the actual spec factory — skill files, commands, lessons, templates, and scoring engine. This is the core implementation task for the meta-spec.

## Dependencies
- **030** — schema and scoring model designed
- **031** — repo created

## Phase Gate
- [ ] `research/030-meta-spec-scoring-model.md` exists
- [ ] Repo exists at `D:\my_ai_projects\project_test_repos\specs\meta-spec`

## Requirements

### Use existing spec as template
Read the template base chosen in task 018 (likely playwright-spec or docker-spec). Use its structure as the pattern for what the factory produces.

### Build skill files
Work in: `D:\my_ai_projects\project_test_repos\specs\meta-spec`

**`.claude/skills/spec-factory/SKILL.md`**
- Identity: "You are a spec factory agent"
- Philosophy: "Build wide on autopilot. Sell narrow with focus."
- 5-step workflow overview: Score → Research → Build → Test → Package
- File index
- Critical rules

**`.claude/skills/spec-factory/workflow.md`**
- Data flow: `{industry}` → `{sub_domains, scores}` → `{spec_files}` → `{test_results}` → `{packaged_spec}`
- Scoring model integration (reference the scoring model from task 030)
- Template expansion rules
- Testing protocol

**`.claude/skills/spec-factory/gate-contract.md`**
- Factory responsibilities: never ship untested spec, never skip scoring, always use template base
- HITL gates: none during autonomous factory runs (entire point is autonomous)
- Quality gates: spec must pass domain-setup, basic cycling test

**Step files:**
- `step-01.md` — Input: industry name or priority queue pick
- `step-02.md` — Research: web search for domain knowledge, regulatory standards, existing tools
- `step-03.md` — Score: evaluate each sub-domain against scoring model
- `step-04.md` — Build: create spec from template, populate with domain content
- `step-05.md` — Test + Package: test in clean repo, package for marketplace, push

### Build templates
The factory uses these templates to stamp out new specs:

**`templates/skill/SKILL.md.tmpl`** — skeleton with placeholders: `{{domain_name}}`, `{{philosophy}}`, `{{workflow_steps}}`
**`templates/skill/workflow.md.tmpl`** — workflow skeleton
**`templates/skill/gate-contract.md.tmpl`** — gate contract skeleton
**`templates/commands/workflow.md.tmpl`** — main workflow command
**`templates/commands/workflow-dev.md.tmpl`** — dev mode command
**`templates/lessons/architecture.md.tmpl`** — seeded architecture lesson
**`templates/framework/interface.py.tmpl`** — interface class skeleton

### Build scoring engine
**`scoring/score_vertical.md`** — instructions for scoring a vertical (reference dimensions from 030)
**`scoring/priority_queue.md`** — how to maintain and advance the priority queue

### Build commands
**`.claude/commands/spec-factory-run.md`** — main factory command: "Given industry X, research domains, score, build specs"
**`.claude/commands/spec-factory-score.md`** — score-only: evaluate a vertical without building
**`.claude/commands/spec-factory-build.md`** — build-only: skip scoring, build spec for given domain

### Build seeded lessons
**`.claude/lessons/lessons.md`** — index
**`.claude/lessons/factory/patterns.md`** — factory patterns: template expansion, domain research, scoring pitfalls
**`.claude/lessons/factory/testing.md`** — testing patterns: clean repo setup, domain-setup validation, cycling smoke test

### Commit and push
- Commit message: `feat: build spec factory — skill files, templates, scoring, commands`
- Push to `isagawa-co/meta-spec`

## Output
- Complete spec factory in meta-spec repo
- All skill files, commands, lessons, templates, scoring engine

## Validation
- [ ] SKILL.md has identity, philosophy, file index
- [ ] workflow.md has data flow and scoring integration
- [ ] Templates have placeholders (not hardcoded domain content)
- [ ] Scoring engine references dimensions from 030
- [ ] Commands have Kernel Loop Integration
- [ ] Lessons seeded with factory patterns
- [ ] Committed and pushed

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
