# Source Resolution Reference

Rules for detecting and resolving source inputs to local directories.

## Detection Rules

| Pattern | Type | Examples |
|---------|------|---------|
| Starts with `https://` | GitHub URL | `https://github.com/isagawa-co/isagawa-kernel` |
| Starts with `http://` | GitHub URL | `http://github.com/org/repo` |
| Contains `github.com` anywhere | GitHub URL | `github.com/org/repo` (bare) |
| Contains `:\` or `/` with no dots | Local path (Windows) | `D:\my_ai_projects\project_test_repos\kernel-minimal` |
| Everything else | Local path | Relative or absolute path |

## GitHub URL Handling

### Supported URL Formats

```
https://github.com/org/repo
https://github.com/org/repo.git
https://github.com/org/repo/tree/branch-name
git@github.com:org/repo.git
```

### Repo Name Extraction

1. Split URL by `/`
2. Take last path segment
3. Strip `.git` suffix if present
4. Strip `/tree/...` suffix if present
5. Lowercase, replace special chars with hyphens

| URL | Extracted Name |
|-----|---------------|
| `https://github.com/isagawa-co/isagawa-kernel` | `isagawa-kernel` |
| `https://github.com/org/my-repo.git` | `my-repo` |
| `https://github.com/org/repo/tree/main` | `repo` |

### Clone Directory

```
D:\my_ai_projects\project_test_repos\eval-[repo-name]-clone\
```

This directory is disposable — deleted and re-created each eval run.

### Clone Command

```bash
# Remove prior clone if exists
rm -rf "D:\my_ai_projects\project_test_repos\eval-[repo-name]-clone"

# Shallow clone (depth 1 is sufficient for eval)
git clone --depth 1 "<url>" "D:\my_ai_projects\project_test_repos\eval-[repo-name]-clone"
```

### Branch/Tag Support

If the URL contains `/tree/<ref>`:
```bash
git clone --depth 1 --branch "<ref>" "<base-url>" "<clone-dir>"
```

If no branch specified, clone default branch.

## Local Path Handling

1. Verify path exists: `test -d "<path>"`
2. Use as-is — no copying, no cloning
3. The source repo is read-only during eval (only the test repo gets modified)

## Error Cases

| Scenario | Action |
|----------|--------|
| URL returns 404 | Abort: "Repository not found: <url>" |
| URL requires auth (private repo) | Abort: "Authentication required for <url>. Clone manually or use a local path." |
| Local path doesn't exist | Abort: "Source path not found: <path>" |
| Clone directory can't be created (permissions) | Abort: "Cannot create clone directory. Check permissions." |
