## Gate Contract

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Competitor analysis written | file_exists | `test -f projects/kernel-architecture/swarms-competitor-analysis.md` | Write file |
| BUILD-02 | Codebase mapping written | file_exists | `test -f projects/kernel-architecture/swarms-codebase-mapping.md` | Write file |
| BUILD-03 | Dedicated-job analysis written | file_exists | `test -f projects/kernel-architecture/swarms-dedicated-jobs.md` | Write file |
| BUILD-04 | Moat assessment written | file_exists | `test -f projects/kernel-architecture/swarms-moat-assessment.md` | Write file |
| BUILD-05 | Viral hook analysis written | file_exists | `test -f projects/kernel-architecture/swarms-viral-hooks.md` | Write file |
| BUILD-06 | Architectural gaps written | file_exists | `test -f projects/kernel-architecture/swarms-architectural-gaps.md` | Write file |
| BUILD-07 | Final report compiled | file_exists | `test -f projects/kernel-architecture/agent-swarms-harness-fit.md` | Compile report |
| TEST-01 | Report covers all 6 questions | run_code | `grep -c "##" projects/kernel-architecture/agent-swarms-harness-fit.md` returns 6+ | Add missing sections |
