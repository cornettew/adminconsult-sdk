from examples.api.auth.auth import get_cred
from adminconsult.api.lists import List, CustomerLinkTypes, Titles

admin_cred = get_cred()

admin_list = List(admin_cred, list_id=50)
print(admin_list.to_json())
admin_cred.print_logs()


# Read values of the list
admin_list.get()

# Print values of the list
print(admin_list.to_json()['values'])
print(admin_list.to_dict())



link_types = CustomerLinkTypes(admin_cred)
link_types.get()
print(link_types.to_dict())


titles = Titles(admin_cred)
titles.get()
print(titles.to_dict())
