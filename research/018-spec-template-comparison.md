# Spec Template Comparison

## Docker Spec (`docker-spec`)

- **Skill name:** `image-testing-guidance`
- **File count:** 25 files in `.claude/`
  - Skill: 12 (SKILL.md, workflow.md, gate-contract.md, 5 steps, 4 checkpoints)
  - Commands: 8 (image-workflow, image-workflow-dev, image-on-failure, image-pre-construction, image-propose-fix, image-reuse-check, pr, run-test)
  - Lessons: 5 (lessons.md + 4 topic files in docker/, error-handling/, framework/, security/)
- **Step count:** 5 steps
- **Gate contract pattern:** 6 responsibilities, HITL mandatory on test failure
- **YAML frontmatter:** No
- **Strengths:**
  - Clean, minimal structure — easy to understand
  - Domain-agnostic layer naming (Image Object / ImageInterface)
  - Good compliance domain mapping (CIS/STIG/FIPS → layers)
  - Compact SKILL.md (69 lines)
- **Weaknesses:**
  - No YAML frontmatter on SKILL.md
  - Fewer seeded lessons (5 vs 11)
  - No communication guidelines section
  - No multi-page/variant step support

## Playwright Spec (`playwright-spec`)

- **Skill name:** `qa-management-layer`
- **File count:** 32 files in `.claude/`
  - Skill: 13 (SKILL.md, workflow.md, gate-contract.md, 6 steps including step-04-multipage, 4 checkpoints)
  - Commands: 8 (qa-workflow, qa-workflow-dev, qa-on-failure, qa-pre-construction, qa-propose-fix, qa-reuse-check, pr, run-test)
  - Lessons: 11 (lessons.md + 10 topic files across 6 categories)
- **Step count:** 5 steps + 1 variant (step-04-multipage)
- **Gate contract pattern:** Same 6 responsibilities, HITL mandatory, stop-and-discuss protocol
- **YAML frontmatter:** Yes (on SKILL.md)
- **Strengths:**
  - YAML frontmatter (marketplace-ready)
  - Richer lesson library (11 files across locators, assertions, MCP, error-handling, advanced, test-org)
  - Communication guidelines (DO/DON'T show users)
  - Self-heal validation protocol
  - Step variant support (step-04-multipage)
  - More detailed layer rules table (Must Have / Must NOT Have)
  - Longer, more thorough SKILL.md (210 lines)
- **Weaknesses:**
  - Larger file count (32 vs 25)
  - More complex structure may be harder to template
  - Playwright-specific MCP integration section (not domain-agnostic)

## Comparison Matrix

| Aspect | Docker Spec | Playwright Spec |
|--------|-------------|-----------------|
| **Total .claude files** | 25 | 32 |
| **Skill files** | 12 | 13 |
| **Commands** | 8 | 8 |
| **Lesson files** | 5 | 11 |
| **YAML frontmatter** | No | Yes |
| **SKILL.md lines** | 69 | 210 |
| **Communication guidelines** | No | Yes |
| **Self-heal protocol** | No | Yes |
| **Step variants** | No | Yes (step-04-multipage) |
| **Layer rules detail** | Basic table | Detailed Must Have / Must NOT Have |
| **Command naming** | `image-*` | `qa-*` |
| **Shared commands** | `pr.md`, `run-test.md` | `pr.md`, `run-test.md` |
| **Marketplace readiness** | Needs frontmatter | Ready |

## Structural Patterns (Shared)

Both specs share identical structural patterns:

1. **Skill folder:** `SKILL.md` → `workflow.md` → `gate-contract.md` → `steps/` → `checkpoints/`
2. **Command set:** 6 domain commands + `pr.md` + `run-test.md`
3. **Command naming:** `[domain]-workflow`, `[domain]-workflow-dev`, `[domain]-on-failure`, `[domain]-pre-construction`, `[domain]-propose-fix`, `[domain]-reuse-check`
4. **Lesson structure:** `lessons.md` (index) + topic folders with `.md` files
5. **5-step workflow:** User Input → Pre-flight → AI Processing → Construction → Execution + HITL
6. **4 checkpoints:** pre-construction, on-failure, propose-fix, layer-validation
7. **Gate contract:** 6 responsibilities + HITL protocol

## Recommendation

**Use playwright-spec as the template base.**

Rationale:
1. **Marketplace-ready** — already has YAML frontmatter
2. **More complete** — communication guidelines, self-heal protocol, detailed layer rules
3. **Richer lessons** — 11 seeded lessons provide more starting material for new domains
4. **Step variants** — supports domain-specific step variants (step-04-multipage)
5. **Battle-tested** — the original v1 spec, live with customers

### How to adapt for the kernel spec:
- Replace `qa-management-layer` with `kernel-governance`
- Replace `qa-*` command prefix with `kernel-*` (but kernel commands already exist — may not need new ones)
- Replace Playwright-specific content (MCP, selectors) with kernel-specific content (hooks, gates, protocol)
- Replace 5-layer architecture with kernel architecture (Loop → Anchor → Work → Learn → Complete)
- Keep: YAML frontmatter, communication guidelines, self-heal protocol, checkpoint pattern
- Reduce lessons to kernel-relevant topics (hook bypass, anchor compliance, etc.)

### How to adapt for the meta-spec factory:
- Extract the shared structural patterns into templates with placeholders
- Template variables: `{{domain_name}}`, `{{skill_name}}`, `{{command_prefix}}`, `{{layer_architecture}}`, `{{workflow_steps}}`
- The factory stamps out new specs by filling these templates with domain-specific content from research
