from examples.api.auth.auth import get_cred
from datetime import datetime
from adminconsult.api.timeregistration import Timeregistration, TimeregistrationList

admin_cred = get_cred()

timeregistration = Timeregistration(admin_cred)
timeregistration.get(2855507)

print('Original value: {}'.format(timeregistration.remarks))

timeregistration.update(remarks='test update')
print('Updated value: {}'.format(timeregistration.remarks))

