# Create master repo directory

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
Create the master repo directory:

```bash
mkdir -p C:/Users/solos/my_ai_projects/platform-ssh-master
```

Initialize git:

```bash
git -C C:/Users/solos/my_ai_projects/platform-ssh-master init
```

## Acceptance Criteria
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-master/` exists
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-master/.git/` exists
