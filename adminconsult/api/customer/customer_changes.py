from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity_changes import EntityChanges

from .customer import CustomerList

class CustomerChanges(EntityChanges):

    def __init__(self, client_credentials: ClientCredentials, extra_tables = []):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='customer/changes', 
                         id_field_name='Id', 
                         primary_property='customer_id', 
                         primary_table='CUSTOMER',
                         extra_tables=extra_tables
                         )

        self.inserts: CustomerList = CustomerList(self._client_credentials)
        self.updates: CustomerList = CustomerList(self._client_credentials)

    def _erase_collection(self):

        self.inserts = CustomerList(self._client_credentials)
        self.updates = CustomerList(self._client_credentials)