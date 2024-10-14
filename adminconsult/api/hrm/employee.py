from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class Employee(Entity):

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        self.employee_id = None
        self.last_name = None
        self.first_name = None
        self.work_email = None
        self.work_phone = None
        self.internal_nbr = None
        self.work_mobile = None
        self.work_fax = None
        self.employee_active = None
        self.function_type = None
        self.main_profile = None
        self.employee_remark = None
        self.main_company = None
        self.main_company_id = None
        self.main_department = None
        self.main_department_id = None
        self.leave_decision_user = None
        self.leave_decision_user2 = None
        self.login_name = None
        self.short_name = None
        self.language = None
        self.registration_only_user = None
        self.dms_user = None
        self.synch_user = None
        self.is_administrator = None
        self.is_hrm = None
        self.last_logon = None
        
        property_mapping = dict({
            'employee_id': {
                'GET': 'EmployeeId',
                'POST': None,
                'PUT': None
            },
            'last_name': {
                'GET': 'LastName',
                'POST': None,
                'PUT': None
            },
            'first_name': {
                'GET': 'FirstName',
                'POST': None,
                'PUT': None
            },
            'work_email': {
                'GET': 'WorkEmail',
                'POST': None,
                'PUT': None
            },
            'work_phone': {
                'GET': 'WorkPhone',
                'POST': None,
                'PUT': None
            },
            'internal_nbr': {
                'GET': 'InternalNbr',
                'POST': None,
                'PUT': None
            },
            'work_mobile': {
                'GET': 'WorkMobile',
                'POST': None,
                'PUT': None
            },
            'work_fax': {
                'GET': 'WorkFax',
                'POST': None,
                'PUT': None
            },
            'employee_active': {
                'GET': 'EmployeeActive',
                'POST': None,
                'PUT': None
            },
            'function_type': {
                'GET': 'FunctionType',
                'POST': None,
                'PUT': None
            },
            'main_profile': {
                'GET': 'MainProfile',
                'POST': None,
                'PUT': None
            },
            'employee_remark': {
                'GET': 'EmployeeRemark',
                'POST': None,
                'PUT': None
            },
            'main_company': {
                'GET': 'MainCompany',
                'POST': None,
                'PUT': None
            },
            'main_company_id': {
                'GET': 'MainCompanyId',
                'POST': None,
                'PUT': None
            },
            'main_department': {
                'GET': 'MainDepartment',
                'POST': None,
                'PUT': None
            },
            'main_department_id': {
                'GET': 'MainDepartmentId',
                'POST': None,
                'PUT': None
            },
            'leave_decision_user': {
                'GET': 'LeaveDecisionUser',
                'POST': None,
                'PUT': None
            },
            'leave_decision_user2': {
                'GET': 'LeaveDecisionUser2',
                'POST': None,
                'PUT': None
            },
            'login_name': {
                'GET': 'LoginName',
                'POST': None,
                'PUT': None
            },
            'short_name': {
                'GET': 'ShortName',
                'POST': None,
                'PUT': None
            },
            'language': {
                'GET': 'Language',
                'POST': None,
                'PUT': None
            },
            'registration_only_user': {
                'GET': 'RegistrationOnlyUser',
                'POST': None,
                'PUT': None
            },
            'dms_user': {
                'GET': 'DmsUser',
                'POST': None,
                'PUT': None
            },
            'synch_user': {
                'GET': 'SynchUser',
                'POST': None,
                'PUT': None
            },
            'is_administrator': {
                'GET': 'IsAdministrator',
                'POST': None,
                'PUT': None
            },
            'is_hrm': {
                'GET': 'IsHRM',
                'POST': None,
                'PUT': None
            },
            'last_logon': {
                'GET': 'LastLogon',
                'POST': None,
                'PUT': None
            },
        })

        super().__init__(client_credentials=client_credentials, endpoint='employees', primary_property='employee_id', property_mapping=property_mapping, payload=payload)

    #IMPROV# Overriding _get_entity() because there is no /api/v1/employeeid/{id} endpoint
    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}?Filter=EmployeeId eq {}'.format(self._endpoint, id))

        return object[0]
    
    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint. '.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))

class EmployeeList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, refresh=False, on_max='ignore', payload=None):

        self._refresh = refresh

        # Set collection element type for autocompletion purposes
        self._collection = [Employee]

        super().__init__(client_credentials=client_credentials, endpoint='employees', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[Employee]:
        return super().__iter__()
    
    def __getitem__(self, item) -> Employee:
        return super().__getitem__(item=item)
        
    def _search_entity(self, url_filter, max_results):

        if self._refresh or not any(self._client_credentials.employees):
            # Alway requests lists with paging enabled. If the endpoint doesn't support paging is will return all results anyway.
            objects, _ = super()._execute_request(method='get', endpoint=self._endpoint, querystring=url_filter, use_paging=True, max_results=max_results)
            self._client_credentials.employees = objects
        
        return self._client_credentials.employees

    def get(self, max_results=20000, erase_former=True, **value_filters):

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def get_active_user_names(self):

        if not any(self._collection):
            self.get()

        return [emp.login_name for emp in self._collection if emp.employee_active == True]

    def _add(self, payload):
        self._collection += [Employee(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = Employee(self._client_credentials)._allowed_get_parameters()