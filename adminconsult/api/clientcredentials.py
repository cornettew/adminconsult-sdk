from datetime import datetime, timedelta
from dateutil import parser
from abc import abstractmethod, ABC
import requests
import time
import json

import os
import hvac
import sqlalchemy as sa
import sqlalchemy.orm as saorm

class ClientCredentials(ABC):

    def __init__(self):
        """
        Client credentials localising the Admin Consult system and storing access keys.
        """

        # Use this to print verbose logs
        self.debug = False

        self._version = 'v1'

        # _auth_in_process attribute prevents concurrency issues when tokens cannot be lock for reading/writing in the external source.
        self._auth_in_process = False
        self._credentials = None

        self._calls_throttling_count = []

        # Central storage of lists to avoid repeatedly reload the same list.
        self._lists = dict({})
        # Central storage of employees to avoid repeatedly reloading all employees.
        self._employees = []

        # API Settings
        self._default_records_per_page = None
        self._max_records_per_page = None
        self._duration_token = None
        self._rate_limit = None

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def api_key(self):
        return self._api_key

    @property
    def access_token(self):
        return self._access_token
    
    @access_token.setter
    def access_token(self, value):
        self._access_token = value

    @property
    def token_valid_until(self):
        return self._token_valid_until
    
    @token_valid_until.setter
    def token_valid_until(self, value):
        if isinstance(value, str):
            self._token_valid_until = parser.isoparse(value)
        elif isinstance(value, datetime):
            self._token_valid_until = value
        elif not value:
            # Set default value if not token value until is passed
            datetime(year=1900, month=1, day=1)
        else:
            TypeError('Argument \'token_valid_until\' must be of type datetime or a str representing a datetime. Got type {} with value \'{}\' instead'.format(type(value), value))
    
    @property
    def lists(self):
        return self._lists
    
    def get_list(self, list_id):
        return self._lists.get(list_id, [])
    
    @lists.setter
    def lists(self, new_item):
        list_id, list_item = new_item
        self._lists[list_id] += [list_item]
    
    def empty_list(self, list_id):
        self._lists[list_id] = []
    
    @property
    def employees(self):
        return self._employees
    
    @employees.setter
    def employees(self, list):
        self._employees = list

    @property
    def calls_throttling_count(self):

        # Remove timestamps which are not within the last minute
        self._calls_throttling_count = [x for x in self._calls_throttling_count if x > (datetime.now() - timedelta(seconds = 63))]

        return len(self._calls_throttling_count)

    @calls_throttling_count.setter
    def calls_throttling_count(self, timestamp):
        # Add new call timestamp
        self._calls_throttling_count = self._calls_throttling_count + [timestamp]
        
        # Remove timestamps which are not within the last minute
        self._calls_throttling_count = [x for x in self._calls_throttling_count if x > (datetime.now() - timedelta(seconds = 63))]

    # API Settings
    @property
    def default_records_per_page(self):
        return self._default_records_per_page
    @property
    def max_records_per_page(self):
        return self._max_records_per_page
    @property
    def duration_token(self):
        return self._duration_token
    @property
    def rate_limit(self):
        return self._rate_limit
    
    def set_api_settings(self, payload):
        self._default_records_per_page = payload['DefaultRecordsPerPage']
        self._max_records_per_page = payload['MaxRecordsPerPage']
        self._duration_token = payload['DurationToken']
        self._rate_limit = payload['RateLimit']

    def _return_tokens_dict(self):

        return dict({'host': self.host,
                     'port': self.port,
                     'api_key': self.api_key,
                     'access_token': self.access_token,
                     'token_valid_until': self.token_valid_until})

    @abstractmethod
    def _read_tokens(self):
        # Develop the reading of tokens from a json file/database or any other source
        raise NotImplementedError()
    
    @abstractmethod
    def _lock_tokens_external_source(self):
        '''
        Lock tokens and refresh
        e.g. lock row in database
        '''

        # Add steps in subclass to lock the transaction

        self._read_tokens()

    @abstractmethod
    def _write_tokens(self):
        # Writing new tokens to external source (json file/database/...)
        # This method is executed upon renewal of tokens by Base Class. method: self.authenticate()
        # Applications using this package should subclass this Class and override this method
        # * localdev/test: write to json
        # * webapplication: write to database
        # * etc.
        # Some examplary subclasses are foreseen in this packages
        raise NotImplementedError()
    
    @abstractmethod
    def _unlock_tokens_external_source(self):
        '''
        Write latest tokens to external source and unlock
        e.g. lock row in database
        '''

        self._write_tokens()
        # Add steps in subclass to unlock the transaction

    def _start_auth(self):
        '''
        Refresh tokens from source and prohibit new auth processes until this one completed.

        Raises a TimeOut if tokens are locked and not released 
        '''

        timeout_limit = 30

        start = time.time()
        while self._auth_in_process == True:
            if time.time() - start > timeout_limit:
                raise TimeoutError('Admin Consult tokens are locked. Starting authentication process timed out after {} seconds.'.format(timeout_limit))
            time.sleep(0.1)

        # Lock tokens
        self._auth_in_process == True

        # Refresh and lock tokens from external source.
        self._lock_tokens_external_source()


    def _stop_auth(self):
        '''
        Write tokens to external source and allow new auth processes.
        '''

        # Write tokens to external source and unlock.
        self._unlock_tokens_external_source()

        # Unlock tokens
        self._auth_in_process = False

    def authenticate(self):

        self._read_tokens()

        # Check if the current access_token is still live
        if (self.token_valid_until - timedelta(seconds=30) < datetime.now()):

            self._start_auth()

            if self.debug:
                print('Getting new Admin access_token...')
            self.calls_throttling_count = datetime.now()
            response = requests.get('{}:{}/api/{}/token/{}'.format(self.host, 
                                                                   self.port, 
                                                                   self._version, 
                                                                   self.api_key)
                                                                   )
            
            # Interpret response
            if response.status_code == 200:
                # Store the access_token and TimeToLive
                self.access_token = response.json()['TokenGuid']
                self.token_valid_until = response.json()['TimeToLive']
                if self.debug:
                    print('New Admin access_token retrieved')
                self._stop_auth()
            else:
                self._stop_auth()
                # Throw error as the connection failed
                raise ConnectionError('Admin Consult API connection error: {} - {}.'.format(response.status_code, response.json()))
        else:
            pass

    def print_logs(self):

        print('Executed {} API calls last 60 seconds [{} - {}]'.format(self.calls_throttling_count, 
                                                                       datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), 
                                                                       (datetime.now()+timedelta(seconds=-60)).strftime("%Y-%m-%dT%H:%M:%S")))


class ClientCredentialsJsonFile(ClientCredentials):
    '''
    Admin Conult credentials object using a local JSON file.
    The credentials are read from and written to this JSON file keeping the connection active.

    The JSON file should have this structure:

    {
        "host": "",
        "port": "",
        "api_key": "",
        "access_token": "",
        "token_valid_until": ""
    }

    Parameters
    ----------
    file_path: str
        Location of the .json file which holds the credentials.

    Returns
    -------
    

    See Also
    --------
    

    Examples
    --------

    '''

    def __init__(self, file_path):

        self._file_path = file_path
        super().__init__()

    @property
    def file_path(self):
        return self._file_path

    def _read_tokens(self):
        with open(self.file_path, mode='r', encoding='utf-8') as credentials_file:
            credentials = json.load(credentials_file)

        # Read Only properties
        self._host = credentials['host']
        self._port = credentials['port']
        self._api_key = credentials['api_key']

        # Read-Write properties
        if 'access_token' in credentials.keys():
            self.access_token = credentials['access_token']
        else:
            self.access_token = ''
        if 'token_valid_until' in credentials.keys():
            self.token_valid_until = credentials['token_valid_until']
        else:
            self.token_valid_until = datetime(1900, 1, 1)

    def _write_tokens(self):
        with open(self.file_path, mode='w', encoding='utf-8') as credential_file:
            json.dump(self._return_tokens_dict(), credential_file, indent=4, default=str)

    def _lock_tokens_external_source(self):
        # Note: there is no protection for concurrency issues caused by multiple processes working on the same json file.
        super()._lock_tokens_external_source()

    def _unlock_tokens_external_source(self):
        # Note: there is no protection for concurrency issues caused by multiple processes working on the same json file.
        super()._unlock_tokens_external_source()



class ClientCredentialsHvac(ClientCredentials):
    '''
    Admin Conult credentials object using a local JSON file.
    The credentials are read from and written to this JSON file keeping the connection active.

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

    def __init__(self, url: str, token: str, mount_point: str = '', path: str = 'adminconsult_api', cert: str = None):
        
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

        self._api_key = read_response['data']['data']['api_key']
        self._host = read_response['data']['metadata']['custom_metadata']['host']
        self._port = read_response['data']['metadata']['custom_metadata']['port']

        # Read-Write properties
        self.access_token = read_response['data']['data'].get('access_token', '')
        self.token_valid_until = read_response['data']['metadata']['custom_metadata'].get('token_valid_until', datetime(1900, 1, 1))

    def _write_tokens(self):

        self.client.secrets.kv.v2.create_or_update_secret(
            mount_point=self.mount_point, 
            path=self.path, 
            secret=dict(access_token=self.access_token, api_key=self.api_key),
            )
        
        self.client.secrets.kv.v2.update_metadata(
            mount_point=self.mount_point, 
            path=self.path, 
            custom_metadata={
                'host': self.host,
                'port': self.port,
                'token_valid_until': self.token_valid_until.isoformat()
            }
        )
        # with open(self.file_path, mode='w', encoding='utf-8') as credential_file:
        #     json.dump(self._return_tokens_dict(), credential_file, indent=4, default=str)

    def _lock_tokens_external_source(self):
        # Note: there is no protection for concurrency issues caused by multiple processes working on the same json file.
        super()._lock_tokens_external_source()

    def _unlock_tokens_external_source(self):
        # Note: there is no protection for concurrency issues caused by multiple processes working on the same json file.
        super()._unlock_tokens_external_source()