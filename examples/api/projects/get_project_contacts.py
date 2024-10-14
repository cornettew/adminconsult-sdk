from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectContact, ProjectContactList

admin_cred = get_cred()

project_contacts = ProjectContactList(admin_cred)
project_contacts.get(in__project_id = [33493])
print(project_contacts.to_json())
