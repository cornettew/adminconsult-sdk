from examples.api.auth.auth import get_cred
from adminconsult.api.extrafield import ExtraData, ExtraDataList

admin_cred = get_cred()

extra_data = ExtraData(admin_cred, table_id=104, foreign_key=45921)
print(extra_data.record_id)
extra_data.get(1)
print(extra_data.record_id)

for label, subtask in extra_data._fields.items():
    print('{} - {}'.format(label, subtask.value))

    

extra_data_list = ExtraDataList(admin_cred, table_id=104)
extra_data_list.get()

print(extra_data_list.count)

for extra_data in extra_data_list[:3]:

    for label, subtask in extra_data._fields.items():
        print('{} - {}'.format(label, subtask.value))
        