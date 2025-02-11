from examples.api.auth.auth import get_cred
from adminconsult.api.hrm import Employee, EmployeeList

admin_cred = get_cred()


# Get employee list
admin_employees = EmployeeList(admin_cred)
admin_employees.get(max_results=120)
print(admin_employees.to_json()[:2])
print(admin_employees.count)

# Get one employee
admin_employee = Employee(admin_cred)
print(admin_employee.short_name)
admin_employee.get(id=43)
print(admin_employee.short_name)
print(admin_employee.is_hrm)
print(admin_employee.to_json())
