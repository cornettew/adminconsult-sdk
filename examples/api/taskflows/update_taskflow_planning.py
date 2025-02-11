from examples.api.auth.auth import get_cred
from datetime import datetime, timedelta
from adminconsult.api.taskflow import TaskFlowPlanned
from adminconsult.api.admin import Change, ChangeList

admin_cred = get_cred()


taskflow_planning = TaskFlowPlanned(admin_cred)
taskflow_planning.get(162485)


print('Original value: {}'.format(taskflow_planning.planning_stop))
# taskflow_planning.update(planning_stop=datetime(2024, 4, 15))
taskflow_planning.update(task_id=6, planning_stop=datetime(2017, 1, 1))
print('Updated value: {}'.format(taskflow_planning.planning_stop))

changes = ChangeList(admin_cred, on_technical_max='ignore')
changes.get(ge__date_action=datetime.now()-timedelta(minutes=5), eq__db_user='Hermes', limit_last_logs=1000)

print(changes.to_dataframe())
print('{} changes'.format(changes.count))
