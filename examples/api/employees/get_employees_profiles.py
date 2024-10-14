from examples.api.auth.auth import get_cred
from adminconsult.api.hrm import EmployeeProfile, EmployeeProfileList

admin_cred = get_cred()


# Get employee list
admin_employee_profiles = EmployeeProfileList(admin_cred)
admin_employee_profiles.get()
print(admin_employee_profiles)
print(admin_employee_profiles.to_json())
print(f'Found {admin_employee_profiles.count} profiles')

# Get one customer
admin_employee_profile = EmployeeProfile(admin_cred)
print(admin_employee_profile.profile_name)
admin_employee_profile.get(id=15)
print(admin_employee_profile.profile_name)
print(admin_employee_profile.to_json())
