from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity_changes import EntityChanges

from . import CustomerAddressList

class CustomerAddressChanges(EntityChanges):

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='changedetails', 
                         id_field_name='RowIdentification', 
                         primary_property='customer_address_id', 
                         primary_table='CUSTOMER_ADRESS')

        self.inserts: CustomerAddressList = CustomerAddressList(self._client_credentials)
        self.updates: CustomerAddressList = CustomerAddressList(self._client_credentials)

    def _erase_collection(self):

        self.inserts = CustomerAddressList(self._client_credentials)
        self.updates = CustomerAddressList(self._client_credentials)