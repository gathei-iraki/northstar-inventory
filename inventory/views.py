from django.shortcuts import render
from django.http import JsonResponse

from .models import WarehouseProduct, InventoryItem

def warehouse_products(request):
    products = WarehouseProduct.objects.all()

    data = [
        {
            "sku": product.sku,
            "name": product.name,
            "quantity": product.quantity,
        }
        for product in products
    ]

    return JsonResponse({"products": data})


def inventory_detail(request, sku):
    try:
        item = InventoryItem.objects.get(sku=sku)
    except InventoryItem.DoesNotExist:
        return JsonResponse(
            {"error": "Product not found"},
            status=404,
        )

    return JsonResponse(
        {
            "sku": item.sku,
            "name": item.name,
            "quantity": item.quantity,
            "in_stock": item.in_stock,
            "updated_at": item.updated_at.isoformat(),
        }
    )