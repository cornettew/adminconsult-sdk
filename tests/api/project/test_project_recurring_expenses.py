import os
import json
from time import sleep
from datetime import datetime, timedelta

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.project import ProjectRecurringExpense, ProjectRecurringExpenseList

def test_get_recurring_expense(client_credentials: ClientCredentials):

    admin_project_recurring_expense_list = ProjectRecurringExpenseList(client_credentials)
    admin_project_recurring_expense_list.get(max_results=1250)

    if admin_project_recurring_expense_list.count > 0:
        admin_project_recurring_expense_list[0].refresh()
        project_recurring_expense_id = admin_project_recurring_expense_list[0].project_recurring_expense_id

        admin_project_recurring_expense = ProjectRecurringExpense(client_credentials)
        admin_project_recurring_expense.get(project_recurring_expense_id)
        assert admin_project_recurring_expense_list[0] == admin_project_recurring_expense
    else:
        # No project recurring expense found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

def test_create_recurring_expense(client_credentials: ClientCredentials):

    admin_project_recurring_expense = ProjectRecurringExpense(client_credentials)

    # Read and set taskflow planned data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'project', 'data', 'new_recurring_expense.json'), mode='r', encoding='utf-8') as f:
        admin_project_recurring_expense_details: dict = json.load(f)

    for k, v in admin_project_recurring_expense_details.items():
        if k in admin_project_recurring_expense._datetime_properties: 
            admin_project_recurring_expense_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
        setattr(admin_project_recurring_expense, k, v)
    
    admin_project_recurring_expense.create()

    # Get new taskflow planned and verify data
    admin_project_recurring_expense_new = ProjectRecurringExpense(client_credentials)
    admin_project_recurring_expense_new.get(admin_project_recurring_expense.project_recurring_expense_id)
    
    assert admin_project_recurring_expense_details == {k: v for k, v in admin_project_recurring_expense.to_json().items() if k in admin_project_recurring_expense_details.keys()}


def test_update_recurring_expense(client_credentials: ClientCredentials):
    '''
    Create recurring expense, update field-by-field and compare on each update.
    Test if no other fields are implicitly modified when updating one specific field.
    '''

    admin_project_recurring_expense = ProjectRecurringExpense(client_credentials)

    # Read and set recurring expense data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'project', 'data', 'new_recurring_expense.json'), mode='r', encoding='utf-8') as f:
        admin_project_recurring_expense_details: dict = json.load(f)

    for k, v in admin_project_recurring_expense_details.items():
        if k in admin_project_recurring_expense._datetime_properties: 
            admin_project_recurring_expense_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
        setattr(admin_project_recurring_expense, k, v)
    
    admin_project_recurring_expense.create()
    admin_project_recurring_expense.refresh()

    # Read and set recurring expense data to update
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'project', 'data', 'updated_recurring_expense.json'), mode='r', encoding='utf-8') as f:
        recurring_expense_update_details = json.load(f)
    for k, v in recurring_expense_update_details.items():
        if k in admin_project_recurring_expense._datetime_properties: 
            recurring_expense_update_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')

    for k, new_value in recurring_expense_update_details.items():
        # Store the to-be situation for comparison
        recurring_expense_details_post = admin_project_recurring_expense.to_json()
        recurring_expense_details_post[k] = new_value

        # Write to Admin Consult
        admin_project_recurring_expense.update(**{k: new_value})
        admin_project_recurring_expense.refresh()

        assert recurring_expense_details_post == {k: v for k, v in admin_project_recurring_expense.to_json().items() if k in recurring_expense_details_post.keys()}


def test_delete_recurring_expense(client_credentials: ClientCredentials):
    '''
    Deactivate project recurring expense
    '''
    admin_project_recurring_expense = ProjectRecurringExpense(client_credentials)

    # Read and set recurring expense data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'project', 'data', 'new_recurring_expense.json'), mode='r', encoding='utf-8') as f:
        admin_project_recurring_expense_details: dict = json.load(f)

    for k, v in admin_project_recurring_expense_details.items():
        if k in admin_project_recurring_expense._datetime_properties: 
            admin_project_recurring_expense_details[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
        setattr(admin_project_recurring_expense, k, v)
    
    admin_project_recurring_expense.create()
    admin_project_recurring_expense.refresh()

    admin_project_recurring_expense.delete()

    assert admin_project_recurring_expense.project_recurring_expense_id is None
