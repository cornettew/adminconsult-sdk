import os
import json

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.lists import Countries

def test_get_countries(client_credentials: ClientCredentials):
    # This test assumes there is at least on list defined in the system.

    admin_countries = Countries(client_credentials)

    admin_countries.get()

    assert admin_countries.get_country_code(22) == 'BE'
    assert admin_countries.get_country_name(74) == 'Frankrijk'
    assert admin_countries.get_country_id(country_code='BE') == 22
    assert admin_countries.get_country_id(country_name='Frankrijk') == 74