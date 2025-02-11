from examples.api.auth.auth import get_cred
from adminconsult.api.customer import Customer, CustomerList

admin_cred = get_cred()


# Get one customer
admin_customer = Customer(admin_cred)
print(admin_customer.name)
admin_customer.get(id=9580)
print(admin_customer.name)
print(admin_customer.date_of_birth)
print(admin_customer.to_json())

# Get customer list
admin_customers = CustomerList(admin_cred)
admin_customers.get(max_results=750)
print(admin_customers.count)

# Get filtered customer list
admin_customers.get(max_results=750, gt__customer_id=8620, eq__is_active=False)

# Print first element of customer list
print(admin_customers[0].to_json())
print('\'{}\''.format(admin_customers[0]))

# Print logs
admin_cred.print_logs()
