from examples.api.auth.auth import get_cred
from adminconsult.api.customer import Customer

admin_cred = get_cred()


# Create Customer object
admin_customer = Customer(admin_cred)
admin_customer.is_company = False
admin_customer.customer_crm_type = 8
admin_customer.title = 'Dhr.'
admin_customer.language = 'NL'
admin_customer.name = 'Cornette'
admin_customer.first_name = 'Ward'
admin_customer.street_1 = 'Dorpstraat'
admin_customer.zip_code = 8500
admin_customer.city = 'Kortrijk'
admin_customer.country_code = 'FR'

# Commit the customer data to Admin Consult
admin_customer.create()

# Print newly created customer°id
print(admin_customer.customer_id)

admin_customer.print_logs()
