from examples.api.auth.auth import get_cred
from adminconsult.api.taskflow import TaskFlowPlannedList

admin_cred = get_cred()


taskflow_planning_list = TaskFlowPlannedList(admin_cred)
taskflow_planning_list.get(eq__project_id=1062)

print('{} taskflows selected'.format(taskflow_planning_list.count))

# Print first element
print(taskflow_planning_list[0].to_json())
print(taskflow_planning_list[0].planning_start)
print(taskflow_planning_list[0].planning_stop)

# for planning in taskflow_planning_list:
#     planning.delete()

admin_cred.print_logs()
