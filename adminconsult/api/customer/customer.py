from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

from .customer_address import CustomerAddressList
from adminconsult.api.lists import Titles, Countries, List

from datetime import datetime

class Customer(Entity):

    acc_code = None
    accountancy_software = None
    accountancy_software_label = None
    city = None
    commercial_name = None
    # Countries are validated for existance. Id and value are automatically translated using countries endpoint
    _country_code = None
    _country_id: int = None
    _country_name = None
    company_id: int = None
    creation_date = None
    cupboard_number = None
    curreny = None
    cust_code = None
    cust_kind = None
    customer_crm_type = None
    customer_group = None
    customer_group_label = None
    customer_id: int = None
    date_of_birth = None
    disabled_date = None
    distance = None
    email = None
    fax = None
    first_name = None
    holding = None
    home_page = None
    house_box = None
    house_nr = None
    is_active = None
    is_company = None
    # Languages are validated for existance. Id and value are automatically translated using list 19
    _language_id: int = None
    _language = None
    mobile = None
    nace_code = None
    name = None
    nationality = None
    newsletter = None
    phone = None
    phone2 = None
    place_of_birth = None
    reason_for_leaving = None
    registration_nr = None
    remarks = None
    rpr = None
    sector = None
    sector_id: int = None
    sex = None
    social_security_number = None
    street_1 = None
    street_2 = None
    # Titles are validated for existance. Id and value are automatically translated using list 2
    _title_id: int = None
    _title = None
    vat_nr = None
    zip_code = None

    _property_mapping = dict({
        'acc_code': {
            'GET': 'AccCode',
            'POST': 'AccCode',
            'PUT': 'AccCode'
        },
        'accountancy_software': {
            'GET': 'AccountancySoftware',
            'POST': None,
            'PUT': None
        },
        'accountancy_software_label': {
            'GET': 'AccountancySoftwareLabel',
            'POST': None,
            'PUT': None
        },
        'city': {
            'GET': None,
            'POST': 'City',
            'PUT': 'City'
        },
        'commercial_name': {
            'GET': 'CommercialName',
            'POST': 'CommercialName',
            'PUT': 'CommercialName'
        },
        'country_code': {
            'GET': None,
            'POST': 'CountryCode',
            'PUT': 'CountryCode'
        },
        'country_id': {
            'GET': None,
            'POST': None,
            'PUT': None
        },
        'country_name': {
            'GET': None,
            'POST': None,
            'PUT': None
        },
        'company_id': {
            'GET': 'CompanyId',
            'POST': None,
            'PUT': None
        },
        'creation_date': {
            'GET': 'CreationDate',
            'POST': None,
            # Removed this parameter via def _allowed_put_parameters()
            'PUT': 'CreationDate'
        },
        'cupboard_number': {
            'GET': 'CupboardNumber',
            'POST': 'CupboardNumber',
            'PUT': 'CupboardNumber'
        },
        'curreny': {
            'GET': 'Currency',
            'POST': None,
            'PUT': None
        },
        'cust_code': {
            'GET': 'CustCode',
            'POST': 'CustCode',
            'PUT': 'CustCode'
        },
        'cust_kind': {
            'GET': 'CustKind',
            'POST': None,
            'PUT': None
        },
        'customer_crm_type': {
            'GET': 'CustomerCrmType',
            'POST': 'CustomerCrmType',
            'PUT': 'CustomerCrmType'
        },
        'customer_group': {
            'GET': 'CustomerGroup',
            'POST': 'CustomerGroup',
            'PUT': 'CustomerGroup'
        },
        'customer_group_label': {
            'GET': 'CustomerGroupLabel',
            'POST': None,
            'PUT': None
        },
        'customer_id': {
            'GET': 'CustomerId',
            'POST': 'CustomerId',
            'PUT': 'CustomerId'
        },
        'date_of_birth': {
            'GET': 'DateOfBirth',
            'POST': None,
            'PUT': None
        },
        'disabled_date': {
            'GET': 'DisabledDate',
            'POST': None,
            'PUT': None
        },
        'distance': {
            'GET': 'Distance',
            'POST': None,
            'PUT': None
        },
        'email': {
            'GET': 'Email',
            'POST': 'Email',
            'PUT': 'Email'
        },
        'fax': {
            'GET': 'Fax',
            'POST': None,
            'PUT': None
        },
        'first_name': {
            'GET': 'Firstname',
            'POST': 'Firstname',
            'PUT': 'Firstname'
        },
        'holding': {
            'GET': 'Holding',
            'POST': None,
            'PUT': None
        },
        'home_page': {
            'GET': 'Homepage',
            'POST': 'Homepage',
            'PUT': 'Homepage'
        },
        'house_box': {
            'GET': None,
            'POST': 'Box',
            'PUT': 'Box'
        },
        'house_nr': {
            'GET': None,
            'POST': 'Nr',
            'PUT': 'Nr'
        },
        'is_active': {
            'GET': 'IsActive',
            'POST': None,
            'PUT': None
        },
        'is_company': {
            'GET': 'IsCompany',
            'POST': 'IsCompany',
            'PUT': 'IsCompany'
        },
        'language': {
            'GET': 'Language',
            'POST': 'Language',
            'PUT': 'Language'
        },
        'language_id': {
            'GET': None,
            'POST': None,
            'PUT': None
        },
        'mobile': {
            'GET': 'Mobile',
            'POST': 'Mobile',
            'PUT': 'Mobile'
        },
        'nace_code': {
            'GET': 'NaceCode',
            'POST': 'NaceCode',
            'PUT': 'NaceCode'
        },
        'name': {
            'GET': 'Name',
            'POST': 'Name',
            'PUT': 'Name'
        },
        'nationality': {
            'GET': 'Nationality',
            'POST': None,
            'PUT': None
        },
        'newsletter': {
            'GET': 'Newsletter',
            'POST': None,
            'PUT': None
        },
        'phone': {
            'GET': 'Phone',
            'POST': 'Phone',
            'PUT': 'Phone'
        },
        'phone2': {
            'GET': 'Phone2',
            'POST': None,
            'PUT': None
        },
        'place_of_birth': {
            'GET': 'PlaceOfBirth',
            'POST': None,
            'PUT': None
        },
        'reason_for_leaving': {
            'GET': 'ReasonForLeaving',
            'POST': None,
            'PUT': None
        },
        'registration_nr': {
            'GET': 'RegistrationNr',
            'POST': 'RegistrationNr',
            'PUT': 'RegistrationNr'
        },
        'remarks': {
            'GET': 'Remarks',
            'POST': 'Remarks',
            'PUT': 'Remarks'
        },
        'rpr': {
            'GET': 'RPR',
            'POST': 'RPR',
            'PUT': 'RPR'
        },
        'sector': {
            'GET': 'Sector',
            'POST': None,
            'PUT': None
        },
        'sector_id': {
            'GET': 'SectorId',
            'POST': None,
            'PUT': None
        },
        'sex': {
            'GET': 'Sex',
            'POST': None,
            'PUT': None
        },
        'social_security_number': {
            'GET': 'SocialSecurityNumber',
            'POST': 'SocialSecurityNumber',
            'PUT': 'SocialSecurityNumber'
        },
        'street_1': {
            'GET': None,
            'POST': 'Street1',
            'PUT': 'Street1'
        },
        'street_2': {
            'GET': None,
            'POST': 'Street2',
            'PUT': 'Street2'
        },
        # Title id is not available in the customers endpoints
        'title_id': {
            'GET': None,
            'POST': None,
            'PUT': None
        },
        'title': {
            'GET': 'Title',
            'POST': 'Title',
            'PUT': 'Title'
        },
        'vat_nr': {
            'GET': 'VATNr',
            'POST': 'VATNr',
            'PUT': 'VATNr'
        },
        'zip_code': {
            'GET': None,
            'POST': 'Zipcode',
            'PUT': 'Zipcode'
        }
    })

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='customers', 
                         primary_property='customer_id', 
                         datetime_properties=['date_of_birth', 'creation_date', 'disabled_date'],
                         payload=payload)


    ####################################
    ###  DATA VALIDATION/FORMATTING  ###
    ####################################

    # COUNTRIES
    # Incautious creation of customers with a non-existing title would result in the implicit assignement to country BE

    @property
    def country_id(self):
        return self._country_id
    
    @country_id.setter
    def country_id(self, country_id):

        countries = Countries(self._client_credentials)
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
        
    # TITLES
    # Set title_id - Enforce that list items exists
    # Incautious creation of customers with a non-existing title would result in the implicit creation of a title.

    @property
    def title_id(self):
        return self._title_id
    
    @title_id.setter
    def title_id(self, id):

        list_titles = Titles(self._client_credentials)
        self._title = list_titles.get_item_value(id, is_company=self.is_company)

        self._title_id = id

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):

        # Title value can be None in Admin...
        if value:
            list_titles = Titles(self._client_credentials)
            self._title_id = list_titles.get_item_id(value, is_company=self.is_company)

        self._title = value
        
    # LANGUAGES
    # Validate language ids

    @property
    def language_id(self):
        return self._language_id
    
    @language_id.setter
    def language_id(self, id):

        list_languages = List(self._client_credentials, list_id=19)
        self._language = list_languages.get_item_value(id)

        self._language_id = id

    @property
    def language(self):
        return self._language
    
    @language.setter
    def language(self, value):

        list_languages = List(self._client_credentials, list_id=19)
        self._language_id = list_languages.get_item_id(value)

        self._language = value


    # Extend method to include HQ Address
    #IMPROV# If the basic GET /api/v1/customer/{id} would include the (HQ?) address, this method doesn't need to be overridden.
    def get(self, id):
        super().get(id=id)

        # Get Customer HQ Address
        customer_addresses = CustomerAddressList(self._client_credentials)
        customer_addresses.get(eq__customer_id=id, eq__registered_office=True, max_results=1)
        try:
            customer_hq_address = customer_addresses[0]
        except LookupError as le:
            raise Exception('Please add a HQ Address for customer \'{}\' ({})'.format('{} {}'.format(self.name, self.first_name).strip(' '), self.customer_id))
        
        # Set customer properties with HQ Address details
        for attr in ['city', 'zip_code', 'country_code', 'street_1', 'street_2', 'house_nr', 'house_box']:
            setattr(self, attr, getattr(customer_hq_address, attr))
    
    # Overriding this method to disallow address via Customers endpoint. This implicitly manages the HQ address 
    def _allowed_put_parameters(self) -> dict:

        allowed_put_parameters = super()._allowed_put_parameters()
        del allowed_put_parameters['city']
        del allowed_put_parameters['zip_code']
        del allowed_put_parameters['country_code']
        del allowed_put_parameters['street_1']
        del allowed_put_parameters['street_2']
        del allowed_put_parameters['house_nr']
        del allowed_put_parameters['house_box']
        del allowed_put_parameters['creation_date']

        # Extra allowed PUT parameters. Not mapped to a field in the payload but impactful via setters and therefore allowed.
        allowed_put_parameters['language_id'] = '-'
        allowed_put_parameters['title_id'] = '-'
        allowed_put_parameters['country_id'] = '-'
        allowed_put_parameters['country_name'] = '-'

        return allowed_put_parameters

    def set_attributes(self, payload: dict):

        super().set_attributes(payload)

        #IMPROV# This should not be required if empty values are properly returned as None (null)
        if self.accountancy_software == 0:
            self.accountancy_software = None
        if self.customer_group == 0:
            self.customer_group = None

    def create(self):

        super().create()

    def deactivate(self, disabled_date: datetime = None):

        self._update_active_status(is_active=False, disabled_date=disabled_date)

    def reactivate(self):

        self._update_active_status(is_active=True)

    def _update_active_status(self, is_active: bool, disabled_date: datetime = None):

        if disabled_date:
            disabled_date = disabled_date.strftime('%Y-%m-%d')
        else:
            disabled_date = datetime.now().strftime('%Y-%m-%d')

        payload = dict({
            'CustomerId': self.customer_id,
            'DisabledDate': disabled_date,
            'IsActive': is_active
            # ReasonForLeaving
        })

        self._execute_request(method='post', endpoint='{}/{}/activatedeactivate'.format(self._endpoint, self.customer_id), payload=payload)
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))

    def __str__(self):
        
        return '{} {}'.format(self.name, self.first_name if isinstance(self.first_name, str) else '').strip()

class CustomerList(EntityCollection):

    _collection: list[Customer]

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        self._collection = []

        super().__init__(client_credentials=client_credentials, endpoint='customers', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[Customer]:
        return super().__iter__()
    
    def __getitem__(self, item) -> Customer:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True, **value_filters):

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [Customer(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = Customer(self._client_credentials)._allowed_get_parameters()