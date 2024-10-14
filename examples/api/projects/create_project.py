from examples.api.auth.auth import get_cred
from adminconsult.api.project import Project

admin_cred = get_cred()


project = Project(admin_cred)

project.create(template_id=43976, 
               taskflow_customer_id=37541, 
               company_id=7, 
               project_manager_id=43, 
               bill_to_customer_id=501)

print(project.project_id)
print(project.project_title)
print(project.project_manager)
