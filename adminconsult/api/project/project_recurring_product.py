from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ProjectRecurringProduct(Entity):
        
    invoice_text = None
    last_creation_date = None
    person_id: int = None
    planning_stop = None
    product_id: int = None
    project_id: int = None
    project_recurring_product_id: int = None
    quantity = None
    schedule_abbr_nr = None
    schedule_abbr_unit = None
    schedule_date = None
    text_id: int = None
    text_type = None

    _property_mapping = dict({
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
        "product_id": {
            "GET": "ProductId",
            "POST": "ProductId",
            "PUT": "ProductId"
        },
        "project_id": {
            "GET": "ProjectId",
            "POST": "ProjectId",
            "PUT": None
        },
        "project_recurring_product_id": {
            "GET": "ProjectRecurringProductId",
            "POST": None,
            "PUT": "ProjectRecurringProductId"
        },
        "quantity": {
            "GET": "Quantity",
            "POST": "Quantity",
            "PUT": "Quantity"
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

    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='projectrecurringproducts', 
                         primary_property='project_recurring_product_id', 
                         payload=payload,
                         endpoint_parent='projects',
                         parent_id_property='project_id',
                         endpoint_suffix='projectrecurringproducts',
                         child_id_property='project_recurring_product_id',
                         datetime_properties=['schedule_date', 'last_creation_date', 'planning_stop'])


    #IMPROV# Overriding _get_entity() because there is no /api/v1/projects/{project_id}/projectrecurringproducts/{id} endpoint
    def _get_entity(self, id: int):

        object, _ = self._execute_request(method='get', endpoint='{}?Filter=ProjectRecurringProductId eq {}'.format(self._endpoint, id))

        return object[0]
    
    def _update_entity(self):

        _ = self._execute_request(method='put', endpoint=str('{}/{}/{}'.format(self._endpoint_parent, getattr(self, self._parent_id_property), self._endpoint_suffix)).rstrip('/'), payload=self._create_put_payload())
    
class ProjectRecurringProductList(EntityCollection):

    _collection: list[ProjectRecurringProduct]

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        self._collection = []

        super().__init__(client_credentials=client_credentials, endpoint='projectrecurringproducts', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[ProjectRecurringProduct]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ProjectRecurringProduct:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True, **value_filters):

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [ProjectRecurringProduct(self._client_credentials, payload=payload)]
    
    def _load_search_parameters(self):
        self._search_parameters = ProjectRecurringProduct(self._client_credentials)._allowed_get_parameters()