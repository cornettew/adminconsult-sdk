from examples.api.auth.auth import get_cred
from adminconsult.api.customer import CustomerEmailDataChanges

admin_cred = get_cred()

admin_customer_email_changes = CustomerEmailDataChanges(admin_cred)
admin_customer_email_changes.get(ge__log_id=55907229, lt__log_id=55909999)

print(admin_customer_email_changes.inserts.to_json())
print(admin_customer_email_changes.updates.to_json())
print(admin_customer_email_changes.deletes)

# Print logs
admin_cred.print_logs()
