# Copy master repo to test repo

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
Create a fresh copy of the master repo as the test workspace:

```bash
cp -r C:/Users/solos/my_ai_projects/platform-ssh-master C:/Users/solos/my_ai_projects/platform-ssh-test
```

## Acceptance Criteria
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-test/` exists
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-test/CLAUDE.md` exists
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-test/framework/_reference/ssh_interface.py` exists
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-test/run-task.sh` exists
