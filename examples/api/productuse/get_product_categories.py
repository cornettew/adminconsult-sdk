from examples.api.auth.auth import get_cred
from adminconsult.api.productuse import ProductCategory, ProductCategoryList


admin_cred = get_cred()

admin_product_categories = ProductCategoryList(admin_cred)
admin_product_categories.get()

print('{} product categories found'.format(admin_product_categories.count))

print(admin_product_categories.to_json())
