# Admin Consult Python SDK

[![Syneton Hermes Consult API Version](https://img.shields.io/badge/Syneton_Hermes_Consult_API-1.2.2-blue)](http://consultapi.syneton.be:2100/doc#/)

This sdk implements interaction with a <a href="https://www.syneton.be/admin-en-admin-consult" target="_blank">Syneton Admin Consult</a> client via the API endpoints as well as via direct SQL access.

## Support

For support on this Python library or questions regarding interfacing options with Admin Consult, please contact [ward.cornette@num3rix.fr](mailto:ward.cornette@num3rix.fr).

## Example usage REST API

To setup and configure the Admin Consult REST API, please consult the [documentation by Syneton](https://syneton.zendesk.com/hc/nl/articles/360015107099-Admin-IS-Admin-Consult-API-activatie-en-configuratie).

``` python
from examples.api.auth.auth import get_cred
from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.customer import Customer

admin_cred: ClientCredentials = get_cred()

# Get one customer
admin_customer = Customer(admin_cred)
admin_customer.get(id=9580)
print(admin_customer.name)
```

## Example usage SQL

For use of SQL implementation, you must have SQL Anywhere driver installed: [download SQL Anywhere (Sybase)](https://help.sap.com/docs/SUPPORT_CONTENT/sqlany/3362971128.html). Also, you need to request a DB user with read access via [Syneton Support](https://syneton.zendesk.com/).

``` python
from examples.sql.auth.auth import get_cred
from adminconsult.sql import DbEngine

admin_cred_sql = get_cred()
admin_db = DbEngine(admin_cred_sql)

df_customers = admin_db.sql_query_df('''
                                     SELECT *
                                     FROM DBA.CUSTOMER c
                                     WHERE c.COMPANY LIKE '%A' ''')

print('{} customers'.format(df_customers.shape[0]))
``` 

## Authentication methods

Use or create a subclass of the `ClientCredentials` class for API or SQL authentication. This object reads and writes tokens using external storage.

Use one of the pre-implemented storage methods:

* json file
* hvac vault

## Run examples

The examples in this repo use credentials stored in a local json files. Create a `.env` file which contains the path to the folder with these local json files. The .env file should look like this:

```
credentials_dir='C:\..'
```

# API dependant improvements

Developments which might be improved but require an extension/change of the Admin Consult API are marked with `#IMPROV#`

<!-- # Postman collection

Include in repository ? -->
