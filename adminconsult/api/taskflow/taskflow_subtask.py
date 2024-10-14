from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class TaskFlowSubtask(Entity):
    
    def __init__(self, client_credentials: ClientCredentials, task_id: int, payload=None):

        self.task_id = task_id
        self.subtask_id = None
        self.subtask_name = None
        self.subtask_order = None
        self.subtask_percentage = None
        self.subtask_active = None
        self.subtask_responsable = None
        self.is_real_subtask = None
        self.subtask_percentage = None
        self.deadline_variance_unit = None
        self.deadline_variance_nr = None

        property_mapping = dict({
            'task_id': {
                'GET': 'TaskId',
                'POST': None,
                'PUT': None
            },
            'subtask_id': {
                'GET': 'SubtaskId',
                'POST': None,
                'PUT': None
            },
            'subtask_name': {
                'GET': 'SubtaskName',
                'POST': None,
                'PUT': None
            },
            'subtask_order': {
                'GET': 'SubtaskOrder',
                'POST': None,
                'PUT': None
            },
            'subtask_percentage': {
                'GET': 'SubTaskPercentage',
                'POST': None,
                'PUT': None
            },
            'subtask_active': {
                'GET': 'SubtaskActive',
                'POST': None,
                'PUT': None
            },
            'subtask_responsable': {
                'GET': 'SubTaskResponsable',
                'POST': None,
                'PUT': None
            },
            'is_real_subtask': {
                'GET': 'IsRealSubtask',
                'POST': None,
                'PUT': None
            },
            'deadline_variance_unit': {
                'GET': 'DeadlineVarianceUnit',
                'POST': None,
                'PUT': None
            },
            'deadline_variance_nr': {
                'GET': 'DeadlineVarianceNr',
                'POST': None,
                'PUT': None
            }
        })

        super().__init__(client_credentials=client_credentials, endpoint='taskflow/tasks/{}/subtasks'.format(task_id), primary_property='subtask_id', property_mapping=property_mapping, payload=payload)


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


class TaskFlowSubtaskList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, task_id: int, on_max='ignore', payload=None):

        self._task_id = task_id

        super().__init__(client_credentials=client_credentials, endpoint='taskflow/tasks/{}/subtasks'.format(task_id), on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[TaskFlowSubtask]:
        return super().__iter__()
    
    def __getitem__(self, item) -> TaskFlowSubtask:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def _add(self, payload):
        self._collection += [TaskFlowSubtask(self._client_credentials, task_id=self._task_id, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = TaskFlowSubtask(self._client_credentials, task_id=self._task_id)._allowed_get_parameters()
