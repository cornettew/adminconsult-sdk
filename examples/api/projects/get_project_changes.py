from examples.api.auth.auth import get_cred
from datetime import datetime
from adminconsult.api.project import ProjectChanges

admin_cred = get_cred()


project_changes = ProjectChanges(admin_cred)

project_changes.get(date_from=datetime(2024, 5, 11, 11, 30, 0), date_until=datetime.now())

for updated_project in project_changes.updates:
    print(updated_project.project_title)
    print(updated_project.customer_id)

for delete_id in project_changes.deletes:
    print(delete_id)

admin_cred.print_logs()