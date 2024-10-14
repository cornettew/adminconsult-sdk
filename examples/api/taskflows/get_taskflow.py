from examples.api.auth.auth import get_cred
from adminconsult.api.taskflow import TaskFlowSubtask, TaskFlowSubtaskList

admin_cred = get_cred()


admin_taskflow_subtasks = TaskFlowSubtaskList(admin_cred, task_id=209)
admin_taskflow_subtasks.get()

print('{} subtasks found'.format(admin_taskflow_subtasks.count))
print(admin_taskflow_subtasks.to_json())



admin_taskflow_subtask = TaskFlowSubtask(admin_cred, task_id=209)
admin_taskflow_subtask.get(1)

print(admin_taskflow_subtask.to_json())
