from examples.api.auth.auth import get_cred
from adminconsult.api.expensedeclaration import ExpenseItem, ExpenseItemList

admin_cred = get_cred()

admin_expense_items = ExpenseItemList(admin_cred)
admin_expense_items.get()

print('{} expense items found'.format(admin_expense_items.count))

print(admin_expense_items.to_json())

for expense_item in admin_expense_items:
    print(expense_item.expense_type)
