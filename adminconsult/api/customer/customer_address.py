from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

from adminconsult.api.lists import Countries

class CustomerAddress(Entity):
        
    address_id: int = None
    city = None
    _country_code = None
    _country_id: int = None
    _country_name = None
    customer_address_id: int = None
    customer_id: int = None
    exploitation_address = None
    house_box = None
    house_nr = None
    invoice_address = None
    postal_address = None
    registered_office = None
    street_1 = None
    street_2 = None
    street_name = None
    zip_code = None

    _property_mapping = dict({
        'address_id': {
            'GET': 'AddressId',
            'POST': None,
            'PUT': None
        },
        'city': {
            'GET': 'City',
            'POST': 'City',
            'PUT': 'City'
        },
        'country_code': {
            'GET': 'CountryCode',
            'POST': None,
            'PUT': None
        },
        'country_id': {
            'GET': 'CountryId',
            'POST': 'CountryId',
            'PUT': 'CountryId'
        },
        'country_name': {
            'GET': None,
            'POST': None,
            'PUT': None
        },
        'customer_address_id': {
            'GET': 'CustomerAddressId',
            'POST': None,
            'PUT': None
        },
        'customer_id': {
            'GET': 'CustomerId',
            'POST': None,
            'PUT': None
        },
        'exploitation_address': {
            'GET': 'ExploitationAddress',
            'POST': 'ExploitationAddress',
            'PUT': 'ExploitationAddress'
        },
        'house_box': {
            'GET': 'HouseBox',
            'POST': 'HouseBox',
            'PUT': 'HouseBox'
        },
        'house_nr': {
            'GET': 'HouseNr',
            'POST': 'HouseNr',
            'PUT': 'HouseNr'
        },
        'invoice_address': {
            'GET': 'InvoiceAddress',
            'POST': 'InvoiceAddress',
            'PUT': 'InvoiceAddress'
        },
        'postal_address': {
            'GET': 'PostalAddress',
            'POST': 'PostalAddress',
            'PUT': 'PostalAddress'
        },
        'registered_office': {
            'GET': 'RegisteredOffice',
            'POST': 'RegisteredOffice',
            'PUT': 'RegisteredOffice'
        },
        'street_1': {
            # Invert with streetname which doesn't contain housenr./box
            'GET': 'StreetName',
            'POST': 'Street1',
            'PUT': 'Street1'
        },
        'street_2': {
            'GET': 'Street2',
            'POST': 'Street2',
            'PUT': 'Street2'
        },
        'street_name': {
            # Invert with street_1 which contains housenr./box
            'GET': 'Street1',
            # Technically allowed to post but blocked to not confuse with expanded fiels street1, street2, housenr., ...
            'POST': None,
            'PUT': None
        },
        'zip_code': {
            'GET': 'ZipCode',
            'POST': 'ZipCode',
            'PUT': 'ZipCode'
        }
    })

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='customeraddresses', 
                         primary_property='customer_address_id', 
                         payload=payload,
                         endpoint_parent='customers',
                         parent_id_property='customer_id',
                         endpoint_suffix='addresses',
                         child_id_property='address_id')
    @property
    def country_id(self):
        return self._country_id
    
    @country_id.setter
    def country_id(self, country_id):

        countries = Countries(self._client_credentials)
        if isinstance(country_id, int) and country_id != 0:
            self._country_code = countries.get_country_code(country_id)
            self._country_name = countries.get_country_name(country_id)

        self._country_id = country_id
        
    @property
    def country_code(self):
        return self._country_code
    
    @country_code.setter
    def country_code(self, country_code):

        if country_code:
            countries = Countries(self._client_credentials)
            self._country_id = countries.get_country_id(country_code=country_code)
            self._country_name = countries.get_country_name(self._country_id)

        self._country_code = country_code
        
    @property
    def country_name(self):
        return self._country_name
    
    @country_name.setter
    def country_name(self, country_name):
        countries = Countries(self._client_credentials)
        self._country_id = countries.get_country_id(country_name=country_name)
        self._country_code = countries.get_country_code(self._country_id)

        self._country_name = country_name

    def _create_put_payload(self):
        self.street_1 = '{} {}'.format(str(self.street_1 or '') , '{}/{}'.format(str(self.house_nr or ''), str(self.house_box or '')).strip('/')).strip(' ')
        return super()._create_put_payload()

    #IMPROV# Overriding _get_entity() because there is no /api/v1/customeraddress/{id} endpoint
    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}?Filter=CustomerAddressId eq {}'.format(self._endpoint, id))

        return object[0]
    

class CustomerAddressList(EntityCollection):

    _collection: list[CustomerAddress]

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        self._collection = []

        super().__init__(client_credentials=client_credentials, endpoint='customeraddresses', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[CustomerAddress]:
        return super().__iter__()
    
    def __getitem__(self, item) -> CustomerAddress:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True, **value_filters):

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [CustomerAddress(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = CustomerAddress(self._client_credentials)._allowed_get_parameters()