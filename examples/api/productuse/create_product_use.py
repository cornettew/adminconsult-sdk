from examples.api.auth.auth import get_cred
from adminconsult.api.productuse import ProductUse
from datetime import datetime

admin_cred = get_cred()

# Create Customer object
product_use = ProductUse(admin_cred)
product_use.date_product_use = datetime.now()
product_use.internal_remarks = 'test api'
# product_use.invoicable = True
product_use.period = 37
product_use.person_id = 182
product_use.product_id = 166
product_use.product_number = 5
product_use.project_id = 1115
product_use.remarks = 'invoice text'

# Commit the customer data to Admin Consult
product_use.create()

# Print newly created recurring project
print(product_use.product_use_id)
print(product_use.invoicable)


product_use.update(remarks='updated text')
product_use.update(project_id=1123)

product_use.set_invoiced()

product_use.clear_invoiced()

product_use.delete()

# Print newly created recurring project
print(product_use.to_json())

product_use.print_logs()
