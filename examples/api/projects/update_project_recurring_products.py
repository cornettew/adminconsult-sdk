from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectRecurringProduct
from datetime import datetime

admin_cred = get_cred()


project_recurring_product = ProjectRecurringProduct(admin_cred)
project_recurring_product.get(3291)
print(f'project_id = {project_recurring_product.project_id}')

if project_recurring_product.person_id == 161:
    print('Original value: {}'.format(project_recurring_product.person_id))
    project_recurring_product.update(planning_stop=datetime(2024, 3, 1), person_id=43)
    # project_recurring_product.update(schedule_abbr_nr=3, schedule_abbr_unit='m')
    print('Updated value: {}'.format(project_recurring_product.person_id))
else:
    print('Original value: {}'.format(project_recurring_product.person_id))
    project_recurring_product.update(planning_stop=datetime(2024, 3, 1), person_id=161)
    # project_recurring_product.update(schedule_abbr_nr=3, schedule_abbr_unit='m')
    print('Updated value: {}'.format(project_recurring_product.person_id))
