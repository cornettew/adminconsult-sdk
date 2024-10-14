from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class PriceGrid(Entity):
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        self.column_category = None
        self.column_category_description = None
        self.price_grid_id = None
        self.price_grid_name = None
        self.row_category = None
        self.row_category_description = None

        property_mapping = dict({
            "column_category": {
                "GET": "ColumnCategory",
                "POST": None,
                "PUT": None
            },
            "column_category_description": {
                "GET": "ColumnCategoryDescription",
                "POST": None,
                "PUT": None
            },
            "price_grid_id": {
                "GET": "PriceGridId",
                "POST": None,
                "PUT": None
            },
            "price_grid_name": {
                "GET": "PriceGridName",
                "POST": None,
                "PUT": None
            },
            "row_category": {
                "GET": "RowCategory",
                "POST": None,
                "PUT": None
            },
            "row_category_description": {
                "GET": "RowCategoryDescription",
                "POST": None,
                "PUT": None
            }
        })

        super().__init__(client_credentials=client_credentials, 
                         endpoint='pricegrid', 
                         primary_property='price_grid_id', 
                         property_mapping=property_mapping, 
                         payload=payload)
    
    def get(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def update(self):

        raise AttributeError('Cannot execute PUT request on \'{}\' endpoint. '.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))


class PriceGridList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        super().__init__(client_credentials=client_credentials, endpoint='pricegrid', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[PriceGrid]:
        return super().__iter__()
    
    def __getitem__(self, item) -> PriceGrid:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def _add(self, payload):
        self._collection += [PriceGrid(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = PriceGrid(self._client_credentials)._allowed_get_parameters()