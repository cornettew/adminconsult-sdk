from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.lists import NamedList, ListItem

class NaceCodes(NamedList):

    def __init__(self, client_credentials: ClientCredentials):
        super().__init__(client_credentials, list_name= "nacecodes")

    def set_attributes(self, payload: list[dict]):
        
        for idx, nace_code in enumerate(payload):
            nace_code.update({
                'ListValueId': idx+1,
                'ListValue': None,
                'ExtCode': None,
                'LegalForm': None
            })
            self._client_credentials.lists = (self.list_id, ListItem(self.list_id, nace_code))

    def get_nace_description(self, nace_code: str):

        nace_item: ListItem = self._get_item(nace_code=nace_code, refresh=False)

        return nace_item.nace_description