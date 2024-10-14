from examples.api.auth.auth import get_cred
from adminconsult.api.customer import CustomerLinkCustomer, CustomerLinkCustomerList

admin_cred = get_cred()

shareholders = CustomerLinkCustomerList(client_credentials=admin_cred)
shareholders.get(eq__customer_id_pk = 12, eq__customer_link_type_id = 6)
print(shareholders.count)

shareholder = shareholders[0]
shareholder.delete()
