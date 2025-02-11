from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity_changes import EntityChanges

from . import CustomerLinkCustomerList

class CustomerLinkCustomerChanges(EntityChanges):

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials=client_credentials, endpoint='changedetails', id_field_name='RowIdentification', primary_property='customer_link_customer_id', primary_table='CUSTOMER_LINK_CUSTOMER')

        self.inserts: CustomerLinkCustomerList = CustomerLinkCustomerList(self._client_credentials)
        self.updates: CustomerLinkCustomerList = CustomerLinkCustomerList(self._client_credentials)

    def _erase_collection(self):

        self.inserts = CustomerLinkCustomerList(self._client_credentials)
        self.updates = CustomerLinkCustomerList(self._client_credentials)