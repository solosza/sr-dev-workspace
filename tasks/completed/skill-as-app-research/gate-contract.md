# Gate Contract — Skill-as-App Architecture Research

## Verification Methods
See `.claude/skills/task-builder/references/verification-methods.md`

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project dir exists | file_exists | `test -d projects/kernel-architecture` | Create directory |
| BUILD-02 | Research report exists | file_exists | `test -f projects/kernel-architecture/skill-as-app-research.md` | Create file |
| BUILD-03 | Decision framework section | grep | `grep -q '## Decision Framework' projects/kernel-architecture/skill-as-app-research.md` | Add section |
| BUILD-04 | Generation skills design section | grep | `grep -q '## Generation Skills' projects/kernel-architecture/skill-as-app-research.md` | Add section |
| BUILD-05 | Website cloner analysis | grep | `grep -q 'website-cloner' projects/kernel-architecture/skill-as-app-research.md` | Add analysis |
| BUILD-06 | Fraud detector analysis | grep | `grep -q 'fraud' projects/kernel-architecture/skill-as-app-research.md` | Add analysis |
| BUILD-07 | Report has trade-offs | grep | `grep -q 'trade-off\|tradeoff\|Trade-off' projects/kernel-architecture/skill-as-app-research.md` | Add trade-offs |
