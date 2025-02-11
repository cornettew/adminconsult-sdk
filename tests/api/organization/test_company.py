import os
import json

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.organization import Company, CompanyList


def test_get_companies(client_credentials: ClientCredentials):

    admin_companies = CompanyList(client_credentials)
    admin_companies.get(max_results=1250)

    if admin_companies.count > 0:
        admin_companies[0].refresh()
        company_id = admin_companies[0].company_id

        admin_company = Company(client_credentials)
        admin_company.get(company_id)
        assert admin_companies[0] == admin_company
    else:
        # No companies found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

