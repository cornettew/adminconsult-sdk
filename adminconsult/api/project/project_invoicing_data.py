from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity
from adminconsult.api.entity_collection import EntityCollection

class ProjectInvoicingData(Entity):

    def __init__(self, client_credentials: ClientCredentials, payload=None):
        
        self.acc_code = None
        self.administrative_cost_perc = None
        self.charge_expenses = None
        self.charge_product_use = None
        self.credit_restriction_perc = None
        self.delay_duration = None
        self.delay_type = None
        self.delay_type_id = None
        self.invoice_group = None
        self.invoice_group_id = None
        self.invoicing_remark = None
        self.km_price = None
        self.ledger_account = None
        self.project_id = None
        self.tarification_list = None
        self.tarification_list_id = None
        self.use_project_employee_tarification = None

        property_mapping = dict({
            'acc_code': {
                'GET': 'AccCode',
                'POST': None,
                'PUT': 'AccCode'
            },
            'administrative_cost_perc': {
                'GET': 'AdministrativeCostPerc',
                'POST': None,
                'PUT': 'AdministrativeCostPerc'
            },
            'charge_expenses': {
                'GET': 'ChargeExpenses',
                'POST': None,
                'PUT': 'ChargeExpenses'
            },
            'charge_product_use': {
                'GET': 'ChargeProductUse',
                'POST': None,
                'PUT': 'ChargeProductUse'
            },
            'credit_restriction_perc': {
                'GET': 'CreditRestrictionPerc',
                'POST': None,
                'PUT': 'CreditRestrictionPerc'
            },
            'delay_duration': {
                'GET': 'DelayDuration',
                'POST': None,
                'PUT': 'DelayDuration'
            },
            'delay_type': {
                'GET': 'DelayType',
                'POST': None,
                'PUT': None
            },
            'delay_type_id': {
                'GET': 'DelayTypeId',
                'POST': None,
                'PUT': 'DelayTypeId'
            },
            'invoice_group': {
                'GET': 'InvoiceGroup',
                'POST': None,
                'PUT': None
            },
            'invoice_group_id': {
                'GET': 'InvoiceGroupId',
                'POST': None,
                'PUT': 'InvoiceGroupId'
            },
            'invoicing_remark': {
                'GET': 'InvoicingRemark',
                'POST': None,
                'PUT': 'InvoicingRemark'
            },
            'km_price': {
                'GET': 'KmPrice',
                'POST': None,
                'PUT': 'KmPrice'
            },
            'ledger_account': {
                'GET': 'LedgerAccount',
                'POST': None,
                'PUT': 'LedgerAccount'
            },
            'project_id': {
                'GET': 'ProjectId',
                'POST': None,
                'PUT': 'ProjectId'
            },
            'tarification_list': {
                'GET': 'TarificationList',
                'POST': None,
                'PUT': None
            },
            'tarification_list_id': {
                'GET': 'TarificationListId',
                'POST': None,
                'PUT': 'TarificationListId'
            },
            'use_project_employee_tarification': {
                'GET': 'UseProjectEmployeeTarification',
                'POST': None,
                'PUT': 'UseProjectEmployeeTarification'
            }
        })
        
        super().__init__(client_credentials=client_credentials, 
                         endpoint='invoicingdata', 
                         primary_property='project_id', 
                         property_mapping=property_mapping, 
                         payload=payload,
                         endpoint_parent='projects',
                         parent_id_property='project_id',
                         endpoint_suffix='invoicingdata',
                         child_id_property='')

    #IMPROV# Overriding _get_entity() because there is no cross project query to get invoicingdata details of a project
    def _get_entity(self, id):

        object, _ = self._execute_request(method='get', endpoint=str('{}/{}/{}'.format(self._endpoint_parent, id, self._endpoint_suffix)))
        return object
    
    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))
