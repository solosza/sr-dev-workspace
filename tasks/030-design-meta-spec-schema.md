# Design Meta-Spec Schema and Scoring Model

## Context
The meta-spec is a domain spec that teaches an agent how to BUILD OTHER domain specs. It needs a scoring model that evaluates verticals and a schema that defines what the factory produces. This is the design task — implementation follows in 031-032.

Reference: `docs/isagawa-spec-led-growth.md` — "The Factory" section.

## Dependencies
- **018** — spec template comparison (provides the template base the factory will use)

## Phase Gate
- [ ] `research/018-spec-template-comparison.md` exists with chosen template

## Requirements

### Research scoring dimensions
Read the spec-led growth doc and extract the scoring criteria mentioned:
- Revenue potential
- Buyer accessibility
- Pain intensity
- Documentation availability

Expand with additional dimensions the agent should evaluate:
- Regulatory/compliance requirements (creates switching costs)
- Existing open-source tooling (competitive landscape)
- Repetitive workflow patterns (spec suitability — does the domain have repeatable patterns?)
- Community demand signals (GitHub issues, forum posts, job postings)

### Design the scoring model
Create `research/030-meta-spec-scoring-model.md` with:

1. **Scoring dimensions** — each dimension, weight, how to evaluate (1-5 scale)
2. **Threshold** — minimum score to proceed with spec build
3. **Priority queue** — how scored verticals get ordered
4. **Data sources** — where the agent sources info for each dimension (web search, GitHub, job boards, etc.)

### Design the spec schema
Define what a meta-spec-produced spec looks like:

1. **Input** — what the meta-spec receives: `{industry, sub_domains[]?, constraints[]?}`
2. **Discovery phase** — how the agent researches the domain (web search for authoritative docs, existing frameworks, regulatory standards)
3. **Spec structure** — what files the factory outputs (skill files, commands, lessons, reference code, tests, docs)
4. **Validation phase** — how the factory verifies the spec works (drop into clean repo, domain-setup, basic cycling test)
5. **Template base** — which existing spec serves as the template (from task 018 output)

### Design the factory loop
Define the autonomous build cycle:
```
1. Receive industry input (or pick from priority queue)
2. Research sub-domains within that industry
3. Score each sub-domain
4. For each passing sub-domain (above threshold):
   a. Create spec repo
   b. Build spec files from template
   c. Populate with domain-specific content
   d. Test in clean repo
   e. Package for marketplace
   f. Push to GitHub
5. Log results, advance to next industry
```

## Output
- `research/030-meta-spec-scoring-model.md` — scoring model + factory loop design

## Validation
- [ ] Scoring dimensions defined with weights
- [ ] Minimum threshold defined
- [ ] Spec schema (input → output) documented
- [ ] Factory loop steps documented
- [ ] Data sources for research identified

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
