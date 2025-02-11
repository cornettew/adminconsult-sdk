from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectEmployee, ProjectEmployeeList

admin_cred = get_cred()

project_employees = ProjectEmployeeList(admin_cred)
project_employees.get(eq__project_id=12854)

for project_employee in project_employees:
    print(project_employee.employee)

    project_employee.update(employee_id=149)
    print(project_employee.employee)
    
    print(project_employee.to_json())
