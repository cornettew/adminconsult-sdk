from examples.api.auth.auth import get_cred
from adminconsult.api.customer import CustomerEmailData

admin_cred = get_cred()

# Create Customer object
admin_customer_email = CustomerEmailData(admin_cred, customer_id=12)

admin_customer_email.document_group_id = None
admin_customer_email.document_template_id = 31
admin_customer_email.document_type = 2
admin_customer_email.email = 'ward.cornette@rfn.fr'
admin_customer_email.to_recipient = True
admin_customer_email.cc_recipient = True
admin_customer_email.bcc_recipient = False

# Commit the customer data to Admin Consult
admin_customer_email.create()

# Print newly created customer email
print(admin_customer_email.email)

admin_customer_email.update(email='test@rfn.fr')
admin_customer_email.update(cc_recipient=False)

print(admin_customer_email.to_json())

# admin_customer_email.delete()

admin_customer_email.print_logs()