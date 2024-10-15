from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class TaskFlowSchedule(Entity):

    schedule_id: int = None
    schedule_name = None
    schedule_active = None

    _property_mapping = dict({
        'schedule_id': {
            'GET': 'ScheduleId',
            'POST': None,
            'PUT': None
        },
        'schedule_name': {
            'GET': 'ScheduleName',
            'POST': None,
            'PUT': None
        },
        'schedule_active': {
            'GET': 'ScheduleActive',
            'POST': None,
            'PUT': None
        }
    })
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='taskflow/taskschedules', 
                         primary_property='schedule_id', 
                         payload=payload)


    # Overriding _get_entity() because of the requirement to pass datefrom and dateuntil
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


class TaskFlowScheduleList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        super().__init__(client_credentials=client_credentials, endpoint='taskflow/taskschedules', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[TaskFlowSchedule]:
        return super().__iter__()
    
    def __getitem__(self, item) -> TaskFlowSchedule:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def _add(self, payload):
        self._collection += [TaskFlowSchedule(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = TaskFlowSchedule(self._client_credentials)._allowed_get_parameters()
