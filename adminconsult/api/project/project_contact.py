from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ProjectContact(Entity):

    contact = None
    contact_email = None
    contact_id: int = None
    contact_language = None
    contact_mobile = None
    contact_phone = None
    contact_title = None
    is_active = None
    is_invoice_contact = None
    project_contact_id: int = None
    project_id: int = None
    receives_newsletter = None
    
    _property_mapping = dict({
        "contact": {
            "GET": "Contact",
            "POST": None,
            "PUT": None
        },
        "contact_email": {
            "GET": "ContactEmail",
            "POST": None,
            "PUT": None
        },
        "contact_id": {
            "GET": "ContactId",
            "POST": "ContactId",
            "PUT": None
        },
        "contact_language": {
            "GET": "ContactLanguage",
            "POST": None,
            "PUT": None
        },
        "contact_mobile": {
            "GET": "ContactMobile",
            "POST": None,
            "PUT": None
        },
        "contact_phone": {
            "GET": "ContactPhone",
            "POST": None,
            "PUT": None
        },
        "contact_title": {
            "GET": "ContactTitle",
            "POST": None,
            "PUT": None
        },
        "is_active": {
            "GET": "IsActive",
            "POST": None,
            "PUT": None
        },
        "is_invoice_contact": {
            "GET": "IsInvoiceContact",
            "POST": "IsInvoiceContact",
            "PUT": None
        },
        "project_contact_id": {
            "GET": "ProjectContactId",
            "POST": None,
            "PUT": None
        },
        "project_id": {
            "GET": "ProjectId",
            "POST": "ProjectId",
            "PUT": None
        },
        "receives_newsletter": {
            "GET": "ReceivesNewsletter",
            "POST": None,
            "PUT": None
        }
    })

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='projectcontacts', 
                         primary_property='project_contact_id', 
                         payload=payload,
                         endpoint_parent='projects',
                         parent_id_property='project_id',
                         endpoint_suffix='projectcontacts',
                         child_id_property='project_contact_id')

    #IMPROV# Overriding _get_entity() because there is no /api/v1/projects/{id}/projectcontacts/{id} endpoint
    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}?Filter=ProjectContactId eq {}'.format(self._endpoint, id))

        return object[0]

    #IMPROV# It is not possible to update a linked contact to a project via the API
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint. '.format(self._endpoint))

class ProjectContactList(EntityCollection):

    _collection: list[ProjectContact]

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        self._collection = []

        super().__init__(client_credentials=client_credentials, endpoint='projectcontacts', payload=payload)
    
    def __iter__(self) -> Iterator[ProjectContact]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ProjectContact:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, **value_filters):

        super().get(max_results=max_results, **value_filters)

    def _add(self, payload):
        self._collection += [ProjectContact(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = ProjectContact(self._client_credentials)._allowed_get_parameters()