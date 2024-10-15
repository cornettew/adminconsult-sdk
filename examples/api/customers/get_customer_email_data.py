from examples.api.auth.auth import get_cred
from adminconsult.api.customer import CustomerEmailData, CustomerEmailDataList

admin_cred = get_cred()

# Get one customer emaildata
customer_email = CustomerEmailData(admin_cred, customer_id=10694)
print(customer_email.email)
customer_email.get(id=27729)
print(customer_email.email)
print(customer_email.to_json())


# Get customer list
customer_emails = CustomerEmailDataList(admin_cred, customer_id=10694)
customer_emails.get(max_results=750)
print(customer_emails.count)

# Print first element of customer list
print(customer_emails[0].to_json())

for customer_emails in customer_emails:
    print(customer_emails.email)
    # email.delete()
    
# Print logs
admin_cred.print_logs()
