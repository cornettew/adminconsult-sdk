from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity

from datetime import datetime

class Private(Entity):
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        self.customer_id = None
        self.date_of_birth: datetime = None
        self.date_of_death: datetime = None
        self.eid_expiration_date: datetime = None
        self.eid_file = None
        self.eid_nr = None
        self.handicap = None
        self.marital_status = None
        self.marital_status_id = None
        self.nationality = None
        self.national_nr = None
        self.place_of_birth = None
        self.place_of_death = None
        self.profession = None
        self.profession_id = None
        self.self_employed_since = None
        self.sex = None

        property_mapping = dict({
            'customer_id': {
                'GET': 'CustomerId',
                'POST': None,
                'PUT': None
            },
            'date_of_birth': {
                'GET': 'DateOfBirth',
                'POST': 'DateOfBirth',
                'PUT': 'DateOfBirth'
            },
            'date_of_death': {
                'GET': 'DateOfDeath',
                'POST': 'DateOfDeath',
                'PUT': 'DateOfDeath'
            },
            'eid_expiration_date': {
                'GET': 'EidExpirationDate',
                'POST': 'EidExpirationDate',
                'PUT': 'EidExpirationDate'
            },
            'eid_file': {
                'GET': 'EidFile',
                'POST': 'EidFile',
                'PUT': 'EidFile'
            },
            'eid_nr': {
                'GET': 'EidNr',
                'POST': 'EidNr',
                'PUT': 'EidNr'
            },
            'handicap': {
                'GET': 'Handicap',
                'POST': 'Handicap',
                'PUT': 'Handicap'
            },
            'marital_status': {
                'GET': 'MaritalStatus',
                'POST': None,
                'PUT': None
            },
            'marital_status_id': {
                'GET': 'MaritalStatusId',
                'POST': 'MaritalStatusId',
                'PUT': 'MaritalStatusId'
            },
            'nationality': {
                'GET': 'Nationality',
                'POST': 'Nationality',
                'PUT': 'Nationality'
            },
            'national_nr': {
                'GET': 'NationalNr',
                'POST': 'NationalNr',
                'PUT': 'NationalNr'
            },
            'place_of_birth': {
                'GET': 'PlaceOfBirth',
                'POST': 'PlaceOfBirth',
                'PUT': 'PlaceOfBirth'
            },
            'place_of_death': {
                'GET': 'PlaceOfDeath',
                'POST': 'PlaceOfDeath',
                'PUT': 'PlaceOfDeath'
            },
            'profession': {
                'GET': 'Profession',
                'POST': None,
                'PUT': None
            },
            'profession_id': {
                'GET': 'ProfessionId',
                'POST': 'ProfessionId',
                'PUT': 'ProfessionId'
            },
            'self_employed_since': {
                'GET': 'SelfEmployedSince',
                'POST': 'SelfEmployedSince',
                'PUT': 'SelfEmployedSince'
            },
            'sex': {
                'GET': 'Sex',
                'POST': 'Sex',
                'PUT': 'Sex'
            },
        })

        super().__init__(client_credentials=client_credentials, 
                         endpoint='private', 
                         primary_property='customer_id', 
                         property_mapping=property_mapping, 
                         payload=payload,
                         endpoint_parent='customers',
                         parent_id_property='customer_id',
                         endpoint_suffix='private',
                         datetime_properties=['date_of_birth', 'date_of_death', 'eid_expiration_date'])
        
    #IMPROV# Overriding _get_entity() because there is no cross customer query to get private details of all customers
    def _get_entity(self, id):

        object, _ = self._execute_request(method='get', endpoint=str('{}/{}/{}'.format(self._endpoint_parent, id, self._endpoint_suffix)))
        return object
    
    #IMPROV# Overriding _update_entitity() because there is no put /api/v1/customers/{customerid}/private endpoint, only post
    def _update_entity(self):
        
        if self._endpoint_parent is None:
            _ = self._execute_request(method='post', endpoint='{}'.format(self._endpoint), payload=self._create_put_payload())
        else:
            _ = self._execute_request(method='post', endpoint='{}/{}/{}'.format(self._endpoint_parent, getattr(self, self._parent_id_property), self._endpoint_suffix), payload=self._create_put_payload())    

    def create(self):

        created_object = self._create_entity()

        self.set_attributes(payload=created_object)