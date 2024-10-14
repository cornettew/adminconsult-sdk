from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity_changes import EntityChanges

from . import ProjectContactList

class ProjectContactChanges(EntityChanges):

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials=client_credentials, endpoint='changedetails', id_field_name='RowIdentification', primary_property='project_contact_id', primary_table='PROJECT_LINK_CUSTOMER')

        self.inserts: ProjectContactList = ProjectContactList(self._client_credentials)
        self.updates: ProjectContactList = ProjectContactList(self._client_credentials)

    def _erase_collection(self):

        self.inserts = ProjectContactList(self._client_credentials)
        self.updates = ProjectContactList(self._client_credentials)