from examples.api.auth.auth import get_cred
from datetime import datetime
from adminconsult.api.taskflow import TaskFlowPlanned

admin_cred = get_cred()


taskflow_planning = TaskFlowPlanned(admin_cred)

taskflow_planning.project_id = 49809
taskflow_planning.task_id = 377
taskflow_planning.schedule_id = 0
taskflow_planning.recurring_deviation_unit = 'a'
taskflow_planning.recurring_deviation_nr = 1
taskflow_planning.one_time_date = datetime(2024, 10, 5)

taskflow_planning.create()

print(taskflow_planning.to_json())

taskflow_planning.delete()

print(taskflow_planning.to_json())

admin_cred.print_logs()
