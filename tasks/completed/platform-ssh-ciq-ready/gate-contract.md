# Gate Contract — Platform-SSH CIQ Ready

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | LICENSE file exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/LICENSE` | Create file |
| BUILD-02 | LICENSE contains MIT text | grep | `grep -q 'MIT License' D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/LICENSE` | Fix content |
| BUILD-03 | README has badges | grep | `grep -q 'img.shields.io' D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/README.md` | Add badges |
| BUILD-04 | README has contact section | grep | `grep -q 'alain@isagawa.co' D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/README.md` | Add contact |
| BUILD-05 | README has example output | grep | `grep -q 'Example.*Output\|Example.*Scan' D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/README.md` | Add example |
| BUILD-06 | Landing page has contact CTA | grep | `grep -q 'contact-cta\|Talk to Us\|Schedule' D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html` | Add CTA |
| BUILD-07 | Landing page has enterprise section | grep | `grep -q 'Why Isagawa\|enterprise' D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html` | Add section |
| BUILD-08 | Landing page links attestation | grep | `grep -q 'feed.html' D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html` | Add link |
| TEST-01 | GitHub repo pushed | run_code | `git -C D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh log --oneline -1` shows recent commit | Push repo |
| TEST-02 | Website repo pushed | run_code | `git -C D:/my_ai_projects/isagawa-co.github.io log --oneline -1` shows recent commit | Push repo |
