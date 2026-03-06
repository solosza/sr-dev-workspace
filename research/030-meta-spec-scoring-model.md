# Meta-Spec Scoring Model and Factory Design

## Scoring Dimensions

8 dimensions, each scored 1–5. Weights reflect business impact.

| # | Dimension | Weight | What It Measures | How to Score |
|---|-----------|--------|-----------------|--------------|
| 1 | **Revenue Potential** | 3x | Market size × willingness to pay | 5=Enterprise budgets, clear ROI; 1=Hobbyist, no budget |
| 2 | **Pain Intensity** | 3x | How badly the domain needs AI enforcement | 5=Costly failures, compliance risk; 1=Nice-to-have |
| 3 | **Repetitive Patterns** | 3x | Does the domain have repeatable workflows that map to 5 layers? | 5=Highly structured (CIS checks, test suites); 1=Creative/unstructured |
| 4 | **Buyer Accessibility** | 2x | Can we reach buyers through LinkedIn/GitHub/communities? | 5=Clear title (CTO, QA Lead), findable online; 1=Diffuse, no central role |
| 5 | **Documentation Availability** | 2x | Public docs the agent can source for spec content | 5=Official standards, extensive docs; 1=Tribal knowledge only |
| 6 | **Compliance/Regulatory** | 2x | Standards that create switching costs | 5=Mandatory compliance (HIPAA, SOC2, CIS); 1=No standards |
| 7 | **Community Demand** | 2x | GitHub issues, forum posts, job postings signaling need | 5=Active demand, trending topic; 1=No visible demand |
| 8 | **Existing Tooling** | 1x (inverse) | Open-source tools already solving this | 5=No tools exist (greenfield); 1=Saturated market |

**Total possible:** (3+3+3+2+2+2+2+1) × 5 = 90

### Threshold

| Score | Action |
|-------|--------|
| ≥70 (78%+) | **BUILD** — high-priority, start immediately |
| 50–69 (56–77%) | **QUEUE** — viable, build when bandwidth allows |
| 30–49 (33–55%) | **DEFER** — revisit when market conditions change |
| <30 (<33%) | **SKIP** — not viable for autonomous spec build |

### Priority Queue

Within each tier, sort by:
1. Revenue Potential × Pain Intensity (business impact)
2. Documentation Availability (build feasibility)
3. Compliance (switching costs / stickiness)

---

## Spec Schema

### Input

```json
{
  "industry": "infrastructure-testing",
  "sub_domains": ["docker-images", "cloud-amis", "vm-snapshots"],
  "constraints": ["python-only", "no-cloud-credentials"],
  "template_base": "playwright-spec",
  "target_stack": {
    "language": "python",
    "test_runner": "pytest",
    "transport": "docker"
  }
}
```

### Discovery Phase

The agent researches the domain before building:

| Step | Action | Sources |
|------|--------|---------|
| 1 | Identify authoritative standards | Web search: official docs, RFCs, compliance frameworks |
| 2 | Map domain hierarchy | Standards docs → categories → checks → 5-layer mapping |
| 3 | Find existing tooling | GitHub search: repos, stars, activity |
| 4 | Identify buyer personas | LinkedIn: job titles, company types, headcount |
| 5 | Catalog common failures | GitHub issues, Stack Overflow, forums |
| 6 | Extract vocabulary | Domain-specific terms → naming conventions for layers |

### 5-Layer Mapping

The factory maps domain concepts to the universal 5-layer architecture:

| Universal Layer | Template Variable | Example: QA | Example: Docker | Example: Compliance |
|----------------|-------------------|-------------|-----------------|---------------------|
| Interface | `{{interface_name}}` | BrowserInterface | ImageInterface | AuditInterface |
| Object | `{{object_name}}` | Page Object | Image Object | Control Object |
| Task | `{{task_name}}` | Task | Task | Assessment Task |
| Role | `{{role_name}}` | Role | Role | Auditor Role |
| Test | `{{test_name}}` | Test | Test | Audit Test |

### Output — What the Factory Produces

```
{{domain}}-spec/
├── .claude/
│   ├── commands/
│   │   ├── {{prefix}}-workflow.md
│   │   ├── {{prefix}}-workflow-dev.md
│   │   ├── {{prefix}}-on-failure.md
│   │   ├── {{prefix}}-pre-construction.md
│   │   ├── {{prefix}}-propose-fix.md
│   │   ├── {{prefix}}-reuse-check.md
│   │   ├── pr.md
│   │   └── run-test.md
│   │
│   ├── lessons/
│   │   ├── lessons.md                      ← Index
│   │   ├── framework/architecture.md       ← 5-layer rules for this domain
│   │   ├── {{topic_1}}/{{lesson_1}}.md     ← Domain-specific seeded lessons
│   │   └── error-handling/ci.md            ← CI patterns
│   │
│   └── skills/
│       └── {{skill_name}}/
│           ├── SKILL.md                    ← Identity, philosophy, rules
│           ├── workflow.md                 ← Data flow, state persistence
│           ├── gate-contract.md            ← 6 responsibilities, HITL
│           ├── steps/
│           │   ├── step-01.md              ← User Input
│           │   ├── step-02.md              ← Pre-flight
│           │   ├── step-03.md              ← AI Processing
│           │   ├── step-04.md              ← Discovery + Construction
│           │   └── step-05.md              ← Execution + HITL
│           └── checkpoints/
│               ├── pre-construction.md
│               ├── on-failure.md
│               ├── propose-fix.md
│               └── layer-validation.md
│
├── framework/
│   ├── _reference/
│   │   ├── README.md
│   │   ├── {{objects}}/                    ← Reference Object implementations
│   │   ├── tasks/                          ← Reference Task implementations
│   │   ├── roles/                          ← Reference Role implementations
│   │   └── tests/                          ← Reference Test implementations
│   │
│   ├── interfaces/
│   │   └── {{interface_file}}.py           ← Domain-specific interface wrapper
│   │
│   └── resources/
│       ├── config/environment_config.json
│       └── utilities/autologger.py
│
├── tests/
│   ├── conftest.py
│   └── data/
│
├── requirements.txt
├── README.md
├── FRAMEWORK.md
├── CONTRIBUTING.md
└── LICENSE
```

### Template Variables

| Variable | Source | Example |
|----------|--------|---------|
| `{{domain}}` | Input `industry` | `docker`, `compliance`, `data-pipeline` |
| `{{prefix}}` | Derived from domain | `image`, `audit`, `pipeline` |
| `{{skill_name}}` | `{{domain}}-guidance` | `image-testing-guidance` |
| `{{interface_name}}` | Discovery phase | `ImageInterface`, `AuditInterface` |
| `{{interface_file}}` | Snake case of interface | `image_interface`, `audit_interface` |
| `{{object_name}}` | Discovery phase | `Image Object`, `Control Object` |
| `{{objects}}` | Plural snake case | `image_objects`, `control_objects` |
| `{{task_name}}` | Usually "Task" | `Task`, `Assessment Task` |
| `{{role_name}}` | Usually "Role" | `Role`, `Auditor Role` |
| `{{test_name}}` | Usually "Test" | `Test`, `Audit Test` |
| `{{topic_N}}` | Domain lesson categories | `docker/`, `security/`, `browser/` |
| `{{lesson_N}}` | Lesson file names | `containers.md`, `compliance.md` |

---

## Validation Phase

After building, the factory validates:

| Check | Method | Pass Criteria |
|-------|--------|---------------|
| File completeness | Glob all expected paths | All template files exist |
| YAML frontmatter | Read SKILL.md, steps, checkpoints | All have valid frontmatter |
| Layer rules | Read architecture.md | 5 layers defined with constants/returns/decorator rules |
| Reference code | Read _reference/ files | At least 1 example per layer |
| Interface methods | Read interface file | Core methods implemented |
| Test infrastructure | Read conftest.py + data/ | Fixtures defined, test data present |
| README | Read README.md | Requirements section, install flow, kernel-first |
| Dry-run domain-setup | Drop into clean cognitive-agent, run setup | Completes without error |
| Basic cycling | Run one test against reference code | Test passes |

---

## Factory Loop

```
┌─────────────────────────────────────────────┐
│ 1. RECEIVE                                  │
│    Input: {industry, sub_domains}            │
│    Or: pick next from priority queue         │
├─────────────────────────────────────────────┤
│ 2. RESEARCH                                 │
│    Web search: standards, docs, tools        │
│    GitHub search: repos, issues, demand      │
│    LinkedIn: buyer personas, company types    │
├─────────────────────────────────────────────┤
│ 3. SCORE                                    │
│    Evaluate 8 dimensions (1-5)               │
│    Apply weights → composite score           │
│    Decision: BUILD / QUEUE / DEFER / SKIP    │
├─────────────────────────────────────────────┤
│ 4. BUILD (if score ≥ threshold)             │
│    a. Create spec repo from template         │
│    b. Fill template variables                │
│    c. Write domain-specific content:         │
│       - Interface methods                    │
│       - Reference code (1 per layer)         │
│       - Seeded lessons                       │
│       - Skill steps (discovery, construction)│
│    d. Write docs (README, FRAMEWORK)         │
├─────────────────────────────────────────────┤
│ 5. VALIDATE                                 │
│    a. File completeness check                │
│    b. Drop into cognitive-agent              │
│    c. Run domain-setup                       │
│    d. Run reference tests                    │
│    e. Fix failures → learn loop              │
├─────────────────────────────────────────────┤
│ 6. PUBLISH                                  │
│    a. Push to GitHub (private)               │
│    b. Add to spec catalog                    │
│    c. Log results, scoring, build time       │
│    d. Advance to next in queue               │
└─────────────────────────────────────────────┘
```

### Data Sources per Dimension

| Dimension | Primary Source | Secondary Source |
|-----------|---------------|------------------|
| Revenue Potential | LinkedIn (company sizes, funding) | Job boards (salary ranges = budget proxy) |
| Pain Intensity | GitHub Issues (complaint patterns) | Stack Overflow (question frequency) |
| Repetitive Patterns | Official docs (workflow steps) | Existing tools (feature lists) |
| Buyer Accessibility | LinkedIn Sales Navigator | GitHub contributor profiles |
| Documentation | Official standards bodies | Open-source project docs |
| Compliance/Regulatory | Government/industry standards sites | Compliance tool vendors |
| Community Demand | GitHub stars/forks on related tools | Reddit/HN discussions |
| Existing Tooling | GitHub search (repos, stars, recency) | Package registries (npm, PyPI) |

---

## Example Scoring: Docker Image Testing

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Revenue Potential | 4 | 3x | 12 |
| Pain Intensity | 5 | 3x | 15 |
| Repetitive Patterns | 5 | 3x | 15 |
| Buyer Accessibility | 4 | 2x | 8 |
| Documentation | 5 | 2x | 10 |
| Compliance/Regulatory | 5 | 2x | 10 |
| Community Demand | 4 | 2x | 8 |
| Existing Tooling (inv) | 3 | 1x | 3 |
| **Total** | | | **81/90** |

**Decision: BUILD** (81 ≥ 70)

**Rationale:**
- CIS/STIG/FIPS create mandatory compliance → pain is real
- 200+ checks per framework → highly repetitive, perfect for 5-layer
- Official benchmark docs are public and detailed → agent can self-source
- DevOps/Platform Eng titles are findable on LinkedIn
- Existing tools (OpenSCAP, Lynis) validate but don't enforce → differentiated

---

## Template Base

**Chosen template: playwright-spec** (from task 018 analysis)

Rationale:
- YAML frontmatter (marketplace-ready)
- Richer lesson library (11 seeded files)
- Communication guidelines, self-heal protocol
- Step variant support
- Battle-tested (live with customers)

Template adaptation: extract shared structural patterns into templates with placeholders. The factory stamps out new specs by filling templates with domain-specific content from the research phase.

---

*Designed for autonomous factory execution. No human in the loop after meta-spec is written.*
