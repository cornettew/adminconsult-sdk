from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectInvoicingData

admin_cred = get_cred()


project_invoicing_data = ProjectInvoicingData(admin_cred)

project_invoicing_data.get(44952)

print(project_invoicing_data.to_json())
print(project_invoicing_data.invoicing_remark)
