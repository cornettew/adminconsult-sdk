from examples.api.auth.auth import get_cred
from adminconsult.api.customer import Customer

admin_cred = get_cred()

# Get Customer object
admin_customer = Customer(admin_cred)
admin_customer.get(id=12)

# Update Customer object
admin_customer.update(title_id=25)

# Posting a Title as string value which does not yet exist in Admin Consult, will result in an error produced by this SDK.
# The Admin Consult API does accept new values but this implicitly creates a new Title. This SDK catches this undesirable behaviour.
# If possible, always updating using the title id.
admin_customer.update(title='SARL')

# admin_customer.update(title_id=14)
# admin_customer.update(title='NV')
