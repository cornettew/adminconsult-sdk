import os
import json

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.productuse import ProductUse, ProductUseList

def test_get_product_use(client_credentials: ClientCredentials):

    product_uses = ProductUseList(client_credentials)
    product_uses.get(max_results=1250)

    if product_uses.count > 0:
        product_uses[0].refresh()
        product_use_id = product_uses[0].product_use_id

        product_use = ProductUse(client_credentials)
        product_use.get(product_use_id)
        assert product_uses[0] == product_use
    else:
        # No product_uses found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

def test_create_product_use(client_credentials: ClientCredentials):

    product_use = ProductUse(client_credentials)

    # Read and set product_use data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'productuse', 'data', 'new_product_use.json'), mode='r', encoding='utf-8') as f:
        product_use_details: dict = json.load(f)

    for k, v in product_use_details.items():
        setattr(product_use, k, v)
    
    product_use.create()

    # Get new product_use and veriry data
    product_use_new = ProductUse(client_credentials)
    product_use_new.get(product_use.product_use_id)
    
    assert product_use_details == {k: v for k, v in product_use_new.to_json().items() if k in product_use_details.keys()}


def test_update_product_use(client_credentials: ClientCredentials):
    '''
    Create product_use, update field-by-field and compare on each update.
    Test if no other fields are implicitly modified when updating one specific field.
    '''
    admin_product_use = ProductUse(client_credentials)

    # Read and set new_product_use data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'productuse', 'data', 'new_product_use.json'), mode='r', encoding='utf-8') as f:
        product_use_details = json.load(f)

    for k, v in product_use_details.items():
        setattr(admin_product_use, k, v)
    
    admin_product_use.create()
    admin_product_use.refresh()

    # Read and set customer data to update
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'productuse', 'data', 'updated_product_use.json'), mode='r', encoding='utf-8') as f:
        product_use_update_details = json.load(f)

    for k, new_value in product_use_update_details.items():
        # Store the to-be situation for comparison
        product_use_details_post = admin_product_use.to_json()
        product_use_details_post[k] = new_value
        del product_use_details_post['customer_id']; del product_use_details_post['product_price']

        # Write to Admin Consult
        admin_product_use.update(**{k: new_value})
        admin_product_use.refresh()

        assert product_use_details_post == {k: v for k, v in admin_product_use.to_json().items() if k in product_use_details_post.keys()}

def test_invoice_product_use(client_credentials: ClientCredentials):

    product_use = ProductUse(client_credentials)

    # Read and set product_use data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'productuse', 'data', 'new_product_use.json'), mode='r', encoding='utf-8') as f:
        product_use_details: dict = json.load(f)

    for k, v in product_use_details.items():
        setattr(product_use, k, v)
    
    product_use.create()

    # Get new product_use and veriry data
    product_use_new = ProductUse(client_credentials)
    product_use_new.get(product_use.product_use_id)

    product_use_new.set_invoiced()
    product_use_details['invoice_id'] = -1
    
    assert product_use_details == {k: v for k, v in product_use_new.to_json().items() if k in product_use_details.keys()}

    product_use_new.clear_invoiced()
    product_use_details['invoice_id'] = None
    
    assert product_use_details == {k: v for k, v in product_use_new.to_json().items() if k in product_use_details.keys()}

    
def test_delete_product_use(client_credentials: ClientCredentials):

    product_use = ProductUse(client_credentials)

    # Read and set product_use data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'productuse', 'data', 'new_product_use.json'), mode='r', encoding='utf-8') as f:
        product_use_details: dict = json.load(f)

    for k, v in product_use_details.items():
        setattr(product_use, k, v)
    
    product_use.create()

    # Get new product_use and veriry data
    product_use_new = ProductUse(client_credentials)
    product_use_new.get(product_use.product_use_id)

    product_use_new.delete()
    