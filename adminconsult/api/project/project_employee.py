from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ProjectEmployee(Entity):

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        self.project_employee_pk = None
        self.project_id = None
        self.employee_profile = None
        self.employee = None
        self.employee_profile_id = None
        self.employee_id = None
        self.is_taskflow_employee = None
        self.is_active = None
        
        property_mapping = dict({
            'project_employee_pk': {
                'GET': 'ProjectEmployeePk',
                'POST': None,
                'PUT': 'ProjectEmployeePk'
            },
            'project_id': {
                'GET': 'ProjectId',
                'POST': None,
                'PUT': None
            },
            'employee_profile': {
                'GET': 'EmployeeProfile',
                'POST': None,
                'PUT': None
            },
            'employee': {
                'GET': 'Employee',
                'POST': None,
                'PUT': None
            },
            'employee_profile_id': {
                'GET': 'EmployeeProfileId',
                'POST': 'EmployeeProfileId',
                'PUT': 'EmployeeProfileId'
            },
            'employee_id': {
                'GET': 'EmployeeId',
                'POST': 'EmployeeId',
                'PUT': 'EmployeeId'
            },
            'is_taskflow_employee': {
                'GET': 'IsTaskflowEmployee',
                'POST': 'IsTaskflowEmployee',
                'PUT': 'IsTaskflowEmployee'
            },
            'is_active': {
                'GET': 'IsActive',
                'POST': 'IsActive',
                'PUT': 'IsActive'
            }
        })

        super().__init__(client_credentials=client_credentials, 
                         endpoint='projectemployees', 
                         primary_property='project_employee_pk', 
                         property_mapping=property_mapping, 
                         payload=payload,
                         endpoint_parent='projects',
                         parent_id_property='project_id',
                         endpoint_suffix='projectemployee',
                         child_id_property='')

    #IMPROV# Overriding _get_entity() because there is no /api/v1/projects/{id}/projectemployees/{id} endpoint
    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}?Filter=ProjectEmployeePk eq {}'.format(self._endpoint, id))

        return object[0]

    #IMPROV# It is not possible to delete a linked employee to a project via the API
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))

class ProjectEmployeeList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        # Set collection element type for autocompletion purposes
        self._collection = [ProjectEmployee]

        super().__init__(client_credentials=client_credentials, endpoint='projectemployees', payload=payload)
    
    def __iter__(self) -> Iterator[ProjectEmployee]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ProjectEmployee:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, **value_filters):

        super().get(max_results=max_results, **value_filters)

    def _add(self, payload):
        self._collection += [ProjectEmployee(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = ProjectEmployee(self._client_credentials)._allowed_get_parameters()