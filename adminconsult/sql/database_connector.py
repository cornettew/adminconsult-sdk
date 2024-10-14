import pandas as pd
from datetime import datetime
import sqlalchemy as sa
from sqlalchemy_sqlany.base import SQLAnyDialect
# import sqlanydb
from adminconsult.sql import ClientCredentials

class DbEngine():

    def __init__(self, client_credentials: ClientCredentials) -> None:
        """
        SQL Anywhere Database: https://help.sap.com/doc/9457f880abbe4bc8bebc18109daae0ca/17.0/en-US/SQL-Anywhere-Server-Programming-en.pdf ($1.15.4)

        Requirements to set up connections using SQLAlchemy
        * specific dialect: sqlalchemy-sqlany (available on PyPi: https://pypi.org/project/sqlalchemy-sqlany/)
        * SQL Anywhere Python driver, which is included in the SQL Anywhere install, but it is also available from https://github.com/sqlanywhere/sqlanydb

        """

        self._client_credentials = client_credentials

        # Initialize the ODBC connection
        self.__url = '{}://{}:{}@{}:{}/{}'.format(self._client_credentials.driver, 
                                                self._client_credentials.username, 
                                                self._client_credentials.password, 
                                                self._client_credentials.host, 
                                                self._client_credentials.port, 
                                                self._client_credentials.db_name
                                                )
        SQLAnyDialect.supports_statement_cache = False
        self.__engine = sa.create_engine(self.__url, pool_pre_ping=True)
        
        if self._client_credentials.debug:
            print('Established Admin Consult ODBC connection {{Host: {}, Driver: {}}}'.format(self._client_credentials.host, self._client_credentials.driver))
        
        # Set encoding
        # self.__cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='ISO-8859-1')
        # self.__cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='ISO-8859-1')
        # self.__cnxn.setencoding(encoding='ISO-8859-1')
        # pyodbc.setDecimalSeparator('.')

    def sql_query_df(self, query):
       
        connection = self.__engine.connect()
        df =  pd.DataFrame(connection.execute(sa.text(query)))
        connection.close()
        
        return df

    def sql_update_query(self, query):
       
        connection = self.__engine.connect()
        connection.execute(sa.text(query))
        connection.close()

    def _get_max_logid(self):

        df_logs = self.sql_query_df('''
                        SELECT MAX(LOGID) AS LOGID
                        FROM DBA.SYNETON_LOGTABLE_DATA
                        ''')
        
        return df_logs['LOGID'][0]

    def get_logs(self, last_logs_limit=10000, person_id: int=None, dbuser: str=None, table_name: str=None, column_name: str=None, date_action_from: datetime=None, date_action_until: datetime=None, output='dataframe', print_limit=10):
        '''
        last_logs_limit: 
            Improves search efficiency by only search most recents logs
        output:
            Set output method. Allowed values = ['dataframe', 'print']
        '''

        last_logs_id_start = self._get_max_logid() - last_logs_limit

        filters = ['LOGID >= {}'.format(last_logs_id_start)]
        
        if person_id:
            filters += ['PERSON_ID = {}'.format(person_id)]
        if dbuser:
            filters += ['DBUSER = \'{}\''.format(dbuser)]
        if table_name:
            filters += ['TABLE_NAME = \'{}\''.format(table_name)]
        if column_name:
            filters += ['COLUMN_NAME = \'{}\''.format(column_name)]
        if date_action_from:
            filters += ['DATE_ACTION > \'{}\''.format(date_action_from.strftime('%Y-%m-%d %H:%M:%S'))]
        if date_action_until:
            filters += ['DATE_ACTION < \'{}\''.format(date_action_until.strftime('%Y-%m-%d %H:%M:%S'))]

        df_logs = self.sql_query_df('''
                        SELECT *
                        FROM DBA.SYNETON_LOGTABLE_DATA
                        WHERE {}
                        ORDER BY LOGID DESC
                        '''.format(' AND '.join(filters)))
        
        if output == 'dataframe':
            return df_logs
        elif output == 'print':
            for _, row in df_logs[:print_limit].iterrows():
                print('{:<30}\t\t{:<80}{:<}'.format(row['DATE_ACTION'], '{} on {}-{}'.format(row['ACTIONTYPE'], row['TABLE_NAME'], row['COLUMN_NAME']), '[\'{}\' -> \'{}\']'.format(row['OLD_VALUE'], row['NEW_VALUE'])))
        else:
            raise Exception('Invalid output method \'{}\''.format(output))
