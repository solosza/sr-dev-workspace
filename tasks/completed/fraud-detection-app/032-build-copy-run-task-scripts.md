# Copy run-task.sh Scripts

## Type
BUILD

## Description
Copy kernel run-task infrastructure into the fraud-detection-app repo.

## Requirements
Copy from `D:\my_ai_projects\project_test_repos\sr_dev_workspace\` to `D:\my_ai_projects\fraud-detection-app\`:
- `run-task.sh` → `run-task.sh`
- `run-task-batch.sh` → `run-task-batch.sh`
- `lib/common.sh` → `lib/common.sh` (create lib/ dir first)

Make scripts executable: `chmod +x run-task.sh run-task-batch.sh`

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/run-task.sh`
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/run-task-batch.sh`
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/lib/common.sh`
