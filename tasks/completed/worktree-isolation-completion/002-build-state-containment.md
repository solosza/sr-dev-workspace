# Task 002: State Containment — Routed Agents Never Write Parent State
**Type:** BUILD | **Gates:** WI-02
## Action
Audit run-task.sh (state pre-init + all state write paths) and ensure that when KERNEL_AGENT_ID is set, EVERY workflow/session write routes to agent-{id}-*.json and the PARENT sr_dev_workflow.json / session_state.json are never touched.
## Spec
READ run-task.sh state pre-init + anchor.md State File Routing first. For KERNEL_AGENT_ID set: task_folder, total_tasks, anchored, completed_tasks, current_task, actions log — ALL route to agent-{id} files. Find any residual write to the parent sr_dev_workflow.json/session_state.json (the `anchored` flag is the critical one — a routed agent flipping the parent's anchored:false is what blocked the interactive session repeatedly) and route it. Do NOT change the non-routed (agent_id null) path — the interactive session still owns the parent files. State writes Python/Write only.
## Acceptance
When KERNEL_AGENT_ID is set, zero writes to parent sr_dev_workflow.json/session_state.json; all state routes to agent-{id}. Non-routed path unchanged.
