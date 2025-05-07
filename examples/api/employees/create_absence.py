from datetime import datetime
from examples.api.auth.auth import get_cred
from adminconsult.api.hrm import Planning, PlanningList

admin_cred = get_cred()

# Create absence
planning = Planning(admin_cred)
planning.date_start = datetime(2025, 5, 2)
planning.duration = 1
planning.is_public = True
planning.person_id = 182
planning.prestation_id = 3115 # Must be an ID from PRESTATIE table with SPECIAL_TYPE eq to time off
planning.remarks = 'verlof'
planning.time_start = '13:00'

planning.create_absence()

print(planning.planning_id)
