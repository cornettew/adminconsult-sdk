from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class CustomerEmailData(Entity):
    
    def __init__(self, client_credentials: ClientCredentials, customer_id, payload=None):

        self.customer_email_recipient_id = None
        self.customer_id = customer_id
        self.document_group = None
        self.document_group_id = None
        self.document_template = None
        self.document_template_id = None
        self.document_type = None
        self.document_type_description = None
        self.email = None
        self.to_recipient = None
        self.cc_recipient = None
        self.bcc_recipient = None

        property_mapping = dict({
            "customer_email_recipient_id": {
                "GET": "CustomerEmailRecipientId",
                "POST": None,
                "PUT": "CustomerEmailRecipientId"
            },
            "customer_id": {
                "GET": "CustomerId",
                "POST": "CustomerId",
                "PUT": None
            },
            "document_group": {
                "GET": "DocumentGroup",
                "POST": None,
                "PUT": None
            },
            "document_group_id": {
                "GET": "DocumentGroupId",
                "POST": "DocumentGroupId",
                "PUT": "DocumentGroupId"
            },
            "document_template": {
                "GET": "DocumentTemplate",
                "POST": None,
                "PUT": None
            },
            "document_template_id": {
                "GET": "DocumentTemplateId",
                "POST": "DocumentTemplateId",
                "PUT": "DocumentTemplateId"
            },
            "document_type": {
                "GET": "DocumentType",
                "POST": "DocumentType",
                "PUT": "DocumentType"
            },
            "document_type_description": {
                "GET": "DocumentTypeDescription",
                "POST": None,
                "PUT": None
            },
            "email": {
                "GET": "Email",
                "POST": "Email",
                "PUT": "Email"
            },
            "to_recipient": {
                "GET": "ToRecipient",
                "POST": "ToRecipient",
                "PUT": "ToRecipient"
            },
            "cc_recipient": {
                "GET": "CcRecipient",
                "POST": "CcRecipient",
                "PUT": "CcRecipient"
            },
            "bcc_recipient": {
                "GET": "BccRecipient",
                "POST": "BccRecipient",
                "PUT": "BccRecipient"
            }
        })

        super().__init__(client_credentials=client_credentials, 
                         endpoint='customers/{}/emaildata'.format(self.customer_id), 
                         primary_property='customer_email_recipient_id', 
                         property_mapping=property_mapping, 
                         payload=payload,
                         endpoint_parent='customers',
                         parent_id_property='customer_id',
                         endpoint_suffix='emaildata',
                         child_id_property='customer_email_recipient_id')


    #IMPROV# Overriding _get_entity() because there is no /api/v1/customer/{customerid}/emaildata/{id} endpoint
    def _get_entity(self, id: int):
        
        entities, _ = self._execute_request(method='get', endpoint='{}'.format(self._endpoint))
        entity = [entity for entity in entities if entity[self._property_mapping[self._primary_property]['GET']] == id][0]

        return entity

    def _update_entity(self):
        
        _ = self._execute_request(method='put', endpoint='{}/{}/{}'.format(self._endpoint_parent, getattr(self, self._parent_id_property), self._endpoint_suffix), payload=self._create_put_payload())
    

class CustomerEmailDataList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, customer_id, on_max='ignore', payload=None):

        self._customer_id = customer_id

        super().__init__(client_credentials=client_credentials, endpoint='customers/{}/emaildata'.format(self._customer_id), on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[CustomerEmailData]:
        return super().__iter__()
    
    def __getitem__(self, item) -> CustomerEmailData:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def _add(self, payload):
        self._collection += [CustomerEmailData(self._client_credentials, customer_id=self._customer_id, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = CustomerEmailData(self._client_credentials, customer_id=self._customer_id)._allowed_get_parameters()
