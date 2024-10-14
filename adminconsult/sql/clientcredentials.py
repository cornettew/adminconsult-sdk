from abc import abstractmethod, ABC
import os
import json

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
