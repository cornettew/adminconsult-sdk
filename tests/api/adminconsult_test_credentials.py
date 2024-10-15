import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv('.env')

import pytest
from adminconsult.api import ClientCredentials

@pytest.fixture(scope='package')
def client_credentials() -> ClientCredentials:
    return ClientCredentialsTestCase()

class ClientCredentialsTestCase(ClientCredentials):
    '''
    Load Admin Consult API Credentials from Environment Variables.
    '''

    def __init__(self):
        self._host = os.environ.get('TESTCLIENT_API_HOST')
        self._port = os.environ.get('TESTCLIENT_API_PORT')
        self._api_key = os.environ.get('TESTCLIENT_API_KEY')
        self.access_token = ''
        self.token_valid_until = datetime(1900, 1, 1)

        super().__init__()

    def _read_tokens(self):
        ...

    def _write_tokens(self):
        ...

    def _lock_tokens_external_source(self):
        super()._lock_tokens_external_source()

    def _unlock_tokens_external_source(self):
        super()._unlock_tokens_external_source()