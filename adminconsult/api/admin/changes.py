from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

import warnings

class Change(Entity):

    action_type = None
    column_name = None
    date_action = None
    db_user = None
    display_name = None
    log_id: int = None
    new_value = None
    old_value = None
    person_name = None
    row_identification = None
    table_name = None

    _property_mapping = dict({
        'action_type': {
            'GET': 'ActionType',
            'POST': None,
            'PUT': None
        },
        'column_name': {
            'GET': 'ColumnName',
            'POST': None,
            'PUT': None
        },
        'date_action': {
            'GET': 'DateAction',
            'POST': None,
            'PUT': None
        },
        'db_user': {
            'GET': 'Dbuser',
            'POST': None,
            'PUT': None
        },
        'display_name': {
            'GET': 'DisplayName',
            'POST': None,
            'PUT': None
        },
        'log_id': {
            'GET': 'LogId',
            'POST': None,
            'PUT': None
        },
        'new_value': {
            'GET': 'NewValue',
            'POST': None,
            'PUT': None
        },
        'old_value': {
            'GET': 'OldValue',
            'POST': None,
            'PUT': None
        },
        'person_name': {
            'GET': 'PersonName',
            'POST': None,
            'PUT': None
        },
        'row_identification': {
            'GET': 'RowIdentification',
            'POST': None,
            'PUT': None
        },
        'table_name': {
            'GET': 'TableName',
            'POST': None,
            'PUT': None
        }
    })

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='changedetails', 
                         primary_property='log_id', 
                         datetime_properties=['date_action'],
                         payload=payload)
        
    #IMPROV# Overriding _get_entity() because there is no /api/v1/customeraddress/{id} endpoint
    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}?Filter={} eq {}'.format(self._endpoint, self._property_mapping[self._primary_property]['GET'], id))

        return object[0]
    
    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint. '.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))
    

class ChangeList(EntityCollection):

    _collection: list[Change]

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', on_technical_max='raise', payload=None):

        self._collection = []

        super().__init__(client_credentials=client_credentials, endpoint='changedetails', on_max=on_max, technical_max_results=1000, on_technical_max=on_technical_max, payload=payload)
    
    def __iter__(self) -> Iterator[Change]:
        return super().__iter__()
    
    def __getitem__(self, item) -> Change:
        return super().__getitem__(item=item)

    def _get_max_log_id(self):

        return max([log.get('LogId') for log in self._search_entity(url_filter=None, max_results=1000)])

    def get(self, max_results=1000, erase_former=True, limit_last_logs: int=None, on_max=None, on_technical_max=None, **value_filters):
        '''
        limit_last_logs:
            For a more efficient search
        '''

        if limit_last_logs:
            log_id_from = self._get_max_log_id() - limit_last_logs
            super().get(max_results=max_results, erase_former=erase_former, on_max=on_max, on_technical_max=on_technical_max, ge__log_id=log_id_from, **value_filters)
        else:
            super().get(max_results=max_results, erase_former=erase_former, on_max=on_max, on_technical_max=on_technical_max, **value_filters)

    def _add(self, payload):
        self._collection += [Change(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = Change(self._client_credentials)._allowed_get_parameters()