from examples.api.auth.auth import get_cred
from adminconsult.api.project import ProjectInvoicingData

admin_cred = get_cred()

project_invoicing_data = ProjectInvoicingData(admin_cred)
project_invoicing_data.get(44952)
print('Original value: {}'.format(project_invoicing_data.invoicing_remark))

project_invoicing_data.update(invoicing_remark='api update2')
print('Updated value: {}'.format(project_invoicing_data.invoicing_remark))
