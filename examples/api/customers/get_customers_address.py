from examples.api.auth.auth import get_cred
from adminconsult.api.customer import CustomerAddress, CustomerAddressList

admin_cred = get_cred()

# Get one customer address
admin_customer_address = CustomerAddress(admin_cred)
print(admin_customer_address.street_1)
admin_customer_address.get(id=9580)
print(admin_customer_address.street_1)
print(admin_customer_address.city)
print(admin_customer_address.to_json())

# Get customer address list
admin_customer_addresss = CustomerAddressList(admin_cred)
admin_customer_addresss.get(max_results=750)
print(admin_customer_addresss.count)

# Get filtered customer address list
admin_customer_addresss.get(max_results=750, gt__customer_id=35620)

# Print first element of customer list
print(admin_customer_addresss[0].to_json())
print('\'{}\''.format(admin_customer_addresss[0]))

# Print logs
admin_cred.print_logs()
