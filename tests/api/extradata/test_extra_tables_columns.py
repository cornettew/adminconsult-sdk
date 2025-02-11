from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.extrafield import ExtraTable, ExtraColumn
from adminconsult.api.extrafield import ExtraTableList, ExtraColumnList

def test_get_extra_tables(client_credentials: ClientCredentials):

    extra_tables = ExtraTableList(client_credentials)
    extra_tables.get()

    if extra_tables.count > 0:
        extra_table_id = extra_tables[0].extra_table_id

        extra_table = ExtraTable(client_credentials)
        extra_table.get(extra_table_id)
        assert extra_table.extra_table_id == extra_table_id
    else:
        # No extra tables found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

def test_get_extra_columns(client_credentials: ClientCredentials):

    extra_tables = ExtraTableList(client_credentials)
    extra_tables.get()

    if extra_tables.count > 0:
        extra_table_id = extra_tables[0].extra_table_id

        extra_columns = ExtraColumnList(client_credentials, extra_table_id=extra_table_id)
        extra_columns.get()

        if extra_columns.count > 0:
            extra_column_id = extra_columns[0].extra_column_id

            extra_column = ExtraColumn(client_credentials, extra_table_id=extra_table_id)
            extra_column.get(extra_column_id)
            
            assert extra_column._extra_table_id == extra_table_id
            assert extra_column.extra_column_id == extra_column_id
        else:
            # No extra columns found. Assume the extra table is empty.
            assert client_credentials.calls_throttling_count > 0
    else:
        # No extra tables found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0
