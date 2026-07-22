#!/usr/bin/env python3
"""
L1 Test: Structure + Lexicon (Task 005)
- Checks soap_service.py + WSDL mount present on branch
- Extended vocab lexicon 0 hits on branch diff
- py_compile all new files
"""

import os
import sys
import re
import py_compile
import subprocess
import json
from pathlib import Path

def run_test():
    # Target repo
    target_repo = r'D:\my_ai_projects\project_test_repos\hmsa-qa-platform'

    # 1. Check if soap_service.py exists
    soap_service = Path(target_repo) / 'harness' / 'orderly' / 'soap_service.py'
    if not soap_service.exists():
        print(f'FAIL: soap_service.py does not exist at {soap_service}')
        return False
    print('PASS: soap_service.py exists')

    # 2. Check if WSDL mount is in main.py
    main_py = Path(target_repo) / 'harness' / 'orderly' / 'main.py'
    if not main_py.exists():
        print(f'FAIL: main.py does not exist at {main_py}')
        return False

    with open(main_py) as f:
        main_content = f.read()

    if 'WSGIMiddleware' not in main_content:
        print('FAIL: WSDL mount (WSGIMiddleware) not found in main.py')
        return False
    if 'soap_app' not in main_content.lower():
        print('FAIL: soap_app reference not found in main.py')
        return False
    print('PASS: WSDL mount found in main.py (WSGIMiddleware + soap_app)')

    # 3. Check extended vocab lexicon - healthcare terms that should NOT be present
    # Per lesson #32/46 - extended vocab ban list for clean-room
    healthcare_vocab = [
        r'\bhmsa\b', r'\bhealthcare\b', r'\bclaim\b', r'\bpatient\b',
        r'\bmember\b', r'\bsubscriber\b', r'\beligib', r'\bEOB\b',
        r'\bremittance\b', r'\bdiagnosis\b', r'\bprovider', r'\bautopend\b',
        r'\bDRG\b', r'\bPCN\b', r'\b837\b'
    ]

    # Get diff from main branch
    try:
        result = subprocess.run(
            ['git', '-C', target_repo, 'diff', 'main'],
            capture_output=True,
            text=True,
            check=False
        )
        diff_output = result.stdout
    except Exception as e:
        print(f'FAIL: Could not get git diff: {e}')
        return False

    violations = []
    for pattern in healthcare_vocab:
        matches = list(re.finditer(pattern, diff_output, re.IGNORECASE))
        if matches:
            violations.append((pattern, len(matches)))

    if violations:
        print(f'FAIL: Healthcare vocab found in diff ({len(violations)} patterns):')
        for pattern, count in violations:
            print(f'  {pattern}: {count} hits')
        return False
    print('PASS: Extended vocab lexicon check (0 hits)')

    # 4. py_compile all new files
    new_files = [soap_service]
    for file in new_files:
        try:
            py_compile.compile(str(file), doraise=True)
        except py_compile.PyCompileError as e:
            print(f'FAIL: py_compile error in {file}: {e}')
            return False
    print('PASS: All files compile successfully')

    print('\nL1 TEST PASSED')
    return True

if __name__ == '__main__':
    success = run_test()
    sys.exit(0 if success else 1)
