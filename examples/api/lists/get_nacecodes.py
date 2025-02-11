from examples.api.auth.auth import get_cred
from adminconsult.api.lists.nacecodes import NaceCodes

admin_cred = get_cred()

admin_nacecodes = NaceCodes(admin_cred)
print(admin_nacecodes.to_json())
admin_cred.print_logs()


# Read values of the list
admin_nacecodes.get()

# Print values of the list
print(admin_nacecodes.get_nace_description('01'))
# Throws an exception because it doesn't exist
try:
    print(admin_nacecodes.get_nace_description('123')) 
except Exception as e:
    print(f'Exception: {e}')
    