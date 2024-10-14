from examples.api.auth.auth import get_cred
from adminconsult.api.productuse import ProductPriceGrid, ProductPriceGridList

admin_cred = get_cred()


admin_product_price_grid = ProductPriceGrid(admin_cred)
admin_product_price_grid.get(127)
print(admin_product_price_grid.to_json())


admin_product_price_grid_list = ProductPriceGridList(admin_cred)
admin_product_price_grid_list.get()

print('{} product price grids found'.format(admin_product_price_grid_list.count))

print(admin_product_price_grid_list[2].to_json())
