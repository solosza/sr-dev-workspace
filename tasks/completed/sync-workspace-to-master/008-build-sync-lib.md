# Task 008: Build — Copy lib/ Directory

## Objective
Copy lib/common.sh and lib/attestation/ to master.

## Instructions

1. Create directory structure:
   ```bash
   mkdir -p "D:/my_ai_projects/isagawa-kernel/lib/attestation"
   ```
2. Copy files:
   ```bash
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/common.sh" "D:/my_ai_projects/isagawa-kernel/lib/"
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/attestation/__init__.py" "D:/my_ai_projects/isagawa-kernel/lib/attestation/"
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/attestation/intent.py" "D:/my_ai_projects/isagawa-kernel/lib/attestation/"
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/attestation/attest.py" "D:/my_ai_projects/isagawa-kernel/lib/attestation/"
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/attestation/sign.py" "D:/my_ai_projects/isagawa-kernel/lib/attestation/"
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/attestation/rekor.py" "D:/my_ai_projects/isagawa-kernel/lib/attestation/"
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/attestation/collect.py" "D:/my_ai_projects/isagawa-kernel/lib/attestation/"
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/attestation/schema.py" "D:/my_ai_projects/isagawa-kernel/lib/attestation/"
   ```
3. Verify intent.py exists in master

## Acceptance Criteria
- `lib/common.sh` exists in master
- `lib/attestation/intent.py` exists in master
- 8 total files in lib/

## Gate
BUILD-08
