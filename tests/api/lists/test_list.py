import os
import json

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.lists import List, ListList, ListItem

def test_get_lists(client_credentials: ClientCredentials):
    # This test assumes there is at least on list defined in the system.

    admin_lists = ListList(client_credentials)

    admin_lists.get()

    assert isinstance(admin_lists[0], List)
    

def test_get_listitems(client_credentials: ClientCredentials):
    # This test assumes there is at least on list defined in the system and there is at least one item defined in that list.

    admin_lists = ListList(client_credentials)
    admin_lists.get()

    admin_list = List(client_credentials, list_id=admin_lists[0].list_id)
    admin_list.get()

    # Test if list items are stored in session variable (client_credentials)
    assert isinstance(list(client_credentials._lists.values())[0][0], ListItem)
    

def test_get_listitem_id(client_credentials: ClientCredentials):
    # This test assumes there is at least on list defined in the system and there is at least one item defined in that list.

    # Get all lists
    admin_lists = ListList(client_credentials)
    admin_lists.get()

    # Load items for first list
    admin_list = List(client_credentials, list_id=admin_lists[0].list_id)
    admin_list.get()

    # Get key for the first item in that list based on its value
    assert isinstance(admin_list.get_item_id(item_value=list(client_credentials._lists.values())[0][0].item_value), int)
    