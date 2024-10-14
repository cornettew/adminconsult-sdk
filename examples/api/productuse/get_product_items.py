from examples.api.auth.auth import get_cred
from adminconsult.api.productuse import ProductItem, ProductItemList

admin_cred = get_cred()


admin_products = ProductItemList(admin_cred)
admin_products.get()

print('{} products found'.format(admin_products.count))

print(admin_products.to_json())
