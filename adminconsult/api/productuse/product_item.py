from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ProductItem(Entity):
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        self.account_nr = None
        self.invoicable = None
        self.is_active = None
        self.order_nr = None
        self.price = None
        self.product = None
        self.product_category_id = None
        self.product_id = None
        self.purchase_price = None

        property_mapping = dict({
            "account_nr": {
                "GET": "AccountNr",
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
            "order_nr": {
                "GET": "OrderNr",
                "POST": None,
                "PUT": None
            },
            "price": {
                "GET": "Price",
                "POST": None,
                "PUT": None
            },
            "product": {
                "GET": "Product",
                "POST": None,
                "PUT": None
            },
            "product_category_id": {
                "GET": "ProductCategoryId",
                "POST": None,
                "PUT": None
            },
            "product_id": {
                "GET": "ProductId",
                "POST": None,
                "PUT": None
            },
            "purchase_price": {
                "GET": "PurchasePrice",
                "POST": None,
                "PUT": None
            }
        })

        super().__init__(client_credentials=client_credentials, endpoint='productuses/productitem', primary_property='product_id', property_mapping=property_mapping, payload=payload)


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


class ProductItemList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        super().__init__(client_credentials=client_credentials, endpoint='productuses/productitem', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[ProductItem]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ProductItem:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True):

        super().get(max_results=max_results, erase_former=erase_former)

    def _add(self, payload):
        self._collection += [ProductItem(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = ProductItem(self._client_credentials)._allowed_get_parameters()