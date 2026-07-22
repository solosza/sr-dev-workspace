# Task 003: Create GitHub Repo + Push

**Type:** BUILD | **Gates:** PF-03

## Action
ONE gh operation: check gh auth status; create a PUBLIC repo named portfolio (or the account's github.io repo if the user has none - prefer '<username>.github.io' when available for the cleanest URL) from D:/my_ai_projects/portfolio-site; add remote; push main.

If gh is not authenticated: report BLOCKED with gh auth status output and STOP - never attempt interactive login.

## Acceptance
gh repo view succeeds; push clean.
