import os
import json

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.customer import CustomerAddress, CustomerAddressList

def test_get_customer_addresses(client_credentials: ClientCredentials):

    admin_customer_addresses = CustomerAddressList(client_credentials)
    admin_customer_addresses.get(max_results=1250)

    if admin_customer_addresses.count > 0:
        customer_address_id = admin_customer_addresses[0].customer_address_id

        admin_customer_address = CustomerAddress(client_credentials)
        admin_customer_address.get(customer_address_id)
        assert admin_customer_addresses[0] == admin_customer_address
    else:
        # No customers found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0
        
def test_create_customer_address(client_credentials: ClientCredentials):

    admin_customer_address = CustomerAddress(client_credentials)

    # Read and set customer data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer_address.json'), mode='r', encoding='utf-8') as f:
        customer_address_details = json.load(f)

    customer_address_details['customer_id'] = 14614

    for k, v in customer_address_details.items():
        setattr(admin_customer_address, k, v)
    
    admin_customer_address.create()

    # Get new customer and veriry data
    admin_customer_address_new = CustomerAddress(client_credentials)
    admin_customer_address_new.get(admin_customer_address.customer_address_id)
    
    #IMPROV# house_box and house_nr are not saved in Admin.  and k not in ['street_1', 'house_nr', 'house_box']
    ignored_fields = ['street_1', 'house_nr', 'house_box']
    assert {k: v for k, v in customer_address_details.items() if k not in ignored_fields} == {k: v for k, v in admin_customer_address.to_json().items() if k in customer_address_details.keys() and k not in ignored_fields}
    # assert customer_address_details == {k: v for k, v in admin_customer_address.to_json().items() if k in customer_address_details.keys()}
