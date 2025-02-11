import os
import json
from datetime import datetime

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.customer import CustomerLinkCustomer, CustomerLinkCustomerList, Customer
from adminconsult.api.customer import List

def test_get_customer_link_customers(client_credentials: ClientCredentials):

    customer_links = CustomerLinkCustomerList(client_credentials=client_credentials)
    customer_links.get(max_results=100)

    if customer_links.count > 0:
        customer_link_id = customer_links[0].customer_link_customer_id

        customer_link = CustomerLinkCustomer(client_credentials=client_credentials)
        customer_link.get(customer_link_id)
        assert customer_link.customer_link_customer_id == customer_link_id
    else:
        # No customer links found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

def test_create_customer_link_customer(client_credentials: ClientCredentials):

    admin_customer_link_customer_contact = Customer(client_credentials)
    admin_customer_link_customer_company = Customer(client_credentials)

    # Read and set contact data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer_link_customer_contact.json'), mode='r', encoding='utf-8') as f:
        customer_link_customer_contact_details = json.load(f)

    for k, v in customer_link_customer_contact_details.items():
        setattr(admin_customer_link_customer_contact, k, v)
    
    admin_customer_link_customer_contact.create()

    # Read and set customer data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer_link_customer_company.json'), mode='r', encoding='utf-8') as f:
        customer_link_customer_company_details = json.load(f)

    for k, v in customer_link_customer_company_details.items():
        setattr(admin_customer_link_customer_company, k, v)
    
    admin_customer_link_customer_company.create()

    # Get function Id

    function_ids = List(client_credentials=client_credentials, list_id=10)

    function_ids.get()

    # Link contact with customer

    admin_customer_link_customer = CustomerLinkCustomer(client_credentials)
    customer_link_customer_details = {
        "customer_id_pk": admin_customer_link_customer_company.customer_id,
        "customer_id_fk": admin_customer_link_customer_contact.customer_id,
        "customer_link_type_id": 8,
        "function_id": function_ids.to_json()['values'][0]['item_id'],
    }

    for k, v in customer_link_customer_details.items():
        setattr(admin_customer_link_customer, k, v)

    admin_customer_link_customer.create()

    # Get new customer and veriry data
    admin_customer_link_customer_new = CustomerLinkCustomer(client_credentials)
    admin_customer_link_customer_new.get(admin_customer_link_customer.customer_link_customer_id)
    
    assert customer_link_customer_details == {k: v for k, v in admin_customer_link_customer_new.to_json().items() if k in customer_link_customer_details.keys()}

def test_update_customer_link_customer(client_credentials: ClientCredentials):

    admin_customer_link_customer_contact = Customer(client_credentials)
    admin_customer_link_customer_company = Customer(client_credentials)

    # Read and set contact data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer_link_customer_contact.json'), mode='r', encoding='utf-8') as f:
        customer_link_customer_contact_details = json.load(f)

    for k, v in customer_link_customer_contact_details.items():
        setattr(admin_customer_link_customer_contact, k, v)
    
    admin_customer_link_customer_contact.create()

    # Read and set customer data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer_link_customer_company.json'), mode='r', encoding='utf-8') as f:
        customer_link_customer_company_details = json.load(f)

    for k, v in customer_link_customer_company_details.items():
        setattr(admin_customer_link_customer_company, k, v)
    
    admin_customer_link_customer_company.create()

    # Link shareholder with customer

    admin_customer_link_customer = CustomerLinkCustomer(client_credentials)
    customer_link_customer_details = {
        "customer_id_pk": admin_customer_link_customer_company.customer_id,
        "customer_id_fk": admin_customer_link_customer_contact.customer_id,
        "customer_link_type_id": 6,
        "begin_mandate": None,
        "end_mandate": None,
        "stock_type": 1,
        "stock_owned": 100,
        "remark": "Test1",
    }

    for k, v in customer_link_customer_details.items():
        setattr(admin_customer_link_customer, k, v)
    
    admin_customer_link_customer.create()
    admin_customer_link_customer.refresh()

    # Stock type cannot be updated --> will create new shareholder
    update_details = {
        "begin_mandate": datetime(2020, 1, 1),
        "end_mandate": datetime(2022, 12, 31),
        "represented_by": admin_customer_link_customer_company.customer_id,
        "inv_contact": True,
        "stock_category": 597,
        "stock_voting": True,
        "stock_owned": 749.00,
        "remark": "Test2",
        "stock_voting_nr": 20,
        "child_parency": True,
        "child_of_giver": True
    }

    for k, new_value in update_details.items():
        # Store the to-be situation for comparison
        customer_link_customer_details_post = admin_customer_link_customer.to_json()
        customer_link_customer_details_post[k] = new_value
        if k == 'end_mandate':
            customer_link_customer_details_post['has_end_mandate'] = True

        # Write to Admin Consult
        admin_customer_link_customer.update(**{k: new_value})
        admin_customer_link_customer.refresh()

        assert customer_link_customer_details_post == {k: v for k, v in admin_customer_link_customer.to_json().items() if k in customer_link_customer_details_post.keys()}

def test_delete_customer_link_customer(client_credentials: ClientCredentials):

    admin_customer_link_customer_contact = Customer(client_credentials)
    admin_customer_link_customer_company = Customer(client_credentials)

    # Read and set contact data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer_link_customer_contact.json'), mode='r', encoding='utf-8') as f:
        customer_link_customer_contact_details = json.load(f)

    for k, v in customer_link_customer_contact_details.items():
        setattr(admin_customer_link_customer_contact, k, v)
    
    admin_customer_link_customer_contact.create()

    # Read and set customer data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer_link_customer_company.json'), mode='r', encoding='utf-8') as f:
        customer_link_customer_company_details = json.load(f)

    for k, v in customer_link_customer_company_details.items():
        setattr(admin_customer_link_customer_company, k, v)
    
    admin_customer_link_customer_company.create()

    # Link contact with customer

    admin_customer_link_customer = CustomerLinkCustomer(client_credentials)

    # Get function Id

    function_ids = List(client_credentials=client_credentials, list_id=10)

    function_ids.get()

    # Also added test for update/create director
    customer_link_customer_details = {
        "customer_id_pk": admin_customer_link_customer_company.customer_id,
        "customer_id_fk": admin_customer_link_customer_contact.customer_id,
        "customer_link_type_id": 4,
        "function_id": function_ids.to_json()['values'][0]['item_id'],
        "begin_mandate": "2023-06-14T00:00:00",
        "end_mandate": "2023-06-15T00:00:00",
        "public_remuneration": True,
        "statutory_mandate": True,
        "publication_nr": "123",
        "ext_representation": "testabc",
        "has_end_mandate": True,
    }

    for k, v in customer_link_customer_details.items():
        setattr(admin_customer_link_customer, k, v)

    admin_customer_link_customer.create()

    # Delete contact with customer
    admin_customer_link_customer.delete()

    all_links_customer = CustomerLinkCustomerList(client_credentials=client_credentials)
    all_links_customer.get(eq__customer_id_pk=admin_customer_link_customer_company.customer_id)

    assert admin_customer_link_customer.customer_link_customer_id not in {item.to_json()['customer_link_customer_id'] for item in all_links_customer._collection}