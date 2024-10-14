from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class TaskFlow(Entity):
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        self.task_id = None
        self.task_name = None
        self.task_active = None

        property_mapping = dict({
            'task_id': {
                'GET': 'TaskId',
                'POST': None,
                'PUT': None
            },
            'task_name': {
                'GET': 'TaskName',
                'POST': None,
                'PUT': None
            },
            'task_active': {
                'GET': 'TaskActive',
                'POST': None,
                'PUT': None
            }
        })

        super().__init__(client_credentials=client_credentials, endpoint='taskflow/tasks', primary_property='task_id', property_mapping=property_mapping, payload=payload)


    def _get_entity(self, id: int):

        entities, _ = self._execute_request(method='get', endpoint=self._endpoint)
        entity = [entity for entity in entities if entity[self._property_mapping[self._primary_property]['GET']] == id][0]

        return entity
    
    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint. '.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))


class TaskFlowList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        super().__init__(client_credentials=client_credentials, endpoint='taskflow/tasks', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[TaskFlow]:
        return super().__iter__()
    
    def __getitem__(self, item) -> TaskFlow:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def _add(self, payload):
        self._collection += [TaskFlow(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = TaskFlow(self._client_credentials)._allowed_get_parameters()