from examples.api.auth.auth import get_cred
from adminconsult.api.taskflow import TaskFlowData, TaskFlowDataList
from datetime import datetime

admin_cred = get_cred()

admin_taskflowdata_244 = TaskFlowData(admin_cred, 244)
admin_taskflowdata_244.get(11)
print(admin_taskflowdata_244.to_json())

admin_taskflowdata_244_list = TaskFlowDataList(admin_cred, 244)
admin_taskflowdata_244_list.get(date_from=datetime(2023, 1, 1), date_until=datetime(2023, 12, 31), eq__company_id=4)

print('{} taskflows selected'.format(admin_taskflowdata_244_list.count))

# Print first element
admin_taskflowdata_244 = admin_taskflowdata_244_list[0]
print(admin_taskflowdata_244.deadline)
print(admin_taskflowdata_244.deadline.month)
print(admin_taskflowdata_244.deadline.day)
print(admin_taskflowdata_244.to_json())
print(admin_taskflowdata_244.get_subtask_column_name(5))

for st in admin_taskflowdata_244_list:
    print(st.customer_id)
