from examples.api.auth.auth import get_cred
from adminconsult.api.expensedeclaration import ExpenseDeclaration, ExpenseDeclarationList
from datetime import datetime

admin_cred = get_cred()

admin_expense_declarations = ExpenseDeclarationList(admin_cred)
admin_expense_declarations.get(max_results=750, eq__person_id=143, ge__date_expense=datetime(2022, 11, 1))

print('{} expense declarations found'.format(admin_expense_declarations.count))

print(admin_expense_declarations.to_json())

for expense in admin_expense_declarations:
    # Print expense amount
    print('{} - € {}'.format(expense.expense_id, expense.expense))


admin_expense_declaration = ExpenseDeclaration(admin_cred)
admin_expense_declaration.get(35921)

print(admin_expense_declaration.to_json())
