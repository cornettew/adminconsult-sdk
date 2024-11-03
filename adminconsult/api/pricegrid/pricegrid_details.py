from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class PriceGridDetail(Entity):

    price_grid_id: int = None
    row_value_id: int = None
    column_value_id: int = None
    tariff = None
    column_value_description = None
    row_value_description = None

    _property_mapping = dict({
        "price_grid_id": {
            "GET": "PriceGridId",
            "POST": None,
            "PUT": None
        },
        "row_value_id": {
            "GET": "RowValueId",
            "POST": None,
            "PUT": None
        },
        "column_value_id": {
            "GET": "ColumnValueId",
            "POST": None,
            "PUT": None
        },
        "tariff": {
            "GET": "Tariff",
            "POST": None,
            "PUT": None
        },
        "column_value_description": {
            "GET": "ColumnValueDescription",
            "POST": None,
            "PUT": None
        },
        "row_value_description": {
            "GET": "RowValueDescription",
            "POST": None,
            "PUT": None
        }
    })
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='pricegrid', 
                         primary_property='price_grid_id', 
                         payload=payload)
    
    def get(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint. '.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))
    
class PriceGridDetailList(EntityCollection):

    _collection: list[PriceGridDetail]

    def __init__(self, client_credentials: ClientCredentials, price_grid_id: int, on_max='ignore', payload=None):

        self.price_grid_id = price_grid_id
        self._collection = []

        super().__init__(client_credentials=client_credentials, endpoint=f'pricegrid/{self.price_grid_id}', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[PriceGridDetail]:
        return super().__iter__()
    
    def __getitem__(self, item) -> PriceGridDetail:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def _add(self, payload):
        self._collection += [PriceGridDetail(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = PriceGridDetail(self._client_credentials)._allowed_get_parameters()