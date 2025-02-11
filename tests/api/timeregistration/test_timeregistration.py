import os
import json
from datetime import datetime, date, time
from dateutil.parser import isoparse

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.timeregistration import Timeregistration, TimeregistrationList

def test_get_timeregistration(client_credentials: ClientCredentials):

    timeregistrations = TimeregistrationList(client_credentials)
    timeregistrations.get(max_results=1250)

    if timeregistrations.count > 0:
        timeregistrations[0].refresh()
        timeregistration_id = timeregistrations[0].timeregistration_id

        timeregistration = Timeregistration(client_credentials)
        timeregistration.get(timeregistration_id)
        assert timeregistrations[0] == timeregistration
    else:
        # No timeregistrations found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

def test_create_timeregistration(client_credentials: ClientCredentials):

    timeregistration = Timeregistration(client_credentials)

    # Read and set timeregistration data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'timeregistration', 'data', 'new_timeregistration.json'), mode='r', encoding='utf-8') as f:
        timeregistration_details: dict = json.load(f)
    timeregistration_details['time_from'] = time(int(timeregistration_details['time_from'].split(':')[0]), int(timeregistration_details['time_from'].split(':')[1]), int(timeregistration_details['time_from'].split(':')[2]))

    for k, v in timeregistration_details.items():
        setattr(timeregistration, k, v)
    
    timeregistration.create()

    for k in timeregistration._datetime_properties:
        timeregistration_details[k] = isoparse(timeregistration_details[k])

    # Get new timeregistration and veriry data
    timeregistration_new = Timeregistration(client_credentials)
    timeregistration_new.get(timeregistration.timeregistration_id)
    
    assert timeregistration_details == {k: v for k, v in timeregistration_new.to_json().items() if k in timeregistration_details.keys()}


def test_update_timeregistration(client_credentials: ClientCredentials):
    '''
    Create timeregistration, update field-by-field and compare on each update.
    Test if no other fields are implicitly modified when updating one specific field.
    '''
    admin_timeregistration = Timeregistration(client_credentials)

    # Read and set new_timeregistration data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'timeregistration', 'data', 'new_timeregistration.json'), mode='r', encoding='utf-8') as f:
        timeregistration_details = json.load(f)
    timeregistration_details['time_from'] = time(int(timeregistration_details['time_from'].split(':')[0]), int(timeregistration_details['time_from'].split(':')[1]), int(timeregistration_details['time_from'].split(':')[2]))

    for k, v in timeregistration_details.items():
        setattr(admin_timeregistration, k, v)
    
    admin_timeregistration.create()
    admin_timeregistration.refresh()

    # Read and set customer data to update
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'timeregistration', 'data', 'updated_timeregistration.json'), mode='r', encoding='utf-8') as f:
        timeregistration_update_details = json.load(f)
    timeregistration_update_details['time_from'] = time(int(timeregistration_update_details['time_from'].split(':')[0]), int(timeregistration_update_details['time_from'].split(':')[1]), int(timeregistration_update_details['time_from'].split(':')[2]))

    for k, new_value in timeregistration_update_details.items():
        # Store the to-be situation for comparison
        timeregistration_details_post = admin_timeregistration.to_json()
        timeregistration_details_post[k] = new_value
        del timeregistration_details_post['customer_id']; del timeregistration_details_post['time_to']; del timeregistration_details_post['date_registration']

        # Write to Admin Consult
        admin_timeregistration.update(**{k: new_value})
        admin_timeregistration.refresh()

        assert timeregistration_details_post == {k: v for k, v in admin_timeregistration.to_json().items() if k in timeregistration_details_post.keys()}

def test_invoice_timeregistration(client_credentials: ClientCredentials):

    timeregistration = Timeregistration(client_credentials)

    # Read and set timeregistration data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'timeregistration', 'data', 'new_timeregistration.json'), mode='r', encoding='utf-8') as f:
        timeregistration_details: dict = json.load(f)
    timeregistration_details['time_from'] = time(int(timeregistration_details['time_from'].split(':')[0]), int(timeregistration_details['time_from'].split(':')[1]), int(timeregistration_details['time_from'].split(':')[2]))

    for k, v in timeregistration_details.items():
        setattr(timeregistration, k, v)
    
    timeregistration.create()

    for k in timeregistration._datetime_properties:
        timeregistration_details[k] = isoparse(timeregistration_details[k])

    # Get new timeregistration and veriry data
    timeregistration_new = Timeregistration(client_credentials)
    timeregistration_new.get(timeregistration.timeregistration_id)

    timeregistration_new.set_invoiced()
    timeregistration_details['invoice_id'] = -1
    
    assert timeregistration_details == {k: v for k, v in timeregistration_new.to_json().items() if k in timeregistration_details.keys()}

    timeregistration_new.clear_invoiced()
    timeregistration_details['invoice_id'] = None
    
    assert timeregistration_details == {k: v for k, v in timeregistration_new.to_json().items() if k in timeregistration_details.keys()}