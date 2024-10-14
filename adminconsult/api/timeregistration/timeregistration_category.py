from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class TimeregistrationCategory(Entity):
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        self.is_active = None
        self.category = None
        self.category_id = None

        property_mapping = dict({
            "is_active": {
                "GET": "IsActive",
                "POST": None,
                "PUT": None
            },
            "category": {
                "GET": "RegistrationCategory",
                "POST": None,
                "PUT": None
            },
            "category_id": {
                "GET": "RegistrationCategoryId",
                "POST": None,
                "PUT": None
            }
        })

        super().__init__(client_credentials=client_credentials, endpoint='timeregistrations/registrationcategory', primary_property='category_id', property_mapping=property_mapping, payload=payload)


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


class TimeregistrationCategoryList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        super().__init__(client_credentials=client_credentials, endpoint='timeregistrations/registrationcategory', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[TimeregistrationCategory]:
        return super().__iter__()
    
    def __getitem__(self, item) -> TimeregistrationCategory:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def _add(self, payload):
        self._collection += [TimeregistrationCategory(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = TimeregistrationCategory(self._client_credentials)._allowed_get_parameters()