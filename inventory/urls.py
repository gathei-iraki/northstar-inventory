from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.dashboard,
        name="dashboard",
    ),
    path(
        "warehouse/add/",
        views.add_warehouse_product,
        name="add-warehouse-product",
    ),
    path(
        "warehouse/<int:product_id>/quantity/",
        views.update_warehouse_quantity,
        name="update-warehouse-quantity",
    ),
    path(
        "inventory/sync/",
        views.sync_inventory,
        name="sync-inventory",
    ),
    path(
        "api/warehouse/products/",
        views.warehouse_products_api,
        name="warehouse-products-api",
    ),
    path(
        "api/inventory/<str:sku>/",
        views.inventory_detail,
        name="inventory-detail",
    ),
]      