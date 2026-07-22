# Task 004: Enable GitHub Pages

**Type:** BUILD | **Gates:** PF-04

## Action
ONE gh api call: enable Pages for the repo (source: main branch, root). `gh api repos/{owner}/{repo}/pages -X POST -f "source[branch]=main" -f "source[path]=/"` (adjust per gh api requirements - READ `gh api --help` output first if unsure). If Pages already enabled (422), treat as success.

## Acceptance
Pages status endpoint returns built/building; note the live URL in output.
