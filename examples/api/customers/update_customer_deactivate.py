from examples.api.auth.auth import get_cred

from adminconsult.api.customer import Customer
from datetime import datetime

admin_cred = get_cred()

# Get Customer object
admin_customer = Customer(admin_cred)
admin_customer.get(id=25)

admin_customer.deactivate()

admin_customer.reactivate()

admin_customer.deactivate(disabled_date=datetime(2023, 9, 15))

admin_customer.reactivate()
