from examples.api.auth.auth import get_cred

from adminconsult.api.customer import Juridical

admin_cred = get_cred()

customer_juridical = Juridical(admin_cred)
customer_juridical.get(14614)

print(customer_juridical.to_json())

print(customer_juridical.closing_date)
