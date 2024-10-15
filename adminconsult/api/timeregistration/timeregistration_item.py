from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class TimeregistrationItem(Entity):

    account_nr = None
    benchmark_required = None
    fixed_price = None
    invoicable = None
    is_absence = None
    is_active = None
    prestation = None
    prestation_code = None
    prestation_id: int = None
    subcategory_id: int = None
    usage_description = None

    _property_mapping = dict({
        "account_nr": {
            "GET": "AccountNr",
            "POST": None,
            "PUT": None
        },
        "benchmark_required": {
            "GET": "BenchmarkRequired",
            "POST": None,
            "PUT": None
        },
        "fixed_price": {
            "GET": "FixedPrice",
            "POST": None,
            "PUT": None
        },
        "invoicable": {
            "GET": "Invoicable",
            "POST": None,
            "PUT": None
        },
        "is_absence": {
            "GET": "IsAbsence",
            "POST": None,
            "PUT": None
        },
        "is_active": {
            "GET": "IsActive",
            "POST": None,
            "PUT": None
        },
        "prestation": {
            "GET": "Prestation",
            "POST": None,
            "PUT": None
        },
        "prestation_code": {
            "GET": "PrestationCode",
            "POST": None,
            "PUT": None
        },
        "prestation_id": {
            "GET": "PrestationId",
            "POST": None,
            "PUT": None
        },
        "subcategory_id": {
            "GET": "SubcategoryId",
            "POST": None,
            "PUT": None
        },
        "usage_description": {
            "GET": "UsageDescription",
            "POST": None,
            "PUT": None
        }
    })
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='timeregistrations/registrationitem', 
                         primary_property='prestation_id', 
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


class TimeregistrationItemList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        super().__init__(client_credentials=client_credentials, endpoint='timeregistrations/registrationitem', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[TimeregistrationItem]:
        return super().__iter__()
    
    def __getitem__(self, item) -> TimeregistrationItem:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def _add(self, payload):
        self._collection += [TimeregistrationItem(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = TimeregistrationItem(self._client_credentials)._allowed_get_parameters()