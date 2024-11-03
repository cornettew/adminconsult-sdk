from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ProjectAuthorizedRegistration(Entity):
        
    prestation_id: int = None
    project_id = None

    _property_mapping = dict({
        "prestation_id": {
            "GET": "PrestationId",
            "POST": None,
            "PUT": None
        },
        "project_id": {
            "GET": "ProjectId",
            "POST": None,
            "PUT": None
        }
    })

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='projectauthorizedregistrations', 
                         #IMPROV# API should return the id of the authorized prestation
                         primary_property='??', 
                         payload=payload)


    #IMPROV# Overriding _get_entity() because there is no /api/v1/projects/{project_id}/projectrecurringexpenses/{id} endpoint
    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}?Filter=?? eq {}'.format(self._endpoint, id))

        return object[0]
    
    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint. '.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))

class ProjectAuthorizedRegistrationList(EntityCollection):

    _collection: list[ProjectAuthorizedRegistration]

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        self._collection = []

        super().__init__(client_credentials=client_credentials, endpoint='projectauthorizedregistrations', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[ProjectAuthorizedRegistration]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ProjectAuthorizedRegistration:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True, **value_filters):

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [ProjectAuthorizedRegistration(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = ProjectAuthorizedRegistration(self._client_credentials)._allowed_get_parameters()