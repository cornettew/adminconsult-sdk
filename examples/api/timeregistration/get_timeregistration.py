from examples.api.auth.auth import get_cred
from datetime import datetime
from adminconsult.api.timeregistration import Timeregistration, TimeregistrationList

admin_cred = get_cred()

admin_timeregistrations = TimeregistrationList(admin_cred)
admin_timeregistrations.get(max_results=20000, eq__person_id=143, ge__date_registration=datetime(2022, 9, 1), null__invoice_id=1)
admin_timeregistrations.get(eq__timeregistration_id=2855524)

print('{} time registrations found'.format(admin_timeregistrations.count))

print(admin_timeregistrations[0].to_json())


admin_time_registration = Timeregistration(admin_cred)
admin_time_registration.get(2855524)
print(admin_time_registration.to_json())
