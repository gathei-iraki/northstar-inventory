from django.contrib import admin
from .models import WarehouseProduct, InventoryItem

admin.site.register(WarehouseProduct)
admin.site.register(InventoryItem)