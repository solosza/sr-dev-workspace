# Gate Contract — Skill-as-App Architecture Research

## Gate Contract

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project dir exists | file_exists | `test -d projects/kernel-architecture/` | Create dir |
| BUILD-02 | Decision framework exists | file_exists | `test -f projects/kernel-architecture/decision-framework.md` | Create file |
| BUILD-03 | Generation skill design exists | file_exists | `test -f projects/kernel-architecture/generation-skill-design.md` | Create file |
| BUILD-04 | Research report exists | file_exists | `test -f projects/kernel-architecture/report.md` | Create file |
| FUNC-01 | Report covers website-cloner | grep | `grep -q "website-cloner\|Website Cloner" projects/kernel-architecture/report.md` | Add analysis |
| FUNC-02 | Report covers fraud detector | grep | `grep -q "fraud\|Fraud Detector" projects/kernel-architecture/report.md` | Add analysis |
| FUNC-03 | Decision framework has criteria | grep | `grep -q "When to use" projects/kernel-architecture/decision-framework.md` | Add criteria |
| FUNC-04 | Generation design has architecture | grep | `grep -q "architecture\|Architecture\|pipeline\|Pipeline" projects/kernel-architecture/generation-skill-design.md` | Add architecture |
