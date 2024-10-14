from examples.api.auth.auth import get_cred
from adminconsult.api.customer import CustomerLinkCustomer, CustomerLinkCustomerList
from datetime import datetime

admin_cred = get_cred()

shareholders = CustomerLinkCustomerList(client_credentials=admin_cred)
shareholders.get(eq__customer_id_pk=501, eq__customer_link_type_id=6)

shareholder = shareholders[0]
shareholder.update(begin_mandate=datetime(2024, 1, 1))
