from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class Planning(Entity):

    customer_id = None
    date_start = None
    duration = None
    is_public = None
    out_of_office = None
    person_id = None
    planning_id = None
    prestation_id = None
    project_id = None
    remarks = None
    reminder_minutes = None
    time_start = None
    
    _property_mapping = dict({
        'customer_id': {
            'GET': 'CustomerId',
            'POST': 'CustomerId',
            'PUT': None
        },
        'date_start': {
            'GET': 'DateStart',
            'POST': 'DateStart',
            'PUT': None
        },
        'duration': {
            'GET': 'Duration',
            'POST': 'Duration',
            'PUT': None
        },
        'is_public': {
            'GET': 'IsPublic',
            'POST': 'IsPublic',
            'PUT': None
        },
        'out_of_office': {
            'GET': 'OutOfOffice',
            'POST': 'OutOfOffice',
            'PUT': None
        },
        'person_id': {
            'GET': 'PersonId',
            'POST': 'PersonId',
            'PUT': None
        },
        'planning_id': {
            'GET': 'PlanningId',
            'POST': None,
            'PUT': None
        },
        'prestation_id': {
            'GET': 'PrestationId',
            'POST': 'PrestationId',
            'PUT': None
        },
        'project_id': {
            'GET': 'ProjectId',
            'POST': 'ProjectId',
            'PUT': None
        },
        'remarks': {
            'GET': 'Remarks',
            'POST': 'Remarks',
            'PUT': None
        },
        'reminder_minutes': {
            'GET': 'ReminderMinutes',
            'POST': 'ReminderMinutes',
            'PUT': None
        },
        'time_start': {
            'GET': 'TimeStart',
            'POST': 'TimeStart',
            'PUT': None
        }
    })

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='planning', 
                         primary_property='planning_id', 
                         payload=payload)

    #IMPROV# Overriding _get_entity() because there is no /api/v1/planning/{id} endpoint
    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}?Filter=PlanningId eq {}'.format(self._endpoint, id))

        return object[0]

    def create_absence(self):
        '''
        Ticket gelogd om ook de eenheid (dag/uur) te kunnen specifiëren en niet alleen 'duration'.
        Momenteel niet mogelijk om een afwezigheid correct in te laden.
        https://syneton.zendesk.com/hc/nl/requests/177609
        '''
        
        if getattr(self, self._primary_property) is not None:
            raise Exception('{} already exists ({} = {})'.format(type(self).__name__, self._primary_property, getattr(self, self._primary_property)))

        created_object, _ = self._execute_request(method='post', endpoint='absence', payload=self._create_post_payload())

        self.set_attributes(payload=created_object)
    
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint. '.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))

class PlanningList(EntityCollection):

    _collection: list[Planning]

    def __init__(self, client_credentials: ClientCredentials, refresh=False, on_max='ignore', payload=None):

        self._refresh = refresh
        self._collection = []

        super().__init__(client_credentials=client_credentials, endpoint='planning', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[Planning]:
        return super().__iter__()
    
    def __getitem__(self, item) -> Planning:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True, **value_filters):

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [Planning(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = Planning(self._client_credentials)._allowed_get_parameters()