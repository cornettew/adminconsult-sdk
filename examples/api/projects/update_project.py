from examples.api.auth.auth import get_cred
from datetime import datetime, timedelta
from adminconsult.api.project import Project
from adminconsult.api.admin import Change, ChangeList

admin_cred = get_cred()

project = Project(admin_cred)
project.get(id=44952)
print(project.project_description)

project.update(project_description='test4')
project.update(department_id=12)


changes = ChangeList(admin_cred, on_technical_max='ignore')
changes.get(ge__date_action=datetime.now()-timedelta(minutes=5), eq__db_user='Hermes', limit_last_logs=1000)

print(changes.to_dataframe())
print('{} changes'.format(changes.count))
