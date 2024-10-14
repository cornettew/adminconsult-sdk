from examples.sql.auth.auth import get_cred
from adminconsult.sql import DbEngine

admin_cred_sql = get_cred()
admin_db = DbEngine(admin_cred_sql)

df_customers = admin_db.sql_query_df('''
                                     SELECT *
                                     FROM DBA.CUSTOMER c
                                     WHERE c.COMPANY LIKE '%A' ''')

print('{} customers'.format(df_customers.shape[0]))
