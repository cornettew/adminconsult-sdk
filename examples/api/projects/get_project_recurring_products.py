from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectRecurringProduct, ProjectRecurringProductList

admin_cred = get_cred()


# Get one customer
project_recurring_product = ProjectRecurringProduct(admin_cred)
print(project_recurring_product.project_id)
project_recurring_product.get(id=85)
print(project_recurring_product.project_id)
print(project_recurring_product.to_json())


# Get customer list
project_recurring_products = ProjectRecurringProductList(admin_cred)
project_recurring_products.get(max_results=750)
print(project_recurring_products.count)


# Get filtered customer list
project_recurring_products.get(max_results=750, eq__project_id=2687)
print(project_recurring_products.count)

# Print first element of customer list
print(project_recurring_products[0].to_json())

# for pps in project_recurring_products:
#     pps.delete()

# Print logs
admin_cred.print_logs()