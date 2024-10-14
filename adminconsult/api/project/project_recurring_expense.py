from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ProjectRecurringExpense(Entity):

    def __init__(self, client_credentials: ClientCredentials, payload=None):
        
        self.amount = None
        self.expense_id = None
        self.invoice_text = None
        self.last_creation_date = None
        self.person_id = None
        self.planning_stop = None
        self.project_id = None
        self.project_recurring_expense_id = None
        self.schedule_abbr_nr = None
        self.schedule_abbr_unit = None
        self.schedule_date = None
        self.text_id = None
        self.text_type = None

        property_mapping = dict({
            "amount": {
                "GET": "Amount",
                "POST": "Amount",
                "PUT": "Amount"
            },
            "expense_id": {
                "GET": "ExpenseId",
                "POST": "ExpenseId",
                "PUT": "ExpenseId"
            },
            "invoice_text": {
                "GET": "InvoiceText",
                "POST": "InvoiceText",
                "PUT": "InvoiceText"
            },
            "last_creation_date": {
                "GET": "LastCreationDate",
                "POST": None,
                "PUT": None
            },
            "person_id": {
                "GET": "PersonId",
                "POST": "PersonId",
                "PUT": "PersonId"
            },
            "planning_stop": {
                "GET": "PlanningStop",
                "POST": "PlanningStop",
                "PUT": "PlanningStop"
            },
            "project_id": {
                "GET": "ProjectId",
                "POST": "ProjectId",
                "PUT": None
            },
            "project_recurring_expense_id": {
                "GET": "ProjectRecurringExpenseId",
                "POST": None,
                "PUT": "ProjectRecurringExpenseId"
            },
            "schedule_abbr_nr": {
                "GET": "ScheduleAbbrNr",
                "POST": "ScheduleAbbrNr",
                "PUT": "ScheduleAbbrNr"
            },
            "schedule_abbr_unit": {
                "GET": "ScheduleAbbrUnit",
                "POST": "ScheduleAbbrUnit",
                "PUT": "ScheduleAbbrUnit"
            },
            "schedule_date": {
                "GET": "ScheduleDate",
                "POST": "ScheduleDate",
                "PUT": "ScheduleDate"
            },
            "text_id": {
                "GET": "TextId",
                "POST": "TextId",
                "PUT": "TextId"
            },
            "text_type": {
                "GET": "TextType",
                "POST": "TextType",
                "PUT": "TextType"
            }
        })

        super().__init__(client_credentials=client_credentials, 
                         endpoint='projectrecurringexpenses', 
                         primary_property='project_recurring_expense_id', 
                         property_mapping=property_mapping, 
                         payload=payload,
                         endpoint_parent='projects',
                         parent_id_property='project_id',
                         endpoint_suffix='projectrecurringexpenses',
                         child_id_property='project_recurring_expense_id',
                         datetime_properties=['planning_start', 'planning_stop'])

    #IMPROV# Overriding _get_entity() because there is no /api/v1/projects/{project_id}/projectrecurringexpenses/{id} endpoint
    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}?Filter=ProjectRecurringExpenseId eq {}'.format(self._endpoint, id))

        return object[0]
    
    def _update_entity(self):
        
        _ = self._execute_request(method='put', endpoint=str('{}/{}/{}'.format(self._endpoint_parent, getattr(self, self._parent_id_property), self._endpoint_suffix)).rstrip('/'), payload=self._create_put_payload())


class ProjectRecurringExpenseList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        # Set collection element type for autocompletion purposes
        self._collection = [ProjectRecurringExpense]

        super().__init__(client_credentials=client_credentials, endpoint='projectrecurringexpenses', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[ProjectRecurringExpense]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ProjectRecurringExpense:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True, **value_filters):

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [ProjectRecurringExpense(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = ProjectRecurringExpense(self._client_credentials)._allowed_get_parameters()