from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity_changes import EntityChanges

from . import CustomerEmailDataList

class CustomerEmailDataChanges(EntityChanges):

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='customer/changes', 
                         id_field_name='OwnId', 
                         primary_property='customer_email_recipient_id', 
                         primary_table='CUSTOMER_EMAIL')

        self.inserts: CustomerEmailDataList = CustomerEmailDataList(self._client_credentials, customer_id=0)
        self.updates: CustomerEmailDataList = CustomerEmailDataList(self._client_credentials, customer_id=0)

    def _load_admin_data(self, changes: list[dict]):

        insert_ids = [change[self._id_field_name] for change in changes if (change['ActionType'] == 'INSERT' and change['TableName'] == self._primary_table)]
        delete_ids = [change[self._id_field_name] for change in changes if (change['ActionType'] == 'DELETE' and change['TableName'] == self._primary_table)]
        # Ignore updates for entities which are already marked for creation/deletion
        update_ids = list(set([change[self._id_field_name] for change in changes if change[self._id_field_name] not in insert_ids+delete_ids]))
        
        insert_customer_ids = list(set([change['Id'] for change in changes if (change['ActionType'] == 'INSERT' and change['TableName'] == self._primary_table) and change['Id'] != 0]))
        update_customer_ids = list(set([change['Id'] for change in changes if change[self._id_field_name] not in insert_ids+delete_ids and change['Id'] !=0]))
        
        for insert_customer_id in insert_customer_ids:
            insert_customer_email_data = CustomerEmailDataList(self._client_credentials, customer_id=insert_customer_id)
            insert_customer_email_data.get()
            self.inserts._collection += [ce for ce in insert_customer_email_data if ce.customer_email_recipient_id in insert_ids]
        for update_customer_id in update_customer_ids:
            update_customer_email_data = CustomerEmailDataList(self._client_credentials, customer_id=update_customer_id)
            update_customer_email_data.get()
            self.updates._collection += [ce for ce in update_customer_email_data if ce.customer_email_recipient_id in update_ids]
        self.deletes = delete_ids

    def _erase_collection(self):

        self.inserts = CustomerEmailDataList(self._client_credentials, customer_id=0)
        self.updates = CustomerEmailDataList(self._client_credentials, customer_id=0)