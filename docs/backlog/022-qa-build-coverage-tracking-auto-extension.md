# Coverage Tracking + Automatic Suite Extension

## Status
Open

## Priority
Medium — Brian requested. Addresses the gap between "features shipped" and "features tested." Devs add features but don't extend the test suite.

## Summary
Build coverage tracking and automatic suite extension into the QA framework. The framework tracks which features/pages/workflows have test coverage and which don't. When a dev adds new features (new pages, new workflows, new API endpoints), the framework detects the gap and either auto-generates skeleton tests or guides the dev to write them. Closes the loop between development and testing.

## Requirements
- Coverage tracking: map test files to features/pages/workflows they cover
- Gap detection: identify features/pages with no test coverage
- Auto-extension guidance: when new page objects or workflows are added, suggest or generate skeleton test files
- Coverage report: dashboard or CLI output showing coverage percentage per feature area
- Integration with existing workflow: coverage check runs as part of the test pipeline, not a separate tool
- Support close-out: when a feature is "done," verify test coverage meets threshold before marking complete

## References
- Brian's request (2026-03-23 text conversation): "coverage tracking and close out to support automatically extending suite when the dev adds new features"
- py-selenium-framework-mcp (local reference implementation)
- isagawa-qa/platform-selenium (GitHub)
- Test structure: `tests/{workflow_name}/test_*.py`
- Framework structure: `framework/pages/`, `framework/tasks/`, `framework/roles/`

## Task Builder Input
- **Deliverable:** Coverage tracking module + auto-extension generator. Produces coverage report (which features are tested, which aren't) and generates skeleton test files for uncovered features.
- **Scope:** BUILD
- **Constraints:** Must work within existing 4-layer architecture. Coverage mapping needs a convention for linking tests to features (by directory name, decorator, or config). Auto-generated tests should follow the existing test template pattern.
