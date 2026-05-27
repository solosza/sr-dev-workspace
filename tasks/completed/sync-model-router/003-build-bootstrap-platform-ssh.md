# Task 003: Bootstrap full kernel infra for platform-ssh

## Objective
Platform-ssh has no run-task.sh or lib/. Copy the full kernel execution infrastructure.

Source: `D:\my_ai_projects\project_test_repos\sr_dev_workspace`
Target: `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh`

## Instructions

1. Create `lib/` directory in target
2. Copy `lib/common.sh` to target `lib/`
3. Copy `lib/model-router.sh` to target `lib/`
4. Copy `lib/model-routing-config.json` to target `lib/`
5. Copy `lib/attestation/` directory to target `lib/`
6. Copy `run-task.sh` to target root
7. Copy `run-task-batch.sh` to target root

## Acceptance Criteria
- [ ] `lib/common.sh` exists in platform-ssh
- [ ] `lib/model-router.sh` exists in platform-ssh
- [ ] `lib/model-routing-config.json` exists in platform-ssh
- [ ] `lib/attestation/` directory exists in platform-ssh
- [ ] `run-task.sh` exists in platform-ssh
- [ ] `run-task-batch.sh` exists in platform-ssh

## Gate
BUILD-03
