# Admin Consult Python SDK

[![Syneton Hermes Consult API Version](https://img.shields.io/badge/Syneton_Hermes_Consult_API-1.2.2-blue)](http://consultapi.syneton.be:2100/doc#/)

Python SDK for accessing [Syneton Admin Consult](https://www.syneton.be/admin-en-admin-consult).

# Getting Started

This sdk allows to interact with an Admin Consult client via the API endpoints as well as via direct SQL access.

For use of SQL implementation, you must have SQL Anywhere driver installed: [download SQL Anywhere (Sybase)](https://help.sap.com/docs/SUPPORT_CONTENT/sqlany/3362971128.html).

## Example usage

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

# Postman collection

Include in repository ?
