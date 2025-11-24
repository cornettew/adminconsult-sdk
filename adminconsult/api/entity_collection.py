from typing import List
from abc import abstractmethod
from adminconsult.api.base import Base
from adminconsult.api.clientcredentials import ClientCredentials

import warnings
import pandas as pd
from datetime import datetime

class EntityCollection(Base):

    _collection: list

    def __init__(self, client_credentials: ClientCredentials, endpoint, on_max='ignore', technical_max_results=999999, on_technical_max='raise', payload: List[dict] = None):   #, entity: Entity

        super().__init__(client_credentials=client_credentials)

        self._endpoint = endpoint
        self._on_max = on_max
        self._technical_max_results = technical_max_results
        self._on_technical_max = on_technical_max

        self._collection = []
        self._load_search_parameters()

        if isinstance(payload, list):
            for entity in payload:
                self._add(payload=entity)

    def __iter__(self):
        return self._collection.__iter__()
    
    def __getitem__(self, item):
        return self._collection[item]

    @property
    def count(self):
        return len(self._collection)

    def _search_entity(self, url_filter, max_results) -> List[dict]:

        # Alway requests lists with paging enabled. If the endpoint doesn't support paging is will return all results anyway.
        objects, _ = super()._execute_request(method='get', endpoint=self._endpoint, querystring=url_filter, use_paging=True, max_results=max_results)

        return objects

    def _erase_collection(self):

        self._collection = []

    def to_json(self) -> list:

        return [obj.to_json() for obj in self._collection]

    def to_dataframe(self) -> pd.DataFrame:

        if len(self.to_json()) > 0:
            return pd.DataFrame(self.to_json())
        else:
            return pd.DataFrame([], columns=[k for k in self._search_parameters])
    
    def _format_filter_value(self, value):

        ## Format filter_value
        if isinstance(value, str):
            return '\'{}\''.format(value)
        elif isinstance(value, datetime):
            return value.strftime('\'%Y-%m-%d %H:%M:%S\'')
        elif isinstance(value, bool):
            # Convert to 0 or 1
            return int(value)
        else:
            return value

    def _generate_url_filter(self, **value_filters):

        # Apply filters on GET method
        filters = []

        # Interpret and verify filters
        # https://syneton.zendesk.com/hc/nl/articles/360017252439-Admin-IS-Admin-Consult-API-Werking-voor-de-Softwareleverancier#h_01EH216FCGKKEQ2HD24B6KK4EC
        for k, value in value_filters.items():
            ## Interpret kwarg
            try:
                operator = str(k).split('__')[0]
                attribute = str(k).split('__')[1]
            except IndexError:
                raise IndexError('Make sure the value_filters follow the structure \'operator__attribute_name\'. Got filter keyword \'{}\''.format(k))

            # Format filter values
            if isinstance(value, list):
                for i in range(len(value)):
                    value[i] = self._format_filter_value(value[i])
                value = '({})'.format(', '.join([str(v) for v in value]))
            else:
                value = self._format_filter_value(value)

            ## Construct URL filter
            try:
                if operator in ['eq', 'ne', 'ge', 'gt', 'le', 'lt', 'in', 'not_in']:
                    filters += ['{} {} {}'.format(self._search_parameters[attribute], operator.replace('_', ' '), value)]
                elif operator == 'null':
                    if isinstance(bool(value), bool):
                        if bool(value):
                            filters += ['{} is null'.format(self._search_parameters[attribute])]
                        else:
                            filters += ['{} is not null'.format(self._search_parameters[attribute])]
                    else:
                        raise Exception('Set a bool value for a \'null__\' filter. Got a \'{}\' value.'.format(type(value)))
                elif operator == 'startswith':
                    filters += ['StartsWith({}, {})'.format(self._search_parameters[attribute], value)]
                elif operator == 'endswith':
                    filters += ['EndsWith({}, {})'.format(self._search_parameters[attribute], value)]
                elif operator == 'contains':
                    filters += ['Contains({}, {})'.format(self._search_parameters[attribute], value)]
                # elif operator == 'like':
                #     filters += ['{} like {}'.format(self._search_parameters[attribute], value)]
                else:
                    raise Exception('Filter operater must be one of [\'eq\', \'ne\', \'ge\', \'gt\', \'le\', \'lt\', \'in\', \'not_in\', \'null\', \'startswith\', \'endswith\', \'contains\']. Got \'{}\''.format(operator))
            except KeyError:
                raise AttributeError('{} has no attribute \'{}\'. Therefore the url filter \'{}\' cannot work.'.format(self.__class__.__name__, attribute, k))

        if any(filters):
            return 'Filter={}'.format(' and '.join(filters))
        else:
            return None

    # Always override this method. With our without value_filters if parameter filter is allowed.
    @abstractmethod
    def get(self, max_results, erase_former=True, on_max=None, on_technical_max=None, **value_filters):
        '''
        value_filters: Use prefix [eq, ne, gt, lt, ge, le, in, not_in] followed by '__property_name'
        erase_former, default = True: first erase all previous results.
        on_max: ['raise', 'warn', 'ignore'], defaults to cass setting
        on_technical_max: ['raise', 'warn', 'ignore'], defaults to cass setting
        '''

        # Warn if more results are requested than technically allowed
        if max_results > self._technical_max_results:
            warnings.warn('The \'{}\' endpoint only allows for a technical maximum of {} results returned. Use filters for a more specific search and avoid having unreported {} by exceeding this technical maximum.'.format(self._endpoint, self._technical_max_results, self._endpoint))

        if erase_former:
            self._erase_collection()

        objs = self._search_entity(url_filter=self._generate_url_filter(**value_filters), max_results=max_results)

        for obj in objs:
            self._add(obj)

        # Test if maximum results are exceeded and report so if requested.
        if on_max is None:
            on_max = self._on_max
        self._test_max_result_limit(self.count, max_results, on_max, query=str(self._generate_url_filter(**value_filters) or ''))

        # Test if maximum results are exceeded and report so if requested.
        if on_technical_max is None:
            on_technical_max = self._on_technical_max
        self._test_max_result_limit(self.count, self._technical_max_results, on_technical_max, query=str(self._generate_url_filter(**value_filters) or ''))

    def _test_max_result_limit(self, count, max, on_max, query):

        if on_max == 'ignore':
            pass
        elif on_max == 'raise' and count >= max:
            raise Exception('Reached maximum result. Reported list of \'{}\' within queryfilters \'{}\' is incomplete !'.format(self._endpoint, query))
        elif on_max == 'warn' and self.count >= max:
            warnings.warn('Reached maximum changes. Reported list of \'{}\' within queryfilters \'{}\' is incomplete !'.format(self._endpoint, query))
        elif self.count >= max:
            raise Exception('Agument \'on_max\' must be one of [\'raise\', \'warn\', \'ignore\']. Got \'{}\''.format(on_max))

    @abstractmethod
    def _add(self):
        ...

    @abstractmethod
    def _load_search_parameters(self, k, v):
        self._search_parameters = {}