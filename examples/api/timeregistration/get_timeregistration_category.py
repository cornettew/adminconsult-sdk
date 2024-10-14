from examples.api.auth.auth import get_cred
from adminconsult.api.timeregistration import TimeregistrationCategory, TimeregistrationCategoryList

admin_cred = get_cred()


admin_timeregistration_category = TimeregistrationCategory(admin_cred)
admin_timeregistration_category.get(id=1)

print(admin_timeregistration_category.to_json())

admin_timeregistration_categories = TimeregistrationCategoryList(admin_cred)
admin_timeregistration_categories.get()

print('{} timeregistration categories found'.format(admin_timeregistration_categories.count))

print(admin_timeregistration_categories.to_json())
