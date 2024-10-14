from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class Company(Entity):

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        self.bank = None
        self.bic = None
        self.block_text = None
        self.city = None
        self.close_date = None
        self.company_id = None
        self.company_name = None
        self.country = None
        self.email = None
        self.fax = None
        self.http = None
        self.iban = None
        self.is_visible = None
        self.open_date = None
        self.rpr = None
        self.rsz = None
        self.street_1 = None
        self.street_2 = None
        self.tel = None
        self.vat = None
        self.venture_number = None
        self.zip_code = None

        property_mapping = dict({
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

        super().__init__(client_credentials=client_credentials, endpoint='companies', primary_property='company_id', property_mapping=property_mapping, payload=payload)
                                                                                

        
    def _get_entity(self, id: int):

        entities, _ = self._execute_request(method='get', endpoint=self._endpoint)
        entity = [entity for entity in entities if entity[self._property_mapping[self._primary_property]['GET']] == id][0]

        return entity
    


class CompanyList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        # Set collection element type for autocompletion purposes
        self._collection = [Company]

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
