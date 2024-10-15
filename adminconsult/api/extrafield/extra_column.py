from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ExtraColumn(Entity):

    _extra_table_id: int = None
    extra_column_id: int = None
    extra_column_name = None
    extra_column_display_type = None
    extra_column_default_value = None
    
    _property_mapping = dict({
        'extra_column_id': {
            'GET': 'ExtraColumnId',
            'POST': None,
            'PUT': None
        },
        'extra_column_name': {
            'GET': 'ExtraColumnName',
            'POST': None,
            'PUT': None
        },
        'extra_column_display_type': {
            'GET': 'ExtraColumnDisplayType',
            'POST': None,
            'PUT': None
        },
        'extra_column_default_value': {
            'GET': 'ExtraColumnDefaultValue',
            'POST': None,
            'PUT': None
        }
    })

    def __init__(self, client_credentials: ClientCredentials, extra_table_id, payload=None):
        
        self._extra_table_id = extra_table_id

        super().__init__(client_credentials=client_credentials, 
                         endpoint='extracolumns', 
                         primary_property='extra_column_id', 
                         payload=payload)

    #IMPROV# Overriding _get_entity() because there is no /api/v1/extracolumns/{id} endpoint
    def _get_entity(self, id):

        entities, _ = self._execute_request(method='get', endpoint='{}/{}'.format(self._endpoint, self._extra_table_id))
        entity = [entity for entity in entities if entity[self._property_mapping[self._primary_property]['GET']] == id][0]

        return entity

    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint.'.format(self._endpoint))
    
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint.'.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))
    
class ExtraColumnList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, extra_table_id, on_max='ignore', payload=None):

        # Set collection element type for autocompletion purposes
        self._collection = [ExtraColumn]

        self._extra_table_id = extra_table_id

        super().__init__(client_credentials=client_credentials, endpoint='extracolumns', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[ExtraColumn]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ExtraColumn:
        return super().__getitem__(item=item)

    def get(self, erase_former=True, max_results=20000):

        super().get(max_results=max_results, erase_former=erase_former)
    
    def _search_entity(self, url_filter, max_results):

        # Alway requests lists with paging enabled. If the endpoint doesn't support paging is will return all results anyway.
        objects, _ = super()._execute_request(method='get', endpoint='{}/{}'.format(self._endpoint, self._extra_table_id), querystring=url_filter, max_results=max_results, use_paging=False)

        return objects

    def _add(self, payload):
        self._collection += [ExtraColumn(self._client_credentials, extra_table_id=self._extra_table_id, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = ExtraColumn(self._client_credentials, extra_table_id=self._extra_table_id)._allowed_get_parameters()