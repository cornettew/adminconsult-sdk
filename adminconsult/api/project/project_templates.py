from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ProjectTemplate(Entity):
        
    company = None
    company_id: int = None
    customer_id: int = None
    date_accepted = None
    date_proposal = None
    deadline = None
    department = None
    department_id: int = None
    invoice_percentage = None
    is_accepted = None
    is_active = None
    is_taskflow_customer = None
    p_onumber = None
    project_description = None
    project_id: int = None
    project_manager = None
    project_manager_id: int = None
    project_number = None
    project_status = None
    project_status_id: int = None
    project_title = None
    project_type = None
    project_type_id = None

    _property_mapping = dict({
        'company': {
            'GET': 'Company',
            'POST': None,
            'PUT': None
        },
        'company_id': {
            'GET': 'CompanyId',
            'POST': None,
            'PUT': None
        },
        'customer_id': {
            'GET': 'CustomerId',
            'POST': None,
            'PUT': None
        },
        'date_accepted': {
            'GET': 'DateAccepted',
            'POST': None,
            'PUT': None
        },
        'date_proposal': {
            'GET': 'DateProposal',
            'POST': None,
            'PUT': None
        },
        'deadline': {
            'GET': 'Deadline',
            'POST': None,
            'PUT': None
        },
        'department': {
            'GET': 'Department',
            'POST': None,
            'PUT': None
        },
        'department_id': {
            'GET': 'DepartmentId',
            'POST': None,
            'PUT': None
        },
        'invoice_percentage': {
            'GET': 'InvoicePercentage',
            'POST': None,
            'PUT': None
        },
        'is_accepted': {
            'GET': 'IsAccepted',
            'POST': None,
            'PUT': None
        },
        'is_active': {
            'GET': 'IsActive',
            'POST': None,
            'PUT': None
        },
        'is_taskflow_customer': {
            'GET': 'IsTaskflowCustomer',
            'POST': None,
            'PUT': None
        },
        'p_onumber': {
            'GET': 'POnumber',
            'POST': None,
            'PUT': None
        },
        'project_description': {
            'GET': 'ProjectDescription',
            'POST': None,
            'PUT': None
        },
        'project_id': {
            'GET': 'ProjectId',
            'POST': None,
            'PUT': None
        },
        'project_manager': {
            'GET': 'ProjectManager',
            'POST': None,
            'PUT': None
        },
        'project_manager_id': {
            'GET': 'ProjectManagerId',
            'POST': None,
            'PUT': None
        },
        'project_number': {
            'GET': 'ProjectNumber',
            'POST': None,
            'PUT': None
        },
        'project_status': {
            'GET': 'ProjectStatus',
            'POST': None,
            'PUT': None
        },
        'project_status_id': {
            'GET': 'ProjectStatusId',
            'POST': None,
            'PUT': None
        },
        'project_title': {
            'GET': 'ProjectTitle',
            'POST': None,
            'PUT': None
        },
        'project_type': {
            'GET': 'ProjectType',
            'POST': None,
            'PUT': None
        },
        'project_type_id': {
            'GET': 'ProjectTypeId',
            'POST': None,
            'PUT': None
        }
    })

    def __init__(self, client_credentials: ClientCredentials, payload=None):
        
        super().__init__(
            client_credentials=client_credentials, 
            endpoint='projects/templates', 
            primary_property='project_id', 
            payload=payload)

    #IMPROV# Overriding _get_entity() because there is no /api/v1/projects/templates/{id} endpoint
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
    
class ProjectTemplateList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        # Set collection element type for autocompletion purposes
        self._collection = [ProjectTemplate]

        super().__init__(client_credentials=client_credentials, 
                         endpoint='projects/templates', 
                         payload=payload)
    

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def __iter__(self) -> Iterator[ProjectTemplate]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ProjectTemplate:
        return super().__getitem__(item=item)

    def _add(self, payload):
        self._collection += [ProjectTemplate(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = ProjectTemplate(self._client_credentials)._allowed_get_parameters()
