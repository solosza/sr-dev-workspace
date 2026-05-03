# Copy shell scripts to master repo

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
```bash
cp C:/Users/solos/my_ai_projects/run-task-resume-master/run-task.sh C:/Users/solos/my_ai_projects/platform-ssh-master/
cp C:/Users/solos/my_ai_projects/run-task-resume-master/run-task-batch.sh C:/Users/solos/my_ai_projects/platform-ssh-master/
chmod +x C:/Users/solos/my_ai_projects/platform-ssh-master/run-task.sh
chmod +x C:/Users/solos/my_ai_projects/platform-ssh-master/run-task-batch.sh
```

## Acceptance Criteria
- [ ] `run-task.sh` exists in master repo
- [ ] `run-task-batch.sh` exists in master repo
