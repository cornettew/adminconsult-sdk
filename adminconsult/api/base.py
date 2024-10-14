import requests
import json
import time
import regex as re
from abc import ABC
from datetime import datetime, timedelta

from adminconsult.api import ClientCredentials

class Base(ABC):

    def __init__(self, client_credentials: ClientCredentials) -> None:

        self._client_credentials = client_credentials
                 
    def __get_access_token(self):

        # Refresh access token if expired
        self._client_credentials.authenticate()

        return self._client_credentials.access_token
    
    def __generate_request_url(self, endpoint, querystring=''):
        
        return '{}:{}/api/{}/{}?{}'.format(self._client_credentials.host, 
                                            self._client_credentials.port, 
                                            self._client_credentials._version, 
                                            endpoint, 
                                            querystring or '').rstrip('?')

    def _execute_request(self, method: str, endpoint, querystring=None, payload=None, headers=None, use_paging=False, max_results=100000):
        
        # Set headers
        headers = {'synetonToken' : self.__get_access_token()}
        if headers:
            headers.update(headers)
        
        self.__get_api_settings()
        self.__check_throttling_limit()

        # Update querystring with paging parameters
        if use_paging:
            querystring = '&'.join([str(i) for i in [querystring, 'per_page='+str(self._client_credentials._max_records_per_page)] if isinstance(i, str)])
        else:
            querystring = str(querystring or '')

        url = self.__generate_request_url(endpoint, querystring)

        if self._client_credentials.debug:
            print('{} {}'.format(method.upper(), url))

        if method.lower() == 'get':
            response = requests.get(url, headers=headers, json=payload)
        elif method.lower() == 'post':
            response = requests.post(url, headers=headers, json=payload)
        elif method.lower() == 'put':
            response = requests.put(url, headers=headers, json=payload)
        elif method.lower() == 'delete':
            response = requests.delete(url, headers=headers, json=payload)
        else:
            raise ValueError('Method argument must be one of: [\'get\', \'post\', \'put\', \'delete\']')
        
        try:
            return self.__interpret_response(response, method, endpoint, querystring, payload, headers, max_results)
        except json.decoder.JSONDecodeError:
            raise Exception('Admin Consult returned unstructured error message: \'{}\''.format(response.text))

    def __interpret_response(self, response: requests.Response, method: str, endpoint, querystring, payload, headers, max_results):

        # Successful responses
        if response.status_code >= 200 and response.status_code <= 203:

            # Test if paging is applied
            if method.lower() == 'get' and 'per_page' in querystring and max_results-len(response.json()) > 0 and 'link' in response.headers.keys():
                # Iterate the return links
                for link in re.finditer(r'<.+?>; rel=".+?",', response.headers['link']):
                    # Process 'next' page link
                    if re.compile(r'(?<=; rel=").+?(?=")').search(link.group()).group() == 'next':
                        next_page, _ = self._execute_request(method, 
                                                              endpoint, 
                                                              querystring=re.compile(r'(?<=<).+?(?=>)').search(link.group()).group().split('?')[1], 
                                                              payload=payload, 
                                                              headers=headers, 
                                                              use_paging=False, 
                                                              max_results=max_results-len(response.json()))
                        break
                    else:
                        next_page = []
                return response.json() + next_page, response.status_code #
            else:
                return response.json(), response.status_code
            
        if response.status_code == 204:
            return [], response.status_code
            
        # Catch false error in case of empty result
        elif response.status_code == 404 and any(msg in response.json()['ErrorMessage'].lower() for msg in ['nothing found', 'no extradata found', 'no taskdata found']):
            return [], 200

        elif method.lower() == 'delete':
            if response.status_code == 404 and any(msg in response.json()['ErrorMessage'].lower() for msg in ['nothing found']):
                return [], 200
            elif response.status_code == 400 and any(msg in response.json()['ErrorMessage'].lower() for msg in ['does not exist', 'taskflow customer can\'t be deleted']):
                 raise LookupError(response.json()['ErrorMessage'])
            elif response.json()['ErrorMessage']:
                raise Exception('Admin: ' + response.json()['ErrorMessage'])
            else:
                raise(Exception('Unknown Admin Exception: {} - {}'.format(response.status_code, response.json())))


        # Exception handling
        elif response.status_code == 403 and 'you are throttling the system' in response.json()['ErrorMessage'].lower():
            raise ConnectionError('Erreur de connexion (Admin): limite de demandes atteint.')
        elif response.status_code == 403 and 'no valid configuration for token' in response.json()['ErrorMessage'].lower():
            raise PermissionError('Erreur d\'autorisation (Admin):  {}.'.format(endpoint))
        elif response.status_code == 414:
            raise Exception('URI too long')
        elif type(response.json()) == list and response.json()[0]['ErrorMessage']:
            error_messages = ""
            for i in response.json():
                if i != response.json()[-1]:
                    error_messages = error_messages + i['ErrorMessage'] + ", "
                else:
                    error_messages = error_messages + i['ErrorMessage']
            raise Exception('Admin: ' + error_messages)
        elif response.json()['ErrorMessage']:
            raise Exception('Admin: ' + response.json()['ErrorMessage'])
        else:
            raise(Exception('Unknown Admin Exception: {} - {}'.format(response.status_code, response.json())))

    def __get_api_settings(self):

        # Only if settings are not yet loaded
        if not self._client_credentials.max_records_per_page:
        
            # Set headers
            headers = {'synetonToken' : self.__get_access_token()}

            self._client_credentials.calls_throttling_count = datetime.now()

            # Execute API Call
            url = self.__generate_request_url(endpoint='apisettings')
            if self._client_credentials.debug:
                print('{} {}'.format('GET', url))
            response = requests.get(url, headers=headers)
            
            # Process response
            if response.status_code == 200:
                self._client_credentials.set_api_settings(response.json())

            elif response.status_code == 403 and 'you are throttling the system' in response.json()['ErrorMessage'].lower():
                raise ConnectionError('Erreur de connexion (Admin): limite de demandes atteint.')
            elif response.json()['ErrorMessage']:
                raise ConnectionError(response.json()['ErrorMessage'])
            else:
                raise(Exception('Unknown Admin Exception: {} - {}'.format(response.status_code, response.json())))

    def __check_throttling_limit(self):

        self._client_credentials.calls_throttling_count = datetime.now()

        # Wait until below the limit
        while self._client_credentials.calls_throttling_count >= self._client_credentials._rate_limit:
            print('Throttling limit reached, waiting...')
            time.sleep(0.5)

    def print_logs(self):

        self._client_credentials.print_logs()