from examples.api.auth.auth import get_cred
from adminconsult.api.productuse import ProductUse, ProductUseList
from datetime import datetime

admin_cred = get_cred()


admin_products = ProductUseList(admin_cred)
admin_products.get(max_results=750, eq__person_id=143, ge__date_product_use=datetime(2022, 11, 1))

print('{} product uses found'.format(admin_products.count))

print(admin_products.to_json())
