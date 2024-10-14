from examples.api.auth.auth import get_cred
from adminconsult.api.expensedeclaration import ExpenseDeclaration
from datetime import datetime

admin_cred = get_cred()


# Create Expense Declaration object
expense_declaration = ExpenseDeclaration(admin_cred)
expense_declaration.expense_type = 39
expense_declaration.date_expense = datetime.now()
expense_declaration.internal_remarks = 'test api'
# expense_declaration.invoicable = True
expense_declaration.period = 37
expense_declaration.person_id = 182
expense_declaration.expense = 50
expense_declaration.project_id = 1115
expense_declaration.remarks = 'invoice text'

# Post the expense declaration to Admin Consult
expense_declaration.create()

# Print newly created expense declaration
print(expense_declaration.expense_id)



# Update the expense declaration
expense_declaration.update(remarks='updated text')
expense_declaration.update(project_id=1123)

expense_declaration.set_invoiced()

expense_declaration.clear_invoiced()

expense_declaration.delete()

# Print newly created recurring project
print(expense_declaration.to_json())

expense_declaration.print_logs()
