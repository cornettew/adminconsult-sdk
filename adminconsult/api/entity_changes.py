from abc import abstractmethod
from adminconsult.api.entity_collection import EntityCollection
from adminconsult.api.base import Base
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.admin import Change

from datetime import datetime, date, time
import warnings

class EntityChanges(Base):

    def __init__(self, client_credentials: ClientCredentials, 
                 endpoint: str, 
                 id_field_name: str,
                 
                 primary_property: str, 
                 primary_table: str, 
                 extra_tables: list = [], 
                 
                 on_max='ignore', 
                 on_technical_max='raise'):

        super().__init__(client_credentials=client_credentials)

        self._id_field_name = id_field_name
        self._endpoint = endpoint
        
        self._primary_property = primary_property
        self._primary_table = primary_table
        self._table_names = [self._primary_table] + extra_tables

        self._on_max = on_max
        self._technical_max_results = 1000
        self._on_technical_max = on_technical_max

        self.inserts: EntityCollection
        self.updates: EntityCollection
        self.deletes: list[int] = []
        self.related_delete_ids: dict = {}

    def _get_changes_datetime(self, date_from: datetime, date_until: datetime):

        changes, _ = self._execute_request(method='get', 
                                           endpoint=self._endpoint, 
                                           querystring='Filter=TableName in (\'{}\') and DateAction ge \'{}\' and DateAction lt \'{}\''.format(
                                               '\',\''.join(self._table_names),
                                               date_from.strftime('%Y-%m-%d %H:%M:%S'), 
                                               date_until.strftime('%Y-%m-%d %H:%M:%S')),
                                               use_paging=True
                                               )
        return changes

    def _get_changes_logid(self, ge__log_id: datetime, lt__log_id: datetime):

        changes, _ = self._execute_request(method='get', 
                                           endpoint=self._endpoint, 
                                           querystring='Filter=TableName in (\'{}\') and l.LogId ge {} and l.LogId lt {}'.format(
                                               '\',\''.join(self._table_names),
                                               ge__log_id, 
                                               lt__log_id),
                                               use_paging=True
                                               )
        return changes

    @abstractmethod
    def _erase_collection(self):

        self.inserts = []
        self.updates = []
        self.deletes = []

    def get(self, 
            date_from: datetime = None, 
            date_until: datetime = None, 
            ge__log_id: int = None, 
            lt__log_id: int = None,
            max_results=1000, erase_former=True, on_max=None, on_technical_max=None):

        # Warn if more results are requested than technically allowed
        if max_results > self._technical_max_results:
            warnings.warn('The \'{}\' endpoint only allows for a technical maximum of {} results returned. Use filters for a more specific search and avoid having unreported {} by exceeding this technical maximum.'.format(self._endpoint, self._technical_max_results, self._endpoint))

        if erase_former:
            self._erase_collection()

        if isinstance(date_from, datetime) and isinstance(date_from, datetime):
            changes = self._get_changes_datetime(date_from=date_from, date_until=date_until)
        elif isinstance(ge__log_id, int) and isinstance(lt__log_id, int):
            changes = self._get_changes_logid(ge__log_id, lt__log_id)
        else:
            raise ValueError('Must pass a set of [\'date_from\', \'date_until\'] or [\'ge__log_id\', \'lt__log_id\'] as arguments')

        # Test if maximum results are exceeded and report so if requested.
        if on_max is None:
            on_max = self._on_max
        self._test_max_result_limit(len(changes), max_results, on_max, date_from, date_until)

        # Test if maximum results are exceeded and report so if requested.
        if on_technical_max is None:
            on_technical_max = self._on_technical_max
        self._test_max_result_limit(len(changes), self._technical_max_results, on_technical_max, date_from, date_until)

        # # Remove entities which and created and deleted within the time interval
        # insert_delete_ids = [insert_id for insert_id in insert_ids if insert_id in delete_ids]
        # insert_ids = [insert_id for insert_id in insert_ids if insert_id not in insert_delete_ids]
        # delete_ids = [delete_id for delete_id in delete_ids if delete_id not in insert_delete_ids]

        self._load_admin_data(changes)

    def _load_admin_data(self, changes: list[dict]):

        insert_ids = [change[self._id_field_name] for change in changes if (change['ActionType'] == 'INSERT' and change['TableName'] == self._primary_table)]
        delete_ids = [change[self._id_field_name] for change in changes if (change['ActionType'] == 'DELETE' and change['TableName'] == self._primary_table)]
        related_delete_ids = {table_name: [change['OwnId'] for change in changes if (change['ActionType'] == 'DELETE' and change['TableName'] == table_name)] for table_name in list(set([change['TableName'] for change in changes if (change['ActionType'] == 'DELETE' and change['TableName'] != self._primary_table)]))}
        # Ignore updates for entities which are already marked for creation/deletion
        update_ids = list(set([change[self._id_field_name] for change in changes if change[self._id_field_name] not in insert_ids+delete_ids+[0]]))
        
        if len(insert_ids):
            self.inserts.get(**{'in__{}'.format(self._primary_property): insert_ids})
        if len(update_ids):
            self.updates.get(**{'in__{}'.format(self._primary_property): update_ids})
        self.deletes = delete_ids
        self.related_delete_ids = related_delete_ids

    def _test_max_result_limit(self, count, max, on_max, date_from: datetime, date_until: datetime):

        if on_max == 'ignore':
            pass
        elif on_max == 'raise' and count >= max:
            raise Exception('Reached maximum result. Reported list of \'{}\' changes from \'{}\' until \'{}\' is incomplete !'.format(self._endpoint, date_from.strftime('%Y-%m-%d %H:%M:%S'), date_until.strftime('%Y-%m-%d %H:%M:%S')))
        elif on_max == 'warn' and count >= max:
            warnings.warn('Reached maximum changes. Reported list of \'{}\' changes from \'{}\' until \'{}\' is incomplete !'.format(self._endpoint, date_from.strftime('%Y-%m-%d %H:%M:%S'), date_until.strftime('%Y-%m-%d %H:%M:%S')))
        elif count >= max:
            raise Exception('Agument \'on_max\' must be one of [\'raise\', \'warn\', \'ignore\']. Got \'{}\''.format(on_max))
