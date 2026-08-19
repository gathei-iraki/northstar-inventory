from django.urls import path

from . import views


urlpatterns = [
    path(
        "warehouse/products/",
        views.warehouse_products,
        name="warehouse-products",
    ),
    path(
        "inventory/<str:sku>/",
        views.inventory_detail,
        name="inventory-detail",
    ),
]