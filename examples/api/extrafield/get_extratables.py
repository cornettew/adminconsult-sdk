from examples.api.auth.auth import get_cred
from adminconsult.api.extrafield import ExtraTable, ExtraTableList

admin_cred = get_cred()

# Get extra tables
admin_customer_email = ExtraTableList(admin_cred)
admin_customer_email.get()
print(admin_customer_email.to_json())
