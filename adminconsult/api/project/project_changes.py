from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity_changes import EntityChanges

from .project import ProjectList

class ProjectChanges(EntityChanges):

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials=client_credentials, endpoint='projects/changes', id_field_name='Id', primary_property='project_id', primary_table='PROJECT', extra_tables=['PROJECT_CUSTOMER'])

        self.inserts: ProjectList = ProjectList(self._client_credentials)
        self.updates: ProjectList = ProjectList(self._client_credentials)

    def _load_admin_data(self, changes: list[dict]):
        
        insert_ids = [change[self._id_field_name] for change in changes if (change['ActionType'] == 'INSERT' and change['TableName'] == self._primary_table)]
        delete_ids = [change[self._id_field_name] for change in changes if (change['ActionType'] == 'DELETE' and change['TableName'] == self._primary_table)]
        # Ignore updates for entities which are already marked for creation/deletion
        update_ids = list(set([change[self._id_field_name] for change in changes if change[self._id_field_name] not in insert_ids+delete_ids]))
    
        if len(insert_ids):
            self.inserts.get(**{'in__{}'.format(self._primary_property): insert_ids}, eq__is_taskflow_customer=None)
        if len(update_ids):
            self.updates.get(**{'in__{}'.format(self._primary_property): update_ids}, eq__is_taskflow_customer=None)
        self.deletes = delete_ids

    def _erase_collection(self):

        self.inserts = ProjectList(self._client_credentials)
        self.updates = ProjectList(self._client_credentials)