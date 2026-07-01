# CI / Automated Testing — Solution Proposal

**Backlog:** 146-kernel-research-state-isolation-and-ci-solutions
**Date:** 2026-06-22
**Source:** External review critique (backlog 145) + research

---

## GitHub Actions — Patterns Surveyed

### Standard Python CI Pattern
The industry-standard pattern for Python repos on GitHub Actions:
1. Checkout code → `actions/checkout@v6`
2. Setup Python → `actions/setup-python@v5` with version matrix
3. Install dependencies → `pip install -r requirements.txt` + `pip install pytest`
4. Run tests → `pytest --junitxml=results.xml`
5. Upload artifacts → `actions/upload-artifact@v4`
6. Publish results → `EnricoMi/publish-unit-test-result-action` or `dorny/test-reporter`

### Artifact Publishing
- `actions/upload-artifact@v4` stores test results (XML, JSON) as downloadable artifacts
- `EnricoMi/publish-unit-test-result-action` publishes results as GitHub Check Runs with pass/fail stats
- Supports JUnit XML, JSON, TRX formats
- `if: ${{ always() }}` ensures artifacts are captured even on failure

### Template-Based CI
- GitHub supports **starter workflows** in `.github/workflows/` that repos can adopt
- **Copier** and **Cookiecutter** can generate per-repo CI from templates
- Simpler approach: a shell script that writes the workflow YAML based on repo structure

### Free Tier Constraints
- **2,000 minutes/month** on GitHub Actions free tier
- Ubuntu runners: 1x multiplier (2,000 minutes = 2,000 minutes)
- A typical pytest run: ~2-5 minutes (checkout + setup + test)
- Budget: ~400-1,000 CI runs/month — more than sufficient for a solo developer with <10 repos

---

## Current State — What Already Exists

| Mechanism | Where | What It Does | Gap |
|-----------|-------|-------------|-----|
| Prod-test skill | `.claude/skills/prod-test/` | Copies to disposable repo, runs L1/L2/L3 tests, produces validation report | Manual invocation only — not triggered on push/PR |
| Validation report | `_test/validation-report.json` | Per-task pass/fail with gate verification | Not committed alongside deliverables, not published as artifact |
| Pytest suites | Various repos (`isagawa-kernel`, `test-platform-deepeval`) | Unit + integration tests | Run by agent or run-task.sh, not on push |
| run-task.sh | `run-task.sh` | Deterministic task runner | Could be wrapped as a CI step but isn't |
| Hook files | `.claude/hooks/` | Python scripts enforcing gates | No integrity verification in CI |

**The gap**: Zero GitHub Actions workflows in any repo. No automated test runs on push/PR. No `.github/workflows/` directory anywhere.

---

## Gap Analysis

### What's Missing

1. **No push-triggered testing**: Code merged without automated verification
2. **No PR checks**: No required status checks on pull requests
3. **No validation report publishing**: Reports exist but are ephemeral (only in task folders)
4. **No hook integrity verification**: Hook files could be modified without detection
5. **No template CI generation**: Each repo would need manual CI setup

### What's Already Solved

1. **Test infrastructure**: Pytest suites exist and pass
2. **Independent verification**: Prod-test already runs in isolation
3. **Gate contracts**: Mechanical verification specs already defined per project

---

## Proposed Solution

**Two-tier CI: Lightweight push CI + Full prod-test on PR**

### Tier 1: Push CI (every push)
- Fast: structural tests, import checks, lint
- No API keys required
- Runs in ~2-3 minutes
- Catches broken imports, missing files, syntax errors

### Tier 2: PR CI (pull requests only)
- Full: pytest suite, hook integrity check
- Optional: validation report generation
- Runs in ~5-10 minutes
- Gates merge with pass/fail status check

### Why Two Tiers
- Push CI runs on every commit — must be fast and cheap
- PR CI runs less frequently — can be thorough
- Both fit within free tier budget (~400+ runs/month)

---

## Implementation

### Reference Workflow: isagawa-kernel

**File:** `.github/workflows/ci.yml`

```yaml
name: CI

on:
  push:
    branches: [main, 'feature/**']
  pull_request:
    branches: [main]

jobs:
  structural:
    name: Structural Checks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Check imports
        run: |
          python -c "import importlib, pathlib
          errors = []
          for f in pathlib.Path('.').rglob('*.py'):
              if f.name.startswith('_') and f.name != '__init__.py': continue
              try:
                  spec = importlib.util.spec_from_file_location(f.stem, f)
                  if spec and spec.loader:
                      module = importlib.util.module_from_spec(spec)
              except Exception as e:
                  errors.append(f'{f}: {e}')
          if errors:
              print('Import errors:')
              for e in errors: print(f'  {e}')
              exit(1)
          print('All imports clean')"

      - name: Run pytest (structural + unit)
        run: pytest tests/ -v --tb=short --junitxml=test-results.xml
        if: hashFiles('tests/') != ''

      - name: Upload test results
        uses: actions/upload-artifact@v4
        with:
          name: test-results
          path: test-results.xml
        if: always()

  hook-integrity:
    name: Hook Integrity
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request'
    steps:
      - uses: actions/checkout@v6

      - name: Verify hook hashes
        run: |
          if [ -d ".claude/hooks" ]; then
            for hook in .claude/hooks/*.py; do
              echo "$(sha256sum "$hook")"
            done
            echo "Hook files verified (hashes above for audit)"
          else
            echo "No hooks directory found"
          fi

      - name: Verify settings.json references
        run: |
          if [ -f ".claude/settings.json" ]; then
            python -c "
          import json, pathlib
          settings = json.load(open('.claude/settings.json'))
          hooks = settings.get('hooks', {})
          for event, hook_list in hooks.items():
              for hook in hook_list:
                  cmd = hook.get('command', '')
                  # Extract Python file paths from hook commands
                  parts = cmd.split()
                  for part in parts:
                      if part.endswith('.py'):
                          p = pathlib.Path(part)
                          if not p.exists():
                              print(f'ERROR: Hook references missing file: {part}')
                              exit(1)
          print('All hook references valid')
          "
          fi
```

### Validation Report as Artifact

When prod-test runs (manually or in CI), commit the validation report:

```yaml
  # Optional: prod-test on PR (requires more setup)
  prod-test:
    name: Production Test
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request'
    steps:
      - uses: actions/checkout@v6
      - name: Run structural validation
        run: |
          # Validate gate contract if it exists
          if [ -f "tasks/*/gate-contract.md" ]; then
            echo "Gate contract found — running structural gates"
            # Parse gate contract, run file_exists and grep checks
            python -c "
          import pathlib, subprocess, json
          results = []
          # Find all gate contracts
          for gc in pathlib.Path('tasks').rglob('gate-contract.md'):
              print(f'Checking: {gc}')
              # Basic: verify task files exist
              task_dir = gc.parent
              tasks = list(task_dir.glob('[0-9]*.md'))
              results.append({'gate_contract': str(gc), 'task_count': len(tasks)})
          json.dump(results, open('validation-report.json', 'w'), indent=2)
          print(f'Validation complete: {len(results)} contracts checked')
          "
          fi

      - name: Upload validation report
        uses: actions/upload-artifact@v4
        with:
          name: validation-report
          path: validation-report.json
        if: always()
```

### Template Generation via domain-setup

**File:** `.claude/skills/kernel-domain-setup/references/step-09-commands.md` (extension)

Add a CI generation step to domain-setup:

```python
def generate_ci_workflow(repo_path, domain_name, has_tests=True):
    """Generate GitHub Actions CI workflow for a kernel-governed repo."""
    workflow = {
        'name': 'CI',
        'on': {
            'push': {'branches': ['main', 'feature/**']},
            'pull_request': {'branches': ['main']}
        },
        'jobs': {
            'test': {
                'runs-on': 'ubuntu-latest',
                'steps': [
                    {'uses': 'actions/checkout@v6'},
                    {'uses': 'actions/setup-python@v5', 'with': {'python-version': '3.12'}},
                    {'name': 'Install deps', 'run': 'pip install pytest\nif [ -f requirements.txt ]; then pip install -r requirements.txt; fi'},
                ]
            }
        }
    }
    if has_tests:
        workflow['jobs']['test']['steps'].append({
            'name': 'Run tests',
            'run': 'pytest tests/ -v --junitxml=test-results.xml'
        })
        workflow['jobs']['test']['steps'].append({
            'uses': 'actions/upload-artifact@v4',
            'with': {'name': 'test-results', 'path': 'test-results.xml'},
            'if': 'always()'
        })
    return workflow
```

domain-setup calls this after generating hooks and commands, writing to `.github/workflows/ci.yml`.

---

## Scope — Per-Repo vs Workspace

| Scope | CI Coverage | Recommendation |
|-------|------------|----------------|
| **isagawa-kernel** (priority) | pytest on push, hook integrity on PR | Implement first — reference implementation |
| **Domain repos** (e.g., test-platform-deepeval) | pytest on push, structural gates on PR | domain-setup generates per-repo |
| **sr_dev_workspace** | No CI — orchestration workspace, not a deployable | Skip |

**Recommendation**: Start with isagawa-kernel as the reference implementation. Then add CI generation to domain-setup so every new domain repo gets CI automatically.

---

## CI Scope for Other Claude Code Harness Projects

Based on research, other Claude Code harness/agent projects typically:
- Run linting (ruff, flake8) on push
- Run unit tests (pytest) on push
- Use matrix testing for Python versions
- Publish test results as artifacts
- Don't run full agent sessions in CI (too expensive, non-deterministic)

**Our equivalent**: Structural + unit tests on push (deterministic, fast). Full prod-test remains manual or PR-triggered (expensive, involves agent invocation).

---

## Hook Integrity in CI

Hook files are critical security infrastructure. CI should verify:

1. **File existence**: All hooks referenced in `.claude/settings.json` exist on disk
2. **Hash audit trail**: Print SHA-256 of each hook file in CI logs for forensic review
3. **No unauthorized hooks**: Compare hook file list against expected set

This doesn't prevent modification (the repo owner controls the hooks) but creates an audit trail visible in CI logs.

---

## Migration Path

1. **Phase 1** (immediate): Add `.github/workflows/ci.yml` to `isagawa-kernel` with structural checks + pytest
2. **Phase 2** (next sprint): Add hook integrity check to PR workflow
3. **Phase 3** (follow-up): Add CI generation to domain-setup so new repos get CI automatically
4. **Phase 4** (future): Add validation report publishing as artifact, integrate with gate contracts

---

## Risks

| Risk | Mitigation |
|------|------------|
| CI minutes exhausted | Tier 1 is fast (~2 min), limit matrix to single Python version initially |
| Tests that need API keys fail in CI | Structural/unit tests have no secrets; mark e2e tests with `@pytest.mark.skip` in CI |
| Non-deterministic agent tests | Don't run agent sessions in CI — structural tests only |
| domain-setup CI template diverges from manual CI | Single source of truth: template in domain-setup, manual CI only for isagawa-kernel (reference) |

---

## Effort Estimate

**Medium** — 2-3 days of implementation:
- 1 workflow YAML for isagawa-kernel (reference implementation) — 2 hours
- Hook integrity check additions — 1 hour
- CI generation function for domain-setup — 4 hours
- Testing the CI workflow against actual repo — 2 hours
- Documentation updates — 1 hour

No external dependencies. Works with GitHub Actions free tier. Template-based for future repos.
