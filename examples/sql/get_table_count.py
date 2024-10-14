from examples.sql.auth.auth import get_cred
from adminconsult.sql import DbEngine

admin_cred_sql = get_cred()
admin_db = DbEngine(admin_cred_sql)

table_name = 'SYNETON_TASKFLOW_CUSTOMER_SCHEDULE'

df_table = admin_db.sql_query_df('''
                                 SELECT COUNT(*) AS COUNT
                                 FROM DBA.{}
                                 -- WHERE PROJECT_ID = 15103 
                                 '''.format(table_name))

print('{} rows in table \'{}\''.format(df_table['COUNT'].iloc[0], table_name))
