from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity

from datetime import datetime

class Juridical(Entity):

    customer_id: int = None
    new_company_law = None
    closing_date = None
    closing_date_first_year = None
    commercial_court = None
    commercial_court_id: int = None
    share_register = None
    date_share_register = None
    founding_date = None
    founding_date_publication = None
    founding_date_filing = None
    last_amendments_to_constitutions = None
    company_duration_limited = None
    company_duration_end_date = None
    founding_publication_number = None
    subscribed_capital = None
    sub_capital_currency = None
    sub_capital_currency_id: int = None
    paid_up_capital = None
    capital_fully_paid_up = None
    bankruptcy = None
    date_bankruptcy = None
    annual_account = None
    annual_account_type = None
    annual_account_scheme = None
    annual_account_consolidated = None
    annual_account_consolidated_type = None
    annual_account_where = None
    annual_account_date_last_deposit = None
    method_of_deposit = None
    method_of_deposit_id: int = None
    date_draft_annual_accounts = None
    general_meeting = None
    general_meeting_formula = None
    general_meeting_description = None
    general_meeting_saturday_is_workday = None
    general_meeting_when_holiday = None
    general_meeting_location = None
    general_meeting_hour = None
    general_meeting_calling_by = None
    general_meeting_calling_how = None
    lei_number = None
    lei_valid_until = None
    social_goal = None
    remarks = None

    _property_mapping = dict({
        'customer_id': {
            'GET': 'CustomerId',
            'POST': None,
            'PUT': None
        },
        'new_company_law': {
            'GET': 'NewCompanyLaw',
            'POST': None,
            'PUT': None
        },
        'closing_date': {
            'GET': 'ClosingDate',
            'POST': None,
            'PUT': 'ClosingDate'
        },
        'closing_date_first_year': {
            'GET': 'ClosingDateFirstYear',
            'POST': None,
            'PUT': 'ClosingDateFirstYear'
        },
        'commercial_court': {
            'GET': 'CommercialCourt',
            'POST': None,
            'PUT': None
        },
        'commercial_court_id': {
            'GET': 'CommercialCourtId',
            'POST': None,
            'PUT': 'CommercialCourtId'
        },
        'share_register': {
            'GET': 'ShareRegister',
            'POST': None,
            'PUT': 'ShareRegister'
        },
        'date_share_register': {
            'GET': 'DateShareRegister',
            'POST': None,
            'PUT': 'DateShareRegister'
        },
        'founding_date': {
            'GET': 'FoundingDate',
            'POST': None,
            'PUT': 'FoundingDate'
        },
        'founding_date_publication': {
            'GET': 'FoundingDatePublication',
            'POST': None,
            'PUT': 'FoundingDatePublication'
        },
        'founding_date_filing': {
            'GET': 'FoundingDateFiling',
            'POST': None,
            'PUT': 'FoundingDateFiling'
        },
        'last_amendments_to_constitutions': {
            'GET': 'LastAmendmentsToConstitutions',
            'POST': None,
            'PUT': 'LastAmendmentsToConstitutions'
        },
        'company_duration_limited': {
            'GET': 'CompanyDurationLimited',
            'POST': None,
            'PUT': 'CompanyDurationLimited'
        },
        'company_duration_end_date': {
            'GET': 'CompanyDurationEndDate',
            'POST': None,
            'PUT': 'CompanyDurationEndDate'
        },
        'founding_publication_number': {
            'GET': 'FoundingPublicationNumber',
            'POST': None,
            'PUT': 'FoundingPublicationNumber'
        },
        'subscribed_capital': {
            'GET': 'SubscribedCapital',
            'POST': None,
            'PUT': 'SubscribedCapital'
        },
        'sub_capital_currency': {
            'GET': 'SubCapitalCurrency',
            'POST': None,
            'PUT': None
        },
        'sub_capital_currency_id': {
            'GET': 'SubCapitalCurrencyId',
            'POST': None,
            'PUT': 'SubCapitalCurrency'
        },
        'paid_up_capital': {
            'GET': 'PaidUpCapital',
            'POST': None,
            'PUT': 'PaidUpCapital'
        },
        'capital_fully_paid_up': {
            'GET': 'CapitalFullyPaidUp',
            'POST': None,
            'PUT': 'CapitalFullyPaidUp'
        },
        'bankruptcy': {
            'GET': 'Bankruptcy',
            'POST': None,
            'PUT': 'Bankruptcy'
        },
        'date_bankruptcy': {
            'GET': 'DateBankruptcy',
            'POST': None,
            'PUT': 'DateBankruptcy'
        },
        'annual_account': {
            'GET': 'AnnualAccount',
            'POST': None,
            'PUT': None
        },
        'annual_account_type': {
            'GET': 'AnnualAccountType',
            'POST': None,
            'PUT': None
        },
        'annual_account_scheme': {
            'GET': 'AnnualAccountScheme',
            'POST': None,
            'PUT': None
        },
        'annual_account_consolidated': {
            'GET': 'AnnualAccountConsolidated',
            'POST': None,
            'PUT': 'AnnualAccountConsolidated'
        },
        'annual_account_consolidated_type': {
            'GET': 'AnnualAccountConsolidatedType',
            'POST': None,
            'PUT': None
        },
        'annual_account_where': {
            'GET': 'AnnualAccountWhere',
            'POST': None,
            'PUT': None
        },
        'annual_account_date_last_deposit': {
            'GET': 'AnnualAccountDateLastDeposit',
            'POST': None,
            'PUT': None
        },
        'method_of_deposit': {
            'GET': 'MethodOfDeposit',
            'POST': None,
            'PUT': 'MethodOfDeposit'
        },
        'method_of_deposit_id': {
            'GET': 'MethodOfDepositId',
            'POST': None,
            'PUT': None
        },
        'date_draft_annual_accounts': {
            'GET': 'DateDraftAnnualAccounts',
            'POST': None,
            'PUT': 'DateDraftAnnualAccounts'
        },
        'general_meeting': {
            'GET': 'GeneralMeeting',
            'POST': None,
            'PUT': 'GeneralMeeting'
        },
        'general_meeting_formula': {
            'GET': 'GeneralMeetingFormula',
            'POST': None,
            'PUT': 'GeneralMeetingFormula'
        },
        'general_meeting_description': {
            'GET': 'GeneralMeetingDescription',
            'POST': None,
            'PUT': None
        },
        'general_meeting_saturday_is_workday': {
            'GET': 'GeneralMeetingSaturdayIsWorkday',
            'POST': None,
            'PUT': 'GeneralMeetingSaturdayIsWorkday'
        },
        'general_meeting_when_holiday': {
            'GET': 'GeneralMeetingWhenHoliday',
            'POST': None,
            'PUT': None
        },
        'general_meeting_location': {
            'GET': 'GeneralMeetingLocation',
            'POST': None,
            'PUT': 'GeneralMeetingLocation'
        },
        'general_meeting_hour': {
            'GET': 'GeneralMeetingHour',
            'POST': None,
            'PUT': 'GeneralMeetingHour'
        },
        'general_meeting_calling_by': {
            'GET': 'GeneralMeetingCallingBy',
            'POST': None,
            'PUT': None
        },
        'general_meeting_calling_how': {
            'GET': 'GeneralMeetingCallingHow',
            'POST': None,
            'PUT': None
        },
        'lei_number': {
            'GET': 'LeiNumber',
            'POST': None,
            'PUT': 'LeiNumber'
        },
        'lei_valid_until': {
            'GET': 'LeiValidUntil',
            'POST': None,
            'PUT': 'LeiValidUntil'
        },
        'social_goal': {
            'GET': 'SocialGoal',
            'POST': None,
            'PUT': 'SocialGoal'
        },
        'remarks': {
            'GET': 'Remarks',
            'POST': None,
            'PUT': 'Remarks'
        }
    })
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        super().__init__(client_credentials=client_credentials, 
                         endpoint='juridical', 
                         primary_property='customer_id', 
                         payload=payload,
                         endpoint_parent='customers',
                         parent_id_property='customer_id',
                         endpoint_suffix='juridical',
                         child_id_property='',
                         datetime_properties=['closing_date_first_year', 'date_share_register', 'founding_date', 'founding_date_publication', 'founding_date_filing', 'company_duration_end_date', 'date_bankruptcy', 'annual_account_date_last_deposit', 'date_draft_annual_accounts'])
        
    #IMPROV# Overriding _get_entity() because there is no cross customer query to get juridical details of all customers
    def _get_entity(self, id):

        object, _ = self._execute_request(method='get', endpoint=str('{}/{}/{}'.format(self._endpoint_parent, id, self._endpoint_suffix)))
        return object
    
    def create(self):

        raise AttributeError('Cannot execute POST request on \'{}\' endpoint. '.format(self._endpoint))
    
    def delete(self):

        raise AttributeError('Cannot execute DELETE request on \'{}\' endpoint. '.format(self._endpoint))