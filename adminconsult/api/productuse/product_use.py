from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ProductUse(Entity):

    customer_id: int = None
    date_product_use = None
    internal_remarks = None
    invoicable = None
    invoice_id: int = None
    period = None
    person_id: int = None
    product_id: int = None
    product_number = None
    product_price = None
    product_use_id: int = None
    product_vat = None
    project_id: int = None
    ready_for_invoice = None
    remarks = None
    repayable = None

    _property_mapping = dict({
        "customer_id": {
            "GET": "CustomerId",
            "POST": None,
            "PUT": None
        },
        "date_product_use": {
            "GET": "DateProductUse",
            "POST": "DateProductUse",
            "PUT": "DateProductUse"
        },
        "internal_remarks": {
            "GET": "InternalRemarks",
            "POST": "InternalRemarks",
            "PUT": "InternalRemarks"
        },
        "invoicable": {
            "GET": "Invoicable",
            "POST": "Invoicable",
            "PUT": "Invoicable"
        },
        "invoice_id": {
            "GET": "InvoiceId",
            "POST": None,
            "PUT": None
        },
        "period": {
            "GET": "Period",
            "POST": "Period",
            "PUT": "Period"
        },
        "person_id": {
            "GET": "PersonId",
            "POST": "PersonId",
            "PUT": "PersonId"
        },
        "product_id": {
            "GET": "ProductId",
            "POST": "ProductId",
            "PUT": "ProductId"
        },
        "product_number": {
            "GET": "ProductNumber",
            "POST": "ProductNumber",
            "PUT": "ProductNumber"
        },
        "product_price": {
            "GET": "ProductPrice",
            "POST": None,
            "PUT": None
        },
        "product_use_id": {
            "GET": "ProductUseId",
            "POST": None,
            "PUT": "ProductUseId"
        },
        "product_vat": {
            "GET": "ProductVat",
            "POST": None,
            "PUT": None
        },
        "project_id": {
            "GET": "ProjectId",
            "POST": "ProjectId",
            "PUT": "ProjectId"
        },
        "ready_for_invoice": {
            "GET": "ReadyForInvoice",
            "POST": "ReadyForInvoice",
            "PUT": "ReadyForInvoice"
        },
        "remarks": {
            "GET": "Remarks",
            "POST": "Remarks",
            "PUT": "Remarks"
        },
        "repayable": {
            "GET": "Repayable",
            "POST": None,
            "PUT": None
        }
    })
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='productuses', 
                         primary_property='product_use_id',
                         payload=payload)

    def create(self):
        
        if self.invoicable is None:
            self.invoicable = True

        return super().create()
    
    def set_invoiced(self, refresh=True):

        self._execute_request(method='put', endpoint='{}/{}/setinvoiced'.format(self._endpoint, getattr(self, self._primary_property)))
        if refresh:
            self.refresh()

    def clear_invoiced(self, refresh=True):

        self._execute_request(method='put', endpoint='{}/{}/clearinvoice'.format(self._endpoint, getattr(self, self._primary_property)))
        if refresh:
            self.refresh()

class ProductUseList(EntityCollection):

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        super().__init__(client_credentials=client_credentials, endpoint='productuses', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[ProductUse]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ProductUse:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True, **value_filters):

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [ProductUse(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = ProductUse(self._client_credentials)._allowed_get_parameters()