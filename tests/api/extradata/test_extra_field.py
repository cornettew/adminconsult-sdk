from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.extrafield import ExtraTableList
from adminconsult.api.extrafield import ExtraData, ExtraDataList, ExtraField

def test_get_extra_data(client_credentials: ClientCredentials):

    extra_tables = ExtraTableList(client_credentials)
    extra_tables.get()

    if extra_tables.count > 0:
        extra_table_id = extra_tables[0].extra_table_id
        extra_data = ExtraDataList(client_credentials, table_id=extra_table_id)

        extra_data.get()

        if extra_data.count > 0:
            assert type(extra_data[0]) == ExtraData

            if len(extra_data[0]._fields) > 0:
                assert isinstance(list(extra_data[0]._fields.values())[0], ExtraField)
                assert isinstance(list(extra_data[0]._fields.values())[0]._label, str)
        else:
            # No extra data found in first extra_table found. Assume the system is empty.
            assert client_credentials.calls_throttling_count > 0


    else:
        # No extra tables found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

def test_post_extra_field(client_credentials: ClientCredentials):

    extra_tables = ExtraTableList(client_credentials)
    extra_tables.get()

    if extra_tables.count > 0:
        extra_table_id = extra_tables[0].extra_table_id
        extra_data = ExtraDataList(client_credentials, table_id=extra_table_id)

        extra_data.get()

        if extra_data.count > 0:
            assert type(extra_data[0]) == ExtraData

            if len(extra_data[0]._fields) > 0:
                # Update field value with same value
                list(extra_data[0]._fields.values())[0].update(value=list(extra_data[0]._fields.values())[0].value)
                list(extra_data[0]._fields.values())[0].refresh()
        else:
            # No extra data found in first extra_table found. Assume the system is empty.
            assert client_credentials.calls_throttling_count > 0


    else:
        # No extra tables found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

def test_post_extra_record(client_credentials: ClientCredentials):

    pass