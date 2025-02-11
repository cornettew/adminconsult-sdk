from examples.api.auth.auth import get_cred
from adminconsult.api.project import Project, ProjectList
from adminconsult.api.hrm import Employee, EmployeeList

admin_cred = get_cred()

customer_id = 501
project_type_id = 844

project = ProjectList(admin_cred)

project.get(eq__customer_id = customer_id, eq__project_type_id = project_type_id)

if len(project.to_json()) == 1:
    obtained_employee = EmployeeList(admin_cred)
    obtained_employee.get(eq__employee_id = project[0].project_manager_id)
    print(obtained_employee[0].work_email)
elif len(project.to_json()) > 1:
    raise LookupError("More than one project found.")
else:
    raise LookupError("No projects found.")
