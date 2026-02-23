#!/usr/bin/env python3
"""
Sr Dev Gate Enforcer - Blocks code quality violations.

Mechanically enforced anti-patterns:
- Debug statements (console.log, print, etc.)
- Hardcoded secrets
- Wildcard imports
- Skipped tests
- File size > 300 lines
"""
import json
import re
import sys
from pathlib import Path

# Files to skip (infrastructure, config, tests)
SKIP_PATTERNS = [
    r'\.claude/',
    r'node_modules/',
    r'__pycache__/',
    r'\.git/',
    r'\.test\.',
    r'test_',
    r'_test\.',
    r'\.spec\.',
    r'spec_',
    r'docs/design/',
]

# Debug statement patterns by extension
DEBUG_PATTERNS = {
    '.py': [
        r'^\s*print\s*\(',
        r'^\s*pprint\s*\(',
    ],
    '.js': [
        r'^\s*console\.(log|debug|info|warn|error)\s*\(',
        r'^\s*debugger\s*;?',
    ],
    '.ts': [
        r'^\s*console\.(log|debug|info|warn|error)\s*\(',
        r'^\s*debugger\s*;?',
    ],
    '.tsx': [
        r'^\s*console\.(log|debug|info|warn|error)\s*\(',
        r'^\s*debugger\s*;?',
    ],
    '.jsx': [
        r'^\s*console\.(log|debug|info|warn|error)\s*\(',
        r'^\s*debugger\s*;?',
    ],
    '.go': [
        r'^\s*fmt\.Print(ln|f)?\s*\(',
        r'^\s*log\.Print(ln|f)?\s*\(',
    ],
    '.rs': [
        r'^\s*println!\s*\(',
        r'^\s*dbg!\s*\(',
    ],
    '.java': [
        r'^\s*System\.out\.print(ln)?\s*\(',
    ],
}

# Secret patterns (all languages)
SECRET_PATTERNS = [
    r'password\s*=\s*["\'][^"\']+["\']',
    r'secret\s*=\s*["\'][^"\']+["\']',
    r'api_key\s*=\s*["\'][^"\']+["\']',
    r'apikey\s*=\s*["\'][^"\']+["\']',
    r'token\s*=\s*["\'][^"\']+["\']',
    r'AWS_SECRET',
    r'PRIVATE_KEY\s*=',
]

# Wildcard import patterns
WILDCARD_PATTERNS = {
    '.py': [r'from\s+\S+\s+import\s+\*'],
    '.js': [r'import\s+\*\s+from'],
    '.ts': [r'import\s+\*\s+from'],
}

# Skipped test patterns
SKIP_TEST_PATTERNS = [
    r'\.skip\s*\(',
    r'@pytest\.mark\.skip',
    r'\bxit\s*\(',
    r'\bxdescribe\s*\(',
    r'@Ignore',
    r'#\s*\[ignore\]',
]

MAX_FILE_LINES = 300


def should_skip(file_path: str) -> bool:
    """Check if file should be skipped."""
    for pattern in SKIP_PATTERNS:
        if re.search(pattern, file_path):
            return True
    return False


def get_extension(file_path: str) -> str:
    """Get file extension."""
    return Path(file_path).suffix.lower()


def check_debug_statements(content: str, ext: str) -> list:
    """Check for debug statements."""
    violations = []
    patterns = DEBUG_PATTERNS.get(ext, [])

    for i, line in enumerate(content.split('\n'), 1):
        for pattern in patterns:
            if re.search(pattern, line, re.IGNORECASE):
                violations.append(f"Line {i}: Debug statement detected")
                break

    return violations


def check_secrets(content: str) -> list:
    """Check for hardcoded secrets."""
    violations = []

    for i, line in enumerate(content.split('\n'), 1):
        for pattern in SECRET_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                violations.append(f"Line {i}: Possible hardcoded secret")
                break

    return violations


def check_wildcard_imports(content: str, ext: str) -> list:
    """Check for wildcard imports."""
    violations = []
    patterns = WILDCARD_PATTERNS.get(ext, [])

    for i, line in enumerate(content.split('\n'), 1):
        for pattern in patterns:
            if re.search(pattern, line):
                violations.append(f"Line {i}: Wildcard import")
                break

    return violations


def check_skipped_tests(content: str, file_path: str) -> list:
    """Check for skipped tests (only in test files)."""
    # Only check test files
    if not any(p in file_path.lower() for p in ['test', 'spec']):
        return []

    violations = []

    for i, line in enumerate(content.split('\n'), 1):
        for pattern in SKIP_TEST_PATTERNS:
            if re.search(pattern, line):
                violations.append(f"Line {i}: Skipped test")
                break

    return violations


def check_file_size(content: str) -> list:
    """Check file doesn't exceed max lines."""
    lines = content.count('\n') + 1
    if lines > MAX_FILE_LINES:
        return [f"File has {lines} lines (max {MAX_FILE_LINES})"]
    return []


def smart_block(violations: list, category: str):
    """Block with helpful message."""
    msg = f"""BLOCKED: Sr Dev code quality violation - {category}

Violations found:
{chr(10).join('  - ' + v for v in violations[:5])}
{'  ... and ' + str(len(violations) - 5) + ' more' if len(violations) > 5 else ''}

FIX:
1. Remove or fix the violations above
2. For debug statements: remove before commit
3. For secrets: use environment variables
4. For wildcard imports: import specific items
5. For skipped tests: unskip or remove

Then retry your write.
"""
    print(msg, file=sys.stderr)
    sys.exit(2)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_name = data.get('tool_name', '')
    if tool_name not in ('Write', 'Edit'):
        sys.exit(0)

    tool_input = data.get('tool_input', {})
    file_path = tool_input.get('file_path', '').replace('\\', '/')

    # Skip infrastructure files
    if should_skip(file_path):
        sys.exit(0)

    # Get content to check
    content = tool_input.get('content', '')
    if not content and 'new_string' in tool_input:
        content = tool_input.get('new_string', '')

    if not content:
        sys.exit(0)

    ext = get_extension(file_path)

    # Run all checks
    debug_violations = check_debug_statements(content, ext)
    if debug_violations:
        smart_block(debug_violations, "Debug statements")

    secret_violations = check_secrets(content)
    if secret_violations:
        smart_block(secret_violations, "Hardcoded secrets")

    wildcard_violations = check_wildcard_imports(content, ext)
    if wildcard_violations:
        smart_block(wildcard_violations, "Wildcard imports")

    skip_violations = check_skipped_tests(content, file_path)
    if skip_violations:
        smart_block(skip_violations, "Skipped tests")

    size_violations = check_file_size(content)
    if size_violations:
        smart_block(size_violations, "File too large")

    # All checks passed
    sys.exit(0)


if __name__ == '__main__':
    main()
