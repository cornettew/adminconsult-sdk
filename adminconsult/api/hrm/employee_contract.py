from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class EmployeeContract(Entity):
        
    contract_date_end = None
    contract_date_start = None
    contract_date_test_end = None
    contract_duration = None
    contract_duration_id = None
    contract_freetext = None
    contract_status = None
    contract_status_id = None
    contract_term_of_notice = None
    contract_type = None
    contract_type_id = None
    employee_id = None
    resignation_reason_1 = None
    resignation_reason_2 = None
    resignation_reason_3 = None
    voluntary_resignation = None


    _property_mapping = dict({
        'contract_date_end': {
            'GET': 'ContractDateEnd',
            'POST': None,
            'PUT': None
        },
        'contract_date_start': {
            'GET': 'ContractDateStart',
            'POST': None,
            'PUT': None
        },
        'contract_date_test_end': {
            'GET': 'ContractDateTestEnd',
            'POST': None,
            'PUT': None
        },
        'contract_duration': {
            'GET': 'ContractDuration',
            'POST': None,
            'PUT': None
        },
        'contract_duration_id': {
            'GET': 'ContractDurationId',
            'POST': None,
            'PUT': None
        },
        'contract_freetext': {
            'GET': 'ContractFreetext',
            'POST': None,
            'PUT': None
        },
        'contract_status': {
            'GET': 'ContractStatus',
            'POST': None,
            'PUT': None
        },
        'contract_status_id': {
            'GET': 'ContractStatusId',
            'POST': None,
            'PUT': None
        },
        'contract_term_of_notice': {
            'GET': 'ContractTermOfNotice',
            'POST': None,
            'PUT': None
        },
        'contract_type': {
            'GET': 'ContractType',
            'POST': None,
            'PUT': None
        },
        'contract_type_id': {
            'GET': 'ContractTypeId',
            'POST': None,
            'PUT': None
        },
        'employee_id': {
            'GET': 'EmployeeId',
            'POST': None,
            'PUT': None
        },
        'resignation_reason_1': {
            'GET': 'ResignationReason1',
            'POST': None,
            'PUT': None
        },
        'resignation_reason_2': {
            'GET': 'ResignationReason2',
            'POST': None,
            'PUT': None
        },
        'resignation_reason_3': {
            'GET': 'ResignationReason3',
            'POST': None,
            'PUT': None
        },
        'voluntary_resignation': {
            'GET': 'VoluntaryResignation',
            'POST': None,
            'PUT': None
        }
    })

    def __init__(self, client_credentials: ClientCredentials, payload=None):
        
        super().__init__(client_credentials=client_credentials, 
                         endpoint='contract', 
                         primary_property='employee_id', 
                         payload=payload,
                         endpoint_parent='employees',
                         parent_id_property='employee_id',
                         endpoint_suffix='contract',
                         child_id_property='')

    #IMPROV# Overriding _get_entity() because there is no cross project query to get invoicingdata details of a project
    def _get_entity(self, id):

        object, _ = self._execute_request(method='get', endpoint=str('{}/{}/{}'.format(self._endpoint_parent, id, self._endpoint_suffix)))
        return object
    
    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))
