from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ExtraTable(Entity):
        
    extra_table_id: int = None
    extra_table_name = None
    extra_table_relation = None
    
    _property_mapping = dict({
        'extra_table_id': {
            'GET': 'ExtraTableId',
            'POST': None,
            'PUT': None
        },
        'extra_table_name': {
            'GET': 'ExtraTableName',
            'POST': None,
            'PUT': None
        },
        'extra_table_relation': {
            'GET': 'ExtraTableRelation',
            'POST': None,
            'PUT': None
        }
    })

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='extratables', 
                         primary_property='extra_table_id', 
                         payload=payload)

    #IMPROV# Overriding _get_entity() because there is no /api/v1/extratables/{id} endpoint
    def _get_entity(self, id):

        entities, _ = self._execute_request(method='get', endpoint='{}'.format(self._endpoint))
        entity = [entity for entity in entities if entity[self._property_mapping[self._primary_property]['GET']] == id][0]

        return entity

    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint.'.format(self._endpoint))
    
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint.'.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))

class ExtraTableList(EntityCollection):

    _collection: list[ExtraTable]

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        self._collection = []

        super().__init__(client_credentials=client_credentials, endpoint='extratables', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[ExtraTable]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ExtraTable:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def _add(self, payload):
        self._collection += [ExtraTable(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = ExtraTable(self._client_credentials)._allowed_get_parameters()