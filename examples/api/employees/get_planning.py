from datetime import datetime
from examples.api.auth.auth import get_cred
from adminconsult.api.hrm import Planning, PlanningList

admin_cred = get_cred()


# Get employee list
plannings = PlanningList(admin_cred)
plannings.get(eq__person_id=182, ge__date_start=datetime(2025, 1, 1), max_results=120)
print(plannings.to_json()[:2])
print(plannings.count)

# Get one employee
planning = Planning(admin_cred)
print(planning.person_id)
planning.get(id=35183)
print(planning.person_id)
print(planning.date_start)
print(planning.to_json())
