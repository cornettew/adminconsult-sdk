from examples.api.auth.auth import get_cred
from adminconsult.api.timeregistration import TimeregistrationSubcategory, TimeregistrationSubcategoryList

admin_cred = get_cred()


admin_timeregistration_subcategory = TimeregistrationSubcategory(admin_cred)
admin_timeregistration_subcategory.get(id=1)

print(admin_timeregistration_subcategory.to_json())

admin_timeregistration_subcategories = TimeregistrationSubcategoryList(admin_cred)
admin_timeregistration_subcategories.get()

print('{} timeregistration subcategories found'.format(admin_timeregistration_subcategories.count))

print(admin_timeregistration_subcategories.to_json())
