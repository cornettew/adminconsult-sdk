from typing import Iterator
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.entity import Entity

from datetime import datetime

class Juridical(Entity):
    
    def __init__(self, client_credentials: ClientCredentials, payload=None):

        self.customer_id = None
        self.new_company_law = None
        self.closing_date = None
        self.closing_date_first_year = None
        self.commercial_court = None
        self.commercial_court_id = None
        self.share_register = None
        self.date_share_register = None
        self.founding_date = None
        self.founding_date_publication = None
        self.founding_date_filing = None
        self.last_amendments_to_constitutions = None
        self.company_duration_limited = None
        self.company_duration_end_date = None
        self.founding_publication_number = None
        self.subscribed_capital = None
        self.sub_capital_currency = None
        self.sub_capital_currency_id = None
        self.paid_up_capital = None
        self.capital_fully_paid_up = None
        self.bankruptcy = None
        self.date_bankruptcy = None
        self.annual_account = None
        self.annual_account_type = None
        self.annual_account_scheme = None
        self.annual_account_consolidated = None
        self.annual_account_consolidated_type = None
        self.annual_account_where = None
        self.annual_account_date_last_deposit = None
        self.method_of_deposit = None
        self.method_of_deposit_id = None
        self.date_draft_annual_accounts = None
        self.general_meeting = None
        self.general_meeting_formula = None
        self.general_meeting_description = None
        self.general_meeting_saturday_is_workday = None
        self.general_meeting_when_holiday = None
        self.general_meeting_location = None
        self.general_meeting_hour = None
        self.general_meeting_calling_by = None
        self.general_meeting_calling_how = None
        self.lei_number = None
        self.lei_valid_until = None
        self.social_goal = None
        self.remarks = None

        property_mapping = dict({
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

        super().__init__(client_credentials=client_credentials, 
                         endpoint='juridical', 
                         primary_property='customer_id', 
                         property_mapping=property_mapping, 
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