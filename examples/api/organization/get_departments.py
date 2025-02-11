from examples.api.auth.auth import get_cred
from adminconsult.api.organization import Department, DepartmentList

admin_cred = get_cred()

# Get one department
admin_department = Department(admin_cred, company_id=10)
admin_department.get(id=11)
print(admin_department.to_json())


# Get Department list
admin_departments = DepartmentList(admin_cred, company_id=10)
admin_departments.get()

print(admin_departments.to_dataframe())

# Print logs
admin_cred.print_logs()
