from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ExpenseDeclaration(Entity):

    customer_id: int = None
    date_expense = None
    expense = None
    expense_ccy = None
    expense_id: int = None
    expense_type = None
    internal_remarks = None
    invoicable = None
    invoice_id: int = None
    km_price = None
    nr_km = None
    period = None
    person_id: int = None
    project_id: int = None
    ready_for_invoice = None
    remarks = None
    repayable = None
    vat_perc = None

    _property_mapping = dict({
        "customer_id": {
            "GET": "CustomerId",
            "POST": None,
            "PUT": None
        },
        "date_expense": {
            "GET": "DateExpense",
            "POST": "DateExpense",
            "PUT": "DateExpense"
        },
        "expense": {
            "GET": "Expense",
            "POST": "Expense",
            "PUT": "Expense"
        },
        "expense_ccy": {
            "GET": "ExpenseCcy",
            "POST": None,
            "PUT": None
        },
        "expense_id": {
            "GET": "ExpenseId",
            "POST": None,
            "PUT": "ExpenseId"
        },
        "expense_type": {
            "GET": "ExpenseType",
            "POST": "ExpenseType",
            "PUT": "ExpenseType"
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
        "km_price": {
            "GET": "KmPrice",
            "POST": None,
            "PUT": None
        },
        "nr_km": {
            "GET": "NrKm",
            "POST": "NrKm",
            "PUT": "NrKm"
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
            "POST": "None",
            "PUT": "Repayable"
        },
        "vat_perc": {
            "GET": "VatPerc",
            "POST": None,
            "PUT": None
        }
    })
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='expensedeclarations', 
                         primary_property='expense_id', 
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

class ExpenseDeclarationList(EntityCollection):

    _collection: list[ExpenseDeclaration]

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        self._collection = []

        super().__init__(client_credentials=client_credentials, endpoint='expensedeclarations', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[ExpenseDeclaration]:
        return super().__iter__()
    
    def __getitem__(self, item) -> ExpenseDeclaration:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True, **value_filters):

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [ExpenseDeclaration(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = ExpenseDeclaration(self._client_credentials)._allowed_get_parameters()