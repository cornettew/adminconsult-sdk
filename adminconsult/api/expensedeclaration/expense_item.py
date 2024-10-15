from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ExpenseItem(Entity):

    account_nr = None
    expense_type = None
    expense_type_id: int = None
    invoicable = None
    is_active = None
    is_km = None

    _property_mapping = dict({
        "account_nr": {
            "GET": "AccountNr",
            "POST": None,
            "PUT": None
        },
        "expense_type": {
            "GET": "ExpenseType",
            "POST": None,
            "PUT": None
        },
        "expense_type_id": {
            "GET": "ExpenseTypeId",
            "POST": None,
            "PUT": None
        },
        "invoicable": {
            "GET": "Invoicable",
            "POST": None,
            "PUT": None
        },
        "is_active": {
            "GET": "IsActive",
            "POST": None,
            "PUT": None
        },
        "is_km": {
            "GET": "IsKm",
            "POST": None,
            "PUT": None
        }
    })
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='expensedeclarations/expenseitem', 
                         primary_property='expense_type_id', 
                         payload=payload)


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


class ExpenseItemList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        super().__init__(client_credentials=client_credentials, endpoint='expensedeclarations/expenseitem', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[ExpenseItem]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ExpenseItem:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def _add(self, payload):
        self._collection += [ExpenseItem(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = ExpenseItem(self._client_credentials)._allowed_get_parameters()