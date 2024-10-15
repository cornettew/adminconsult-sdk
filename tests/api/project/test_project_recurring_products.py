import os
import json
from time import sleep
from datetime import datetime, timedelta

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.project import ProjectRecurringProduct, ProjectRecurringProductList

def test_get_recurring_product(client_credentials: ClientCredentials):

    admin_project_recurring_product_list = ProjectRecurringProductList(client_credentials)
    admin_project_recurring_product_list.get(max_results=1250)

    if admin_project_recurring_product_list.count > 0:
        admin_project_recurring_product_list[0].refresh()
        project_recurring_product_id = admin_project_recurring_product_list[0].project_recurring_product_id

        admin_project_recurring_product = ProjectRecurringProduct(client_credentials)
        admin_project_recurring_product.get(project_recurring_product_id)
        assert admin_project_recurring_product_list[0] == admin_project_recurring_product
    else:
        # No project recurring product found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

def test_create_recurring_product(client_credentials: ClientCredentials):

    admin_project_recurring_product = ProjectRecurringProduct(client_credentials)

    # Read and set taskflow planned data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'project', 'data', 'new_recurring_product.json'), mode='r', encoding='utf-8') as f:
        admin_project_recurring_product_details: dict = json.load(f)

    for k, v in admin_project_recurring_product_details.items():
        if k in admin_project_recurring_product._datetime_properties: 
            admin_project_recurring_product_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
        setattr(admin_project_recurring_product, k, v)
    
    admin_project_recurring_product.create()

    # Get new taskflow planned and verify data
    admin_project_recurring_product_new = ProjectRecurringProduct(client_credentials)
    admin_project_recurring_product_new.get(admin_project_recurring_product.project_recurring_product_id)
    
    assert admin_project_recurring_product_details == {k: v for k, v in admin_project_recurring_product.to_json().items() if k in admin_project_recurring_product_details.keys()}


def test_update_recurring_product(client_credentials: ClientCredentials):
    '''
    Create recurring product, update field-by-field and compare on each update.
    Test if no other fields are implicitly modified when updating one specific field.
    '''

    admin_project_recurring_product = ProjectRecurringProduct(client_credentials)

    # Read and set recurring product data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'project', 'data', 'new_recurring_product.json'), mode='r', encoding='utf-8') as f:
        admin_project_recurring_product_details: dict = json.load(f)

    for k, v in admin_project_recurring_product_details.items():
        if k in admin_project_recurring_product._datetime_properties: 
            admin_project_recurring_product_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
        setattr(admin_project_recurring_product, k, v)
    
    admin_project_recurring_product.create()
    admin_project_recurring_product.refresh()

    # Read and set recurring product data to update
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'project', 'data', 'updated_recurring_product.json'), mode='r', encoding='utf-8') as f:
        recurring_product_update_details = json.load(f)
    for k, v in recurring_product_update_details.items():
        if k in admin_project_recurring_product._datetime_properties: 
            recurring_product_update_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')

    for k, new_value in recurring_product_update_details.items():
        # Store the to-be situation for comparison
        recurring_product_details_post = admin_project_recurring_product.to_json()
        recurring_product_details_post[k] = new_value

        # Write to Admin Consult
        admin_project_recurring_product.update(**{k: new_value})
        admin_project_recurring_product.refresh()

        assert recurring_product_details_post == {k: v for k, v in admin_project_recurring_product.to_json().items() if k in recurring_product_details_post.keys()}


def test_delete_recurring_product(client_credentials: ClientCredentials):
    '''
    Deactivate project recurring product
    '''
    admin_project_recurring_product = ProjectRecurringProduct(client_credentials)

    # Read and set recurring product data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'project', 'data', 'new_recurring_product.json'), mode='r', encoding='utf-8') as f:
        admin_project_recurring_product_details: dict = json.load(f)

    for k, v in admin_project_recurring_product_details.items():
        if k in admin_project_recurring_product._datetime_properties: 
            admin_project_recurring_product_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
        setattr(admin_project_recurring_product, k, v)
    
    admin_project_recurring_product.create()
    admin_project_recurring_product.refresh()

    admin_project_recurring_product.delete()

    assert admin_project_recurring_product.project_recurring_product_id is None
