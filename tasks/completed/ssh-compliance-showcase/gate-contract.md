## Gate Contract

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Feature branch exists | run_code | `git -C "D:/my_ai_projects/isagawa-co.github.io" branch --list feature/showcase-ssh-compliance` returns non-empty | Create branch |
| BUILD-02 | CSS file exists | file_exists | `test -f "D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.css"` | Write file |
| BUILD-03 | HTML file exists | file_exists | `test -f "D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html"` | Write file |
| BUILD-04 | HTML references CSS | grep | `grep -q 'ssh-compliance.css' "D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html"` | Fix link |
| BUILD-05 | Homepage has SSH link | grep | `grep -q 'ssh-compliance.html' "D:/my_ai_projects/isagawa-co.github.io/index.html"` | Add link |
| BUILD-06 | Commit exists on branch | run_code | `git -C "D:/my_ai_projects/isagawa-co.github.io" log feature/showcase-ssh-compliance --oneline -1` returns non-empty | Commit |
| TEST-01 | Page has hero section | grep | `grep -q 'hero' "D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html"` | Fix HTML |
| TEST-02 | Page has framework cards | grep | `grep -q 'STIG' "D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html"` | Fix content |
| TEST-03 | No dashes in content | run_code | `! grep -P ' — ' "D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html"` | Remove dashes |
