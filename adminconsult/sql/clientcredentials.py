from abc import abstractmethod, ABC
import os
import json
import hvac

import sqlalchemy as sa
import sqlalchemy.orm as saorm

class ClientCredentials(ABC):

    def __init__(self):
        """
        Client credentials localising the Admin Consult system and storing access keys.
        """

        self._read_tokens()
        
        # Use this to print verbose logs
        self.debug = False

    @property
    def driver(self):
        return self._driver

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def db_name(self):
        return self._db_name

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @abstractmethod
    def _read_tokens(self):
        # Develop the reading of tokens from a json file/database or any other source
        raise NotImplementedError()


class ClientCredentialsJsonFile(ClientCredentials):

    def __init__(self, file_path):
        '''
        Describe which key should be in de .json file
        * driver
        * host
        * port
        * db_name
        * username
        * password
        '''

        self._file_path = file_path
        super().__init__()

    @property
    def file_path(self):
        return self._file_path

    def _read_tokens(self):
        with open(self.file_path, mode='r', encoding='utf-8') as credentials_file:
            credentials = json.load(credentials_file)

        # Read Only properties
        self._driver = credentials['driver']
        self._host = credentials['host']
        self._port = credentials['port']
        self._db_name = credentials['db_name']
        self._username = credentials['username']
        self._password = credentials['password']


class ClientCredentialsHvac(ClientCredentials):
    '''
    Admin Consult credentials object using HashiCorp Vault.

    Parameters
    ----------
    token: str
        Access token for HashiCorp Vault instance
    

    Returns
    -------
    

    See Also
    --------
    

    Examples
    --------

    '''

    def __init__(self, url: str, token: str, mount_point: str = '', path: str = 'adminconsult_sql', cert: str = None):
        
        self.client = hvac.Client(
            url=url,
            token=token,
            cert=cert
        )

        self.mount_point = mount_point
        self.path = path

        super().__init__()

    def _read_tokens(self):

        read_response = self.client.secrets.kv.v2.read_secret_version(mount_point=self.mount_point, path=self.path)

        self._driver = 'sqlalchemy_sqlany'  #read_response['data']['metadata']['custom_metadata']['host']
        self._host = read_response['data']['metadata']['custom_metadata']['host']
        self._port = read_response['data']['metadata']['custom_metadata']['port']
        self._db_name = 'adminconsult' #read_response['data']['metadata']['custom_metadata']['host']
        self._username = read_response['data']['metadata']['custom_metadata']['username']
        self._password = read_response['data']['data']['password']
