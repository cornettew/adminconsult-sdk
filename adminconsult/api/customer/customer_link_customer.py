from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

from datetime import datetime

class CustomerLinkCustomer(Entity):
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        self.address_type = None
        self.begin_mandate: datetime = None
        self.child_domestication_place = None
        self.child_of_giver = False
        self.child_parency = False
        self.customer_id_fk = None
        self.customer_id_pk = None
        self.customer_link_customer_id = None
        self.customer_link_type_id = None
        self.date_of_change_marital_status = None
        self.date_of_mariage = None
        self.election_date = None
        self._end_mandate: datetime = None
        self.ext_representation = None
        self.function_id = None
        self.has_end_mandate = None
        self.ibr_number = None
        self.inv_contact = False
        self.kind_of_mariage_id = None
        self.license_end_date = None
        self.license_nr = None
        self.license_start_date = None
        self.license_type = None
        self.membership_nr = None
        self.other_parents_name = None
        self.parency = None
        self.place_of_mariage = None
        self.publication_date = None
        self.publication_nr = None
        self.public_remuneration = False
        self.reelection_date = None
        self.relationship = None
        self.remark = None
        self.represented_by = None
        self.repr_rotation_date = None
        self.repr_rotation_nr = None
        self.rotation_date = None
        self.rotation_nr = None
        self.signing_authority = None
        self.statutory_mandate = False
        self.stock_category = None
        self.stock_owned = None
        self.stock_percentage_owned = None
        self.stock_type = None
        self.stock_voting = False
        self.stock_voting_nr = None
        self.verified = None

        property_mapping = dict({
            'address_type': {
                'GET': 'AddressType',
                'POST': 'AddressType',
                'PUT': 'AddressType'
            },
            'begin_mandate': {
                'GET': 'BeginMandate',
                'POST': 'BeginMandate',
                'PUT': 'BeginMandate'
            },
            'child_domestication_place': {
                'GET': 'ChildDomesticationPlace',
                'POST': 'ChildDomesticationPlace',
                'PUT': 'ChildDomesticationPlace'
            },
            'child_of_giver': {
                'GET': 'ChildOfGiver',
                'POST': 'ChildOfGiver',
                'PUT': 'ChildOfGiver'
            },
            'child_parency': {
                'GET': 'ChildParency',
                'POST': 'ChildParency',
                'PUT': 'ChildParency'
            },
            'customer_id_fk': {
                'GET': 'CustomerIdFk',
                'POST': 'CustomerIdFk',
                'PUT': 'CustomerIdFk'
            },
            'customer_id_pk': {
                'GET': 'CustomerIdPk',
                'POST': 'CustomerIdPk',
                'PUT': 'CustomerIdPk'
            },
            'customer_link_customer_id': {
                'GET': 'CustomerLinkCustomerId',
                'POST': 'CustomerLinkCustomerId',
                'PUT': 'CustomerLinkCustomerId'
            },
            'customer_link_type_id': {
                'GET': 'CustomerLinkTypeId',
                'POST': 'CustomerLinkTypeId',
                'PUT': 'CustomerLinkTypeId'
            },
            'date_of_change_marital_status': {
                'GET': 'DateOfChangeMaritalStatus',
                'POST': 'DateOfChangeMaritalStatus',
                'PUT': 'DateOfChangeMaritalStatus'
            },
            'date_of_mariage': {
                'GET': 'DateOfMariage',
                'POST': 'DateOfMariage',
                'PUT': 'DateOfMariage'
            },
            'election_date': {
                'GET': 'ElectionDate',
                'POST': 'ElectionDate',
                'PUT': 'ElectionDate'
            },
            'end_mandate': {
                'GET': 'EndMandate',
                'POST': 'EndMandate',
                'PUT': 'EndMandate'
            },
            'ext_representation': {
                'GET': 'ExtRepresentation',
                'POST': 'ExtRepresentation',
                'PUT': 'ExtRepresentation'
            },
            'function_id': {
                'GET': 'FunctionId',
                'POST': 'FunctionId',
                'PUT': 'FunctionId'
            },
            'has_end_mandate': {
                'GET': 'HasEndMandate',
                'POST': 'HasEndMandate',
                'PUT': 'HasEndMandate'
            },
            'ibr_number': {
                'GET': 'IbrNumber',
                'POST': 'IbrNumber',
                'PUT': 'IbrNumber'
            },
            'inv_contact': {
                'GET': 'InvContact',
                'POST': 'InvContact',
                'PUT': 'InvContact'
            },
            'kind_of_mariage_id': {
                'GET': 'KindOfMariageId',
                'POST': 'KindOfMariageId',
                'PUT': 'KindOfMariageId'
            },
            'license_end_date': {
                'GET': 'LicenseEnddate',
                'POST': 'LicenseEnddate',
                'PUT': 'LicenseEnddate'
            },
            'license_nr': {
                'GET': 'LicenseNr',
                'POST': 'LicenseNr',
                'PUT': 'LicenseNr'
            },
            'license_start_date': {
                'GET': 'LicenseStartdate',
                'POST': 'LicenseStartdate',
                'PUT': 'LicenseStartdate'
            },
            'license_type': {
                'GET': 'LicenseType',
                'POST': 'LicenseType',
                'PUT': 'LicenseType'
            },
            'membership_nr': {
                'GET': 'MembershipNr',
                'POST': 'MembershipNr',
                'PUT': 'MembershipNr'
            },
            'other_parents_name': {
                'GET': 'OtherParentsName',
                'POST': 'OtherParentsName',
                'PUT': 'OtherParentsName'
            },
            'parency': {
                'GET': 'Parency',
                'POST': 'Parency',
                'PUT': 'Parency'
            },
            'place_of_mariage': {
                'GET': 'PlaceOfMariage',
                'POST': 'PlaceOfMariage',
                'PUT': 'PlaceOfMariage'
            },
            'publication_date': {
                'GET': 'PublicationDate',
                'POST': 'PublicationDate',
                'PUT': 'PublicationDate'
            },
            'publication_nr': {
                'GET': 'PublicationNr',
                'POST': 'PublicationNr',
                'PUT': 'PublicationNr'
            },
            'public_remuneration': {
                'GET': 'PublicRemuneration',
                'POST': 'PublicRemuneration',
                'PUT': 'PublicRemuneration'
            },
            'reelection_date': {
                'GET': 'ReelectionDate',
                'POST': 'ReelectionDate',
                'PUT': 'ReelectionDate'
            },
            'relationship': {
                'GET': 'Relationship',
                'POST': 'Relationship',
                'PUT': 'Relationship'
            },
            'remark': {
                'GET': 'Remark',
                'POST': 'Remark',
                'PUT': 'Remark'
            },
            'represented_by': {
                'GET': 'RepresentedBy',
                'POST': 'RepresentedBy',
                'PUT': 'RepresentedBy'
            },
            'repr_rotation_date': {
                'GET': 'ReprRotationDate',
                'POST': 'ReprRotationDate',
                'PUT': 'ReprRotationDate'
            },
            'repr_rotation_nr': {
                'GET': 'ReprRotationNr',
                'POST': 'ReprRotationNr',
                'PUT': 'ReprRotationNr'
            },
            'rotation_date': {
                'GET': 'RotationDate',
                'POST': 'RotationDate',
                'PUT': 'RotationDate'
            },
            'rotation_nr': {
                'GET': 'RotationNr',
                'POST': 'RotationNr',
                'PUT': 'RotationNr'
            },
            'signing_authority': {
                'GET': 'SigningAuthority',
                'POST': 'SigningAuthority',
                'PUT': 'SigningAuthority'
            },
            'statutory_mandate': {
                'GET': 'StatutoryMandate',
                'POST': 'StatutoryMandate',
                'PUT': 'StatutoryMandate'
            },
            'stock_category': {
                'GET': 'StockCategory',
                'POST': 'StockCategory',
                'PUT': 'StockCategory'
            },
            'stock_owned': {
                'GET': 'StockOwned',
                'POST': 'StockOwned',
                'PUT': 'StockOwned'
            },
            'stock_percentage_owned': {
                'GET': 'StockPercentageOwned',
                'POST': 'StockPercentageOwned',
                'PUT': 'StockPercentageOwned'
            },
            'stock_type': {
                'GET': 'StockType',
                'POST': 'StockType',
                'PUT': 'StockType'
            },
            'stock_voting': {
                'GET': 'StockVoting',
                'POST': 'StockVoting',
                'PUT': 'StockVoting'
            },
            'stock_voting_nr': {
                'GET': 'StockVotingNr',
                'POST': 'StockVotingNr',
                'PUT': 'StockVotingNr'
            },
            'verified': {
                'GET': 'Verified',
                'POST': 'Verified',
                'PUT': 'Verified'
            },
        })

        super().__init__(client_credentials=client_credentials, 
                         endpoint='customerlinkcustomer', 
                         primary_property='customer_link_customer_id', 
                         property_mapping=property_mapping, 
                         payload=payload,
                         endpoint_parent='customers',
                         parent_id_property='customer_id_pk',
                         endpoint_suffix='customerlinkcustomer',
                         child_id_property='customer_link_customer_id',
                         datetime_properties=['end_mandate', 'begin_mandate'])


    ####################################
    ###  DATA VALIDATION/FORMATTING  ###
    ####################################
        
    @property
    def end_mandate(self):
        return self._end_mandate
      
    @end_mandate.setter
    def end_mandate(self, end_mandate):
        if isinstance(end_mandate, datetime) and self.customer_link_type_id in [4, 6]:
            self.has_end_mandate = True
        elif end_mandate == None and self.customer_link_type_id in [4, 6]:
            self.has_end_mandate = False
        
        self._end_mandate = end_mandate
        
    #IMPROV# Overriding _get_entity() because there is no /api/v1/customeraddress/{id} endpoint
    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}?Filter=CustomerLinkCustomerId eq {}'.format(self._endpoint, id))

        return object[0]

class CustomerLinkCustomerList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        # Set collection element type for autocompletion purposes
        self._collection = [CustomerLinkCustomer]

        super().__init__(client_credentials=client_credentials, endpoint='customerlinkcustomer', payload=payload)
    
    def __iter__(self) -> Iterator[CustomerLinkCustomer]:
        return super().__iter__()
    
    def __getitem__(self, item) -> CustomerLinkCustomer:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, **value_filters):

        super().get(max_results=max_results, **value_filters)

    def _add(self, payload):
        self._collection += [CustomerLinkCustomer(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = CustomerLinkCustomer(self._client_credentials)._allowed_get_parameters()