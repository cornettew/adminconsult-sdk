from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.lists import List

class Titles(List):

    def __init__(self, client_credentials: ClientCredentials):

        super().__init__(client_credentials=client_credentials, list_id=2)
    
    def to_dict(self):
        '''
        Return two dicts. One with titles for companies and one for persons
        '''

        titles_company = dict({item.item_id: item.item_value for item in self._client_credentials.get_list(self.list_id) if item.legal_form == 'Company'})
        titles_person = dict({item.item_id: item.item_value for item in self._client_credentials.get_list(self.list_id) if item.legal_form == 'Person'})

        return titles_company, titles_person

    def get_item_value(self, item_id, is_company, refresh=False):

        # Read list if still empty or if refresh requested
        if not any(self._client_credentials.get_list(self.list_id)) or refresh:
            self.get()

        if is_company:
            legal_form = 'Company'
        else:
            legal_form = 'Person'

        filtered_items = [item for item in self._client_credentials.get_list(self.list_id) if (item.item_id == item_id and item.legal_form == legal_form)]
        
        if len(filtered_items) == 1:
            return filtered_items[0].item_value
        else:
            raise Exception('Found {} items with id \'{}\' in list Titles for legal form = \'{}\''.format(len(filtered_items), item_id, legal_form))

    def get_item_id(self, item_value, is_company, refresh=False):

        # Read list if still empty or if refresh requested
        if not any(self._client_credentials.get_list(self.list_id)) or refresh:
            self.get()

        if is_company:
            legal_form = 'Company'
        else:
            legal_form = 'Person'

        filtered_items = [item for item in self._client_credentials.get_list(self.list_id) if (item.item_value == item_value and item.legal_form == legal_form)]
        
        if len(filtered_items) == 1:
            return filtered_items[0].item_id
        else:
            raise Exception('Found {} items with value \'{}\' in list Titles for legal form = \'{}\''.format(len(filtered_items), item_value, legal_form))