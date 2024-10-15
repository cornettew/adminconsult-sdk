from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

import regex as re

class ExtraData(Entity):
    '''
    The ExtraData structure contains ExtraField objects
    '''

    _extra_table_id: int = None
    # Unique identifier within an extra table is combination ['foreign_key', 'record_id']
    # Define property getter and setter for foreign_key with a more appropriate name such as 'project_id'
    foreign_key = int
    record_id = None

    _fields = dict({})
    
    _property_mapping = dict({
        'foreign_key': {
            'GET': 'fk',
            'POST': None,
            'PUT': None
        },
        'record_id': {
            'GET': 'record_id',
            'POST': None,
            'PUT': None
        }
    })

    def __init__(self, client_credentials: ClientCredentials, table_id, foreign_key, payload=None):
        
        self._extra_table_id = table_id
        self.foreign_key = foreign_key

        super().__init__(client_credentials=client_credentials, 
                         endpoint='extradata/{}'.format(self._extra_table_id), 
                         primary_property='record_id', 
                         payload=payload)

    #IMPROV# Overriding _get_entity() because there is no /api/v1/extradata/{id} endpoint
    def _get_entity(self, record_id: int):

        entities, _ = self._execute_request(method='get', endpoint='{}/{}'.format(self._endpoint, self.foreign_key))
        entity = [entity for entity in entities if entity['record_id'] == record_id][0]

        return entity
    
    def get(self, record_id):
        
        obj = self._get_entity(record_id)
        self.set_attributes(obj)

    def _get_field_value(self, field_name):
        # Use this method in subclass properties .getter methods

        if self.record_id is None:
            raise Exception('First set a \'record_id\' via .get() in order to get \'field_value\' from a record.')

        if len(self._fields.keys()) == 0:
            self.refresh()
        
        field = [field for label, field in self._fields.items() if label == field_name][0]

        return field.value

    def _update_field_value(self, field_name, field_value):
        # Use this method in subclass properties .setter methods

        if self.record_id is None:
            raise Exception('First set a \'record_id\' via .get() in order to update \'field_value\' of a record.')

        self.refresh()
        
        field = [field for label, field in self._fields.items() if label == field_name][0]

        field.update(field_value)
        self.refresh()

    def _remove_attributes(self):

        super()._remove_attributes()

        for _, field in self._fields.items():
            field.value = None
            field.unique_id = None

    def _create_entity(self):

        current_records = ExtraDataList(self._client_credentials, table_id=self._extra_table_id)
        current_records.get(self.foreign_key)
        current_record_ids = [record.record_id for record in current_records]

        # Set payload
        payload = dict({
            'ExtraTableId': self._extra_table_id,
            'FKId': self.foreign_key
            })
        
        # Execute API Call
        new_records, _ = self._execute_request(method='post', endpoint='extrarecord', payload=payload)
        new_record_ids = [record['record_id'] for record in new_records]

        diff = list(set(new_record_ids) - set(current_record_ids))

        if len(diff) == 1:
            new_record_id = diff[0]
            # Return the new record
            return [new_record for new_record in new_records if new_record['record_id'] == new_record_id][0]
        else:
            raise Exception('Failed to create extra record.')
    
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint.'.format(self._endpoint))
    
    def set_attributes(self, payload: dict):

        super().set_attributes(payload=payload)

        # Drop keys which are already mapped. Retaining the keys which represent tasks
        for mapped_key in {v['GET']: k for k, v in self._property_mapping.items()}.keys():
            del payload[mapped_key]

        for label in payload.keys():
            self._set_field_details(foreign_key=self.foreign_key, record_id=self.record_id, label=label, payload=payload)

    def _set_field_details(self, foreign_key, record_id, label: str, payload):

        # Discard *_ID and *_value labels. These are extra metadata to another fields
        if label.split('_')[-1] in ['ID', 'value']:
            return

        self._fields[re.sub(r'(?<!^|[A-Z_])(?=[A-Z])', '_', label).lower()] = ExtraField(self._client_credentials, record_field_data=(foreign_key, record_id, label, payload))

    # Override to_json to include subtask data.
    def to_json(self):
        ent_json = super().to_json()

        for field in self._fields.values():
            ent_json.update(field._to_json_record())
        
        return ent_json
    
    def _delete_entity(self):

        _ = self._execute_request(method='delete', endpoint='extrarecord/{}/{}/{}'.format(self._extra_table_id, self.foreign_key, getattr(self, self._primary_property)))



class ExtraDataList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, table_id, on_max='ignore', payload=None):

        # Set collection element type for autocompletion purposes
        self._collection = [ExtraData]
        
        self._extra_table_id = table_id

        super().__init__(client_credentials=client_credentials, endpoint='extradata/{}'.format(self._extra_table_id), on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[ExtraData]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ExtraData:
        return super().__getitem__(item=item)

    def _search_entity(self, foreign_key=None):

        if foreign_key:
            objects, _ = super()._execute_request(method='get', endpoint='{}/{}'.format(self._endpoint, foreign_key), querystring=None, use_paging=False)
        else:
            objects, _ = super()._execute_request(method='get', endpoint=self._endpoint, querystring=None, use_paging=False)

        return objects

    def get(self, foreign_key=None, erase_former=True):
        '''
        Optional filter on foreign key.
        '''
        
        if erase_former:
            self._erase_collection()

        objs = self._search_entity(foreign_key=foreign_key)

        for obj in objs:
            self._add(obj)

    def _add(self, payload):
        self._collection += [ExtraData(self._client_credentials, table_id=self._extra_table_id, foreign_key=payload['fk'], payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = ExtraData(self._client_credentials, self._extra_table_id, foreign_key=0)._allowed_get_parameters()





class ExtraField(Entity):
        
    column_id: int = None
    field_type = None
    foreign_key = None
    record_id: int = None
    table_id: int = None
    unique_id: int = None
    value = None
    
    _property_mapping = dict({
        'column_id': {
            'GET': 'ColumnId',
            'POST': None,
            'PUT': 'ColumnId'
        },
        'field_type': {
            'GET': 'FieldType',
            'POST': None,
            'PUT': 'FieldType'
        },
        'foreign_key': {
            'GET': 'FKId',
            'POST': None,
            'PUT': 'FKId'
        },
        'record_id': {
            'GET': 'RecordId',
            'POST': None,
            'PUT': 'RecordId'
        },
        'table_id': {
            'GET': 'TableId',
            'POST': None,
            'PUT': 'TableId'
        },
        'unique_id': {
            'GET': 'UniqueId',
            'POST': None,
            'PUT': 'UniqueId'
        },
        'value': {
            'GET': 'Value',
            'POST': None,
            'PUT': 'Value'
        }
    })

    def __init__(self, client_credentials: ClientCredentials, payload=None, record_field_data: tuple()= None) -> None:

        if record_field_data:
            self._interpret_from_record(record_field_data[0], record_field_data[1], record_field_data[2], record_field_data[3])

        super().__init__(client_credentials=client_credentials, 
                         endpoint='extrafields', 
                         primary_property='unique_id', 
                         payload=payload)
    
    # Implement GET request to get specific field data ? '/api/v1/extrafields/{unique_id}'
    # Or only use via extradata endpoints ?

    def _interpret_from_record(self, field_foreign_key, field_record_id, field_label, field_data):
        
        self.foreign_key = field_foreign_key
        self.record_id = field_record_id
        self._label = re.sub(r'(?<!^|[A-Z_])(?=[A-Z])', '_', field_label).lower()

        # Interpret values
        self.column_id = field_data['{}_ID'.format(field_label)]
        self.unique_id = field_data['{}_value'.format(field_label)]
        self.value = field_data[field_label]

    def _to_json_record(self):

        return dict({
            # '{}_value'.format(self._label): self.unique_id,
            '{}'.format(self._label): self.value#,
            # '{}_id'.format(self._label): self.column_id
        })
    
    def _allowed_put_parameters(self) -> dict:
        # Only allow the value of an extra field to be updated. Not record_id, column_id, foreign_key, ...

        return {'value': self._property_mapping['value']['PUT']}
    
    def _update_entity(self):
        
        _ = self._execute_request(method='post', endpoint='{}'.format(self._endpoint), payload=self._create_put_payload())

    def update(self, value):

        super().update(value=value)

    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint.'.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))
    