from datetime import datetime
from examples.api.auth.auth import get_cred
from adminconsult.api.hrm import Planning, PlanningList

admin_cred = get_cred()

# Get one planning
planning = Planning(admin_cred)
planning.customer_id = 14614
planning.project_id = 21039
planning.prestation_id = 3001
planning.duration = 5
planning.person_id = 182
planning.remarks = 'test'
planning.time_start = '11:00'
planning.date_start = datetime(2025, 5, 2)

planning.create()

print(planning.planning_id)
