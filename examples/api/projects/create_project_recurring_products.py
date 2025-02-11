from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectRecurringProduct
from datetime import datetime

admin_cred = get_cred()


# Create Customer object
project_recurring_product = ProjectRecurringProduct(admin_cred)
project_recurring_product.invoice_text = 'test'
project_recurring_product.person_id = 182
project_recurring_product.planning_stop = datetime(2023, 12, 31)
project_recurring_product.product_id = 95
project_recurring_product.project_id = 49867
project_recurring_product.quantity = 5
project_recurring_product.schedule_abbr_nr = 1
project_recurring_product.schedule_abbr_unit = 'j'
project_recurring_product.schedule_date = datetime(2023, 5, 1)
project_recurring_product.text_id = 929
project_recurring_product.text_type = 0

# Commit the customer data to Admin Consult
project_recurring_product.create()

# Print newly created recurring project
print(project_recurring_product.project_recurring_product_id)

project_recurring_product.delete()

# Print newly created recurring project
print(project_recurring_product.to_json())

project_recurring_product.print_logs()
