# Continuous Spec Factory Loop

## Context
After the meta-spec is built and validated, enter a continuous loop: user provides an industry, agent autonomously identifies the best domains within that industry, scores them, builds specs for each qualifying domain, tests them, packages them, and pushes to GitHub. This is the production factory described in `docs/isagawa-spec-led-growth.md`.

This task is REPEATABLE — it runs once per industry the user provides.

## Dependencies
- **032** — meta-spec files built
- **037** — factory tested on known vertical (proves factory works)

## Phase Gate
- [ ] Meta-spec pushed to `isagawa-co/meta-spec`
- [ ] Factory tested on at least one vertical (task 037)

## Requirements

### Wait for industry input
Ask the user: "What industry should I build specs for?"
The user provides an industry name (e.g., "Healthcare", "FinTech", "DevOps", "E-commerce").

### Phase 1: Domain discovery
Using the meta-spec's research workflow:
1. Web search for the industry's key operational domains
2. Identify 5-10 sub-domains where AI agents could add value
3. Look for: regulatory frameworks, repetitive workflows, compliance requirements, documentation-heavy processes

### Phase 2: Score each sub-domain
Apply the scoring model from task 030:
- Revenue potential (1-5)
- Buyer accessibility (1-5)
- Pain intensity (1-5)
- Documentation availability (1-5)
- Regulatory/compliance requirements (1-5)
- Repetitive workflow patterns (1-5)

Rank by weighted score. Threshold: domains scoring above minimum proceed to build.

### Phase 3: Build specs for qualifying domains
For each domain above threshold:

1. **Create spec repo:**
   - Location: `D:\my_ai_projects\project_test_repos\specs\[domain]-spec`
   - GitHub: `isagawa-co/[domain]-spec` (private)

2. **Build spec from template:**
   - Use meta-spec templates
   - Populate with domain-specific content from research
   - Build: skill files, commands, lessons, reference code (if applicable), docs

3. **Test spec:**
   - Create clean test repo at `D:\my_ai_projects\project_test_repos\test-[domain]-spec`
   - Install kernel spec → domain-setup → verify
   - Install new domain spec → domain-setup → verify
   - NOTE: Testing requires Claude Code restart — document test plan for user

4. **Package for marketplace:**
   - Same process as tasks 027-029
   - YAML frontmatter, Kernel Loop Integration, no absolute paths, README

5. **Push to GitHub:**
   - Commit: `feat: [domain] spec — initial build from spec factory`
   - Push to `isagawa-co/[domain]-spec`

### Phase 4: Log results
Create `research/factory-run-[industry].md` with:
- Industry analyzed
- Sub-domains identified with scores
- Specs built (which domains passed threshold)
- Specs skipped (which domains failed threshold and why)
- Quality notes
- Test results (or test plan for user)

### Phase 5: Advance
After completing all specs for this industry:
- Report to user what was built
- Ask: "Next industry?" or "Review what I built first?"
- If user provides next industry, loop back to Phase 1

### Failure protocol
- Per-spec failures: try 3 times, document, skip that domain, continue with next
- Factory-level failures: document in research file, ask user for guidance

## Output
- Multiple domain specs per industry
- Research log for each factory run
- All specs pushed to GitHub

## Validation
Per spec produced:
- [ ] Spec repo created (local + GitHub)
- [ ] Skill files have YAML frontmatter
- [ ] Commands have Kernel Loop Integration
- [ ] No absolute paths
- [ ] README with install flow
- [ ] Committed and pushed
- [ ] Research log created

## Completion Signal
This task repeats per industry. After each industry run, invoke `/kernel/complete` and report results.
