from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectAuthorizedProductList

admin_cred = get_cred()


# Get authorized products for one project
project_authorized_products = ProjectAuthorizedProductList(admin_cred)
project_authorized_products.get(eq__project_id=15000)

print('{} lines'.format(project_authorized_products.count))
print(project_authorized_products.to_json())

# Print logs
admin_cred.print_logs()
