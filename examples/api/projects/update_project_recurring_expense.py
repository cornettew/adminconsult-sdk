from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectRecurringExpense
from datetime import datetime

admin_cred = get_cred()


project_recurring_expense = ProjectRecurringExpense(admin_cred)
project_recurring_expense.get(598)

# Print newly created recurring project
print(project_recurring_expense.project_recurring_expense_id)

print('Original value: {}'.format(project_recurring_expense.person_id))
# project_recurring_expense.update(planning_stop=datetime(2024, 3, 1), person_id=43)
# project_recurring_expense.update(schedule_abbr_nr=3, schedule_abbr_unit='m')
# project_recurring_expense.update(text_type=0, text_id=921)
project_recurring_expense.update(text_type=1, invoice_text='TELESPAZIO Belgium (1 x 168,99)')
print('Updated value: {}'.format(project_recurring_expense.person_id))
