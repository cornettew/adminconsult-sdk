from examples.api.auth.auth import get_cred
from adminconsult.api.extrafield import ExtraColumn, ExtraColumnList

admin_cred = get_cred()

# Get extra columns
admin_customer_email = ExtraColumnList(admin_cred, extra_table_id=104)
admin_customer_email.get()
print(admin_customer_email.to_json())
