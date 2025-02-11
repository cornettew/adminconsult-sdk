from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectCustomer

admin_cred = get_cred()


# Create ProjectCustomer object
project_customer = ProjectCustomer(admin_cred, project_id=49867)
project_customer.co_contractor = False
project_customer.customer_id = 14614
project_customer.direct_debit = False
project_customer.invoice_annex_id = None
project_customer.invoice_percentage = 25
# project_customer.invoicing_address_id = False
project_customer.is_taskflow_customer = False
project_customer.need_invoice_annex = False
project_customer.project_id = 49867
project_customer.vat_excl_text_id = None
project_customer.vat_incl = True


# Commit the project_customer data to Admin Consult
project_customer.create()

# Print newly created recurring project
print(project_customer.project_customer_id)

# Print newly created recurring project
print(project_customer.to_json())

project_customer.delete()

# Print newly created recurring project
print(project_customer.to_json())

project_customer.print_logs()
