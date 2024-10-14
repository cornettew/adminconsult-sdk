from abc import abstractmethod
from adminconsult.api.base import Base
from adminconsult.api.clientcredentials import ClientCredentials

from datetime import datetime, date, time
from dateutil.parser import parse, ParserError

class Entity(Base):

    def __init__(self, client_credentials: ClientCredentials, endpoint: str, primary_property: str, property_mapping: dict, payload: dict=None, endpoint_parent=None, parent_id_property=None, endpoint_suffix=None, child_id_property=None, datetime_properties=[]):

        super().__init__(client_credentials=client_credentials)

        self._property_mapping = property_mapping
        self.__test_attribute_mapping()
        self._datetime_properties = datetime_properties

        self._endpoint = endpoint
        self._primary_property = primary_property

        # Some objects are to be interpreted and manipulated with reference to a parent object.
        # Example: an address is linked to a customer and therefore the endpoint is '/api/v1/customers/{customer_id}/addresses/{address_id}'
        self._endpoint_parent = endpoint_parent
        self._parent_id_property = parent_id_property
        self._endpoint_suffix = endpoint_suffix
        self._child_id_property = child_id_property

        # If content passed, set class properties
        if payload:
            self.set_attributes(payload=payload)
            
    def __eq__(self, other): 
        return self.to_json() == other.to_json() 

    def __test_attribute_mapping(self):

        # Test if all defined class attributes are mapped to an API field.
        class_attributes = [key for key in self.__dict__.keys() if key[0] != '_']
        mapped_attributes = list(self._property_mapping.keys())
        if any(list(set(class_attributes) - set(mapped_attributes))):
            raise Exception('The attributes [\'{}\'] are defined as entity attributes but not mapped to the API.'.format('\', \''.join(list(set(class_attributes) - set(mapped_attributes)))))
        
        # Test if all mapped attritubes are defined als class attributes. Required for autocompletion purposes.
        unmapped_attributes = []
        for attr in mapped_attributes:
            if not hasattr(self, attr):
                unmapped_attributes += [attr]
        if any(unmapped_attributes):
            raise Exception('The attributes [\'{}\'] are mapped to the API but not defined as entity attributes.'.format('\', \''.join(unmapped_attributes)))

    def set_attributes(self, payload: dict):
        '''
        Set entity properties based on received payload and property mapping.

        
        '''

        property_mapping_inv = {v['GET']: k for k, v in self._property_mapping.items()}
        for payload_key, value in payload.items():
            # Only set attributes which are known to the class. Values available in future api versions need to be mapped explicitly in the subclass
            if payload_key in property_mapping_inv.keys():
                if property_mapping_inv[payload_key] in self._datetime_properties and not isinstance(str(value), datetime):
                    try:
                        setattr(self, property_mapping_inv[payload_key], parse(str(value)))
                    except ParserError:
                        setattr(self, property_mapping_inv[payload_key], value)
                else:
                    setattr(self, property_mapping_inv[payload_key], value)
            # If not from payload, load with attribute key (snake case)
            elif hasattr(self, payload_key) and value is not None:
                if payload_key in self._datetime_properties and not isinstance(str(value), datetime):
                    try:
                        setattr(self, payload_key, parse(str(value)))
                    except ParserError:
                        setattr(self, payload_key, value)
                else:
                    setattr(self, payload_key, value)
    
    def _remove_attributes(self):
        '''
        Used after DELETE
        '''

        for attr in self._property_mapping.keys():
            setattr(self, attr, None)

    def _allowed_get_parameters(self) -> dict:

        return {k: v['GET'] for k, v in self._property_mapping.items() if v['GET']}
    
    def _allowed_put_parameters(self) -> dict:

        return {k: v['PUT'] for k, v in self._property_mapping.items() if v['PUT']}

    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}/{}'.format(self._endpoint, id))

        return object

    def get(self, id):
        
        obj = self._get_entity(id)
        if len(obj) > 0:
            self.set_attributes(obj)
        else:
            raise LookupError('No object with \'{}\' = {} found in endpoint \'{}\'.'.format(self._primary_property, id, self._endpoint))

    def refresh(self):

        self.get(getattr(self, self._primary_property))

    def search(self, name_or_other):

        raise NotImplementedError()

    def to_json(self):
        '''
        Return all attributes of the enitity object in json format.
        '''

        return {k: getattr(self, k) for k in self._property_mapping.keys()}

    def _format_payload_value(self, v):

        if isinstance(v, datetime):
            return v.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(v, date):
            return v.strftime('%Y-%m-%d')
        elif isinstance(v, time):
            return v.strftime('%H:%M:%S')
        else:
            return v

    def _create_post_payload(self):
        '''
        Create payload for a POST request. Keys and values are set based on the property_mapping set in the subclass.
        '''

        property_mapping_inv = {v['POST']: k for k, v in self._property_mapping.items() if v['POST']}
        return {k: self._format_payload_value(getattr(self, v)) for k, v in property_mapping_inv.items() if getattr(self, v) is not None}

    def _create_entity(self):

        if self._endpoint_parent is None:
            created_object, _ = self._execute_request(method='post', endpoint='{}'.format(self._endpoint), payload=self._create_post_payload())
        else:
            if not isinstance(getattr(self, self._parent_id_property), int):
                raise Exception('Must pass \'{}\' to which the new {} has to be linked. Got \'{}\' = \'{}\''.format(self._parent_id_property, type(self).__name__, self._parent_id_property, getattr(self, self._parent_id_property)))
            created_object, _ = self._execute_request(method='post', endpoint='{}/{}/{}'.format(self._endpoint_parent, getattr(self, self._parent_id_property), self._endpoint_suffix), payload=self._create_post_payload())

        return created_object

    def create(self):
        
        if getattr(self, self._primary_property) is not None:
            raise Exception('{} already exists ({} = {})'.format(type(self).__name__, self._primary_property, getattr(self, self._primary_property)))

        created_object = self._create_entity()

        self.set_attributes(payload=created_object)

    def _create_put_payload(self):
        '''
        Create payload for a PUT request. Keys and values are set based on the property_mapping set in the subclass.
        '''

        property_mapping_inv = {v['PUT']: k for k, v in self._property_mapping.items() if v['PUT']}
        return {k: self._format_payload_value(getattr(self, v)) for k, v in property_mapping_inv.items()}

    def _update_entity(self):
        
        if self._endpoint_parent is None:
            _ = self._execute_request(method='put', endpoint='{}'.format(self._endpoint), payload=self._create_put_payload())
        else:
            _ = self._execute_request(method='put', endpoint=str('{}/{}/{}/{}'.format(self._endpoint_parent, getattr(self, self._parent_id_property), self._endpoint_suffix, getattr(self, self._child_id_property, ''))).rstrip('/'), payload=self._create_put_payload())
    
    def update(self, **update_fields):
        '''
        Send data to be updated via kwargs. Not possible by setting attributes because this method refreshes all attributes before posting the update.
        '''

        # Test if update_field is in allowed PUT parameters
        for k in update_fields.keys():
            if k not in self._allowed_put_parameters().keys() or k ==  self._primary_property:
                raise Exception('Field \'{}\' is not allowed in a PUT request for {}'.format(k, type(self).__name__))

        # Always perform GET to get latest data before an update.
        self.refresh()

        # Update attributes
        update = False
        for k in update_fields.keys():
            if getattr(self, k) != update_fields[k]:
                update = True
                setattr(self, k, update_fields[k])

        if update:
            self._update_entity()
            self.refresh()

    def _delete_entity(self):

        if self._endpoint_parent is None:
            _ = self._execute_request(method='delete', endpoint='{}/{}'.format(self._endpoint, getattr(self, self._primary_property)))
        else:
            if not isinstance(getattr(self, self._parent_id_property), int):
                raise Exception('Must pass \'{}\' to which the new {} has to be linked. Got \'{}\' = \'{}\''.format(self._parent_id_property, type(self).__name__, self._parent_id_property, getattr(self, self._parent_id_property)))
            _ = self._execute_request(method='delete', endpoint='{}/{}/{}/{}'.format(self._endpoint_parent, getattr(self, self._parent_id_property), self._endpoint_suffix, getattr(self, self._child_id_property)))

    def delete(self):

        self._delete_entity()

        # Reset properties
        self._remove_attributes()
