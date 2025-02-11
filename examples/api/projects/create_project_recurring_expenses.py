from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectRecurringExpense
from datetime import datetime

admin_cred = get_cred()


# Create Customer object
project_recurring_expense = ProjectRecurringExpense(admin_cred)
project_recurring_expense.invoice_text = 'test'
project_recurring_expense.person_id = 182
project_recurring_expense.planning_stop = datetime(2023, 12, 31)
project_recurring_expense.expense_id = 59
project_recurring_expense.project_id = 49867
project_recurring_expense.amount = 5
project_recurring_expense.schedule_abbr_nr = 1
project_recurring_expense.schedule_abbr_unit = 'j'
project_recurring_expense.schedule_date = datetime(2023, 5, 1)
project_recurring_expense.text_id = None
project_recurring_expense.text_type = 1

# Commit the customer data to Admin Consult
project_recurring_expense.create()

# Print newly created recurring project
print(project_recurring_expense.project_recurring_expense_id)

project_recurring_expense.delete()

# Print newly created recurring project
print(project_recurring_expense.to_json())

project_recurring_expense.print_logs()
