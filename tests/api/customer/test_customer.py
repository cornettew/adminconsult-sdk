import os
import json
from time import sleep
from datetime import datetime, timedelta

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.customer import Customer, CustomerList
from adminconsult.api.customer import CustomerChanges

def test_get_customers(client_credentials: ClientCredentials):

    admin_customers = CustomerList(client_credentials)
    admin_customers.get(max_results=1250)

    if admin_customers.count > 0:
        admin_customers[0].refresh()
        customer_id = admin_customers[0].customer_id

        admin_customer = Customer(client_credentials)
        admin_customer.get(customer_id)
        assert admin_customers[0] == admin_customer
    else:
        # No customers found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

def test_create_customer(client_credentials: ClientCredentials):

    admin_customer = Customer(client_credentials)

    # Read and set customer data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer.json'), mode='r', encoding='utf-8') as f:
        customer_details = json.load(f)

    for k, v in customer_details.items():
        setattr(admin_customer, k, v)
    
    admin_customer.create()

    # Get new customer and veriry data
    admin_customer_new = Customer(client_credentials)
    admin_customer_new.get(admin_customer.customer_id)
    
    assert customer_details == {k: v for k, v in admin_customer_new.to_json().items() if k in customer_details.keys()}


def test_update_customer(client_credentials: ClientCredentials):
    '''
    Create customer, update field-by-field and compare on each update.
    Test if no other fields are implicitly modified when updating one specific field.
    '''
    admin_customer = Customer(client_credentials)

    # Read and set customer data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer.json'), mode='r', encoding='utf-8') as f:
        customer_details = json.load(f)

    for k, v in customer_details.items():
        setattr(admin_customer, k, v)
    
    admin_customer.create()
    admin_customer.refresh()

    # Read and set customer data to update
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'updated_customer.json'), mode='r', encoding='utf-8') as f:
        customer_update_details = json.load(f)

    for k, new_value in customer_update_details.items():
        # Store the to-be situation for comparison
        customer_details_post = admin_customer.to_json()
        customer_details_post[k] = new_value
        del customer_details_post['language_id']; del customer_details_post['title']

        # Write to Admin Consult
        admin_customer.update(**{k: new_value})
        admin_customer.refresh()

        assert customer_details_post == {k: v for k, v in admin_customer.to_json().items() if k in customer_details_post.keys()}

def test_transform_company_to_person(client_credentials: ClientCredentials):
    '''
    Create customer, update field-by-field and compare on each update
    '''
    admin_customer = Customer(client_credentials)

    # Read and set customer data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer.json'), mode='r', encoding='utf-8') as f:
        customer_details = json.load(f)

    for k, v in customer_details.items():
        setattr(admin_customer, k, v)
    
    admin_customer.create()
    admin_customer.refresh()

    customer_update_details = dict({'is_company': False,
                                    'first_name': 'Frans',
                                    'title': 'Mr.'})

    # Store the to-be situation for comparison
    customer_details_post = admin_customer.to_json()
    del customer_details_post['title_id']
    for k, new_value in customer_update_details.items():
        customer_details_post[k] = new_value
    customer_details_post['sex'] = 'O'

    # Write to Admin Consult
    admin_customer.update(**customer_update_details)
    admin_customer.refresh()

    assert customer_details_post == {k: v for k, v in admin_customer.to_json().items() if k in customer_details_post.keys()}


def test_deactivate_customer(client_credentials: ClientCredentials):
    '''
    Deactivate customer
    '''
    admin_customer = Customer(client_credentials)

    # Read and set customer data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer.json'), mode='r', encoding='utf-8') as f:
        customer_details = json.load(f)

    for k, v in customer_details.items():
        setattr(admin_customer, k, v)
    
    admin_customer.create()
    admin_customer.refresh()

    # Store the to-be situation for comparison
    customer_details_post = admin_customer.to_json()
    customer_details_post['is_active'] = False
    del customer_details_post['disabled_date']

    admin_customer.deactivate()
    admin_customer.refresh()

    assert customer_details_post == {k: v for k, v in admin_customer.to_json().items() if k in customer_details_post.keys()}


def test_customer_changes(client_credentials: ClientCredentials):

    admin_customer = Customer(client_credentials)

    # Read and set customer data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer.json'), mode='r', encoding='utf-8') as f:
        customer_details = json.load(f)

    for k, v in customer_details.items():
        setattr(admin_customer, k, v)
    
    date_from = datetime.now()

    admin_customer.create()

    # Get new customer and veriry data
    customer_changes = CustomerChanges(client_credentials)
    sleep(5); customer_changes.get(date_from=date_from, date_until=datetime.now()+timedelta(minutes=1))
    
    assert admin_customer.customer_id in [c.customer_id for c in customer_changes.inserts]