from examples.api.auth.auth import get_cred
from adminconsult.api.customer import CustomerLinkCustomer, CustomerLinkCustomerList
from datetime import datetime

admin_cred = get_cred()

customer_link = CustomerLinkCustomer(admin_cred)

customer_link.customer_id_pk = 12
customer_link.customer_id_fk = 501
customer_link.customer_link_type_id = 6
customer_link.stock_owned = 12
customer_link.stock_type = 1
# customer_link.begin_mandate = datetime(2024, 1, 1)
customer_link.end_mandate = datetime(2023, 12, 31)

customer_link.create()
