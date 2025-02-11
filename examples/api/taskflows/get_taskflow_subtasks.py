from examples.api.auth.auth import get_cred
from adminconsult.api.taskflow import TaskFlowSubtask, TaskFlowSubtaskList

admin_cred = get_cred()


subtasks = TaskFlowSubtaskList(admin_cred, task_id=292)
subtasks.get()

print(subtasks.to_json())

for st in subtasks:
    print(st.subtask_name)
    print(st.deadline_variance_unit)
    print(st.deadline_variance_nr)
