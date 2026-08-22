from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import WarehouseProductForm
from .models import InventoryItem, WarehouseProduct
from .services.inventory_sync import synchronize_inventory


def dashboard(request):
    warehouse_products = WarehouseProduct.objects.all().order_by("sku")
    inventory_items = InventoryItem.objects.all().order_by("sku")

    form = WarehouseProductForm()

    context = {
        "warehouse_products": warehouse_products,
        "inventory_items": inventory_items,
        "form": form,
    }

    return render(request, "inventory/dashboard.html", context)


@require_POST
def add_warehouse_product(request):
    form = WarehouseProductForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, "Warehouse product added.")
    else:
        messages.error(request, "The product could not be added.")

    return redirect("dashboard")


@require_POST
def update_warehouse_quantity(request, product_id):
    product = get_object_or_404(
        WarehouseProduct,
        id=product_id,
    )

    try:
        quantity = int(request.POST.get("quantity", ""))
    except ValueError:
        messages.error(request, "Quantity must be a number.")
        return redirect("dashboard")

    if quantity < 0:
        messages.error(request, "Quantity cannot be negative.")
        return redirect("dashboard")

    product.quantity = quantity
    product.save()

    messages.success(
        request,
        f"Warehouse quantity for {product.sku} updated.",
    )

    return redirect("dashboard")


@require_POST
def sync_inventory(request):
    result = synchronize_inventory()

    messages.success(
        request,
        (
            f"Synchronization complete: "
            f"{result['created']} created and "
            f"{result['updated']} updated."
        ),
    )

    return redirect("dashboard")


def warehouse_products_api(request):
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