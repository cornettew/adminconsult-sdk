from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

from adminconsult.api.customer import Customer
from .project_customer import ProjectCustomer, ProjectCustomerList
from .project_templates import ProjectTemplate

from datetime import datetime

class Project(Entity):
        
    company = None
    company_id: int = None
    customer_id: int = None
    date_accepted = None
    date_proposal = None
    deadline = None
    department = None
    _department_id: int = None
    invoice_percentage = None,
    is_accepted = None
    is_active = None
    is_taskflow_customer = None
    po_number = None
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
        "company": {
            "GET": "Company",
            "POST": None,
            "PUT": None
        },
        "company_id": {
            "GET": "CompanyId",
            "POST": None,
            "PUT": "Company"
        },
        "customer_id": {
            "GET": "CustomerId",
            "POST": None,
            "PUT": None
        },
        "date_accepted": {
            "GET": "DateAccepted",
            "POST": None,
            "PUT": "DateAccepted"
        },
        "date_proposal": {
            "GET": "DateProposal",
            "POST": None,
            "PUT": "DateProposal"
        },
        "deadline": {
            "GET": "Deadline",
            "POST": None,
            "PUT": "Deadline"
        },
        "department": {
            "GET": "Department",
            "POST": None,
            "PUT": None
        },
        "department_id": {
            "GET": "DepartmentId",
            "POST": None,
            "PUT": "Department"
        },
        "invoice_percentage": {
            "GET": "InvoicePercentage",
            "POST": None,
            "PUT": None
        },
        "is_accepted": {
            "GET": "IsAccepted",
            "POST": None,
            "PUT": "IsAccepted"
        },
        "is_active": {
            "GET": "IsActive",
            "POST": None,
            "PUT": None
        },
        "is_taskflow_customer": {
            "GET": "IsTaskflowCustomer",
            "POST": None,
            "PUT": None
        },
        "po_number": {
            "GET": "POnumber",
            "POST": None,
            "PUT": "POnumber"
        },
        "project_description": {
            "GET": "ProjectDescription",
            "POST": None,
            "PUT": "ProjectDescription"
        },
        "project_id": {
            "GET": "ProjectId",
            "POST": None,
            "PUT": None
        },
        "project_manager": {
            "GET": "ProjectManager",
            "POST": None,
            "PUT": None
        },
        "project_manager_id": {
            "GET": "ProjectManagerId",
            "POST": None,
            "PUT": "ProjectManager"
        },
        "project_number": {
            "GET": "ProjectNumber",
            "POST": None,
            "PUT": "ProjectNumber"
        },
        "project_status": {
            "GET": "ProjectStatus",
            "POST": None,
            "PUT": None
        },
        "project_status_id": {
            "GET": "ProjectStatusId",
            "POST": None,
            "PUT": "ProjectStatus"
        },
        "project_title": {
            "GET": "ProjectTitle",
            "POST": None,
            "PUT": "ProjectTitle"
        },
        "project_type": {
            "GET": "ProjectType",
            "POST": None,
            "PUT": None
        },
        "project_type_id": {
            "GET": "ProjectTypeId",
            "POST": None,
            "PUT": "ProjectType"
        }
    })

    def __init__(self, client_credentials: ClientCredentials, payload=None):
        
        super().__init__(
            client_credentials=client_credentials, 
            endpoint='projects', 
            primary_property='project_id', 
            payload=payload)
        
    @property
    def department_id(self):
        return self._department_id
    
    @department_id.setter
    def department_id(self, department_id):

        if isinstance(department_id, int) and department_id != 0:
            self._department_id = department_id
        else:
            self._department_id = None

    #IMPROV# Overriding _get_entity() because there is no /api/v1/projects/{id} endpoint
    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}?Filter=ProjectId eq {}'.format(self._endpoint, id))

        return object[0]

    def _create_entity(self, template_id: int, taskflow_customer_id: int, bill_to_customer_id: int = None):

        self.customer_id = taskflow_customer_id

        template = ProjectTemplate(self._client_credentials)
        template.get(template_id)
        project_title_suffix = template.project_title.split(':')[1]

        customer = Customer(self._client_credentials)
        customer.get(self.customer_id)

        payload = dict({
            'ProjectTitle': '{}:{}'.format(str(customer)[:50-1-len(project_title_suffix)], project_title_suffix),
            'ProjectNumber': template.project_number,
            'TemplateId': template_id
        })

        created_object, _ = self._execute_request(method='post', endpoint='customers/{}/projects'.format(self.customer_id), payload=payload)

        if isinstance(bill_to_customer_id, int) and bill_to_customer_id != taskflow_customer_id:

            # POST Invoice Customer
            project_customer_inv = ProjectCustomer(self._client_credentials, project_id=created_object.get('ProjectId'))
            project_customer_inv.is_taskflow_customer = False
            project_customer_inv.invoice_percentage = 100
            project_customer_inv.customer_id = bill_to_customer_id
            project_customer_inv.co_contractor = False
            project_customer_inv.direct_debit = False
            project_customer_inv.invoice_annex_id: int = None
            project_customer_inv.need_invoice_annex = False
            project_customer_inv.vat_excl_text_id: int = None
            project_customer_inv.vat_incl = True
            project_customer_inv.create()

            # UPDATE Taskflow Customer
            project_customers = ProjectCustomerList(self._client_credentials, project_id=created_object.get('ProjectId'))
            project_customers.get()
            project_customers._collection = [pc for pc in project_customers if pc.customer_id == self.customer_id]
            project_customer_tf = project_customers[0]
            project_customer_tf.update(invoice_percentage = 0)

        return created_object

    def create(self, template_id: int, taskflow_customer_id: int, company_id: int, project_manager_id: int, bill_to_customer_id: int = None):
        
        if getattr(self, self._primary_property) is not None:
            raise Exception('{} already exists ({} = {})'.format(type(self).__name__, self._primary_property, getattr(self, self._primary_property)))

        created_object = self._create_entity(template_id=template_id, taskflow_customer_id=taskflow_customer_id, bill_to_customer_id=bill_to_customer_id)

        self.set_attributes(payload=created_object)

        self.update(project_manager_id=project_manager_id)
        if company_id != self.company_id:
            self.update(company_id=company_id)

    def _update_entity(self):
        
        _ = self._execute_request(method='put', endpoint='{}/{}'.format(self._endpoint, getattr(self, self._primary_property)), payload=self._create_put_payload())

    def deactivate(self):

        self._update_active_status(is_active=False)

    def _update_active_status(self, is_active: bool):

        payload = dict({
            'CustomerId': self.customer_id,
            'IsActive': is_active
            # ReasonForLeaving
        })

        self._execute_request(method='post', endpoint='{}/{}/deactivate'.format(self._endpoint, self.project_id), payload=payload)
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))

class ProjectList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        # Set collection element type for autocompletion purposes
        self._collection = [Project]

        super().__init__(client_credentials=client_credentials, endpoint='projects', payload=payload)
    
    def __iter__(self) -> Iterator[Project]:
        return super().__iter__()
    
    def __getitem__(self, item) -> Project:
        return super().__getitem__(item=item)

    def get(self, eq__is_taskflow_customer=True, max_results=20000, **value_filters):
        '''
        The /api/v1/project endpoint return a line for each project-customer combination. The list of projects might there not be unique.
        Typically, one would only need each project exactly once. Therefore, the 'eq__is_taskflow_customer=True' is added by default.
        '''

        if isinstance(eq__is_taskflow_customer, bool):
            super().get(eq__is_taskflow_customer=eq__is_taskflow_customer, max_results=max_results, **value_filters)
        else:
            super().get(max_results=max_results, **value_filters)

    def _add(self, payload):
        self._collection += [Project(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = Project(self._client_credentials)._allowed_get_parameters()