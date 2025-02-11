from examples.api.auth.auth import get_cred
from datetime import datetime, timedelta
from adminconsult.api.project import ProjectCustomer
from adminconsult.api.admin import Change, ChangeList

admin_cred = get_cred()

project_customer = ProjectCustomer(admin_cred, project_id=44952)
project_customer.get(id=52058)
print(project_customer.customer_id)
print(project_customer.invoice_percentage)
print(project_customer.is_taskflow_customer)

project_customer.update(is_taskflow_customer=True)
project_customer.update(invoice_percentage=120)


changes = ChangeList(admin_cred, on_technical_max='ignore')
changes.get(ge__date_action=datetime.now()-timedelta(minutes=5), eq__db_user='Hermes', limit_last_logs=1000)

print(changes.to_dataframe())

print('{} changes'.format(changes.count))
