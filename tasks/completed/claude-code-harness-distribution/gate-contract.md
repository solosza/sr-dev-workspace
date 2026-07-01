# Gate Contract — Claude Code Harness Distribution Strategy

**Project:** claude-code-harness-distribution
**Backlog:** 131
**Total Gates:** 24

## Gate Contract (5-Column Format)

| ID | Check | Method | Pass Criteria | Fail Action |
|----|----|--------|---|--|
| STRUCT-01 | Project directory exists | file_exists | `test -d projects/claude-code-harness-distribution` | Create directory |
| STRUCT-02 | Test fixtures subdirectory | file_exists | `test -d projects/claude-code-harness-distribution/_test/fixtures` | Create directory |
| STRUCT-03 | Test expected subdirectory | file_exists | `test -d projects/claude-code-harness-distribution/_test/expected` | Create directory |
| BUILD-01 | Platforms inventory report | file_exists | `test -f projects/claude-code-harness-distribution/01-platforms-inventory-and-comparison.md` | Create file |
| BUILD-02 | Platforms comparison matrix | grep | `grep -q "\| Platform \|" projects/claude-code-harness-distribution/01-platforms*.md && [[ $(grep -c "^\|" projects/claude-code-harness-distribution/01-platforms*.md) -ge 10 ]]` | Add 9-platform matrix |
| BUILD-03 | Marketplace gaps report | file_exists | `test -f projects/claude-code-harness-distribution/02-marketplace-gaps-and-opportunities.md` | Create file |
| BUILD-04 | Gaps opportunity ranking | grep | `grep -q "Opportunity Ranking" projects/claude-code-harness-distribution/02-marketplace*.md` | Add ranking table |
| BUILD-05 | Distribution roadmap | file_exists | `test -f projects/claude-code-harness-distribution/03-distribution-roadmap.md` | Create file |
| BUILD-06 | Phase 1 Track A documented | grep | `grep -q "Track A.*Distribution Platform" projects/claude-code-harness-distribution/03-distribution*.md` | Add Track A section |
| BUILD-07 | Phase 1 Track B documented | grep | `grep -q "Track B.*Community" projects/claude-code-harness-distribution/03-distribution*.md` | Add Track B section |
| BUILD-08 | Phase 2 options (3) | grep | `[[ $(grep -c "Phase 2 Option [ABC]:" projects/claude-code-harness-distribution/03-distribution*.md) -ge 3 ]]` | Add all 3 options |
| BUILD-09 | Phase 1 timeline documented | grep | `grep -q "Phase 1 Timeline\|Week 1:" projects/claude-code-harness-distribution/03-distribution*.md` | Add timeline |
| BUILD-10 | Budget summary included | grep | `grep -q "Budget Summary\|Phase 1.*\$.*K" projects/claude-code-harness-distribution/03-distribution*.md` | Add budget table |
| BUILD-11 | Agent Skills specification | file_exists | `test -f projects/claude-code-harness-distribution/04-agent-skills-refactor-spec.md` | Create file |
| BUILD-12 | Harness compatibility matrix | grep | `[[ $(grep -c "Claude Code\|Cursor\|Copilot\|Gemini\|Cline" projects/claude-code-harness-distribution/04-agent*.md) -ge 5 ]]` | Add compatibility matrix |
| BUILD-13 | SKILL.md format documented | grep | `grep -q "SKILL.md\|YAML frontmatter" projects/claude-code-harness-distribution/04-agent*.md` | Add format spec |
| BUILD-14 | Submission templates file | file_exists | `test -f projects/claude-code-harness-distribution/05-submission-templates.md` | Create file |
| BUILD-15 | 4 platform templates | grep | `[[ $(grep -c "## Claude Code Plugins\|## skills.sh\|## claudemarketplaces\|## GitHub" projects/claude-code-harness-distribution/05-submission*.md) -ge 4 ]]` | Add all 4 templates |
| BUILD-16 | Master research report | file_exists | `test -f projects/claude-code-harness-distribution/RESEARCH-REPORT.md` | Create file |
| BUILD-17 | Executive summary in report | grep | `grep -q "Executive Summary" projects/claude-code-harness-distribution/RESEARCH-REPORT.md` | Add section |
| BUILD-18 | Key findings in report | grep | `grep -q "Key Findings\|Critical Insight" projects/claude-code-harness-distribution/RESEARCH-REPORT.md` | Add findings |
| BUILD-19 | Integration design document | file_exists | `test -f projects/claude-code-harness-distribution/INTEGRATION-DESIGN.md` | Create file |
| DOC-01 | Platforms report content quality | manual | Inventory complete, comparison clear, recommendations supported by data | Expand analysis |
| DOC-02 | Gaps analysis actionable | manual | Gaps ranked by opportunity, curator approach justified, cost comparison clear | Refine recommendations |

## Testing Strategy

### Level 1: Structural (File Exists)
- STRUCT-01 through STRUCT-03: Directory structure
- BUILD-01, BUILD-03, BUILD-05, BUILD-11, BUILD-14, BUILD-16, BUILD-19: All deliverable files exist

### Level 2: Functional (Content Validation)
- BUILD-02, BUILD-04, BUILD-06 through BUILD-18: Content validation via grep patterns
- All gates verify specific sections, matrices, and formatted content

### Level 3: Semantic (Manual Review)
- DOC-01, DOC-02: Content quality, completeness, actionability
- Verified during final review before task completion

## Success Criteria

✓ All 24 gates pass
✓ All 7 deliverable files created
✓ All matrices, tables, and checklists present
✓ Content accurate and actionable (L3 gates)
