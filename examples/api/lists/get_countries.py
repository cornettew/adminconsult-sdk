from examples.api.auth.auth import get_cred
from adminconsult.api.lists import Countries

admin_cred = get_cred()

admin_countries = Countries(admin_cred)
print(admin_countries.to_json())
admin_cred.print_logs()


# Read values of the list
admin_countries.get()

# Print values of the list
print(admin_countries.get_country_code(22))
print(admin_countries.get_country_name(74))
print(admin_countries.get_country_id(country_code='BE'))
print(admin_countries.get_country_id(country_name='Frankrijk'))

