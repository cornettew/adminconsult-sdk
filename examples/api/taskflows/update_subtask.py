from examples.api.auth.auth import get_cred
from datetime import datetime
from adminconsult.api.taskflow import TaskFlowDataList

admin_cred = get_cred()


admin_taskflowdata_304 = TaskFlowDataList(admin_cred, 304)
admin_taskflowdata_304.get(date_from=datetime(2023, 1, 1), date_until=datetime(2023, 12, 31), eq__project_id=11458)

print('{} taskflows selected'.format(admin_taskflowdata_304.count))

admin_taskflowdata_304[0].update_subtask(subtask_id=8, value=datetime(2023, 10, 15), employee_id=182)

admin_cred.print_logs()
