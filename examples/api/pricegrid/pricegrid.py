from examples.api.auth.auth import get_cred
from adminconsult.api.pricegrid import PriceGrid, PriceGridList, PriceGridDetail, PriceGridDetailList

admin_cred = get_cred()

price_grids = PriceGridList(admin_cred)
price_grids.get()
print('{} price grids found'.format(price_grids.count))

print(price_grids.to_json())


pricegrid_details = PriceGridDetailList(admin_cred, price_grid_id=44)
pricegrid_details.get()
print('{} price grid details found'.format(pricegrid_details.count))

print(pricegrid_details.to_json())
