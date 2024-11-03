from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

from datetime import datetime, time, timedelta

class Timeregistration(Entity):

    benchmark = None
    customer_id: int = None
    customer_invoice_id: int = None
    date_registration = None
    _duration = None
    ex_forfait = None
    internal_price = None
    internal_remarks = None
    invoicable = None
    invoice_id: int = None
    overtime = None
    period = None
    person_id: int = None
    prestation_id: int = None
    project_id: int = None
    ready_for_invoice = True
    recalc = None
    remarks = None
    _time_from = None
    _time_to = None
    timeregistration_id: int = None
    tr_price = None
    tr_vat = None
    urgent = None

    _property_mapping = dict({
        "benchmark": {
            "GET": "Benchmark",
            "POST": "Benchmark",
            "PUT": "Benchmark"
        },
        "customer_id": {
            "GET": "CustomerId",
            "POST": None,
            "PUT": None
        },
        "customer_invoice_id": {
            "GET": "CustomerInvoiceId",
            "POST": None,
            "PUT": None
        },
        "date_registration": {
            "GET": "DateRegistration",
            "POST": "DateRegistration",
            "PUT": "DateRegistration"
        },
        "duration": {
            "GET": "Duration",
            "POST": "Duration",
            "PUT": "Duration"
        },
        "ex_forfait": {
            "GET": "ExForfait",
            "POST": "ExForfait",
            "PUT": "ExForfait"
        },
        "internal_price": {
            "GET": "InternalPrice",
            "POST": "InternalPrice",
            "PUT": "InternalPrice"
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
        "overtime": {
            "GET": "Overtime",
            "POST": "Overtime",
            "PUT": "Overtime"
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
        "prestation_id": {
            "GET": "PrestationId",
            "POST": "PrestationId",
            "PUT": "PrestationId"
        },
        "project_id": {
            "GET": "ProjectId",
            "POST": "ProjectId",
            "PUT": "ProjectId"
        },
        "ready_for_invoice": {
            "GET": None,
            "POST": "ReadyForInvoice",
            "PUT": "ReadyForInvoice"
        },
        "recalc": {
            "GET": "Recalc",
            "POST": "Recalc",
            "PUT": "Recalc"
        },
        "remarks": {
            "GET": "Remarks",
            "POST": "Remarks",
            "PUT": "Remarks"
        },
        "time_from": {
            "GET": "TimeFrom",
            "POST": "TimeFrom",
            "PUT": "TimeFrom"
        },
        "timeregistration_id": {
            "GET": "TimeRegistrationId",
            "POST": None,
            "PUT": "TimeRegistrationId"
        },
        "time_to": {
            "GET": "TimeTo",
            "POST": "TimeTo",
            "PUT": "TimeTo"
        },
        "tr_price": {
            "GET": "TrPrice",
            "POST": "TrPrice",
            "PUT": "TrPrice"
        },
        "tr_vat": {
            "GET": "TrVat",
            "POST": "TrVat",
            "PUT": "TrVat"
        },
        "urgent": {
            "GET": "Urgent",
            "POST": "Urgent",
            "PUT": "Urgent"
        }
    })
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='timeregistrations', 
                         primary_property='timeregistration_id', 
                         payload=payload,
                         datetime_properties=['date_registration'])

    @property
    def time_from(self):
        return self._time_from
    
    @time_from.setter
    def time_from(self, time_from):
        if time_from is None:
            self._time_from = time(8, 30, 0)
        elif isinstance(time_from, str):
            self._time_from = time(int(time_from.split(':')[0]), int(time_from.split(':')[1]), int(time_from.split(':')[2]))
        else:
            self._time_from = time_from

        # Set time_to if duration is known
        if self.duration:
            datetime_to = datetime(100, 1, 1, self.time_from.hour, self.time_from.minute, self.time_from.second)
            self.time_to = datetime_to + timedelta(minutes=self.duration)
            self.time_to = self.time_to.time()

    @property
    def time_to(self):
        return self._time_to
    
    @time_to.setter
    def time_to(self, time_to):
        self._time_to = time_to

    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, duration):
        self._duration = duration

        # Set time_to is time_from is known
        if self.time_from:
            datetime_to = datetime(100, 1, 1, self.time_from.hour, self.time_from.minute, self.time_from.second)
            self.time_to = datetime_to + timedelta(minutes=self.duration)
            self.time_to = self.time_to.time()

    def set_invoiced(self, refresh=True):

        self._execute_request(method='put', endpoint='{}/{}/setinvoiced'.format(self._endpoint, getattr(self, self._primary_property)))
        if refresh:
            self.refresh()

    def clear_invoiced(self, refresh=True):

        self._execute_request(method='put', endpoint='{}/{}/clearinvoice'.format(self._endpoint, getattr(self, self._primary_property)))
        if refresh:
            self.refresh()

class TimeregistrationList(EntityCollection):

    _collection: list[Timeregistration]

    def __init__(self, client_credentials: ClientCredentials, on_max='ignore', payload=None):

        self._collection = []

        super().__init__(client_credentials=client_credentials, endpoint='timeregistrations', on_max=on_max, payload=payload)
    
    def __iter__(self) -> Iterator[Timeregistration]:
        return super().__iter__()
    
    def __getitem__(self, item) -> Timeregistration:
        return super().__getitem__(item=item)

    def get(self, max_results=20000, erase_former=True, **value_filters):

        super().get(max_results=max_results, erase_former=erase_former, **value_filters)

    def _add(self, payload):
        self._collection += [Timeregistration(self._client_credentials, payload=payload)]

    def _load_search_parameters(self):
        self._search_parameters = Timeregistration(self._client_credentials)._allowed_get_parameters()