from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ProjectCustomer(Entity):
        
    co_contractor = None
    customer_id: int = None
    direct_debit = None
    invoice_annex_id: int = None
    invoice_percentage = None
    invoicing_address_id: int = None
    is_taskflow_customer = None
    need_invoice_annex = None
    project_customer_id: int = None
    project_id: int = None
    vat_excl_text_id: int = None
    vat_incl = None

    _property_mapping = dict({
        'co_contractor': {
            'GET': 'CoContractor',
            'POST': 'CoContractor',
            'PUT': 'CoContractor'
        },
        'customer_id': {
            'GET': 'CustomerId',
            'POST': 'CustomerId',
            'PUT': 'CustomerId'
        },
        'direct_debit': {
            'GET': 'DirectDebit',
            'POST': 'DirectDebit',
            'PUT': 'DirectDebit'
        },
        'invoice_annex_id': {
            'GET': 'InvoiceAnnexId',
            'POST': 'InvoiceAnnexId',
            'PUT': 'InvoiceAnnexId'
        },
        'invoice_percentage': {
            'GET': 'InvoicePercentage',
            'POST': 'InvoicePercentage',
            'PUT': 'InvoicePercentage'
        },
        'invoicing_address_id': {
            'GET': 'InvoicingAddressId',
            'POST': 'InvoicingAddressId',
            'PUT': 'InvoicingAddressId'
        },
        'is_taskflow_customer': {
            'GET': 'IsTaskflowCustomer',
            'POST': 'IsTaskflowCustomer',
            'PUT': 'IsTaskflowCustomer'
        },
        'need_invoice_annex': {
            'GET': 'NeedInvoiceAnnex',
            'POST': 'NeedInvoiceAnnex',
            'PUT': 'NeedInvoiceAnnex'
        },
        'project_customer_id': {
            'GET': 'ProjectCustomerId',
            'POST': None,
            'PUT': None
        },
        'project_id': {
            'GET': 'ProjectId',
            'POST': None,
            'PUT': None
        },
        'vat_excl_text_id': {
            'GET': 'VATExclTextId',
            'POST': 'VATExclTextId',
            'PUT': 'VATExclTextId'
        },
        'vat_incl': {
            'GET': 'VatIncl',
            'POST': 'VatIncl',
            'PUT': 'VatIncl'
        }
    })

    def __init__(self, client_credentials: ClientCredentials, project_id: int, payload=None):
        
        self.project_id = project_id
        
        super().__init__(client_credentials=client_credentials, 
                         endpoint='projects/{}/projectcustomers'.format(self.project_id), 
                         primary_property='project_customer_id', 
                         payload=payload,
                         endpoint_parent='projects',
                         parent_id_property='project_id',
                         endpoint_suffix='projectcustomers',
                         child_id_property='project_customer_id'
                         )

    #IMPROV# Overriding _get_entity() because there is no /api/v1/customeraddress/{id} endpoint
    def _get_entity(self, id: int):

        entities, _ = self._execute_request(method='get', endpoint=self._endpoint)
        entity = [entity for entity in entities if entity[self._property_mapping[self._primary_property]['GET']] == id][0]

        return entity

    def _create_entity(self):

        if not isinstance(getattr(self, self._parent_id_property), int):
            raise Exception('Must pass \'{}\' to which the new {} has to be linked. Got \'{}\' = \'{}\''.format(self._parent_id_property, type(self).__name__, self._parent_id_property, getattr(self, self._parent_id_property)))
        created_objects, _ = self._execute_request(method='post', endpoint='{}/{}/{}'.format(self._endpoint_parent, getattr(self, self._parent_id_property), self._endpoint_suffix), payload=self._create_post_payload())

        return [obj for obj in created_objects if obj.get('CustomerId') == self.customer_id][0]
    
class ProjectCustomerList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, project_id: int, payload=None):

        self._project_id = project_id

        # Set collection element type for autocompletion purposes
        self._collection = [ProjectCustomer]

        super().__init__(client_credentials=client_credentials, 
                         endpoint='projects/{}/projectcustomers'.format(self._project_id), 
                         payload=payload)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def __iter__(self) -> Iterator[ProjectCustomer]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ProjectCustomer:
        return super().__getitem__(item=item)

    def _add(self, payload):
        self._collection += [ProjectCustomer(self._client_credentials, project_id=self._project_id, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = ProjectCustomer(self._client_credentials, project_id=self._project_id)._allowed_get_parameters()
