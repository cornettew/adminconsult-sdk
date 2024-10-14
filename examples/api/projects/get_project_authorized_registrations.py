from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectAuthorizedRegistrationList

admin_cred = get_cred()


# Get authorized registrations for one project
project_authorized_registrations = ProjectAuthorizedRegistrationList(admin_cred)
project_authorized_registrations.get(eq__project_id=781)

print('{} lines'.format(project_authorized_registrations.count))
print(project_authorized_registrations.to_json())

# Print logs
admin_cred.print_logs()
