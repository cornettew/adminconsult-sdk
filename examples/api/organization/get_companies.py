from examples.api.auth.auth import get_cred
from adminconsult.api.organization import Company, CompanyList

admin_cred = get_cred()

# Get all companies
admin_companies = CompanyList(admin_cred)
admin_companies.get()
print(f'Got {admin_companies.count} companies')
print(admin_companies.to_json())

# Get one company
admin_company = Company(admin_cred)
admin_company.get(1)
print(admin_company.country)


# Print logs
admin_cred.print_logs()
