from examples.api.auth.auth import get_cred
from adminconsult.api.lists import Titles

admin_cred = get_cred()

admin_titles = Titles(admin_cred)
print(admin_titles.to_json())
admin_cred.print_logs()


# Read values of the list
admin_titles.get()

# Print values of the list
print(admin_titles.get_item_value(43, is_company=True))
print(admin_titles.get_item_value(13, is_company=False))
print(admin_titles.get_item_id('BV', is_company=True))
print(admin_titles.get_item_id('Mevr.', is_company=False))

