from examples.api.auth.auth import get_cred
from adminconsult.api.project import Project, ProjectList

admin_cred = get_cred()

customer_projects = ProjectList(admin_cred)
customer_projects.get(eq__is_taskflow_customer=True,
                      eq__customer_id=41879, 
                      ge__project_type_id=800)
pids = [p.project_id for p in customer_projects]


customer_project_billto = ProjectList(admin_cred)
customer_project_billto.get(in__project_id=pids,
                            eq__is_taskflow_customer=None,
                            eq__invoice_percentage=100,
                            ne__customer_id=41879, 
                            ge__project_type_id=800)

billto_customer_ids = list(set([p.customer_id for p in customer_project_billto]))
print(billto_customer_ids)

for project in customer_project_billto:
    print(project.project_title)
    