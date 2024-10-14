from examples.api.auth.auth import get_cred
from adminconsult.api.customer import CustomerEmailData, CustomerEmailDataList

admin_cred = get_cred()

# Get one customer emaildata
admin_customer_email = CustomerEmailData(admin_cred, customer_id=10694)
print(admin_customer_email.email)
admin_customer_email.get(id=27729)
print(admin_customer_email.email)
print(admin_customer_email.to_json())


# Get customer list
admin_customer_emails = CustomerEmailDataList(admin_cred, customer_id=10694)
admin_customer_emails.get(max_results=750)
print(admin_customer_emails.count)

# Print first element of customer list
print(admin_customer_emails[0].to_json())

for email in admin_customer_emails:
    print(email)
    # email.delete()
# Print logs
admin_cred.print_logs()
