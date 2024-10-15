from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class Department(Entity):

    company_id: int = None
    department_id: int = None
    department_name = None
    parent_department = None

    _property_mapping = dict({
        'company_id': {
            'GET': 'CompanyId',
            'POST': None,
            'PUT': None
        },
        'department_id': {
            'GET': 'DepartmentId',
            'POST': None,
            'PUT': None
        },
        'department_name': {
            'GET': 'DepartmentName',
            'POST': None,
            'PUT': None
        },
        'parent_department': {
            'GET': 'ParentDepartment',
            'POST': None,
            'PUT': None
        }
    })

    def __init__(self, client_credentials: ClientCredentials, company_id: int, payload=None):

        self.company_id = company_id

        super().__init__(client_credentials=client_credentials, 
                         endpoint='companies/{}/departments'.format(self.company_id),
                         primary_property='department_id', 
                         payload=payload,
                         endpoint_parent='companies',
                         parent_id_property='company_id',
                         endpoint_suffix='departments',
                         child_id_property='department_id')                                         

        
    def _get_entity(self, id: int):

        entities, _ = self._execute_request(method='get', endpoint=self._endpoint)
        entity = [entity for entity in entities if entity[self._property_mapping[self._primary_property]['GET']] == id][0]

        return entity
    


class DepartmentList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, company_id: int, on_max='ignore', payload=None):

        self._company_id = company_id

        # Set collection element type for autocompletion purposes
        self._collection = [Department]

        super().__init__(client_credentials=client_credentials, endpoint='companies/{}/departments'.format(self._company_id), on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[Department]:
        return super().__iter__()
    
    def __getitem__(self, item) -> Department:
        return super().__getitem__(item=item)

    def get(self, max_results=50, erase_former=True, **value_filters): 

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [Department(self._client_credentials, company_id=self._company_id, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = Department(self._client_credentials, company_id=self._company_id)._allowed_get_parameters()
