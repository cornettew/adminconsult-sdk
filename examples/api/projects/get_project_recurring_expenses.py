from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectRecurringExpense, ProjectRecurringExpenseList

admin_cred = get_cred()


# Get one customer
project_recurring_expense = ProjectRecurringExpense(admin_cred)
print(project_recurring_expense.project_id)
project_recurring_expense.get(id=2)
print(project_recurring_expense.project_id)
print(project_recurring_expense.to_json())


# Get customer list
project_recurring_expenses = ProjectRecurringExpenseList(admin_cred)
project_recurring_expenses.get(max_results=750)
print(project_recurring_expenses.count)


# Get filtered customer list
project_recurring_expenses.get(max_results=750, eq__project_id=38992)
print(project_recurring_expenses.count)

# Print first element of customer list
print(project_recurring_expenses[0].to_json())

# for pps in project_recurring_expenses:
#     pps.delete()

# Print logs
admin_cred.print_logs()
