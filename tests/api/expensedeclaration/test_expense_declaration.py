import os
import json

from tests.api import client_credentials

from adminconsult.api import ClientCredentials
from adminconsult.api.expensedeclaration import ExpenseDeclaration, ExpenseDeclarationList

def test_get_expense_declarations(client_credentials: ClientCredentials):

    expense_declarations = ExpenseDeclarationList(client_credentials)
    expense_declarations.get(max_results=1250)

    if expense_declarations.count > 0:
        expense_declarations[0].refresh()
        expense_id = expense_declarations[0].expense_id

        expense_declaration = ExpenseDeclaration(client_credentials)
        expense_declaration.get(expense_id)
        assert expense_declarations[0] == expense_declaration
    else:
        # No expense_declarations found. Assume the system is empty.
        assert client_credentials.calls_throttling_count > 0

def test_create_expense_declaration(client_credentials: ClientCredentials):

    expense_declaration = ExpenseDeclaration(client_credentials)

    # Read and set expense_declaration data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'expensedeclaration', 'data', 'new_expense_declaration.json'), mode='r', encoding='utf-8') as f:
        expense_declaration_details = json.load(f)

    for k, v in expense_declaration_details.items():
        setattr(expense_declaration, k, v)
    
    expense_declaration.create()

    # Get new expense_declaration and veriry data
    expense_declaration_new = ExpenseDeclaration(client_credentials)
    expense_declaration_new.get(expense_declaration.expense_id)
    
    assert expense_declaration_details == {k: v for k, v in expense_declaration_new.to_json().items() if k in expense_declaration_details.keys()}


def test_update_expense_declaration(client_credentials: ClientCredentials):
    '''
    Create expense_declaration, update field-by-field and compare on each update.
    Test if no other fields are implicitly modified when updating one specific field.
    '''
    admin_expense_declaration = ExpenseDeclaration(client_credentials)

    # Read and set new_expense_declaration data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'expensedeclaration', 'data', 'new_expense_declaration.json'), mode='r', encoding='utf-8') as f:
        expense_declaration_details = json.load(f)

    for k, v in expense_declaration_details.items():
        setattr(admin_expense_declaration, k, v)
    
    admin_expense_declaration.create()
    admin_expense_declaration.refresh()

    # Read and set customer data to update
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'expensedeclaration', 'data', 'updated_expense_declaration.json'), mode='r', encoding='utf-8') as f:
        expense_declaration_update_details = json.load(f)

    for k, new_value in expense_declaration_update_details.items():
        # Store the to-be situation for comparison
        expense_declaration_details_post = admin_expense_declaration.to_json()
        expense_declaration_details_post[k] = new_value
        del expense_declaration_details_post['customer_id']

        # Write to Admin Consult
        admin_expense_declaration.update(**{k: new_value})
        admin_expense_declaration.refresh()

        assert expense_declaration_details_post == {k: v for k, v in admin_expense_declaration.to_json().items() if k in expense_declaration_details_post.keys()}

def test_invoice_expense_declaration(client_credentials: ClientCredentials):

    expense_declaration = ExpenseDeclaration(client_credentials)

    # Read and set expense_declaration data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'expensedeclaration', 'data', 'new_expense_declaration.json'), mode='r', encoding='utf-8') as f:
        expense_declaration_details = json.load(f)

    for k, v in expense_declaration_details.items():
        setattr(expense_declaration, k, v)
    
    expense_declaration.create()

    # Get new expense_declaration and veriry data
    expense_declaration_new = ExpenseDeclaration(client_credentials)
    expense_declaration_new.get(expense_declaration.expense_id)

    expense_declaration_new.set_invoiced()
    expense_declaration_details['invoice_id'] = -1
    
    assert expense_declaration_details == {k: v for k, v in expense_declaration_new.to_json().items() if k in expense_declaration_details.keys()}

    expense_declaration_new.clear_invoiced()
    expense_declaration_details['invoice_id'] = None
    
    assert expense_declaration_details == {k: v for k, v in expense_declaration_new.to_json().items() if k in expense_declaration_details.keys()}
    
def test_delete_expense_declaration(client_credentials: ClientCredentials):

    expense_declaration = ExpenseDeclaration(client_credentials)

    # Read and set expense_declaration data
    with open(os.path.join(os.environ.get('BUILD_REPOSITORY_LOCALPATH', ''), 'tests', 'api', 'expensedeclaration', 'data', 'new_expense_declaration.json'), mode='r', encoding='utf-8') as f:
        expense_declaration_details = json.load(f)

    for k, v in expense_declaration_details.items():
        setattr(expense_declaration, k, v)
    
    expense_declaration.create()

    # Get new expense_declaration and veriry data
    expense_declaration_new = ExpenseDeclaration(client_credentials)
    expense_declaration_new.get(expense_declaration.expense_id)

    expense_declaration_new.delete()