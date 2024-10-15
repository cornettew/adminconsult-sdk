import os
import json
from datetime import datetime

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.customer import Customer, Private

def test_private_customer(client_credentials: ClientCredentials):

    customer = Customer(client_credentials)
    
    # Read and set contact data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer_link_customer_contact.json'), mode='r', encoding='utf-8') as f:
        customer_details = json.load(f)

    for k, v in customer_details.items():
        setattr(customer, k, v)
    
    customer.create()

    customer_private = Private(client_credentials)
    
    # Read and set contact data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'private.json'), mode='r', encoding='utf-8') as f:
        customer_private_details = json.load(f)

    for k, v in customer_private_details.items():
        if k in customer_private._datetime_properties: 
            customer_private_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
        setattr(customer_private, k, v)

    customer_private.customer_id = customer.customer_id
    customer_private.create()

    assert customer_private_details == {k: v for k, v in customer_private.to_json().items() if k in customer_private_details.keys()}

