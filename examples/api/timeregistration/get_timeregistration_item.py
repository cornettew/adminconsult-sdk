from examples.api.auth.auth import get_cred
from adminconsult.api.timeregistration import TimeregistrationItem, TimeregistrationItemList

admin_cred = get_cred()


admin_timeregistration_item = TimeregistrationItem(admin_cred)
admin_timeregistration_item.get(id=1)

print(admin_timeregistration_item.to_json())

admin_timeregistration_items = TimeregistrationItemList(admin_cred)
admin_timeregistration_items.get()

print('{} timeregistration items found'.format(admin_timeregistration_items.count))

print(admin_timeregistration_items.to_json())
