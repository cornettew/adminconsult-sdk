import os
import json
from time import sleep
from datetime import datetime, timedelta

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.taskflow import TaskFlowPlanned, TaskFlowPlannedList

def test_get_taskflow_planned(client_credentials: ClientCredentials):

    admin_taskflow_planned_list = TaskFlowPlannedList(client_credentials)
    admin_taskflow_planned_list.get(max_results=1250)

    if admin_taskflow_planned_list.count > 0:
        admin_taskflow_planned_list[0].refresh()
        task_planning_id = admin_taskflow_planned_list[0].task_planning_id

        admin_taskflow_planned = TaskFlowPlanned(client_credentials)
        admin_taskflow_planned.get(task_planning_id)
        assert admin_taskflow_planned_list[0] == admin_taskflow_planned
    else:
        # No admin_taskflow_planned found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

def test_create_taskflow_planned(client_credentials: ClientCredentials):

    admin_taskflow_planned = TaskFlowPlanned(client_credentials)

    # Read and set taskflow planned data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'taskflow', 'data', 'new_taskflow_planned.json'), mode='r', encoding='utf-8') as f:
        admin_taskflow_planned_details: dict = json.load(f)

    for k, v in admin_taskflow_planned_details.items():
        if k in admin_taskflow_planned._datetime_properties: 
            admin_taskflow_planned_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
        setattr(admin_taskflow_planned, k, v)
    
    admin_taskflow_planned.create()

    # Get new taskflow planned and verify data
    admin_taskflow_planned_new = TaskFlowPlanned(client_credentials)
    admin_taskflow_planned_new.get(admin_taskflow_planned.task_planning_id)
    
    assert admin_taskflow_planned_details == {k: v for k, v in admin_taskflow_planned_new.to_json().items() if k in admin_taskflow_planned_details.keys()}


def test_update_taskflow_planned(client_credentials: ClientCredentials):
    '''
    Create taskflow planning, update field-by-field and compare on each update.
    Test if no other fields are implicitly modified when updating one specific field.
    '''
    admin_taskflow_planned = TaskFlowPlanned(client_credentials)

    # Read and set taskflow planning data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'taskflow', 'data', 'new_taskflow_planned.json'), mode='r', encoding='utf-8') as f:
        admin_taskflow_planned_details: dict = json.load(f)
    admin_taskflow_planned_details['project_id'] = 12

    for k, v in admin_taskflow_planned_details.items():
        if k in admin_taskflow_planned._datetime_properties: 
            admin_taskflow_planned_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
        setattr(admin_taskflow_planned, k, v)
    
    admin_taskflow_planned.create()
    admin_taskflow_planned.refresh()

    # Read and set taskflow planning data to update
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'taskflow', 'data', 'updated_taskflow_planned.json'), mode='r', encoding='utf-8') as f:
        taskflow_planned_update_details = json.load(f)
    for k, v in taskflow_planned_update_details.items():
        if k in admin_taskflow_planned._datetime_properties: 
            taskflow_planned_update_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')

    for k, new_value in taskflow_planned_update_details.items():
        # Store the to-be situation for comparison
        taskflow_planned_details_post = admin_taskflow_planned.to_json()
        taskflow_planned_details_post[k] = new_value

        # Write to Admin Consult
        admin_taskflow_planned.update(**{k: new_value})
        admin_taskflow_planned.refresh()

        assert taskflow_planned_details_post == {k: v for k, v in admin_taskflow_planned.to_json().items() if k in taskflow_planned_details_post.keys()}


def test_delete_taskflow_planned(client_credentials: ClientCredentials):
    '''
    Deactivate taskflow planning
    '''
    admin_taskflow_planned = TaskFlowPlanned(client_credentials)

    # Read and set taskflow planning data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'taskflow', 'data', 'new_taskflow_planned.json'), mode='r', encoding='utf-8') as f:
        admin_taskflow_planned_details: dict = json.load(f)

    for k, v in admin_taskflow_planned_details.items():
        if k in admin_taskflow_planned._datetime_properties: 
            admin_taskflow_planned_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
        setattr(admin_taskflow_planned, k, v)
    
    admin_taskflow_planned.create()
    admin_taskflow_planned.refresh()

    admin_taskflow_planned.delete()

    assert admin_taskflow_planned.task_id is None
