from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectTemplate, ProjectTemplateList

admin_cred = get_cred()

admin_project_templates = ProjectTemplateList(admin_cred)
admin_project_templates.get()

for project in admin_project_templates:
    print('{} - {} ({})'.format(project.project_title, project.department, project.department_id))

admin_project_template = ProjectTemplate(admin_cred)
admin_project_template.get(725)
print('{} - {} ({})'.format(admin_project_template.project_title, admin_project_template.department, admin_project_template.department_id))
