from inventory.models import InventoryItem, WarehouseProduct


def synchronize_inventory():
    warehouse_products = WarehouseProduct.objects.all()

    created_count = 0
    updated_count = 0

    for product in warehouse_products:
        item, created = InventoryItem.objects.update_or_create(
            sku=product.sku,
            defaults={
                "name": product.name,
                "quantity": product.quantity,
            },
        )

        if created:
            created_count += 1
        else:
            updated_count += 1

    return {
        "total": len(warehouse_products),
        "created": created_count,
        "updated": updated_count,
    }