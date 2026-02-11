  Prompt:
                                                                                    
  I want you to be my senior dev engineer. Build me a protocol that enforces best
  practices.

  Domain: sr_dev

  Requirements:

  ## Code Quality
  - No functions over 50 lines
  - No files over 300 lines
  - No magic numbers (use constants)
  - No commented-out code committed
  - Type hints required (Python) or TypeScript (JS)

  ## Git Workflow
  - Never commit directly to main
  - Branch naming: feature/, bugfix/, hotfix/
  - Commit messages: conventional commits (feat:, fix:, refactor:, etc.)
  - No force pushes
  - Squash commits before merge

  ## Testing
  - Tests required before merge
  - No skipped tests committed
  - Test file naming: test_*.py or *.test.ts

  ## Documentation
  - README required for new modules
  - Docstrings on public functions
  - CHANGELOG updated for user-facing changes

  ## Architecture
  - No circular imports
  - Single responsibility per file
  - Composition over inheritance
  - No business logic in controllers/routes

  ## Anti-Patterns to Block
  - console.log / print statements in production code
  - Hardcoded credentials or secrets
  - TODO comments older than 1 sprint
  - Catch-all exception handlers (except: pass)

  Start by setting up the protocol enforcement for this domain.