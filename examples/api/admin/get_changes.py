from examples.api.auth.auth import get_cred

from datetime import datetime, timedelta
from adminconsult.api.admin import Change, ChangeList

admin_cred = get_cred()

# Get changes within last five minutes
admin_events = ChangeList(admin_cred, on_technical_max='ignore')
admin_events.get(ge__date_action=datetime.now()-timedelta(minutes=60*24*7), limit_last_logs=1000)
admin_events.get(ge__log_id=60401596, le__log_id=60406680, ne__table_name='PRESTATIE_AUTHORIZED', on_technical_max='warn')

print('{} changes'.format(admin_events.count))
print(admin_events.to_json())

print(type(admin_events[0].date_action))

admin_cred.print_logs()
