from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectEmployee, ProjectEmployeeList

admin_cred = get_cred()

project_employee = ProjectEmployee(admin_cred)

project_employee.project_id = 50
project_employee.employee_profile_id = 1 
project_employee.employee_id = 1
project_employee.is_taskflow_employee = True
project_employee.is_active = True

project_employee.create()
