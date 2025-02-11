from examples.api.auth.auth import get_cred
from datetime import datetime
from adminconsult.api.customer import CustomerChanges, CustomerLinkCustomerChanges, CustomerAddressChanges

admin_cred = get_cred()


date_from = datetime(2024, 5, 20, 8, 0, 0)
customer_changes = CustomerChanges(admin_cred, extra_tables=['CUSTOMER_ADRESS', 'CUSTOMER_EMAIL'])
customer_changes.get(ge__log_id=60347797, lt__log_id=60347999)

for updated_customer in customer_changes.inserts:
    print(updated_customer.customer_id)

for updated_customer in customer_changes.updates:
    print(updated_customer.name)

for delete_id in customer_changes.deletes:
    print(delete_id)
print(customer_changes.related_delete_ids)


## CLC

# clc_changes = CustomerLinkCustomerChanges(admin_cred)
# clc_changes.get(date_from=datetime(2023, 7, 12, 7, 0, 0), date_until=datetime.now())

# for new_clc in clc_changes.inserts:
#     print('Created: {}'.format(new_clc.customer_link_customer_id))

# for updated_clc in clc_changes.updates:
#     print('Updated: {}'.format(updated_clc.customer_link_customer_id))

# for delete_id in clc_changes.deletes:
#     print('Deleted: {}'.format(delete_id))



## ADDRESS

# ca_changes = CustomerAddressChanges(admin_cred)
# ca_changes.get(date_from=date_from, date_until=datetime.now())

# for new_ca in ca_changes.inserts:
#     print('Created: {}'.format(new_ca.customer_address_id))

# for new_ca in ca_changes.updates:
#     print('Updated: {}'.format(new_ca.customer_address_id))

# for delete_id in ca_changes.deletes:
#     print('Deleted: {}'.format(delete_id))

admin_cred.print_logs()
