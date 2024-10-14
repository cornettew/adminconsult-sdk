from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.lists import NamedList, ListItem
    
class AccountancySoftwares(NamedList):

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials, list_name='accountancysoftwares')
    
class AuthorizationKinds(NamedList):

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials, list_name='authorizationkinds')
    
class AuthorizationTypes(NamedList):

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials, list_name='authorizationtypes')
    
class ContactFunctions(NamedList):

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials, list_name='contactfunctions')
    
class CustomerCrmTypes(NamedList):

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials, list_name='customercrmtypes')
    
class CustomerGroups(NamedList):

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials, list_name='customergroups')


class CustomerLinkListItem(ListItem):
    '''
    Capture the data of one list element.
    '''

    def __init__(self, item_data: dict) -> None:

        # Interpret values
        self.item_id = item_data['CustomerLinkTypeId']
        self.item_value = item_data['CustomerLinkTypeDescription']

class CustomerLinkTypes(NamedList):

    def set_attributes(self, payload: dict):

        for val in payload:
            self._client_credentials.lists = (self.list_id, CustomerLinkListItem(val))

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials, list_name='customerlinktypes')
