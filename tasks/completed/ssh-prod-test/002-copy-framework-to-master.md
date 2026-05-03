# Copy framework code to master repo

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
Copy the framework directory from the existing platform repo to the master:

```bash
cp -r C:/Users/solos/my_ai_projects/platform-ssh-verify/framework C:/Users/solos/my_ai_projects/platform-ssh-master/framework
```

Also copy top-level files:

```bash
cp C:/Users/solos/my_ai_projects/platform-ssh-verify/requirements.txt C:/Users/solos/my_ai_projects/platform-ssh-master/
cp C:/Users/solos/my_ai_projects/platform-ssh-verify/FRAMEWORK.md C:/Users/solos/my_ai_projects/platform-ssh-master/
cp C:/Users/solos/my_ai_projects/platform-ssh-verify/README.md C:/Users/solos/my_ai_projects/platform-ssh-master/
```

## Acceptance Criteria
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-master/framework/_reference/ssh_interface.py` exists
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-master/requirements.txt` exists
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-master/FRAMEWORK.md` exists
