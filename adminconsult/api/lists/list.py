from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection


class List(Entity):
    '''
    List with all list items are stored in client_credentials instead of in this class !.
    client_credentials is regarded as a sessions variable and doing so avoid rereading the same list over and over again.
    '''

    # Must initialize with a ListId.
    def __init__(self, client_credentials: ClientCredentials, list_id, list_name=None):

        self.list_id = list_id
        self.list_name = list_name

        property_mapping = dict({
            'list_id': {
                'GET': 'ListId',
                'POST': None,
                'PUT': None
            },
            'list_name': {
                'GET': 'ListName',
                'POST': None,
                'PUT': None
            }
        })

        super().__init__(client_credentials=client_credentials, endpoint='lists', primary_property='list_id', property_mapping=property_mapping)

    def set_attributes(self, payload: dict):

        for val in payload:
            self._client_credentials.lists = (self.list_id, ListItem(self.list_id, val))
        
    def get(self):
        '''
        Read all list items.
        '''

        # Empty the list
        self._client_credentials.empty_list(self.list_id)

        # ListId is set on initialization and therefore not passed during .get() method.
        super().get(self.list_id)

    def get_list(self):

        return self._client_credentials.get_list(self.list_id)

    def _get_item(self, refresh, **filter_field):

        if len(filter_field) != 1:
            raise Exception('Must add exactly one filter_field.')
        filter_key, filter_value = list(filter_field.items())[0]

        # Read list if still empty or if refresh requested
        if not any(self._client_credentials.get_list(self.list_id)) or refresh:
            self.get()

        filtered_items = [item for item in self._client_credentials.get_list(self.list_id) if getattr(item, filter_key) == filter_value]
        
        if len(filtered_items) == 1:
            return filtered_items[0]
        else:
            raise Exception('Found {} items with {} \'{}\' in list {}'.format(len(filtered_items), filter_key, filter_value, self.list_id))

    def get_item_value(self, item_id, refresh=False):

        return self._get_item(refresh=refresh, item_id=item_id).item_value

    def get_item_id(self, item_value, refresh=False):

        return self._get_item(refresh=refresh, item_value=item_value).item_id

    # Override to_json to include values.
    def to_json(self):
    
        json_dict = {k: getattr(self, k) for k in self._property_mapping.keys()}
        json_dict['values'] = [value.to_json() for value in self._client_credentials.get_list(self.list_id)]

        return json_dict
    
    def to_dict(self):

        return dict({item.item_id: item.item_value for item in self._client_credentials.get_list(self.list_id)})
    
    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint. '.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))

class ListList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        # Set collection element type for autocompletion purposes
        self._collection = [List]

        super().__init__(client_credentials=client_credentials, endpoint='lists', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[List]:
        return super().__iter__()
    
    def __getitem__(self, item) -> List:
        return super().__getitem__(item=item)

    def get(self, get_list_items=False):
        # No url filtering possible
        super().get(max_results=99999, erase_former=True)

        if get_list_items:
            for admin_list in self._collection:
                # Issue with list 20. This list is replace by 'nacecodes' endpoint.
                if not admin_list.list_id in [20]:
                    admin_list.get()

    def _add(self, payload):
        self._collection += [List(self._client_credentials, list_id=payload['ListId'], list_name=payload['ListName'])]
    
    def _load_search_parameters(self):
        self._search_parameters = dict({})

class NamedList(List):
    '''
    List with all list items are stored in client_credentials instead of in this class !.
    client_credentials is regarded as a sessions variable and doing so avoid rereading the same list over and over again.
    '''

    # Must initialize with a list_name
    def __init__(self, client_credentials: ClientCredentials, list_name):

        self.list_id = list_name

        super().__init__(client_credentials=client_credentials, list_id=self.list_id, list_name=list_name)

    def _get_entity(self, list_name):

        object, _ = self._execute_request(method='get', endpoint='{}'.format(self.list_id))

        return object

class ListItem():
    '''
    Capture the data of one list element.
    '''

    list_id: int
    item_id: int
    item_value: str

    ext_code: str
    legal_form: str

    country_code: str

    nace_code: str
    nace_description: str

    def __init__(self, list_id: int, item_data: dict) -> None:

        # Interpret values
        self.list_id = list_id
        self.item_id = item_data['ListValueId']
        self.item_value = item_data['ListValue']

        # Extra data used in a some lists only
        self.ext_code = item_data['ExtCode']
        self.legal_form = item_data['LegalForm']

        # Fictional field. Created in the Countries subclass
        self.country_code = item_data.get('CountryCode', None)

        # Specific NaceCode information.
        self.nace_code = item_data.get('NaceId', None)
        self.nace_description = item_data.get('NaceDescription', None)
    
    def to_json(self):

        return dict({k: v for k, v in self.__dict__.items()})  # if k[0] != '_'