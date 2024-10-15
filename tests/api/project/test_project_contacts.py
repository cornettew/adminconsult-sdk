import os
import json

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.project import ProjectContactList, ProjectContact, Project, ProjectList
from adminconsult.api.customer import Customer

def test_get_project_contacts(client_credentials: ClientCredentials):

    admin_project_contacts = ProjectContactList(client_credentials)
    admin_project_contacts.get(max_results=100)

    if admin_project_contacts.count > 0:
        project_contact_id = admin_project_contacts[0].project_contact_id

        admin_project_contact = ProjectContact(client_credentials)
        admin_project_contact.get(project_contact_id)
        assert admin_project_contacts[0] == admin_project_contact
    else:
        # No customers found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

def test_create_project_contact(client_credentials: ClientCredentials):

    # Read and set contact data

    admin_contact = Customer(client_credentials)
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'customer', 'data', 'new_customer_link_customer_contact.json'), mode='r', encoding='utf-8') as f:
        customer_contact_details = json.load(f)

    for k, v in customer_contact_details.items():
        setattr(admin_contact, k, v)
    
    admin_contact.create()

    # Get project
    admin_project = Project(client_credentials)
    admin_project.get(1)

    # Link created contact with obtained project
    admin_project_contact = ProjectContact(client_credentials)

    admin_project_contact_details = dict({
        'contact_id':admin_contact.customer_id,
        'is_invoice_contact':False,
        'project_id':admin_project.project_id
    })

    for k, v in admin_project_contact_details.items():
        setattr(admin_project_contact, k, v)   

    admin_project_contact.create()

    # Get new project contact and verify data
    admin_project_contact_new = ProjectContact(client_credentials)
    admin_project_contact_new.get(admin_project_contact.project_contact_id)
    
    assert admin_project_contact_details == {k: v for k, v in admin_project_contact_new.to_json().items() if k in admin_project_contact_details.keys()}