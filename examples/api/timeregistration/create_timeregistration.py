from examples.api.auth.auth import get_cred
from datetime import datetime, time
from adminconsult.api.timeregistration import Timeregistration

admin_cred = get_cred()


# Create TimeRegistration object
timeregistration = Timeregistration(admin_cred)
timeregistration.date_registration = datetime.now().date()
timeregistration.internal_remarks = 'test api'
timeregistration.invoicable = True
timeregistration.period = 37
timeregistration.person_id = 182
timeregistration.prestation_id = 2035
timeregistration.project_id = 1115
timeregistration.remarks = 'invoice text'
timeregistration.duration = 115
timeregistration.time_from = time(9, 30, 0)


# Commit the time registration to Admin Consult
timeregistration.create()

# Print newly created time registration
print(timeregistration.timeregistration_id)

timeregistration.update(remarks='updated text')
timeregistration.update(project_id=1123)

timeregistration.set_invoiced()

timeregistration.clear_invoiced()

timeregistration.delete()

# Print newly created time registration
print(timeregistration.to_json())

timeregistration.print_logs()
