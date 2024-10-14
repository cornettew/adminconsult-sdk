from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ProductPriceGrid(Entity):
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        self.from_quantity = None
        self.product_id = None
        self.product_price = None
        self.product_price_grid_id = None
        self.to_quantity = None

        property_mapping = dict({
            "from_quantity": {
                "GET": "FromQuantity",
                "POST": None,
                "PUT": None
            },
            "product_id": {
                "GET": "ProductId",
                "POST": None,
                "PUT": None
            },
            "product_price": {
                "GET": "ProductPrice",
                "POST": None,
                "PUT": None
            },
            "product_price_grid_id": {
                "GET": "ProductPriceGridId",
                "POST": None,
                "PUT": None
            },
            "to_quantity": {
                "GET": "ToQuantity",
                "POST": None,
                "PUT": None
            },
        })

        super().__init__(client_credentials=client_credentials, endpoint='productuses/productpricegrid', primary_property='product_price_grid_id', property_mapping=property_mapping, payload=payload)

    def _get_entity(self, id: int):

        entities, _ = self._execute_request(method='get', endpoint=self._endpoint)
        entity = [entity for entity in entities if entity[self._property_mapping[self._primary_property]['GET']] == id][0]

        return entity

class ProductPriceGridList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        super().__init__(client_credentials=client_credentials, endpoint='productuses/productpricegrid', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[ProductPriceGrid]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ProductPriceGrid:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True, **value_filters):

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [ProductPriceGrid(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = ProductPriceGrid(self._client_credentials)._allowed_get_parameters()