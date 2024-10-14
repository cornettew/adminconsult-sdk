from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectCustomer, ProjectCustomerList

admin_cred = get_cred()

project_customer = ProjectCustomer(admin_cred, project_id=43770)
print(project_customer.is_taskflow_customer)
print(project_customer.invoice_percentage)
project_customer.get(id=49945)
print(project_customer.is_taskflow_customer)
print(project_customer.invoice_percentage)
print(project_customer.to_json())


project_customers = ProjectCustomerList(admin_cred, project_id=43770)
project_customers.get()
print(project_customers.count)


# Print first element of customer list
print(project_customers.to_json())

# Print logs
admin_cred.print_logs()
