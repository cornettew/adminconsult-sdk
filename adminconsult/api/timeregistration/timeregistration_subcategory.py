from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class TimeregistrationSubcategory(Entity):

    category_id: int = None
    is_active = None
    subcategory = None
    subcategory_id = None

    _property_mapping = dict({
        "category_id": {
            "GET": "CategoryId",
            "POST": None,
            "PUT": None
        },
        "is_active": {
            "GET": "IsActive",
            "POST": None,
            "PUT": None
        },
        "subcategory": {
            "GET": "Subcategory",
            "POST": None,
            "PUT": None
        },
        "subcategory_id": {
            "GET": "SubcategoryId",
            "POST": None,
            "PUT": None
        }
    })
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='timeregistrations/registrationsubcategory', 
                         primary_property='subcategory_id', 
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


class TimeregistrationSubcategoryList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        super().__init__(client_credentials=client_credentials, endpoint='timeregistrations/registrationsubcategory', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[TimeregistrationSubcategory]:
        return super().__iter__()
    
    def __getitem__(self, item) -> TimeregistrationSubcategory:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def _add(self, payload):
        self._collection += [TimeregistrationSubcategory(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = TimeregistrationSubcategory(self._client_credentials)._allowed_get_parameters()