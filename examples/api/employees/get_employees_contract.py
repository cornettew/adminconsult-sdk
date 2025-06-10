from examples.api.auth.auth import get_cred
from adminconsult.api.hrm import EmployeeContract

admin_cred = get_cred()


# Get employee list
admin_employee_contract = EmployeeContract(admin_cred)
admin_employee_contract.get(182)
print(admin_employee_contract.to_json())
