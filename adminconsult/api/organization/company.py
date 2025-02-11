from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class Company(Entity):

    bank = None
    bic = None
    block_text = None
    city = None
    close_date = None
    company_id: int = None
    company_name = None
    country = None
    email = None
    fax = None
    http = None
    iban = None
    is_visible = None
    open_date = None
    rpr = None
    rsz = None
    street_1 = None
    street_2 = None
    tel = None
    vat = None
    venture_number = None
    zip_code = None

    _property_mapping = dict({
        'bank': {
            'GET': 'Bank',
            'POST': None,
            'PUT': None
        },

        'bic': {
            'GET': 'Bic',
            'POST': None,
            'PUT': None
        },

        'block_text': {
            'GET': 'BlockText',
            'POST': None,
            'PUT': None
        },

        'city': {
            'GET': 'City',
            'POST': None,
            'PUT': None
        },

        'close_date': {
            'GET': 'CloseDate',
            'POST': None,
            'PUT': None
        },

        'company_id': {
            'GET': 'CompanyId',
            'POST': None,
            'PUT': None
        },

        'company_name': {
            'GET': 'CompanyName',
            'POST': None,
            'PUT': None
        },

        'country': {
            'GET': 'Country',
            'POST': None,
            'PUT': None
        },

        'email': {
            'GET': 'Email',
            'POST': None,
            'PUT': None
        },

        'fax': {
            'GET': 'Fax',
            'POST': None,
            'PUT': None
        },

        'http': {
            'GET': 'Http',
            'POST': None,
            'PUT': None
        },

        'iban': {
            'GET': 'Iban',
            'POST': None,
            'PUT': None
        },

        'is_visible': {
            'GET': 'IsVisible',
            'POST': None,
            'PUT': None
        },

        'open_date': {
            'GET': 'OpenDate',
            'POST': None,
            'PUT': None
        },

        'rpr': {
            'GET': 'Rpr',
            'POST': None,
            'PUT': None
        },

        'rsz': {
            'GET': 'Rsz',
            'POST': None,
            'PUT': None
        },

        'street_1': {
            'GET': 'Street1',
            'POST': None,
            'PUT': None
        },

        'street_2': {
            'GET': 'Street2',
            'POST': None,
            'PUT': None
        },

        'tel': {
            'GET': 'Tel',
            'POST': None,
            'PUT': None
        },

        'vat': {
            'GET': 'Vat',
            'POST': None,
            'PUT': None
        },

        'venture_number': {
            'GET': 'VentureNumber',
            'POST': None,
            'PUT': None
        },

        'zip_code': {
            'GET': 'Zipcode',
            'POST': None,
            'PUT': None
        }
    })

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='companies', 
                         primary_property='company_id', 
                         payload=payload)
        
    def _get_entity(self, id: int):

        entities, _ = self._execute_request(method='get', endpoint=self._endpoint)
        entity = [entity for entity in entities if entity[self._property_mapping[self._primary_property]['GET']] == id][0]

        return entity
    


class CompanyList(EntityCollection):

    _collection: list[Company]

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        self._collection = []

        super().__init__(client_credentials=client_credentials, endpoint='companies', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[Company]:
        return super().__iter__()
    
    def __getitem__(self, item) -> Company:
        return super().__getitem__(item=item)

    def get(self, max_results=50, erase_former=True, **value_filters): 

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [Company(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = Company(self._client_credentials)._allowed_get_parameters()
