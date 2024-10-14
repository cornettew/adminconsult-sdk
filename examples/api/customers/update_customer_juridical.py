from examples.api.auth.auth import get_cred
from adminconsult.api.customer import Juridical
from datetime import datetime

admin_cred = get_cred()


customer_juridical = Juridical(admin_cred)
customer_juridical.get(25)

print('Original value: {}'.format(customer_juridical.closing_date))

customer_juridical.update(closing_date=datetime(2024, 3, 1))
print('Updated value: {}'.format(customer_juridical.closing_date))
